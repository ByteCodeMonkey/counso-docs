---
title: "Get a single action"
---
Private session interface. Returns one action attached to an Agent message together with that message's status.

```http
GET /api/w/{wId}/assistant/conversations/{cId}/messages/{mId}/actions/{aId}
```

Base URL: `https://app.counso.ai`

## Authentication

This operation requires a user OAuth access token in `Authorization: Bearer <token>`. A signed-in browser may use its Counso session cookie. A workspace API key does not supply user identity.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes | ID of the workspace |
| `cId` | path | string | Yes | ID of the conversation |
| `mId` | path | string | Yes | ID of the message |
| `aId` | path | string | Yes | ID of the action |

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | Successfully retrieved the action |
| 400 | Invalid request (missing parameters or message is not an agent message) |
| 401 | Unauthorized |
| 404 | Conversation, message, or action not found |

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
    "/api/w/{wId}/assistant/conversations/{cId}/messages/{mId}/actions/{aId}": {
      "get": {
        "summary": "Get a single action",
        "description": "Private session interface. Returns one action attached to an Agent message together with that message's status.",
        "tags": [
          "Private Messages"
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
            "in": "path",
            "name": "aId",
            "required": true,
            "description": "ID of the action",
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
            "description": "Successfully retrieved the action",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "action": {
                      "$ref": "#/components/schemas/PrivateAgentMCPAction"
                    },
                    "messageStatus": {
                      "type": "string",
                      "enum": [
                        "created",
                        "succeeded",
                        "failed",
                        "cancelled",
                        "gracefully_stopped"
                      ]
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Invalid request (missing parameters or message is not an agent message)"
          },
          "401": {
            "description": "Unauthorized"
          },
          "404": {
            "description": "Conversation, message, or action not found"
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
      "PrivateAgentMCPAction": {
        "type": "object",
        "description": "An MCP action with its output.",
        "required": [
          "id",
          "sId",
          "createdAt",
          "updatedAt",
          "agentMessageId",
          "toolName",
          "functionCallName",
          "functionCallId",
          "params",
          "citationsAllocated",
          "status",
          "step",
          "generatedFiles",
          "output"
        ],
        "properties": {
          "id": {
            "type": "integer",
            "description": "Numeric model identifier"
          },
          "sId": {
            "type": "string",
            "description": "Unique string identifier"
          },
          "createdAt": {
            "type": "integer",
            "description": "Unix timestamp of creation"
          },
          "updatedAt": {
            "type": "integer",
            "description": "Unix timestamp of last update"
          },
          "agentMessageId": {
            "type": "integer",
            "description": "ID of the parent agent message"
          },
          "internalMCPServerName": {
            "type": "string",
            "nullable": true,
            "description": "Name of the internal MCP server, if any"
          },
          "toolName": {
            "type": "string",
            "description": "Name of the tool"
          },
          "mcpServerId": {
            "type": "string",
            "nullable": true,
            "description": "ID of the MCP server, if external"
          },
          "functionCallName": {
            "type": "string",
            "description": "Name of the function call"
          },
          "functionCallId": {
            "type": "string",
            "description": "ID of the function call"
          },
          "params": {
            "type": "object",
            "description": "Parameters passed to the tool"
          },
          "citationsAllocated": {
            "type": "integer",
            "description": "Number of citations allocated"
          },
          "status": {
            "type": "string",
            "enum": [
              "succeeded",
              "errored",
              "denied",
              "blocked_authentication_required",
              "blocked_file_authorization_required",
              "blocked_validation_required",
              "blocked_child_action_input_required",
              "blocked_user_answer_required",
              "ready_allowed_explicitly",
              "ready_allowed_implicitly",
              "running"
            ],
            "description": "Execution status of the tool"
          },
          "step": {
            "type": "integer",
            "description": "Step number in the agent execution"
          },
          "executionDurationMs": {
            "type": "integer",
            "nullable": true,
            "description": "Duration of execution in milliseconds"
          },
          "displayLabels": {
            "type": "object",
            "nullable": true,
            "properties": {
              "running": {
                "type": "string"
              },
              "done": {
                "type": "string"
              }
            }
          },
          "generatedFiles": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "fileId": {
                  "type": "string",
                  "nullable": true,
                  "description": "Counso file id for DB-backed files, or null for path-backed files."
                },
                "filePath": {
                  "type": "string",
                  "description": "Canonical scoped path for path-backed files."
                },
                "title": {
                  "type": "string"
                },
                "contentType": {
                  "type": "string"
                },
                "snippet": {
                  "type": "string",
                  "nullable": true
                },
                "createdAt": {
                  "type": "integer"
                },
                "updatedAt": {
                  "type": "integer"
                },
                "isInProjectContext": {
                  "type": "boolean"
                },
                "hidden": {
                  "type": "boolean"
                }
              }
            }
          },
          "output": {
            "type": "array",
            "nullable": true,
            "description": "Tool call result content",
            "items": {
              "type": "object"
            }
          },
          "citations": {
            "type": "object",
            "nullable": true,
            "description": "Map of citation key to citation object"
          }
        }
      }
    }
  }
}
```
