# Playwright Patterns for Autonomous Browsing

This guide provides reusable patterns for using Playwright in Python to navigate complex, interactive websites.

## 1. Robust Login Handling

Always handle SSO redirects and potential "Stay signed in?" prompts.

```python
def login(page, url, username, password):
    page.goto(url)
    # Check for Microsoft/Google SSO
    if "microsoft" in page.url:
        page.fill('input[type="email"]', username)
        page.click('input[type="submit"]')
        page.fill('input[type="password"]', password)
        page.click('input[type="submit"]')
    else:
        # Standard selectors
        page.fill("#username", username)
        page.fill("#password", password)
        page.click("#submit")
    
    page.wait_for_load_state("networkidle")
```

## 2. Dynamic Content and Lazy Loading

Wait for specific elements rather than using static sleep.

```python
# Wait for a list to populate
page.wait_for_selector(".item-list .item", timeout=10000)

# Scroll to trigger lazy loading
page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
```

## 3. Handling Downloads

Use the `expect_download` context manager.

```python
with page.expect_download() as download_info:
    page.click("text=Download PDF")
download = download_info.value
download.save_as("downloads/file.pdf")
```

## 4. Interaction with Modals/Iframes

Use `frame_locator` if the content is inside an iframe.

```python
iframe = page.frame_locator("#upload-iframe")
iframe.locator(".file-input").set_input_files("my_file.txt")
```
