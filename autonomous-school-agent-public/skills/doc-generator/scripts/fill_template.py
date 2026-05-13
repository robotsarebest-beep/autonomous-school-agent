# Doc Generator Script

This script uses `python-docx` to fill templates.

```python
from docx import Document

def fill_doc_template(template_path, output_path, data):
    doc = Document(template_path)
    for paragraph in doc.paragraphs:
        for key, value in data.items():
            if key in paragraph.text:
                paragraph.text = paragraph.text.replace(key, value)
    doc.save(output_path)
    print(f"Filled document saved to {output_path}")
```
