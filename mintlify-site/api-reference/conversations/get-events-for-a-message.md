---
title: "Get events for a message"
---
Returns the event records associated with a message in workspace {wId}.

```http
GET /api/v1/w/{wId}/assistant/conversations/{cId}/messages/{mId}/events
```

Base URL: `https://app.counso.ai`

## Authentication

Send a workspace API key or a user OAuth access token in `Authorization: Bearer <token>`. The credential must belong to this Counso deployment and have access to the requested workspace and resources.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes | ID of the workspace |
| `cId` | path | string | Yes | ID of the conversation |
| `mId` | path | string | Yes | ID of the message |
| `lastEventId` | query | string | No | ID of the last event received |

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | The events |
| 400 | Bad Request |
| 401 | Unauthorized |
| 404 | Not Found |
| 500 | Internal Server Error |

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
    "/api/v1/w/{wId}/assistant/conversations/{cId}/messages/{mId}/events": {
      "get": {
        "summary": "Get events for a message",
        "description": "Returns the event records associated with a message in workspace {wId}.",
        "tags": [
          "Conversations"
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
          },
          {
            "in": "path",
            "name": "mId",
            "required": true,
            "description": "ID of the message",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "lastEventId",
            "description": "ID of the last event received",
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
            "description": "The events",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "events": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "string",
                            "description": "ID of the event"
                          },
                          "type": {
                            "type": "string",
                            "description": "Type of the event"
                          },
                          "data": {
                            "$ref": "#/components/schemas/Message"
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "401": {
            "description": "Unauthorized"
          },
          "404": {
            "description": "Not Found"
          },
          "500": {
            "description": "Internal Server Error"
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
    },
    "schemas": {
      "Message": {
        "type": "object",
        "required": [
          "content",
          "mentions"
        ],
        "properties": {
          "content": {
            "type": "string",
            "description": "The content of the message. Should not be empty.",
            "example": "This is my message"
          },
          "mentions": {
            "type": "array",
            "description": "Empty array is accepted but won't trigger any agent.",
            "items": {
              "$ref": "#/components/schemas/Mention"
            }
          },
          "context": {
            "$ref": "#/components/schemas/Context"
          },
          "modelSelection": {
            "$ref": "#/components/schemas/ModelSelection"
          }
        }
      },
      "Context": {
        "type": "object",
        "required": [
          "username",
          "timezone"
        ],
        "properties": {
          "username": {
            "type": "string",
            "description": "Username in the current context",
            "example": "johndoe123"
          },
          "timezone": {
            "type": "string",
            "description": "User's timezone",
            "example": "America/New_York"
          },
          "fullName": {
            "type": "string",
            "description": "User's full name in the current context",
            "example": "John Doe"
          },
          "email": {
            "type": "string",
            "description": "User's email in the current context",
            "example": "john.doe@example.com"
          },
          "profilePictureUrl": {
            "type": "string",
            "description": "URL of the user's profile picture",
            "example": "https://example.com/profiles/johndoe123.jpg"
          },
          "selectedSpaceIds": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "agenticMessageData": {
            "type": "object",
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "run_agent",
                  "agent_handover"
                ],
                "description": "Type of the agentic message"
              },
              "originMessageId": {
                "type": "string",
                "description": "ID of the origin message",
                "example": "2b8e4f6a0c"
              }
            }
          }
        }
      },
      "Mention": {
        "type": "object",
        "properties": {
          "configurationId": {
            "type": "string",
            "description": "ID of the mentioned agent configuration",
            "example": "7f3a9c2b1e"
          }
        }
      },
      "ModelSelection": {
        "type": "object",
        "description": "Optional per-message model and reasoning-effort override applied to the\nmentioned agent(s). When omitted, each agent runs its configured model.\nA provider/model pair that is not authorized for the workspace is\nrejected with a 400 (`model_disabled`), it does not fall back to the\nagent's configured model. A malformed object, or an unknown reasoning\neffort, also results in a 400.\n",
        "required": [
          "providerId",
          "modelId"
        ],
        "properties": {
          "providerId": {
            "type": "string",
            "description": "The model provider id (e.g. \"anthropic\", \"openai\", \"google_ai_studio\").",
            "example": "anthropic"
          },
          "modelId": {
            "type": "string",
            "description": "The model id to run (e.g. \"claude-sonnet-4-20250514\").",
            "example": "claude-sonnet-4-20250514"
          },
          "reasoningEffort": {
            "type": "string",
            "enum": [
              "none",
              "light",
              "medium",
              "high"
            ],
            "description": "Optional reasoning effort. Honored only if the resolved model supports it.",
            "example": "medium"
          }
        }
      }
    }
  }
}
```
