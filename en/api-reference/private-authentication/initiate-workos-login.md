# Initiate WorkOS login

Starts authentication by redirecting the user to WorkOS AuthKit. Clients can supply PKCE parameters; no existing Bearer token is needed.

```http
GET /api/workos/login
```

Base URL: `https://app.counso.ai`

## Authentication

Start user sign-in without an existing Bearer token. A client using PKCE supplies its registered redirect URI and code challenge. The response redirects the user to the identity provider.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `redirect_uri` | query | string | No | Custom redirect URI (used by extensions for PKCE flow) |
| `code_challenge` | query | string | No | PKCE code challenge |
| `code_challenge_method` | query | string | No | PKCE code challenge method (S256) |

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | Login page HTML |
| 302 | Redirect to WorkOS authorization URL |
| 400 | Bad request |

## Specification

Download the complete [OpenAPI / Postman](../../docs/developer-platform/counso-api-documentation/openapi-and-postman.md) files.

```json
{
  "openapi": "3.0.0",
  "info": {
    "title": "Counso API",
    "version": "1.0.2",
    "description": "API reference for Counso workspaces, Agents, conversations and data sources.",
    "license": {
      "name": "MIT",
      "url": "https://opensource.org/licenses/MIT"
    }
  },
  "servers": [
    {
      "url": "https://app.counso.ai",
      "description": "Counso"
    }
  ],
  "paths": {
    "/api/workos/login": {
      "get": {
        "summary": "Initiate WorkOS login",
        "description": "Starts authentication by redirecting the user to WorkOS AuthKit. Clients can supply PKCE parameters; no existing Bearer token is needed.",
        "tags": [
          "Private Authentication"
        ],
        "security": [],
        "parameters": [
          {
            "in": "query",
            "name": "redirect_uri",
            "required": false,
            "description": "Custom redirect URI (used by extensions for PKCE flow)",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "code_challenge",
            "required": false,
            "description": "PKCE code challenge",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "code_challenge_method",
            "required": false,
            "description": "PKCE code challenge method (S256)",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Login page HTML"
          },
          "302": {
            "description": "Redirect to WorkOS authorization URL"
          },
          "400": {
            "description": "Bad request"
          }
        },
        "x-counso-auth": "login"
      }
    }
  },
  "components": {
    "securitySchemes": {
      "WorkspaceApiKey": {
        "type": "http",
        "scheme": "bearer",
        "description": "A workspace API key issued by this Counso deployment. Permissions and resource access are checked for each operation."
      },
      "UserAccessToken": {
        "type": "http",
        "scheme": "bearer",
        "description": "A user OAuth access token issued for this Counso deployment. A workspace API key is not a substitute for a user token."
      },
      "BrowserSession": {
        "type": "apiKey",
        "in": "cookie",
        "name": "workos_session",
        "description": "The signed-in Counso browser session. External clients should use a user access token."
      }
    }
  }
}
```
