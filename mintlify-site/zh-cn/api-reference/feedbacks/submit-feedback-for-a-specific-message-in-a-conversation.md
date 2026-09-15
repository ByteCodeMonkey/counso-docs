---
title: "提交消息反馈"
---
为对话中的指定消息提交赞或踩的反馈。调用方须完成身份验证，并具备 update:conversation 权限。

```http
POST /api/v1/w/{wId}/assistant/conversations/{cId}/messages/{mId}/feedbacks
```

服务地址：`https://app.counso.ai`

## 认证

在 `Authorization: Bearer <token>` 中传入工作区 API key 或用户 OAuth access token。凭据须由当前 Counso 环境签发，并有权访问目标工作区与资源。

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
| `thumbDirection` | string | 是 |
| `feedbackContent` | string | 否 |
| `isConversationShared` | boolean | 否 |

完整字段约束与嵌套结构见下方接口规范。

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 反馈已提交 |
| 400 | 请求参数或正文无效 |
| 401 | 未授权 |
| 404 | 未找到对话或消息 |

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
    "/api/v1/w/{wId}/assistant/conversations/{cId}/messages/{mId}/feedbacks": {
      "post": {
        "summary": "Submit feedback for a specific message in a conversation",
        "description": "Stores a thumbs-up or thumbs-down rating for a particular conversation message. The authenticated caller must have the update:conversation scope.",
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
          },
          {
            "name": "mId",
            "in": "path",
            "description": "Message ID",
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
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "thumbDirection"
                ],
                "properties": {
                  "thumbDirection": {
                    "type": "string",
                    "enum": [
                      "up",
                      "down"
                    ],
                    "description": "Direction of the thumb feedback"
                  },
                  "feedbackContent": {
                    "type": "string",
                    "description": "Optional feedback text content"
                  },
                  "isConversationShared": {
                    "type": "boolean",
                    "description": "Whether the conversation is shared"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Feedback submitted successfully",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "success": {
                      "type": "boolean"
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Invalid request parameters or body"
          },
          "401": {
            "description": "Unauthorized"
          },
          "404": {
            "description": "Conversation or message not found"
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
