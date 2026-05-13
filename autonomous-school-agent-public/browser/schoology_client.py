import os
import time
from playwright.sync_api import sync_playwright
from core.logger import logger

class SchoologyClient:

    def __init__(self, domain, username, password, headless=True):
        self.domain = domain
        self.username = username
        self.password = password
        self.headless = headless
        self.p = None
        self.browser = None
        self.context = None
        self.page = None

    def login(self):
        logger.info(f"Logging into Schoology at {self.domain}...")
        self.p = sync_playwright().start()
        # High-quality browser profile
        self.browser = self.p.chromium.launch(headless=self.headless)
        self.context = self.browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            viewport={"width": 1920, "height": 1080}
        )
        self.page = self.context.new_page()

        def perform_auth():
            # 1. Email
            email_selector = 'input[type="email"], input[name="loginfmt"], #edit-mail'
            try:
                self.page.wait_for_selector(email_selector, timeout=20000)
                self.page.fill(email_selector, self.username)
                self.page.keyboard.press("Enter")
                logger.info("Email submitted.")
            except:
                logger.warn("Email field not found, maybe already on password page.")

            # 2. Password
            password_selector = '#i0118, input[type="password"], input[name="passwd"], #edit-pass'
            try:
                self.page.wait_for_selector(password_selector, state="visible", timeout=20000)
                self.page.wait_for_timeout(2000)
                self.page.click(password_selector)
                self.page.keyboard.type(self.password, delay=100)
                self.page.keyboard.press("Enter")
                logger.info("Password submitted.")
            except:
                logger.warn("Password field not found.")

            # 3. Stay Signed In
            try:
                self.page.wait_for_selector("#idSIButton9, :text('Yes'), :text('Sign in')", state="visible", timeout=10000)
                self.page.click("#idSIButton9, :text('Yes'), :text('Sign in')")
                logger.info("Clicked Stay Signed In / Confirmation.")
            except: pass

        try:
            self.page.goto(f"https://{self.domain}")
            self.page.wait_for_load_state("networkidle")
            
            # Initial auth
            if "login" in self.page.url or "microsoft" in self.page.url:
                perform_auth()

            # Wait for home
            logger.info("Waiting for session establishment...")
            for i in range(3): # Try up to 3 times to stabilize
                try:
                    self.page.wait_for_url("**/home**", timeout=30000)
                    break
                except:
                    if "login" in self.page.url or "microsoft" in self.page.url:
                        logger.warn(f"Redirect loop detected (Attempt {i+1}). Re-authenticating...")
                        perform_auth()
                    else:
                        logger.info("Not on home page, but not on login either. Attempting forced navigation...")
                        self.page.goto(f"https://{self.domain}/home")

            self.page.wait_for_load_state("networkidle")
            if "schoology.com" in self.page.url and "login" not in self.page.url:
                logger.info("Logged in successfully.")
                return True
            else:
                logger.error(f"Login failed to stabilize. Final URL: {self.page.url}")
                self.page.screenshot(path="login_final_failure.png")
                return False

        except Exception as e:
            logger.error(f"Critical login failure: {e}")
            self.close()
            return False

    def navigate_to_assignment(self, course_id, assignment_id):
        url = f"https://{self.domain}/assignments/{assignment_id}/info"
        logger.info(f"Navigating to assignment URL: {url}")
        self.page.goto(url)
        self.page.wait_for_load_state("networkidle")
        # Ensure we are actually on the assignment page
        try:
            self.page.wait_for_selector(".item-title, .assignment-title", timeout=15000)
            return True
        except:
            logger.error(f"Failed to verify assignment page load for {url}")
            return False

    def get_assignment_data(self, assignment_id=None):
        if assignment_id:
            # Note: Assuming domain is stemia.schoology.com
            self.page.goto(f"https://{self.domain}/assignments/{assignment_id}/info")
            self.page.wait_for_load_state("networkidle")

        try:
            # Schoology assignment title selector
            title_el = self.page.query_selector(".item-title, .assignment-title")
            title = title_el.inner_text().strip() if title_el else "Unknown Assignment"
            
            # Description
            desc_el = self.page.query_selector(".item-body, .assignment-description")
            description = desc_el.inner_text().strip() if desc_el else "No description found."
            
            # Find attachments
            attachments = []
            links = self.page.query_selector_all(".attachment-title a, .assignment-attachments a")
            for link in links:
                attachments.append({
                    "name": link.inner_text().strip(),
                    "url": link.get_attribute("href")
                })

            return {
                "title": title,
                "description": description,
                "attachments": attachments
            }
        except Exception as e:
            logger.error(f"Failed to extract assignment data: {e}")
            return None

    def download_file(self, url, dest_path):
        try:
            with self.page.expect_download() as download_info:
                self.page.goto(url)
            download = download_info.value
            download.save_as(dest_path)
            logger.info(f"Downloaded: {os.path.basename(dest_path)}")
            return True
        except Exception as e:
            logger.error(f"Download failed for {url}: {e}")
            return False

    def submit_assignment(self, assignment_url, file_path):
        logger.info(f"Submitting assignment at {assignment_url}...")
        try:
            self.page.goto(assignment_url)
            self.page.wait_for_load_state("networkidle")
            
            # Click "Submit Assignment" button - handle both initial and re-submit
            # Target by text directly since tag might not be 'button'
            submit_btn = self.page.locator(':text("Submit Assignment"), :text("Re-submit Assignment"), #assignment-submission-button').first
            submit_btn.wait_for(state="visible", timeout=20000)
            submit_btn.click()
            logger.info("Clicked 'Submit Assignment'. Waiting for popup...")
            
            # Wait for the submission modal/iframe
            # The user said: "once you click submit there will be a popup and then you click an upload button and choose your file."
            # We look for the file input which is usually in the popup
            file_input = self.page.locator('input[type="file"]').first
            file_input.wait_for(state="attached", timeout=15000)
            
            logger.info("Popup detected. Uploading file...")
            file_input.set_input_files(file_path)
            
            # Wait for upload to complete (usually a progress bar or the filename appearing)
            self.page.wait_for_timeout(2000) # Buffer for upload start
            
            # Click the final Submit button in the popup
            final_submit = self.page.locator('button:has-text("Submit"), input[type="submit"][value="Submit"]').first
            final_submit.click()
            
            # Check for success message
            try:
                self.page.wait_for_selector(".message-success, .submission-confirmation, :text('Your submission has been received')", timeout=15000)
                logger.info("Assignment submitted successfully!")
                return True
            except:
                logger.warn("Could not confirm submission success message, but submit was clicked.")
                return True

        except Exception as e:
            logger.error(f"Submission failed: {e}")
            self.page.screenshot(path="submission_error.png")
            return False

    def close(self):
        if self.browser:
            self.browser.close()
        if self.p:
            self.p.stop()
        logger.info("Browser and Playwright session closed.")
