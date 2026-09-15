# List agent configurations

Private session interface. Supplies the signed-in user's collection of workspace agent configurations.

```http
GET /api/w/{wId}/assistant/agent_configurations
```

Base URL: `https://app.counso.ai`

## Authentication

This operation requires a user OAuth access token in `Authorization: Bearer <token>`. A signed-in browser may use its Counso session cookie. A workspace API key does not supply user identity.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes | ID of the workspace |
| `view` | query | string | No | Filter agents by view Values: `all`, `analytics`, `list`, `favorites`, `published`, `admin_internal`, `manage_unrestricted`, `global`, `workspace` |
| `limit` | query | integer | No | Maximum number of results to return |
| `withUsage` | query | string | No | Include usage statistics Values: `true` |
| `withAuthors` | query | string | No | Include recent authors Values: `true` |
| `withFeedbacks` | query | string | No | Include feedback counts Values: `true` |
| `withEditors` | query | string | No | Include editors list Values: `true` |
| `sort` | query | string | No | Sort order |

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | Success |
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
    "/api/w/{wId}/assistant/agent_configurations": {
      "get": {
        "summary": "List agent configurations",
        "description": "Private session interface. Supplies the signed-in user's collection of workspace agent configurations.",
        "tags": [
          "Private Agents"
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
            "name": "view",
            "required": false,
            "description": "Filter agents by view",
            "schema": {
              "type": "string",
              "enum": [
                "all",
                "analytics",
                "list",
                "favorites",
                "published",
                "admin_internal",
                "manage_unrestricted",
                "global",
                "workspace"
              ]
            }
          },
          {
            "in": "query",
            "name": "limit",
            "required": false,
            "description": "Maximum number of results to return",
            "schema": {
              "type": "integer"
            }
          },
          {
            "in": "query",
            "name": "withUsage",
            "required": false,
            "description": "Include usage statistics",
            "schema": {
              "type": "string",
              "enum": [
                "true"
              ]
            }
          },
          {
            "in": "query",
            "name": "withAuthors",
            "required": false,
            "description": "Include recent authors",
            "schema": {
              "type": "string",
              "enum": [
                "true"
              ]
            }
          },
          {
            "in": "query",
            "name": "withFeedbacks",
            "required": false,
            "description": "Include feedback counts",
            "schema": {
              "type": "string",
              "enum": [
                "true"
              ]
            }
          },
          {
            "in": "query",
            "name": "withEditors",
            "required": false,
            "description": "Include editors list",
            "schema": {
              "type": "string",
              "enum": [
                "true"
              ]
            }
          },
          {
            "in": "query",
            "name": "sort",
            "required": false,
            "description": "Sort order",
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
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "agentConfigurations": {
                      "type": "array",
                      "items": {
                        "$ref": "#/components/schemas/PrivateLightAgentConfiguration"
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
      "PrivateLightAgentConfiguration": {
        "type": "object",
        "description": "Agent configuration as returned by the private list endpoint.",
        "required": [
          "id",
          "sId",
          "version",
          "name",
          "description",
          "pictureUrl",
          "status",
          "scope",
          "model",
          "maxStepsPerRun",
          "tags"
        ],
        "properties": {
          "id": {
            "type": "integer"
          },
          "sId": {
            "type": "string"
          },
          "version": {
            "type": "integer"
          },
          "versionCreatedAt": {
            "type": "string",
            "nullable": true
          },
          "versionAuthorId": {
            "type": "integer",
            "nullable": true
          },
          "name": {
            "type": "string"
          },
          "description": {
            "type": "string"
          },
          "instructions": {
            "type": "string",
            "nullable": true
          },
          "pictureUrl": {
            "type": "string"
          },
          "status": {
            "type": "string",
            "description": "Agent status",
            "enum": [
              "active",
              "archived",
              "draft",
              "pending",
              "disabled_by_admin",
              "disabled_missing_datasource",
              "disabled_free_workspace"
            ]
          },
          "scope": {
            "type": "string",
            "enum": [
              "global",
              "visible",
              "hidden"
            ]
          },
          "userFavorite": {
            "type": "boolean"
          },
          "model": {
            "type": "object",
            "properties": {
              "providerId": {
                "type": "string"
              },
              "modelId": {
                "type": "string"
              },
              "temperature": {
                "type": "number"
              },
              "reasoningEffort": {
                "type": "string",
                "enum": [
                  "none",
                  "light",
                  "medium",
                  "high"
                ]
              }
            }
          },
          "maxStepsPerRun": {
            "type": "integer"
          },
          "tags": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "sId": {
                  "type": "string"
                },
                "name": {
                  "type": "string"
                }
              }
            }
          },
          "templateId": {
            "type": "string",
            "nullable": true
          },
          "requestedGroupIds": {
            "type": "array",
            "items": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          "requestedSpaceIds": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "canRead": {
            "type": "boolean"
          },
          "canEdit": {
            "type": "boolean"
          },
          "lastAuthors": {
            "type": "array",
            "description": "Optional, returned when withAuthors query param is set",
            "items": {
              "type": "string"
            }
          },
          "editors": {
            "type": "array",
            "description": "Optional, returned when withEditors query param is set",
            "items": {
              "type": "object",
              "properties": {
                "sId": {
                  "type": "string"
                },
                "fullName": {
                  "type": "string"
                },
                "image": {
                  "type": "string",
                  "nullable": true
                }
              }
            }
          },
          "usage": {
            "type": "object",
            "description": "Optional, returned when withUsage query param is set",
            "properties": {
              "messageCount": {
                "type": "integer"
              },
              "conversationCount": {
                "type": "integer"
              },
              "userCount": {
                "type": "integer"
              },
              "timePeriodSec": {
                "type": "integer"
              }
            }
          },
          "feedbacks": {
            "type": "object",
            "description": "Optional, returned when withFeedbacks query param is set",
            "properties": {
              "up": {
                "type": "integer"
              },
              "down": {
                "type": "integer"
              }
            }
          }
        }
      }
    }
  }
}
```
