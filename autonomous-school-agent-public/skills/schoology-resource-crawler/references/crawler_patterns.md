# Schoology Crawler Patterns

Use these patterns to navigate the Schoology structure programmatically.

## Folder Navigation
Folders have the URL pattern: `https://stemia.schoology.com/folder/{folder_id}`.
To list items, look for the `.item-info` class.

## Assignment Detection
Assignments have the URL pattern: `https://stemia.schoology.com/assignment/{assignment_id}/info`.
Extract the `.item-title` and `.item-body`.

## Attachment Extraction
Links to attachments are often in `.attachment-title a`.
Always use the `page.expect_download()` context manager in Playwright.

## Overdue Detection
Found on the `/home` page within the `.overdue-list` container.
Each item is an `.upcoming-event`.
