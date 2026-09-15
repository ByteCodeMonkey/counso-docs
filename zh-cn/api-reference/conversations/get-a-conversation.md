# 获取对话

获取指定工作区中的对话；可用 limit 和 lastValue 查询参数分页读取消息。

```http
GET /api/v1/w/{wId}/assistant/conversations/{cId}
```

服务地址：`https://app.counso.ai`

## 认证

在 `Authorization: Bearer <token>` 中传入工作区 API key 或用户 OAuth access token。凭据须由当前 Counso 环境签发，并有权访问目标工作区与资源。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 | 工作区 ID |
| `cId` | 路径 | string | 是 | 对话 ID |
| `limit` | 查询 | integer | 否 | 最多返回的消息数；省略时返回所有消息。 |
| `lastValue` | 查询 | string | 否 | 上一次响应中的游标值（消息 rank），用于获取下一页消息。 |

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 已成功获取对话。 |
| 400 | 请求错误：参数无效或缺失。 |
| 401 | 未授权：身份验证令牌无效或缺失。 |
| 404 | 未找到对话。 |
| 500 | 内部服务器错误。 |

## 接口规范

可下载完整的[OpenAPI / Postman](../../docs/developer-platform/counso-api-documentation/openapi-and-postman.md) 文件。

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
    "/api/v1/w/{wId}/assistant/conversations/{cId}": {
      "get": {
        "summary": "Get a conversation",
        "description": "Reads a workspace conversation and its messages; limit and lastValue can be supplied to page through the message content.",
        "tags": [
          "Conversations"
        ],
        "security": [
          {
            "WorkspaceApiKey": []
          },
          {
            "UserAccessToken": []
          }
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
            "in": "query",
            "name": "limit",
            "required": false,
            "description": "Maximum number of messages to return. When omitted, all messages are returned.",
            "schema": {
              "type": "integer"
            }
          },
          {
            "in": "query",
            "name": "lastValue",
            "required": false,
            "description": "Cursor value (message rank) from a previous response to fetch the next page of messages.",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Conversation retrieved successfully.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Conversation"
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
          "404": {
            "description": "Conversation not found."
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
