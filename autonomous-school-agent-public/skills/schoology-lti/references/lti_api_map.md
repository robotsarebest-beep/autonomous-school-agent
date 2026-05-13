# Schoology LTI API Patterns

This guide details how to bypass the restrictive iframe UI by interacting directly with the Schoology LTI submission gateway.

## Submission Pattern

Instead of clicking through the iframe, use the endpoint:
`https://lti-submission-microsoft.app.schoology.com/submission-action`

**Headers required:**
- Authorization: Bearer <your-session-token>
- Content-Type: application/json

**Payload:**
```json
{
  "assignment_id": "8359555922",
  "document_url": "<onedrive-url>",
  "user_id": "<your-user-id>"
}
```
*Note: Your session token and user ID can be harvested from the `initSgyUiApp` parameters in the page source.*
