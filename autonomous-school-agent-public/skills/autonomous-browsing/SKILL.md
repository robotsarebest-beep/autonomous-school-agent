---
name: autonomous-browsing
description: Enables advanced web interaction using Playwright. Use when standard search/fetch tools are insufficient (e.g., login-walled sites, dynamic content, file uploads/downloads).
---

# Autonomous Browsing

This skill provides guidance and patterns for using Playwright to navigate the web autonomously, handling complex interactions that go beyond simple static page fetching.

## Overview

While standard tools like `google_web_search` and `web_fetch` are great for open information, many tasks require interacting with web applications (logging in, clicking buttons, uploading files). This skill teaches how to leverage the `playwright` library in Python or Node.js to perform these actions.

## Core Capabilities

1. **Authenticated Access**: Navigating past login screens (including SSO).
2. **Interactive Elements**: Clicking, typing, and submitting forms.
3. **Media & File Handling**: Uploading and downloading files programmatically.
4. **Dynamic Data**: Waiting for JavaScript-rendered content to appear.

## Workflow

1. **Plan**: Identify the target URL and the necessary actions (e.g., "Log in, go to X, download Y").
2. **Script**: Create a surgical script (Python preferred) using the patterns in [references/playwright_patterns.md](references/playwright_patterns.md).
3. **Execute**: Run the script using `run_shell_command`.
4. **Verify**: Check the output or downloaded files to ensure success.

## Usage Example

"Can you download the quarterly report from my dashboard? I'll provide the login."

1. Identify that this is a login-walled site.
2. Use this skill to write a Playwright script that logs in and downloads the file.
