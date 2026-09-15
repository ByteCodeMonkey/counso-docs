---
title: "Download a conversation-scoped file by path"
---
Streams a conversation-mounted file using its scoped path. Prefer the canonical filePath listed under a message action's generatedFiles; the older conversation/foo.pdf form is also accepted. Paths belonging to another conversation or scope, including traversal with .., are rejected.

```http
GET /api/v1/w/{wId}/assistant/conversations/{cId}/files/{rel}
```

Base URL: `https://app.counso.ai`

## Authentication

Send a workspace API key or a user OAuth access token in `Authorization: Bearer <token>`. The credential must belong to this Counso deployment and have access to the requested workspace and resources.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes | ID of the workspace |
| `cId` | path | string | Yes | ID of the conversation |
| `rel` | path | string | Yes | Conversation-scoped file path: the canonical `filePath` returned in a message<br />action's `generatedFiles`, or the legacy `conversation/foo.pdf` form. Paths<br />scoped to another conversation or to a different scope are rejected. Path<br />traversal segments (`..`) are rejected.<br /> |

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | File content streamed directly. |
| 400 | Missing or invalid path parameters (e.g. missing or wrong scope prefix). |
| 403 | Resolved path is outside the conversation scope. |
| 404 | Conversation or file not found. |

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
    "/api/v1/w/{wId}/assistant/conversations/{cId}/files/{rel}": {
      "get": {
        "tags": [
          "Conversations"
        ],
        "summary": "Download a conversation-scoped file by path",
        "description": "Streams a conversation-mounted file using its scoped path. Prefer the canonical filePath listed under a message action's generatedFiles; the older conversation/foo.pdf form is also accepted. Paths belonging to another conversation or scope, including traversal with .., are rejected.",
        "parameters": [
          {
            "name": "wId",
            "in": "path",
            "required": true,
            "description": "ID of the workspace",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "cId",
            "in": "path",
            "required": true,
            "description": "ID of the conversation",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "rel",
            "in": "path",
            "required": true,
            "description": "Conversation-scoped file path: the canonical `filePath` returned in a message\naction's `generatedFiles`, or the legacy `conversation/foo.pdf` form. Paths\nscoped to another conversation or to a different scope are rejected. Path\ntraversal segments (`..`) are rejected.\n",
            "schema": {
              "type": "string"
            }
          }
        ],
        "security": [
          {
            "WorkspaceApiKey": []
          },
          {
            "UserAccessToken": []
          }
        ],
        "responses": {
          "200": {
            "description": "File content streamed directly.",
            "content": {
              "application/octet-stream": {
                "schema": {
                  "type": "string",
                  "format": "binary"
                }
              }
            }
          },
          "400": {
            "description": "Missing or invalid path parameters (e.g. missing or wrong scope prefix)."
          },
          "403": {
            "description": "Resolved path is outside the conversation scope."
          },
          "404": {
            "description": "Conversation or file not found."
          }
        },
        "x-counso-auth": "workspace"
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
