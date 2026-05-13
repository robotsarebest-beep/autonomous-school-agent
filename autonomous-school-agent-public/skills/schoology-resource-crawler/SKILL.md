---
name: schoology-resource-crawler
description: Recursively crawls Schoology course materials to find, download, and organize templates, rubrics, and assignment instructions.
---

# Schoology Resource Crawler

Automate the discovery of all homework materials.

## Features
- **Auto-Discovery**: Crawls all folders in a Schoology course.
- **Resource Extraction**: Downloads all `.docx`, `.pdf`, and `.pptx` files.
- **Metadata Tagging**: Saves metadata (assignment link, description, due date) in `assignment_metadata.json` for each course.

## Workflow
1. Provide a course URL.
2. Crawler visits all folders.
3. Downloads files to `hwbot_resources/{course_name}/`.

## Usage Example
"Find all templates for Innovative Engineering."
1. Run crawler on the course URL.
2. Result: All files downloaded and organized.
