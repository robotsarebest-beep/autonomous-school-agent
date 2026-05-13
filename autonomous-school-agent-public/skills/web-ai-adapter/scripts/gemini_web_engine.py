import os
import time
from playwright.sync_api import sync_playwright

def prompt_gemini_web(prompt, output_file=None):
    profile_dir = "/home/keaston/autonomous-school-agent/browser/profiles/google"
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            profile_dir,
            headless=True,
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        page.goto("https://gemini.google.com/app")
        
        try:
            page.wait_for_selector('div[role="textbox"]', timeout=30000)
            page.fill('div[role="textbox"]', prompt)
            page.keyboard.press("Enter")
            
            # Wait for generation to finish
            print("Status: Generation started...")
            time.sleep(20) 
            
            # Extract the actual markdown content of the response
            # Based on current Gemini web DOM
            response_locator = page.locator('div.message-content, div.markdown, [data-message-author-role="assistant"]')
            
            content = ""
            elements = response_locator.all()
            if elements:
                # Get the last one
                content = elements[-1].inner_text()
                print("Status: Successfully extracted response.")
            else:
                print("Warning: Standard selectors failed. Trying catch-all...")
                content = page.evaluate("() => { const msgs = document.querySelectorAll('div'); for(let m of msgs) { if(m.innerText.includes('Structural Labor Deficit')) return m.innerText; } return document.body.innerText; }")

            if output_file:
                os.makedirs(os.path.dirname(output_file), exist_ok=True)
                with open(output_file, "w") as f:
                    f.write(content)
            return content
                
        except Exception as e:
            print(f"Gemini Web Engine Failure: {e}")
            return None
        finally:
            context.close()

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        prompt_gemini_web(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
