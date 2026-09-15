---
title: "Get a conversation credit attribution"
---
Private session interface. Reports the latest stable credits billed for completed messages directly in this conversation, plus additional attribution calculated only from model-input rows. In-progress messages appear after reaching a terminal state.

```http
GET /api/w/{wId}/assistant/conversations/{cId}/consumption
```

Base URL: `https://app.counso.ai`

## Authentication

This operation requires a user OAuth access token in `Authorization: Bearer <token>`. A signed-in browser may use its Counso session cookie. A workspace API key does not supply user identity.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes |  |
| `cId` | path | string | Yes |  |

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | Conversation credit attribution |
| 404 | Conversation not found |

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
    "/api/w/{wId}/assistant/conversations/{cId}/consumption": {
      "get": {
        "summary": "Get a conversation credit attribution",
        "description": "Private session interface. Reports the latest stable credits billed for completed messages directly in this conversation, plus additional attribution calculated only from model-input rows. In-progress messages appear after reaching a terminal state.",
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
        "responses": {
          "200": {
            "description": "Conversation credit attribution",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "required": [
                    "billedCredits",
                    "details"
                  ],
                  "properties": {
                    "billedCredits": {
                      "type": "number",
                      "description": "Latest stable credits billed across completed messages belonging directly to the conversation."
                    },
                    "details": {
                      "type": "object",
                      "allOf": [
                        {
                          "$ref": "#/components/schemas/PrivateConversationConsumptionDetails"
                        }
                      ],
                      "nullable": true
                    }
                  }
                }
              }
            }
          },
          "404": {
            "description": "Conversation not found"
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
      "PrivateConversationConsumptionDetails": {
        "type": "object",
        "description": "Additive attribution reconciled to the authoritative bill exclusively through model input rows. Each message uses its newest complete stored attribution version. Null when any billed message has no complete stored attribution.",
        "required": [
          "agentWorkCredits",
          "tools",
          "models",
          "agents"
        ],
        "properties": {
          "agentWorkCredits": {
            "type": "number",
            "description": "Agent work after assigning billing reconciliation exclusively to model input rows."
          },
          "tools": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PrivateConversationConsumptionToolDetails"
            }
          },
          "models": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PrivateConversationConsumptionModelDetails"
            }
          },
          "agents": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PrivateConversationConsumptionAgentDetails"
            }
          }
        }
      },
      "PrivateConversationConsumptionAgentDetails": {
        "type": "object",
        "required": [
          "agentId",
          "name",
          "pictureUrl",
          "billedCredits",
          "agentWorkCredits",
          "tools",
          "models"
        ],
        "properties": {
          "agentId": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "pictureUrl": {
            "type": "string",
            "nullable": true
          },
          "billedCredits": {
            "type": "number"
          },
          "agentWorkCredits": {
            "type": "number",
            "description": "Agent work after assigning billing reconciliation exclusively to model input rows."
          },
          "tools": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PrivateConversationConsumptionToolDetails"
            }
          },
          "models": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PrivateConversationConsumptionModelDetails"
            }
          }
        }
      },
      "PrivateConversationConsumptionModelDetails": {
        "type": "object",
        "required": [
          "providerId",
          "modelId",
          "displayName",
          "attributedCredits"
        ],
        "properties": {
          "providerId": {
            "type": "string"
          },
          "modelId": {
            "type": "string"
          },
          "displayName": {
            "type": "string"
          },
          "attributedCredits": {
            "type": "number",
            "description": "Model attribution after reconciling exclusively through its input rows."
          }
        }
      },
      "PrivateConversationConsumptionToolDetails": {
        "type": "object",
        "required": [
          "label",
          "internalMCPServerName",
          "toolName",
          "callCount",
          "attributedCredits",
          "directCredits",
          "pending"
        ],
        "properties": {
          "label": {
            "type": "string"
          },
          "internalMCPServerName": {
            "type": "string",
            "nullable": true
          },
          "toolName": {
            "type": "string"
          },
          "callCount": {
            "type": "integer"
          },
          "attributedCredits": {
            "type": "number",
            "description": "Share of billed credits after reconciling exclusively through model input rows."
          },
          "directCredits": {
            "type": "number"
          },
          "pending": {
            "type": "boolean"
          }
        }
      }
    }
  }
}
```
