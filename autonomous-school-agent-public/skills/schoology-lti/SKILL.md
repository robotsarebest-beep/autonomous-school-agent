---
name: schoology-lti
description: Directly interact with Schoology LTI endpoints for robust submission automation.
---

# Schoology LTI Interaction

Bypass browser iframe security by directly posting assignment submissions to the Schoology LTI submission gateway.

## Workflow

1. **Harvest Metadata**: Extract `assignment_id`, `user_id`, and `token` from `initSgyUiApp` in the page source.
2. **Authenticate**: Construct the authorization header.
3. **Submit**: POST the payload directly to the LTI endpoint.

## Usage Example

"Submit my document directly via LTI API."
1. Run `schoology-lti` to POST the payload.
2. Verify with a status check request.
