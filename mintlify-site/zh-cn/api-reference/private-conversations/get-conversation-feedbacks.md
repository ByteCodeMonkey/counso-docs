---
title: "获取当前用户提交的对话反馈"
---
会话接口：读取当前已认证用户为指定对话提交的全部反馈。

```http
GET /api/w/{wId}/assistant/conversations/{cId}/feedbacks
```

服务地址：`https://app.counso.ai`

## 认证

此接口需要用户身份：外部客户端通过 `Authorization: Bearer <token>` 传入用户 OAuth access token；已登录的浏览器也可使用 Counso 会话 Cookie。工作区 API key 不能代替用户身份。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 | 工作区 ID |
| `cId` | 路径 | string | 是 | 对话 ID |

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 已成功获取反馈记录 |
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
    "/api/w/{wId}/assistant/conversations/{cId}/feedbacks": {
      "get": {
        "summary": "Get conversation feedbacks",
        "description": "Private session interface. Retrieves feedback that the signed-in user submitted for the specified conversation.",
        "tags": [
          "Private Conversations"
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
            "UserAccessToken": []
          },
          {
            "BrowserSession": []
          }
        ],
        "responses": {
          "200": {
            "description": "Successfully retrieved feedbacks",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "feedbacks": {
                      "type": "array",
                      "items": {
                        "$ref": "#/components/schemas/PrivateFeedback"
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
      "PrivateFeedback": {
        "type": "object",
        "description": "User feedback on an agent message.",
        "required": [
          "id",
          "sId",
          "messageId",
          "agentMessageId",
          "userId",
          "thumbDirection",
          "agentConfigurationId",
          "agentConfigurationVersion",
          "isConversationShared",
          "dismissed",
          "createdAt"
        ],
        "properties": {
          "id": {
            "type": "integer"
          },
          "sId": {
            "type": "string"
          },
          "messageId": {
            "type": "string"
          },
          "agentMessageId": {
            "type": "integer"
          },
          "userId": {
            "type": "integer"
          },
          "thumbDirection": {
            "type": "string",
            "enum": [
              "up",
              "down"
            ]
          },
          "content": {
            "type": "string",
            "nullable": true,
            "description": "Optional text feedback from the user"
          },
          "createdAt": {
            "type": "string",
            "format": "date-time"
          },
          "agentConfigurationId": {
            "type": "string"
          },
          "agentConfigurationVersion": {
            "type": "integer"
          },
          "isConversationShared": {
            "type": "boolean"
          },
          "dismissed": {
            "type": "boolean"
          }
        }
      }
    }
  }
}
```
