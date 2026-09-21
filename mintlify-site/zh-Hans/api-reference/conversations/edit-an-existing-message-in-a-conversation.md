---
title: "编辑对话中的现有消息"
---
编辑指定对话中的现有消息内容。

```http
POST /api/v1/w/{wId}/assistant/conversations/{cId}/messages/{mId}/edit
```

服务地址：`https://app.counso.ai`

## 认证

在 `Authorization: Bearer <token>` 中传入工作区 API key 或用户 OAuth access token。凭据须由当前 Counso 环境签发，并有权访问目标工作区与资源。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 | 工作区 ID |
| `cId` | 路径 | string | 是 | 对话 ID |
| `mId` | 路径 | string | 是 | 要编辑的消息 ID |

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
| 200 | 消息已成功编辑 |
| 400 | 请求无效（未找到消息，或该消息不是用户消息） |

## 接口规范

可下载完整的[OpenAPI / Postman](/zh-Hans/docs/developer-platform/counso-api-documentation/openapi-and-postman) 文件。

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
    "/api/v1/w/{wId}/assistant/conversations/{cId}/messages/{mId}/edit": {
      "post": {
        "tags": [
          "Conversations"
        ],
        "summary": "Edit an existing message in a conversation",
        "parameters": [
          {
            "name": "wId",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Workspace ID"
          },
          {
            "name": "cId",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Conversation ID"
          },
          {
            "name": "mId",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Message ID to edit"
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
                  "content",
                  "mentions"
                ],
                "properties": {
                  "content": {
                    "type": "string",
                    "description": "New content for the message"
                  },
                  "mentions": {
                    "type": "array",
                    "description": "List of agent mentions in the message",
                    "items": {
                      "type": "object",
                      "required": [
                        "configurationId"
                      ],
                      "properties": {
                        "configurationId": {
                          "type": "string",
                          "description": "ID of the mentioned agent configuration"
                        }
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
            "description": "Message successfully edited",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "message": {
                      "type": "object",
                      "description": "The edited user message"
                    },
                    "agentMessages": {
                      "type": "array",
                      "description": "Optional array of agent messages generated in response"
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Invalid request (message not found or not a user message)"
          }
        },
        "x-counso-auth": "workspace",
        "description": "Changes the contents of a message that already exists in the specified conversation."
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
