---
title: "List spaces"
---
Private session interface. Provides the collection of Spaces in the workspace.

```http
GET /api/w/{wId}/spaces
```

Base URL: `https://app.counso.ai`

## Authentication

This operation requires a user OAuth access token in `Authorization: Bearer <token>`. A signed-in browser may use its Counso session cookie. A workspace API key does not supply user identity.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes | ID of the workspace |
| `role` | query | string | No | Filter by role (e.g. admin to list all workspace spaces) |
| `kind` | query | array[string] | No | Filter by one or more space kinds. Repeat the parameter to include several kinds. |

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | Success |
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
    "/api/w/{wId}/spaces": {
      "get": {
        "summary": "List spaces",
        "description": "Private session interface. Provides the collection of Spaces in the workspace.",
        "tags": [
          "Private Spaces"
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
            "in": "query",
            "name": "role",
            "required": false,
            "description": "Filter by role (e.g. admin to list all workspace spaces)",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "kind",
            "required": false,
            "description": "Filter by one or more space kinds. Repeat the parameter to include several kinds.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "array",
              "items": {
                "type": "string",
                "enum": [
                  "global",
                  "system",
                  "conversations",
                  "regular",
                  "project"
                ]
              }
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
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "spaces": {
                      "type": "array",
                      "items": {
                        "oneOf": [
                          {
                            "$ref": "#/components/schemas/PrivateSpace"
                          },
                          {
                            "$ref": "#/components/schemas/PrivateProject"
                          }
                        ]
                      }
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
    },
    "schemas": {
      "PrivateProject": {
        "type": "object",
        "description": "A project space with additional metadata.",
        "allOf": [
          {
            "$ref": "#/components/schemas/PrivateSpace"
          },
          {
            "type": "object",
            "properties": {
              "groupIds": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "isRestricted": {
                "type": "boolean"
              },
              "description": {
                "type": "string",
                "nullable": true
              },
              "isMember": {
                "type": "boolean"
              },
              "archivedAt": {
                "type": "integer",
                "nullable": true
              },
              "todoGenerationEnabled": {
                "type": "boolean",
                "description": "Whether automatic todo suggestions from project activity are enabled."
              },
              "lastTodoAnalysisAt": {
                "type": "integer",
                "nullable": true,
                "description": "Unix timestamp (ms) of the last automatic todo suggestion scan, if any."
              },
              "pinnedFramePath": {
                "type": "string",
                "nullable": true,
                "description": "Scoped path to the frame file pinned as the Pod banner (e.g. project/banner.html)."
              },
              "frameTabs": {
                "type": "array",
                "description": "Frames promoted as custom Pod tabs (shared for all members).",
                "items": {
                  "type": "object",
                  "required": [
                    "path",
                    "title",
                    "icon"
                  ],
                  "properties": {
                    "path": {
                      "type": "string",
                      "description": "Canonical scoped path to the frame file in the Pod filesystem."
                    },
                    "title": {
                      "type": "string",
                      "description": "Display title for the tab."
                    },
                    "icon": {
                      "type": "string",
                      "description": "Action icon name (e.g. ActionDashboardIcon)."
                    }
                  }
                }
              },
              "tabsOrder": {
                "type": "array",
                "description": "Interleaved system tab ids and frame paths before Settings.",
                "items": {
                  "type": "string"
                }
              }
            }
          }
        ]
      },
      "PrivateSpace": {
        "type": "object",
        "description": "A space in the workspace.",
        "required": [
          "sId",
          "name",
          "kind"
        ],
        "properties": {
          "sId": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "kind": {
            "type": "string",
            "enum": [
              "global",
              "system",
              "conversations",
              "regular",
              "project"
            ]
          },
          "createdAt": {
            "type": "integer"
          },
          "updatedAt": {
            "type": "integer"
          }
        }
      }
    }
  }
}
```
