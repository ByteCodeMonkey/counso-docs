---
title: "取消定时唤醒"
---
会话接口：取消已安排的 wake-up；仅创建该 wake-up 的用户或工作区管理员可以操作。

```http
DELETE /api/w/{wId}/assistant/conversations/{cId}/wakeups/{wuId}
```

服务地址：`https://app.counso.ai`

## 认证

此接口需要用户身份：外部客户端通过 `Authorization: Bearer <token>` 传入用户 OAuth access token；已登录的浏览器也可使用 Counso 会话 Cookie。工作区 API key 不能代替用户身份。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 | 工作区 ID |
| `cId` | 路径 | string | 是 | 对话 ID |
| `wuId` | 路径 | string | 是 | 要取消的 wake-up 的 sId |

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 已成功取消（或该操作已处于终态） |
| 403 | 调用者不是该 wake-up 的所有者，也不是工作区管理员 |
| 404 | 此对话中未找到 wake-up |

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
    "/api/w/{wId}/assistant/conversations/{cId}/wakeups/{wuId}": {
      "delete": {
        "summary": "Cancel a wake-up",
        "description": "Private session interface. Cancels a scheduled wake-up when requested by its owner or a workspace administrator.",
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
          },
          {
            "in": "path",
            "name": "wuId",
            "required": true,
            "description": "sId of the wake-up to cancel",
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
            "description": "Successfully cancelled (or already terminal)",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "wakeUp": {
                      "$ref": "#/components/schemas/PrivateWakeUp"
                    }
                  }
                }
              }
            }
          },
          "403": {
            "description": "Caller is not the wake-up owner or a workspace admin"
          },
          "404": {
            "description": "Wake-up not found in this conversation"
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
      "PrivateWakeUp": {
        "type": "object",
        "description": "A wake-up scheduled in a conversation to re-invoke the agent at a later time.",
        "required": [
          "id",
          "sId",
          "createdAt",
          "agentConfigurationId",
          "scheduleConfig",
          "reason",
          "status",
          "fireCount",
          "maxFires"
        ],
        "properties": {
          "id": {
            "type": "integer"
          },
          "sId": {
            "type": "string"
          },
          "createdAt": {
            "type": "integer",
            "description": "Unix timestamp (milliseconds)."
          },
          "agentConfigurationId": {
            "type": "string"
          },
          "scheduleConfig": {
            "oneOf": [
              {
                "type": "object",
                "required": [
                  "type",
                  "fireAt"
                ],
                "properties": {
                  "type": {
                    "type": "string",
                    "enum": [
                      "one_shot"
                    ]
                  },
                  "fireAt": {
                    "type": "integer",
                    "description": "Unix timestamp (milliseconds) when the wake-up should fire."
                  }
                }
              },
              {
                "type": "object",
                "required": [
                  "type",
                  "cron",
                  "timezone"
                ],
                "properties": {
                  "type": {
                    "type": "string",
                    "enum": [
                      "cron"
                    ]
                  },
                  "cron": {
                    "type": "string",
                    "description": "5-field cron expression."
                  },
                  "timezone": {
                    "type": "string",
                    "description": "IANA timezone name."
                  }
                }
              }
            ]
          },
          "reason": {
            "type": "string"
          },
          "status": {
            "type": "string",
            "enum": [
              "scheduled",
              "fired",
              "cancelled",
              "expired"
            ]
          },
          "fireCount": {
            "type": "integer"
          },
          "maxFires": {
            "type": "integer"
          }
        }
      }
    }
  }
}
```
