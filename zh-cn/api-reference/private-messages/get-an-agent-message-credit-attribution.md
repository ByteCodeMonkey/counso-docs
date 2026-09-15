# 获取智能体消息的 credits 归因

会话接口：返回智能体消息的直接和总计费 credits；run-agent 工具行包含调用成本及其子智能体树的费用。

```http
GET /api/w/{wId}/assistant/conversations/{cId}/messages/{mId}/consumption
```

服务地址：`https://app.counso.ai`

## 认证

此接口需要用户身份：外部客户端通过 `Authorization: Bearer <token>` 传入用户 OAuth access token；已登录的浏览器也可使用 Counso 会话 Cookie。工作区 API key 不能代替用户身份。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 |  |
| `cId` | 路径 | string | 是 |  |
| `mId` | 路径 | string | 是 |  |

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 智能体消息的 credits 归因 |
| 403 | 该工作区无权查看用量详情 |
| 404 | 未找到对话或智能体消息 |

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
    "/api/w/{wId}/assistant/conversations/{cId}/messages/{mId}/consumption": {
      "get": {
        "summary": "Get an agent message credit attribution",
        "description": "Private session interface. Gives direct and total billed credits for an Agent message; run-agent tool rows include the invocation and charges from its sub-agent tree.",
        "tags": [
          "Private Messages"
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
          },
          {
            "in": "path",
            "name": "mId",
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
            "description": "Credit attribution for the agent message",
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
                      "nullable": true,
                      "description": "Authoritative credits billed directly for this agent message, excluding sub-agents."
                    },
                    "totalBilledCredits": {
                      "type": "number",
                      "description": "Total credits billed by this message and its recursively spawned sub-agents."
                    },
                    "details": {
                      "type": "object",
                      "nullable": true,
                      "description": "Additive attribution reconciled to totalBilledCredits through model input rows. Each run-agent tool row includes its sub-agent subtree's bill. Null when no stored version is complete.",
                      "required": [
                        "attributionVersion",
                        "agentWorkCredits",
                        "tools"
                      ],
                      "properties": {
                        "attributionVersion": {
                          "type": "integer",
                          "description": "Attribution version used for this breakdown."
                        },
                        "agentWorkCredits": {
                          "type": "number",
                          "description": "Non-tool work for the originating message after assigning billing reconciliation exclusively to model input rows."
                        },
                        "tools": {
                          "type": "array",
                          "items": {
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
                                "description": "Share of total billed credits after input-only reconciliation. Run-agent tools include their sub-agent subtree's bill."
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
                  }
                }
              }
            }
          },
          "403": {
            "description": "The workspace does not have access to consumption details"
          },
          "404": {
            "description": "Conversation or agent message not found"
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
    }
  }
}
```
