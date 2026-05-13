---
name: web-auth-vault
description: Securely manages and executes authentication flows for SSO, 2FA, and cross-platform logins (Canva, etc.).
---

# Web Auth Vault

Standardized handling of complex authentication to ensure your automation never gets stuck.

## Features
- **Multi-Provider Support**: Microsoft, Google, Schoology-SSO, Canva.
- **2FA/Code Injection**: Methods for waiting for and entering verification codes.
- **State Preservation**: Saves browser session cookies to avoid constant re-authentication.

## Usage
"Sign into Canva with the alternate account."
1. Calls the vault's `get_auth_flow("canva")`.
2. Executes the pre-defined login script.
3. Injects credentials from your private memory vault.
