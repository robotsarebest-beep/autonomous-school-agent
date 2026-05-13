import os
import sys
import time
from playwright.sync_api import sync_playwright

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.controller import HWBotController

def check_and_act():
    bot = HWBotController()
    env = bot._parse_env()
    
    profile_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "browser", "profiles", "outlook")
    
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            profile_dir,
            headless=env.get("HEADLESS", "True") == "True",
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            viewport={"width": 1920, "height": 1080}
        )
        page = context.new_page()
        
        while True:
            try:
                print(f"[{time.strftime('%H:%M:%S')}] Checking for new emails...")
                page.goto("https://outlook.office.com/mail/inbox")
                
                # Handle login wall using env variables
                if "login.microsoftonline.com" in page.url or "signin" in page.url:
                    print("Login wall detected. Attempting bypass...")
                    email_selector = 'input[type="email"], input[name="loginfmt"]'
                    if page.locator(email_selector).is_visible():
                        page.fill(email_selector, env.get("MICROSOFT_EMAIL", env.get("SCHOOLOGY_EMAIL")))
                        page.keyboard.press("Enter")
                        time.sleep(2)
                    
                    password_selector = 'input[type="password"], input[name="passwd"]'
                    if page.locator(password_selector).is_visible():
                        page.fill(password_selector, env.get("MICROSOFT_PASSWORD", env.get("SCHOOLOGY_PASSWORD")))
                        page.keyboard.press("Enter")
                        time.sleep(2)
                    
                    yes_btn = page.locator('#idSIButton9, :text("Yes")')
                    if yes_btn.is_visible():
                        yes_btn.click()
                
                page.wait_for_selector('div[role="listitem"]', timeout=30000)
                time.sleep(5)
                
                items = page.locator('div[role="listitem"]').all()
                for item in items[:5]:
                    text = item.inner_text().lower()
                    if any(word in text for word in ["assignment", "schoology", "grade"]):
                        print(f"Actionable email found: {text.split('\n')[0]}")
                        # Add custom action logic here
                
                time.sleep(600)
                
            except Exception as e:
                print(f"Error in email cycle: {e}")
                time.sleep(60)

if __name__ == "__main__":
    check_and_act()
