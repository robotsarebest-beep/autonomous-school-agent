---
name: doc-generator
description: Advanced document generation and template filling for homework assignments.
---

# Document Generator

Automate the creation of professionally formatted assignments by populating templates with your details.

## Workflow

1. **Select Template**: Identify a template (`.docx`) in `assets/templates/`.
2. **Define Data**: Map your information to the placeholders in the document (e.g., `{{NAME}}` -> `Keaston`).
3. **Generate**: Use `scripts/fill_template.py` to create the final document.

## Usage Example

"Can you create a Job Application based on the standard template with my name?"
1. Identify `assets/templates/job_application.docx`.
2. Run `fill_template.py`.
3. Submit the resulting file.
