---
title: "获取触发器"
---
使用工作区管理员 API key，按 ID 获取一个定时运行或 Webhook 触发器。

```http
GET /api/v1/w/{wId}/triggers/{tId}
```

服务地址：`https://app.counso.ai`

## 认证

在 `Authorization: Bearer <token>` 中传入工作区管理员 API key。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 | 工作区 ID |
| `tId` | 路径 | string | 是 | 触发器 ID |

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 该触发器 |
| 401 | 未授权：身份验证令牌无效或缺失。 |
| 403 | 禁止访问：需要工作区管理员 API key。 |
| 404 | 未找到工作区或触发器。 |

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
    "/api/v1/w/{wId}/triggers/{tId}": {
      "get": {
        "summary": "Get a trigger",
        "description": "Retrieve one scheduled-run or webhook trigger by its ID using a workspace-admin API key.",
        "tags": [
          "Triggers"
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
            "name": "tId",
            "required": true,
            "description": "ID of the trigger",
            "schema": {
              "type": "string"
            }
          }
        ],
        "security": [
          {
            "WorkspaceApiKey": []
          }
        ],
        "responses": {
          "200": {
            "description": "The trigger",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "trigger": {
                      "$ref": "#/components/schemas/Trigger"
                    }
                  }
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized. Invalid or missing authentication token."
          },
          "403": {
            "description": "Forbidden. Requires a workspace admin API key."
          },
          "404": {
            "description": "Workspace or trigger not found."
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
    },
    "schemas": {
      "Trigger": {
        "type": "object",
        "required": [
          "id",
          "sId",
          "name",
          "agentConfigurationId",
          "kind",
          "status",
          "createdAt",
          "executionMode",
          "configuration"
        ],
        "properties": {
          "id": {
            "type": "integer",
            "example": 12345
          },
          "sId": {
            "type": "string",
            "description": "Unique string identifier for the trigger",
            "example": "0ec9852c2f"
          },
          "name": {
            "type": "string",
            "example": "Daily summary"
          },
          "agentConfigurationId": {
            "type": "string",
            "description": "sId of the agent this trigger runs",
            "example": "8f3a1c2d9e"
          },
          "kind": {
            "type": "string",
            "enum": [
              "schedule",
              "webhook"
            ]
          },
          "status": {
            "type": "string",
            "enum": [
              "enabled",
              "disabled",
              "disabled_by_manager",
              "relocating",
              "downgraded"
            ]
          },
          "createdAt": {
            "type": "integer",
            "example": 1625097600
          },
          "customPrompt": {
            "type": "string",
            "nullable": true
          },
          "naturalLanguageDescription": {
            "type": "string",
            "nullable": true
          },
          "executionMode": {
            "type": "string",
            "enum": [
              "user_pool",
              "workspace_pool"
            ]
          },
          "configuration": {
            "type": "object",
            "description": "For `kind: schedule`, either a cron config (`cron`, `timezone`) or an interval\nconfig (`intervalDays`, `dayOfWeek`, `hour`, `minute`, `timezone`). For\n`kind: webhook`, `{ includePayload, event?, filter? }`.\n"
          },
          "webhookSource": {
            "type": "object",
            "nullable": true,
            "description": "Present only for `kind: webhook` triggers",
            "properties": {
              "name": {
                "type": "string"
              },
              "provider": {
                "type": "string",
                "example": "github"
              }
            }
          }
        }
      }
    }
  }
}
```
