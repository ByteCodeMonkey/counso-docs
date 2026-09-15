---
title: "编辑消息"
---
会话接口：编辑对话中现有用户消息的正文和提及对象。

```http
POST /api/w/{wId}/assistant/conversations/{cId}/messages/{mId}/edit
```

服务地址：`https://app.counso.ai`

## 认证

此接口需要用户身份：外部客户端通过 `Authorization: Bearer <token>` 传入用户 OAuth access token；已登录的浏览器也可使用 Counso 会话 Cookie。工作区 API key 不能代替用户身份。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 | 工作区 ID |
| `cId` | 路径 | string | 是 | 对话 ID |
| `mId` | 路径 | string | 是 | 消息 ID |

## 请求体

`Content-Type: application/json`

| 字段 | 类型 | 必填 |
| --- | --- | --- |
| `content` | string | 是 |
| `mentions` | array[object] | 是 |

完整字段约束与嵌套结构见下方接口规范。

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 已成功编辑消息 |
| 401 | 未授权 |

## 接口规范

可下载完整的[OpenAPI / Postman](/zh-cn/docs/developer-platform/counso-api-documentation/openapi-and-postman) 文件。

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
    "/api/w/{wId}/assistant/conversations/{cId}/messages/{mId}/edit": {
      "post": {
        "summary": "Edit a message",
        "description": "Private session interface. Revises an existing user message, including its text and mentions.",
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
                  "content",
                  "mentions"
                ],
                "properties": {
                  "content": {
                    "type": "string"
                  },
                  "mentions": {
                    "type": "array",
                    "items": {
                      "$ref": "#/components/schemas/PrivateMention"
                    }
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Successfully edited message",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "message": {
                      "$ref": "#/components/schemas/PrivateUserMessage"
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
      "PrivateMention": {
        "type": "object",
        "description": "A mention in a message (agent or user).",
        "properties": {
          "configurationId": {
            "type": "string",
            "description": "Agent configuration sId (for agent mentions)"
          },
          "type": {
            "type": "string",
            "enum": [
              "user"
            ],
            "description": "Present only for user mentions"
          },
          "userId": {
            "type": "string",
            "description": "User sId (for user mentions)"
          }
        }
      },
      "PrivateUserMessage": {
        "type": "object",
        "description": "A user message in a conversation.",
        "required": [
          "type",
          "sId",
          "content",
          "version",
          "rank",
          "created"
        ],
        "properties": {
          "id": {
            "type": "integer"
          },
          "type": {
            "type": "string",
            "enum": [
              "user_message"
            ]
          },
          "sId": {
            "type": "string"
          },
          "created": {
            "type": "integer"
          },
          "visibility": {
            "type": "string",
            "enum": [
              "visible",
              "deleted"
            ]
          },
          "version": {
            "type": "integer"
          },
          "rank": {
            "type": "integer"
          },
          "branchId": {
            "type": "string",
            "nullable": true,
            "description": "Legacy, always null. Branches were removed."
          },
          "user": {
            "type": "object",
            "nullable": true,
            "description": "The user who sent the message",
            "properties": {
              "sId": {
                "type": "string"
              },
              "username": {
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
          },
          "mentions": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PrivateMention"
            }
          },
          "richMentions": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PrivateRichMentionWithStatus"
            }
          },
          "content": {
            "type": "string"
          },
          "context": {
            "$ref": "#/components/schemas/PrivateUserMessageContext"
          },
          "reactions": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PrivateReaction"
            }
          }
        }
      },
      "PrivateReaction": {
        "type": "object",
        "description": "A reaction on a message.",
        "required": [
          "emoji",
          "users"
        ],
        "properties": {
          "emoji": {
            "type": "string"
          },
          "users": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "userId": {
                  "type": "string",
                  "nullable": true
                },
                "username": {
                  "type": "string"
                },
                "fullName": {
                  "type": "string",
                  "nullable": true
                }
              }
            }
          }
        }
      },
      "PrivateRichMentionWithStatus": {
        "type": "object",
        "description": "A rich mention with approval status, used in message responses.",
        "required": [
          "id",
          "type",
          "label",
          "pictureUrl",
          "description",
          "dismissed",
          "status"
        ],
        "properties": {
          "id": {
            "type": "string"
          },
          "type": {
            "type": "string",
            "enum": [
              "agent",
              "user"
            ]
          },
          "label": {
            "type": "string"
          },
          "pictureUrl": {
            "type": "string"
          },
          "description": {
            "type": "string"
          },
          "userFavorite": {
            "type": "boolean"
          },
          "dismissed": {
            "type": "boolean"
          },
          "status": {
            "type": "string",
            "enum": [
              "pending_conversation_access",
              "pending_project_membership",
              "approved",
              "rejected",
              "user_restricted_by_conversation_access",
              "agent_restricted_by_space_usage"
            ]
          }
        }
      },
      "PrivateUserMessageContext": {
        "type": "object",
        "description": "Context metadata for a user message.",
        "required": [
          "username",
          "timezone",
          "origin"
        ],
        "properties": {
          "username": {
            "type": "string"
          },
          "fullName": {
            "type": "string",
            "nullable": true
          },
          "email": {
            "type": "string",
            "nullable": true
          },
          "profilePictureUrl": {
            "type": "string",
            "nullable": true
          },
          "timezone": {
            "type": "string"
          },
          "origin": {
            "type": "string",
            "enum": [
              "web",
              "project_kickoff",
              "extension",
              "agent_sidekick",
              "analytics_panel",
              "api",
              "cli",
              "cli_programmatic",
              "email",
              "excel",
              "gsheet",
              "make",
              "n8n",
              "powerpoint",
              "raycast",
              "slack",
              "slack_workflow",
              "teams",
              "transcript",
              "triggered_programmatic",
              "triggered",
              "wakeup",
              "zapier",
              "zendesk",
              "onboarding_conversation"
            ]
          },
          "selectedSpaceIds": {
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        }
      }
    }
  }
}
```
