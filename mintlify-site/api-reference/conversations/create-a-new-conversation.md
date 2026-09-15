---
title: "Create a new conversation"
---
Opens a fresh conversation in workspace {wId}.

```http
POST /api/v1/w/{wId}/assistant/conversations
```

Base URL: `https://app.counso.ai`

## Authentication

Send a workspace API key or a user OAuth access token in `Authorization: Bearer <token>`. The credential must belong to this Counso deployment and have access to the requested workspace and resources.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes | ID of the workspace |

## Request body

`Content-Type: application/json`

| Field | Type | Required |
| --- | --- | --- |
| `message` | object | Yes |
| `contentFragments` | array[object] | No |
| `title` | string | No |
| `skipToolsValidation` | boolean | No |
| `blocking` | boolean | No |
| `spaceId` | string | No |

Field constraints and nested structures are defined in the specification below.

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | Conversation created successfully. |
| 400 | Bad Request |
| 401 | Unauthorized |
| 429 | Rate limit exceeded. |
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
    "/api/v1/w/{wId}/assistant/conversations": {
      "post": {
        "summary": "Create a new conversation",
        "description": "Opens a fresh conversation in workspace {wId}.",
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
                "type": "object",
                "required": [
                  "message"
                ],
                "properties": {
                  "message": {
                    "$ref": "#/components/schemas/Message"
                  },
                  "contentFragments": {
                    "type": "array",
                    "items": {
                      "$ref": "#/components/schemas/ContentFragment"
                    },
                    "description": "The list of content fragments to attach to this conversation (optional)"
                  },
                  "title": {
                    "type": "string",
                    "description": "The title of the conversation",
                    "example": "My conversation"
                  },
                  "skipToolsValidation": {
                    "type": "boolean",
                    "description": "Whether to skip the tools validation of the agent messages triggered by this user message (optional, defaults to false)",
                    "example": false
                  },
                  "blocking": {
                    "type": "boolean",
                    "description": "Whether to wait for the agent to generate the initial message. If true the query will wait for the agent's answer. If false (default), the API will return a conversation ID directly and you will need to use streaming events to get the messages.",
                    "example": true
                  },
                  "spaceId": {
                    "type": "string",
                    "description": "The sId of the space (project) in which to create the conversation (optional). If not provided, the conversation is created outside projects",
                    "example": "space_abc123"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Conversation created successfully.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Conversation"
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
          "429": {
            "description": "Rate limit exceeded."
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
      "ContentFragment": {
        "type": "object",
        "required": [
          "title"
        ],
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the content fragment",
            "example": "My content fragment"
          },
          "content": {
            "type": "string",
            "description": "The content of the content fragment (optional if `fileId` is set)",
            "example": "This is my content fragment extracted text"
          },
          "contentType": {
            "type": "string",
            "description": "The content type of the content fragment (optional if `fileId` is set)",
            "example": "text/plain"
          },
          "url": {
            "type": "string",
            "description": "The URL of the content fragment",
            "example": "https://example.com/content"
          },
          "fileId": {
            "type": "string",
            "description": "The id of the previously uploaded file (optional if `content` and `contentType` are set)",
            "example": "fil_123456"
          },
          "path": {
            "type": "string",
            "nullable": true,
            "description": "Path of this file inside the sandbox conversation mount.",
            "example": "conversation/report.csv"
          },
          "processedPath": {
            "type": "string",
            "nullable": true,
            "description": "Path of the plain-text sibling of this file inside the sandbox conversation mount (e.g. an audio transcript), when it has one.",
            "example": "conversation/voice.processed.txt"
          },
          "skipFileProcessing": {
            "type": "boolean",
            "description": "Whether upload-time file processing was skipped."
          },
          "nodeId": {
            "type": "string",
            "description": "The id of the content node (optional if `content` and `contentType` are set)",
            "example": "node_123456"
          },
          "nodeDataSourceViewId": {
            "type": "string",
            "description": "The id of the data source view (optional if `content` and `contentType` are set)",
            "example": "dsv_123456"
          },
          "context": {
            "$ref": "#/components/schemas/Context"
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
      "Conversation": {
        "type": "object",
        "properties": {
          "conversation": {
            "type": "object",
            "properties": {
              "id": {
                "type": "integer",
                "example": 67890
              },
              "created": {
                "type": "integer",
                "example": 1625097600
              },
              "sId": {
                "type": "string",
                "description": "Unique string identifier for the conversation",
                "example": "3d8f6a2c1b"
              },
              "owner": {
                "$ref": "#/components/schemas/Workspace"
              },
              "title": {
                "type": "string",
                "description": "Title of the conversation",
                "example": "Customer Inquiry #1234"
              },
              "visibility": {
                "type": "string",
                "description": "Visibility setting of the conversation",
                "example": "private"
              },
              "content": {
                "type": "array",
                "items": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "id": {
                        "type": "integer",
                        "example": 1
                      },
                      "sId": {
                        "type": "string",
                        "description": "Unique string identifier for the message",
                        "example": "9e7d5c3a1f"
                      },
                      "type": {
                        "type": "string",
                        "description": "Type of the message",
                        "example": "human"
                      },
                      "visibility": {
                        "type": "string",
                        "description": "Visibility setting of the message",
                        "example": "visible"
                      },
                      "version": {
                        "type": "integer",
                        "example": 1
                      },
                      "created": {
                        "type": "integer",
                        "example": 1625097700
                      },
                      "user": {
                        "$ref": "#/components/schemas/User"
                      },
                      "mentions": {
                        "type": "array",
                        "items": {
                          "$ref": "#/components/schemas/Mention"
                        }
                      },
                      "content": {
                        "type": "string",
                        "description": "Content of the message",
                        "example": "Hello, I need help with my order."
                      },
                      "context": {
                        "$ref": "#/components/schemas/Context"
                      },
                      "agentMessageId": {
                        "type": "integer",
                        "example": 1
                      },
                      "parentMessageId": {
                        "type": "string",
                        "description": "ID of the parent message",
                        "example": "2b8e4f6a0c"
                      },
                      "status": {
                        "type": "string",
                        "description": "Status of the message",
                        "example": "completed"
                      },
                      "actions": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "generatedFiles": {
                              "type": "array",
                              "description": "Files generated by this action. Path-backed files have `fileId: null`\nand can be downloaded through the conversation files endpoint using\n`filePath`.\n",
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
                                    "description": "Canonical scoped path for path-backed files, as surfaced by agent file system tools."
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
                                  "hidden": {
                                    "type": "boolean"
                                  },
                                  "isInProjectContext": {
                                    "type": "boolean"
                                  }
                                }
                              }
                            }
                          }
                        }
                      },
                      "chainOfThought": {
                        "type": "string",
                        "nullable": true,
                        "description": "Chain of thought for the message",
                        "example": "The user is asking about their order. I should first greet them and then ask for their order number."
                      },
                      "rawContents": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "step": {
                              "type": "integer",
                              "example": 1
                            },
                            "content": {
                              "type": "string",
                              "description": "Content for each step",
                              "example": "Hello! I'd be happy to help you with your order. Could you please provide your order number?"
                            }
                          }
                        }
                      },
                      "error": {
                        "type": "string",
                        "nullable": true,
                        "description": "Error message, if any",
                        "example": null
                      },
                      "configuration": {
                        "$ref": "#/components/schemas/AgentConfiguration"
                      }
                    }
                  }
                }
              }
            }
          }
        }
      },
      "AgentConfiguration": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "example": 12345
          },
          "sId": {
            "type": "string",
            "description": "Unique string identifier for the agent configuration",
            "example": "7f3a9c2b1e"
          },
          "version": {
            "type": "integer",
            "example": 2
          },
          "versionCreatedAt": {
            "type": "string",
            "nullable": true,
            "description": "Timestamp of when the version was created",
            "example": "2023-06-15T14:30:00Z"
          },
          "versionAuthorId": {
            "type": "string",
            "nullable": true,
            "description": "ID of the user who created this version",
            "example": "0ec9852c2f"
          },
          "name": {
            "type": "string",
            "description": "Name of the agent configuration",
            "example": "Customer Support Agent"
          },
          "description": {
            "type": "string",
            "description": "Description of the agent configuration",
            "example": "An AI agent designed to handle customer support inquiries"
          },
          "instructions": {
            "type": "string",
            "nullable": true,
            "description": "Instructions for the agent",
            "example": "Always greet the customer politely and try to resolve their issue efficiently."
          },
          "pictureUrl": {
            "type": "string",
            "description": "URL of the agent's picture",
            "example": "https://example.com/agent-images/support-agent.png"
          },
          "status": {
            "type": "string",
            "description": "Current status of the agent configuration",
            "example": "active"
          },
          "scope": {
            "type": "string",
            "description": "Scope of the agent configuration",
            "example": "workspace"
          },
          "userFavorite": {
            "type": "boolean",
            "description": "Status of the user favorite for this configuration",
            "example": true
          },
          "model": {
            "type": "object",
            "properties": {
              "providerId": {
                "type": "string",
                "description": "ID of the model provider",
                "example": "openai"
              },
              "modelId": {
                "type": "string",
                "description": "ID of the specific model",
                "example": "gpt-4"
              },
              "temperature": {
                "type": "number",
                "example": 0.7
              }
            }
          },
          "actions": {
            "type": "array",
            "example": []
          },
          "skills": {
            "type": "array",
            "description": "Skills attached to the agent. Returned by the agent GET endpoints (list and single-agent) whatever the requested variant. Empty both for an agent with no skill and for an agent whose details were redacted for the caller (canRead false).",
            "items": {
              "$ref": "#/components/schemas/AgentSkill"
            }
          },
          "tags": {
            "type": "array",
            "description": "Tags attached to the agent",
            "items": {
              "type": "object",
              "properties": {
                "sId": {
                  "type": "string",
                  "example": "3f9d1c7a5b"
                },
                "name": {
                  "type": "string",
                  "example": "Support"
                },
                "kind": {
                  "type": "string",
                  "enum": [
                    "standard",
                    "protected"
                  ]
                }
              }
            }
          },
          "requestedSpaceIds": {
            "type": "array",
            "description": "Identifiers of the spaces the agent needs access to",
            "items": {
              "type": "string"
            },
            "example": [
              "vlt_a1b2c3d4e5"
            ]
          },
          "maxStepsPerRun": {
            "type": "integer",
            "example": 10
          },
          "templateId": {
            "type": "string",
            "nullable": true,
            "description": "ID of the template used for this configuration",
            "example": "b4e2f1a9c7"
          }
        }
      },
      "AgentSkill": {
        "type": "object",
        "description": "A skill attached to an agent configuration.",
        "properties": {
          "sId": {
            "type": "string",
            "description": "Unique string identifier for the skill",
            "example": "skill_abc123"
          },
          "name": {
            "type": "string",
            "description": "Name of the skill",
            "example": "Customer Support"
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
      },
      "User": {
        "type": "object",
        "properties": {
          "sId": {
            "type": "string",
            "description": "Unique string identifier for the user",
            "example": "0ec9852c2f"
          },
          "id": {
            "type": "integer",
            "example": 12345
          },
          "createdAt": {
            "type": "integer",
            "example": 1625097600
          },
          "username": {
            "type": "string",
            "description": "User's chosen username",
            "example": "johndoe"
          },
          "email": {
            "type": "string",
            "description": "User's email address",
            "example": "john.doe@example.com"
          },
          "firstName": {
            "type": "string",
            "description": "User's first name",
            "example": "John"
          },
          "lastName": {
            "type": "string",
            "description": "User's last name",
            "example": "Doe"
          },
          "fullName": {
            "type": "string",
            "description": "User's full name",
            "example": "John Doe"
          },
          "provider": {
            "type": "string",
            "description": "Authentication provider used by the user",
            "example": "google"
          },
          "image": {
            "type": "string",
            "description": "URL of the user's profile image",
            "example": "https://example.com/profile/johndoe.jpg"
          }
        }
      },
      "Workspace": {
        "type": "object",
        "required": [
          "regionalModelsOnly"
        ],
        "properties": {
          "id": {
            "type": "integer",
            "example": 67890
          },
          "sId": {
            "type": "string",
            "description": "Unique string identifier for the workspace",
            "example": "dQFf9l5FQY"
          },
          "name": {
            "type": "string",
            "description": "Name of the workspace",
            "example": "My Awesome Workspace"
          },
          "role": {
            "type": "string",
            "description": "User's role in the workspace",
            "example": "admin"
          },
          "segmentation": {
            "type": "string",
            "nullable": true,
            "description": "Segmentation information for the workspace",
            "example": "enterprise"
          },
          "flags": {
            "type": "array",
            "items": {
              "type": "string",
              "description": "Feature flags enabled for the workspace"
            },
            "example": [
              "advanced_analytics",
              "beta_features"
            ]
          },
          "ssoEnforced": {
            "type": "boolean",
            "example": true
          },
          "regionalModelsOnly": {
            "type": "boolean",
            "description": "When true, only models whose regionalAvailability includes the workspace's region are usable.",
            "example": false
          },
          "whiteListedProviders": {
            "type": "array",
            "items": {
              "type": "string",
              "description": "List of allowed authentication providers"
            },
            "example": [
              "google",
              "github"
            ]
          },
          "defaultEmbeddingProvider": {
            "type": "string",
            "nullable": true,
            "description": "Default provider for embeddings in the workspace",
            "example": "openai"
          }
        }
      }
    }
  }
}
```
