---
title: "Update a conversation"
---
Private session interface. Changes the conversation title, read state, Space assignment, or URL-access mode.

```http
PATCH /api/w/{wId}/assistant/conversations/{cId}
```

Base URL: `https://app.counso.ai`

## Authentication

This operation requires a user OAuth access token in `Authorization: Bearer <token>`. A signed-in browser may use its Counso session cookie. A workspace API key does not supply user identity.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes | ID of the workspace |
| `cId` | path | string | Yes | ID of the conversation |

## Request body

`Content-Type: application/json`

Field constraints and nested structures are defined in the specification below.

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | Successfully updated conversation |
| 401 | Unauthorized |

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
    "/api/w/{wId}/assistant/conversations/{cId}": {
      "patch": {
        "summary": "Update a conversation",
        "description": "Private session interface. Changes the conversation title, read state, Space assignment, or URL-access mode.",
        "tags": [
          "Private Conversations"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "wId",
            "required": true,
            "description": "ID of the workspace",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "path",
            "name": "cId",
            "required": true,
            "description": "ID of the conversation",
            "schema": {
              "type": "string"
            }
          }
        ],
        "security": [
          {
            "UserAccessToken": []
          },
          {
            "BrowserSession": []
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "oneOf": [
                  {
                    "type": "object",
                    "required": [
                      "title"
                    ],
                    "properties": {
                      "title": {
                        "type": "string"
                      }
                    }
                  },
                  {
                    "type": "object",
                    "required": [
                      "read"
                    ],
                    "properties": {
                      "read": {
                        "type": "boolean"
                      }
                    }
                  },
                  {
                    "type": "object",
                    "required": [
                      "spaceId"
                    ],
                    "properties": {
                      "spaceId": {
                        "type": "string"
                      }
                    }
                  },
                  {
                    "type": "object",
                    "required": [
                      "accessMode"
                    ],
                    "properties": {
                      "accessMode": {
                        "type": "string",
                        "enum": [
                          "participants_only",
                          "workspace_members"
                        ]
                      }
                    }
                  }
                ]
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Successfully updated conversation",
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
          "401": {
            "description": "Unauthorized"
          }
        },
        "x-counso-auth": "user"
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
