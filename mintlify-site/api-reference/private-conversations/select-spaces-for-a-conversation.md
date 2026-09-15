---
title: "Select Spaces for a conversation"
---
Private session interface. Adds regular Spaces to the conversation's explicitly selected scope.

```http
POST /api/w/{wId}/assistant/conversations/{cId}/selected_spaces
```

Base URL: `https://app.counso.ai`

## Authentication

This operation requires a user OAuth access token in `Authorization: Bearer <token>`. A signed-in browser may use its Counso session cookie. A workspace API key does not supply user identity.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes |  |
| `cId` | path | string | Yes |  |

## Request body

`Content-Type: application/json`

| Field | Type | Required |
| --- | --- | --- |
| `mode` | string | Yes |
| `spaceIds` | array[string] | Yes |

Field constraints and nested structures are defined in the specification below.

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | Selected Spaces and effective ACL summary. |
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
    "/api/w/{wId}/assistant/conversations/{cId}/selected_spaces": {
      "post": {
        "summary": "Select Spaces for a conversation",
        "description": "Private session interface. Adds regular Spaces to the conversation's explicitly selected scope.",
        "tags": [
          "Private Conversations"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "wId",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "path",
            "name": "cId",
            "required": true,
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
                "type": "object",
                "required": [
                  "mode",
                  "spaceIds"
                ],
                "properties": {
                  "mode": {
                    "type": "string",
                    "enum": [
                      "add"
                    ]
                  },
                  "spaceIds": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    }
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Selected Spaces and effective ACL summary.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "selectedSpaces": {
                      "type": "array",
                      "items": {
                        "allOf": [
                          {
                            "$ref": "#/components/schemas/PrivateSpace"
                          },
                          {
                            "type": "object",
                            "properties": {
                              "selected": {
                                "type": "boolean"
                              }
                            }
                          }
                        ]
                      }
                    },
                    "effectiveAcl": {
                      "type": "object",
                      "properties": {
                        "spaceIds": {
                          "type": "array",
                          "items": {
                            "type": "string"
                          }
                        },
                        "viewerMustHaveAll": {
                          "type": "boolean"
                        }
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
