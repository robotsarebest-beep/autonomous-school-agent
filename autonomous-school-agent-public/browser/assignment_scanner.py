import re
from playwright.sync_api import Playwright, sync_playwright

def get_schoology_context(playwright: Playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    # Use the login pattern that successfully worked for you
    page.goto("https://login.microsoftonline.com/common/oauth2/authorize?response_type=code&client_id=f97b3686-bc70-4fee-b56d-f45878420d15&redirect_uri=https%3A%2F%2Fapp.schoology.com%2Flogin%2Fexternal_accounts%2Freceive%2Fmicrosoft&state=c2NoZW1lPWh0dHBzJmhvc3Q9c3RlbWlhLnNjaG9vbG9neS5jb20mcGF0aD0lMkZsb2dpbiUyRmV4dGVybmFsX2FjY291bnRzJTJGcmVjZWl2ZSUyRm1pY3Jvc29mdCZxdWVyeT1kZXN0aW5hdGlvbiUzRGFzc2lnbm1lbnQlMjUyRjgzNTk1NTU5MjIlMjZzY2hvb2xfbmlkJTNENTAzNTg4ODc3NyZzY2hvb2xfbmlkPTUwMzU4ODg3NzcmcmVfYXV0aF91aWQ9JnNfY3VzdG9tX2RvbWFpbj1odHRwcyUzQSUyRiUyRnN0ZW1pYS5zY2hvb2xvZ3kuY29tJnRzPTE3NzgwMzM4NTMmdG9rZW49V0o3NlRVSE8yUEdGTldDTzUzQUE1NTcxNzRCQkZGMTYwMDg5MEVDMzQyMUZDODE4Jmhhc2g9OGRkNWU0NGFjYWY3YTM1ZTFmYmEwNjVjZjg0ZjI0Yjg%3D&scope=openid%26email&nonce=69faa4bd733a6")
    page.get_by_role("textbox", name="Enter your email, phone, or").fill("keastonk018@stemia.ca")
    page.get_by_role("button", name="Next").click()
    page.locator("#i0118").fill("Think123%$#@!")
    page.get_by_role("button", name="Sign in").click()
    
    page.wait_for_load_state("networkidle")
    return browser, context, page

def find_missing_assignments():
    with sync_playwright() as playwright:
        browser, context, page = get_schoology_context(playwright)
        
        # Navigate to grades
        page.goto("https://stemia.schoology.com/grades/grades")
        
        # Look for "0" or "Missing" as you identified
        missing_items = page.locator("div").filter(has_text=re.compile(r"0|Missing"))
        
        results = []
        for i in range(missing_items.count()):
            try:
                text = missing_items.nth(i).inner_text()
                results.append(text)
            except: pass
        
        browser.close()
        return results

if __name__ == "__main__":
    missing = find_missing_assignments()
    print("Found potential missing assignments:", missing)
