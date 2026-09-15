# Create a message

Adds a message to conversation {cId} under workspace {wId}.

```http
POST /api/v1/w/{wId}/assistant/conversations/{cId}/messages
```

Base URL: `https://app.counso.ai`

## Authentication

Send a workspace API key or a user OAuth access token in `Authorization: Bearer <token>`. The credential must belong to this Counso deployment and have access to the requested workspace and resources.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes | ID of the workspace |
| `cId` | path | string | Yes | ID of the conversation |

## Request body

`Content-Type: application/json`

| Field | Type | Required |
| --- | --- | --- |
| `content` | string | Yes |
| `mentions` | array[object] | Yes |
| `context` | object | No |
| `modelSelection` | object | No |

Field constraints and nested structures are defined in the specification below.

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | Message created successfully. |
| 400 | Bad Request. Missing or invalid parameters. |
| 401 | Unauthorized. Invalid or missing authentication token. |
| 403 | Forbidden. Workspace or usage limits exceeded, or access denied. |
| 429 | Rate limit exceeded. |
| 500 | Internal Server Error. |

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
    "/api/v1/w/{wId}/assistant/conversations/{cId}/messages": {
      "post": {
        "summary": "Create a message",
        "description": "Adds a message to conversation {cId} under workspace {wId}.",
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
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Message"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Message created successfully.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Message"
                }
              }
            }
          },
          "400": {
            "description": "Bad Request. Missing or invalid parameters."
          },
          "401": {
            "description": "Unauthorized. Invalid or missing authentication token."
          },
          "403": {
            "description": "Forbidden. Workspace or usage limits exceeded, or access denied."
          },
          "429": {
            "description": "Rate limit exceeded."
          },
          "500": {
            "description": "Internal Server Error."
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
