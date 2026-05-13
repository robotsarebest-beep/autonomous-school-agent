import os
import time
from playwright.sync_api import sync_playwright

def ensure_outlook_logged_in(headless=True):
    profile_dir = "/home/keaston/autonomous-school-agent/browser/profiles/outlook"
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            profile_dir,
            headless=headless,
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            viewport={"width": 1920, "height": 1080}
        )
        page = context.new_page()
        page.goto("https://outlook.cloud.microsoft/mail/")
        
        start = time.time()
        while time.time() - start < 120:
            time.sleep(5)
            if page.locator('button[aria-label="New mail"], [data-testid="new-mail-button"]').first.is_visible():
                print("Status: Outlook already logged in.")
                context.close()
                return True
            if "pick an account" in page.content().lower():
                page.click('div[role="listitem"]')
            elif page.locator('input[name="passwd"]').is_visible():
                page.fill('input[name="passwd"]', "Think123%$#@!")
                page.click('#idSIButton9')
            elif "stay signed in" in page.content().lower():
                page.click('#idSIButton9')
        context.close()
        return False

def ensure_google_logged_in(headless=True):
    profile_dir = "/home/keaston/autonomous-school-agent/browser/profiles/google"
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            profile_dir,
            headless=headless,
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            viewport={"width": 1920, "height": 1080}
        )
        page = context.new_page()
        page.goto("https://accounts.google.com/")
        
        try:
            # If we see "Personal info" or something, we are logged in
            if "Personal info" in page.content() or "keaston9776@gmail.com" in page.content():
                print("Status: Google already logged in.")
                context.close()
                return True
        except: pass
        
        try:
            page.wait_for_selector('input[type="email"]', timeout=15000)
            page.fill('input[type="email"]', "keaston9776@gmail.com")
            page.click('#identifierNext')
            time.sleep(5)
            
            page.wait_for_selector('input[type="password"]', timeout=15000)
            page.fill('input[type="password"]', "Think123%$#@!")
            page.click('#passwordNext')
            time.sleep(10)
            
            print("Status: Google login successful.")
            context.close()
            return True
        except Exception as e:
            print(f"Google Login Error: {e}")
            page.screenshot(path="/home/keaston/autonomous-school-agent/screenshots/google_login_error.png")
            context.close()
            return False

if __name__ == "__main__":
    ensure_google_logged_in(headless=True)
