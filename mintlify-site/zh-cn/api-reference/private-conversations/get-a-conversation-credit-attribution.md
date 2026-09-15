---
title: "获取对话的 credits 归因"
---
会话接口：返回该对话已完成消息的最新稳定计费 credits，以及仅根据模型输入行核算的补充归因；运行中的消息结束后纳入统计。

```http
GET /api/w/{wId}/assistant/conversations/{cId}/consumption
```

服务地址：`https://app.counso.ai`

## 认证

此接口需要用户身份：外部客户端通过 `Authorization: Bearer <token>` 传入用户 OAuth access token；已登录的浏览器也可使用 Counso 会话 Cookie。工作区 API key 不能代替用户身份。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 |  |
| `cId` | 路径 | string | 是 |  |

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 对话的 credits 归因 |
| 404 | 未找到对话 |

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
    "/api/w/{wId}/assistant/conversations/{cId}/consumption": {
      "get": {
        "summary": "Get a conversation credit attribution",
        "description": "Private session interface. Reports the latest stable credits billed for completed messages directly in this conversation, plus additional attribution calculated only from model-input rows. In-progress messages appear after reaching a terminal state.",
        "tags": [
          "Private Conversations"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "wId",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "path",
            "name": "cId",
            "required": true,
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
            "description": "Conversation credit attribution",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "required": [
                    "billedCredits",
                    "details"
                  ],
                  "properties": {
                    "billedCredits": {
                      "type": "number",
                      "description": "Latest stable credits billed across completed messages belonging directly to the conversation."
                    },
                    "details": {
                      "type": "object",
                      "allOf": [
                        {
                          "$ref": "#/components/schemas/PrivateConversationConsumptionDetails"
                        }
                      ],
                      "nullable": true
                    }
                  }
                }
              }
            }
          },
          "404": {
            "description": "Conversation not found"
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
      "PrivateConversationConsumptionDetails": {
        "type": "object",
        "description": "Additive attribution reconciled to the authoritative bill exclusively through model input rows. Each message uses its newest complete stored attribution version. Null when any billed message has no complete stored attribution.",
        "required": [
          "agentWorkCredits",
          "tools",
          "models",
          "agents"
        ],
        "properties": {
          "agentWorkCredits": {
            "type": "number",
            "description": "Agent work after assigning billing reconciliation exclusively to model input rows."
          },
          "tools": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PrivateConversationConsumptionToolDetails"
            }
          },
          "models": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PrivateConversationConsumptionModelDetails"
            }
          },
          "agents": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PrivateConversationConsumptionAgentDetails"
            }
          }
        }
      },
      "PrivateConversationConsumptionAgentDetails": {
        "type": "object",
        "required": [
          "agentId",
          "name",
          "pictureUrl",
          "billedCredits",
          "agentWorkCredits",
          "tools",
          "models"
        ],
        "properties": {
          "agentId": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "pictureUrl": {
            "type": "string",
            "nullable": true
          },
          "billedCredits": {
            "type": "number"
          },
          "agentWorkCredits": {
            "type": "number",
            "description": "Agent work after assigning billing reconciliation exclusively to model input rows."
          },
          "tools": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PrivateConversationConsumptionToolDetails"
            }
          },
          "models": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PrivateConversationConsumptionModelDetails"
            }
          }
        }
      },
      "PrivateConversationConsumptionModelDetails": {
        "type": "object",
        "required": [
          "providerId",
          "modelId",
          "displayName",
          "attributedCredits"
        ],
        "properties": {
          "providerId": {
            "type": "string"
          },
          "modelId": {
            "type": "string"
          },
          "displayName": {
            "type": "string"
          },
          "attributedCredits": {
            "type": "number",
            "description": "Model attribution after reconciling exclusively through its input rows."
          }
        }
      },
      "PrivateConversationConsumptionToolDetails": {
        "type": "object",
        "required": [
          "label",
          "internalMCPServerName",
          "toolName",
          "callCount",
          "attributedCredits",
          "directCredits",
          "pending"
        ],
        "properties": {
          "label": {
            "type": "string"
          },
          "internalMCPServerName": {
            "type": "string",
            "nullable": true
          },
          "toolName": {
            "type": "string"
          },
          "callCount": {
            "type": "integer"
          },
          "attributedCredits": {
            "type": "number",
            "description": "Share of billed credits after reconciling exclusively through model input rows."
          },
          "directCredits": {
            "type": "number"
          },
          "pending": {
            "type": "boolean"
          }
        }
      }
    }
  }
}
```
