---
title: "获取对话反馈"
---
获取指定对话中的全部反馈记录。调用方须完成身份验证，并具备 read:conversation 权限。

```http
GET /api/v1/w/{wId}/assistant/conversations/{cId}/feedbacks
```

服务地址：`https://app.counso.ai`

## 认证

在 `Authorization: Bearer <token>` 中传入工作区 API key 或用户 OAuth access token。凭据须由当前 Counso 环境签发，并有权访问目标工作区与资源。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 | 工作区 ID |
| `cId` | 路径 | string | 是 | 对话 ID |

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 该对话的反馈记录列表 |
| 400 | 请求参数无效 |
| 401 | 未授权 |
| 403 | 禁止访问 |
| 404 | 未找到对话 |
| 500 | 内部服务器错误 |

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
    "/api/v1/w/{wId}/assistant/conversations/{cId}/feedbacks": {
      "get": {
        "summary": "Get feedbacks for a conversation",
        "description": "Returns every feedback entry recorded for the selected conversation. The authenticated caller must have the read:conversation scope.",
        "tags": [
          "Feedbacks"
        ],
        "parameters": [
          {
            "name": "wId",
            "in": "path",
            "description": "Workspace ID",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "cId",
            "in": "path",
            "description": "Conversation ID",
            "required": true,
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
            "description": "List of feedback entries for the conversation",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "feedbacks": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "messageId": {
                            "type": "string",
                            "description": "ID of the message that received feedback"
                          },
                          "agentMessageId": {
                            "type": "number",
                            "description": "ID of the agent message"
                          },
                          "userId": {
                            "type": "number",
                            "description": "ID of the user who gave feedback"
                          },
                          "thumbDirection": {
                            "type": "string",
                            "enum": [
                              "up",
                              "down"
                            ],
                            "description": "Direction of the thumb feedback"
                          },
                          "content": {
                            "type": "string",
                            "nullable": true,
                            "description": "Optional feedback content/comment"
                          },
                          "createdAt": {
                            "type": "number",
                            "description": "Timestamp when feedback was created"
                          },
                          "agentConfigurationId": {
                            "type": "string",
                            "description": "ID of the agent configuration"
                          },
                          "agentConfigurationVersion": {
                            "type": "number",
                            "description": "Version of the agent configuration"
                          },
                          "isConversationShared": {
                            "type": "boolean",
                            "description": "Whether the conversation was shared"
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
            "description": "Invalid request parameters"
          },
          "401": {
            "description": "Unauthorized"
          },
          "403": {
            "description": "Forbidden"
          },
          "404": {
            "description": "Conversation not found"
          },
          "500": {
            "description": "Internal server error"
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
    }
  }
}
```
