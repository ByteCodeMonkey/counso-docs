---
title: "Revoke a session"
---
Revokes the WorkOS session named in session_id to sign that session out. This endpoint does not require a Bearer token.

```http
POST /api/workos/revoke-session
```

Base URL: `https://app.counso.ai`

## Authentication

Submit the session_id to revoke that user session. This sign-out endpoint does not require a Bearer token.

## Request body

`Content-Type: application/json`

| Field | Type | Required |
| --- | --- | --- |
| `session_id` | string | Yes |

Field constraints and nested structures are defined in the specification below.

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | Session revoked successfully |
| 400 | Invalid session_id |

## Specification

Download the complete [OpenAPI / Postman](/docs/developer-platform/counso-api-documentation/openapi-and-postman) files.

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
    "/api/workos/revoke-session": {
      "post": {
        "summary": "Revoke a session",
        "description": "Revokes the WorkOS session named in session_id to sign that session out. This endpoint does not require a Bearer token.",
        "tags": [
          "Private Authentication"
        ],
        "security": [],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "session_id"
                ],
                "properties": {
                  "session_id": {
                    "type": "string"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Session revoked successfully",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "success": {
                      "type": "boolean"
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Invalid session_id"
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
