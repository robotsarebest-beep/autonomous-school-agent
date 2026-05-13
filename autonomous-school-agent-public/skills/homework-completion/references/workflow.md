# Homework Completion Workflow

This reference guide details the step-by-step process for completing a Schoology assignment from start to finish using the `hwbot` framework.

## 1. Discovery and Extraction

The first step is to identify the assignment and extract all relevant materials.

**Action:** Use `SchoologyClient` to fetch assignment data.
```python
from hwbot.browser.schoology_client import SchoologyClient
import os

client = SchoologyClient(domain, username, password)
client.login()
data = client.get_assignment_data(assignment_url)
```

## 2. Material Processing

Extract text from any downloaded attachments (PDFs, DOCX, etc.).

**Action:** Use `FileProcessor`.
```python
from hwbot.file_processing.file_processor import FileProcessor
processor = FileProcessor()
text = processor.process_any(file_path)
```

## 3. Prompt Construction

Build a structured prompt that defines the role, style, and context.

**Action:** Use `PromptBuilder`.
```python
from hwbot.prompt_builder.prompt_builder import PromptBuilder
builder = PromptBuilder()
prompt = builder.build(data, extracted_texts)
```

## 4. Solving (Agent Task)

As the AI assistant, take the generated prompt and produce the assignment content. Ensure you adhere to the Grade 10 student persona and style constraints.

## 5. Formatting and Saving

Save the generated content to a file (e.g., PDF or DOCX) in the `hwbot_output` directory.

**Action:** Save the output to the `final_submission` folder.

## 6. Submission

Upload the final file back to Schoology.

**Action:** Use `SchoologyClient.submit_assignment`.
```python
client.submit_assignment(assignment_url, final_file_path)
client.close()
```
