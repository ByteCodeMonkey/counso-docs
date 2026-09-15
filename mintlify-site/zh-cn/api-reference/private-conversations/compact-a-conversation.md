---
title: "压缩对话上下文"
---
会话接口：总结较早的对话消息并写入压缩摘要；需要指定用于生成摘要的模型。

```http
POST /api/w/{wId}/assistant/conversations/{cId}/compactions
```

服务地址：`https://app.counso.ai`

## 认证

此接口需要用户身份：外部客户端通过 `Authorization: Bearer <token>` 传入用户 OAuth access token；已登录的浏览器也可使用 Counso 会话 Cookie。工作区 API key 不能代替用户身份。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 | 工作区 ID |
| `cId` | 路径 | string | 是 | 对话 ID |

## 请求体

`Content-Type: application/json`

| 字段 | 类型 | 必填 |
| --- | --- | --- |
| `model` | object | 是 |

完整字段约束与嵌套结构见下方接口规范。

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 已开始压缩对话 |
| 400 | 请求正文无效 |
| 404 | 未找到对话 |
| 409 | 冲突：对话压缩或智能体消息已在运行 |

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
    "/api/w/{wId}/assistant/conversations/{cId}/compactions": {
      "post": {
        "summary": "Compact a conversation",
        "description": "Private session interface. Summarizes earlier messages into a compaction entry using the model supplied for summarization.",
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
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "model"
                ],
                "properties": {
                  "model": {
                    "type": "object",
                    "required": [
                      "providerId",
                      "modelId"
                    ],
                    "properties": {
                      "providerId": {
                        "type": "string"
                      },
                      "modelId": {
                        "type": "string"
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
            "description": "Compaction started",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "compactionMessage": {
                      "$ref": "#/components/schemas/PrivateCompactionMessage"
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Invalid request body"
          },
          "404": {
            "description": "Conversation not found"
          },
          "409": {
            "description": "Conflict — compaction or agent message is already running"
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
      "PrivateCompactionMessage": {
        "type": "object",
        "description": "A compaction message summarizing earlier conversation content.",
        "required": [
          "type",
          "sId",
          "status",
          "version",
          "rank",
          "created"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "compaction_message"
            ]
          },
          "id": {
            "type": "integer"
          },
          "compactionMessageId": {
            "type": "integer"
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
          "sourceConversationId": {
            "type": "string",
            "nullable": true
          },
          "status": {
            "type": "string",
            "enum": [
              "created",
              "succeeded",
              "failed"
            ]
          },
          "content": {
            "type": "string",
            "nullable": true,
            "description": "Compacted summary. Null while status is \"created\"."
          }
        }
      }
    }
  }
}
```
