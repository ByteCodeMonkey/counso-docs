# 回答对话消息中的用户问题

提交对话中某条消息所含问题的答案。

```http
POST /api/v1/w/{wId}/assistant/conversations/{cId}/messages/{mId}/answer-question
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
| `actionId` | string | 是 |
| `answer` | object | 是 |

完整字段约束与嵌套结构见下方接口规范。

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 答案已成功提交 |
| 400 | 请求正文无效，或操作当前并未处于阻止状态 |
| 403 | 用户无权回答此问题 |
| 404 | 未找到对话、消息或操作 |
| 500 | 内部服务器错误 |

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
    "/api/v1/w/{wId}/assistant/conversations/{cId}/messages/{mId}/answer-question": {
      "post": {
        "summary": "Answer a user question in a conversation message",
        "description": "Submits the user's response to a question an Agent placed in a particular conversation message.",
        "tags": [
          "Conversations"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "wId",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Workspace ID"
          },
          {
            "in": "path",
            "name": "cId",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Conversation ID"
          },
          {
            "in": "path",
            "name": "mId",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Message ID"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "actionId",
                  "answer"
                ],
                "properties": {
                  "actionId": {
                    "type": "string",
                    "description": "ID of the action to answer"
                  },
                  "answer": {
                    "type": "object",
                    "required": [
                      "selectedOptions"
                    ],
                    "properties": {
                      "selectedOptions": {
                        "type": "array",
                        "items": {
                          "type": "integer"
                        },
                        "description": "Indices of selected options"
                      },
                      "customResponse": {
                        "type": "string",
                        "description": "Optional free-text response"
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Answer submitted successfully",
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
            "description": "Invalid request body or action not blocked"
          },
          "403": {
            "description": "User not authorized to answer this question"
          },
          "404": {
            "description": "Conversation, message, or action not found"
          },
          "500": {
            "description": "Internal server error"
          }
        },
        "security": [
          {
            "WorkspaceApiKey": []
          },
          {
            "UserAccessToken": []
          }
        ],
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
