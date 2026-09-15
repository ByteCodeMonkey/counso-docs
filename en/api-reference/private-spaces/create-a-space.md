# Create a space

Private session interface. Creates a Space inside the workspace.

```http
POST /api/w/{wId}/spaces
```

Base URL: `https://app.counso.ai`

## Authentication

This operation requires a user OAuth access token in `Authorization: Bearer <token>`. A signed-in browser may use its Counso session cookie. A workspace API key does not supply user identity.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes | ID of the workspace |

## Request body

`Content-Type: application/json`

| Field | Type | Required |
| --- | --- | --- |
| `isRestricted` | boolean | Yes |
| `name` | string | Yes |
| `spaceKind` | string | Yes |
| `memberIds` | array[string] | No |
| `groupIds` | array[string] | No |

Field constraints and nested structures are defined in the specification below.

## Responses

| HTTP status | Description |
| --- | --- |
| 201 | Successfully created space |
| 401 | Unauthorized |

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
    "/api/w/{wId}/spaces": {
      "post": {
        "summary": "Create a space",
        "description": "Private session interface. Creates a Space inside the workspace.",
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
                  "isRestricted",
                  "name",
                  "spaceKind"
                ],
                "properties": {
                  "isRestricted": {
                    "type": "boolean"
                  },
                  "name": {
                    "type": "string"
                  },
                  "spaceKind": {
                    "type": "string",
                    "enum": [
                      "regular",
                      "project"
                    ]
                  },
                  "memberIds": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    },
                    "description": "The space's manual member list. Omitted or empty means the space starts with no manual member."
                  },
                  "groupIds": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    },
                    "description": "The groups given access to the space. Omitted or empty means no group has access to it."
                  }
                }
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Successfully created space",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "space": {
                      "$ref": "#/components/schemas/PrivateSpace"
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
