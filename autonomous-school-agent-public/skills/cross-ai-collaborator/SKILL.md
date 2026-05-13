---
name: cross-ai-collaborator
description: Integration layer for programmatically querying other AIs (ChatGPT, Claude, etc.) for brainstorming or complex reasoning.
---

# Cross-AI Collaborator

Leverage the power of multiple AI models to enhance your assignment quality.

## Features
- **Prompt Chaining**: Send prompts to multiple models (e.g., brainstorm in ChatGPT, refine in Claude).
- **Consensus Analysis**: Compare responses to ensure high-quality, balanced content.

## Usage
"Draft a portfolio response using ChatGPT for the creative style."
1. Calls the `cross-ai-collaborator` script.
2. Injects your assignment prompt into the selected AI's API.
3. Returns the output for use in your assignment.
