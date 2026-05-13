---
name: homework-completion
description: Automates the end-to-end homework lifecycle on Schoology. Use this skill when the user asks to "do my homework" or prepare/submit assignments from Schoology.
---

# Homework Completion

This skill enables the automated fetching, solving, and submission of Schoology assignments using the `hwbot` framework.

## Overview

The `homework-completion` skill transforms the AI from a simple assistant into a proactive student agent. It leverages Playwright via `SchoologyClient` to interact with the learning management system, `FileProcessor` to understand materials, and `PromptBuilder` to maintain a consistent persona.

## Core Workflow

To complete an assignment, follow these steps:

1. **Discovery**: Log into Schoology and fetch the assignment details (title, description, attachments).
2. **Extraction**: Download and extract text from all attached materials.
3. **Solving**: Use the extracted data to generate the assignment content, following the Grade 10 student persona.
4. **Submission**: Save the result and upload it back to the original assignment page.

For detailed implementation patterns and code snippets, see [references/workflow.md](references/workflow.md).

## Usage Example

"Hey, can you do the History assignment for me? It's the one due on Friday."

1. Search for the assignment URL.
2. Initialize `SchoologyClient`.
3. Follow the `workflow.md` to fetch, solve, and submit.
