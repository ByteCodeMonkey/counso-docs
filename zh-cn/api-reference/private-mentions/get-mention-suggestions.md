# 获取工作区提及建议

会话接口：获取工作区范围内可用的提及建议。

```http
GET /api/w/{wId}/assistant/mentions/suggestions
```

服务地址：`https://app.counso.ai`

## 认证

此接口需要用户身份：外部客户端通过 `Authorization: Bearer <token>` 传入用户 OAuth access token；已登录的浏览器也可使用 Counso 会话 Cookie。工作区 API key 不能代替用户身份。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 | 工作区 ID |
| `query` | 查询 | string | 否 | 用于筛选建议的搜索词 |
| `select` | 查询 | string | 否 | 按类型筛选（agents、users 或两者） 可选值：`agents`, `users` |
| `current` | 查询 | string | 否 | 是否仅包含当前提及对象 可选值：`true`, `false` |
| `spaceId` | 查询 | string | 否 | 按 Space 筛选提及建议 |

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 成功 |
| 401 | 未授权 |

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
    "/api/w/{wId}/assistant/mentions/suggestions": {
      "get": {
        "summary": "Get mention suggestions",
        "description": "Private session interface. Provides mention suggestions available in the workspace.",
        "tags": [
          "Private Mentions"
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
            "in": "query",
            "name": "query",
            "required": false,
            "description": "Search query to filter suggestions",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "select",
            "required": false,
            "description": "Filter by type (agents, users, or both)",
            "schema": {
              "type": "string",
              "enum": [
                "agents",
                "users"
              ]
            }
          },
          {
            "in": "query",
            "name": "current",
            "required": false,
            "description": "Whether to include only current mentions",
            "schema": {
              "type": "string",
              "enum": [
                "true",
                "false"
              ]
            }
          },
          {
            "in": "query",
            "name": "spaceId",
            "required": false,
            "description": "Filter suggestions by space",
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
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "suggestions": {
                      "type": "array",
                      "items": {
                        "$ref": "#/components/schemas/PrivateMentionSuggestion"
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
      "PrivateMentionSuggestion": {
        "type": "object",
        "description": "A rich mention suggestion for agents or users.",
        "required": [
          "id",
          "type",
          "label",
          "pictureUrl",
          "description"
        ],
        "properties": {
          "id": {
            "type": "string",
            "description": "Agent sId or user sId"
          },
          "type": {
            "type": "string",
            "enum": [
              "agent",
              "user"
            ]
          },
          "label": {
            "type": "string",
            "description": "Display name"
          },
          "pictureUrl": {
            "type": "string"
          },
          "description": {
            "type": "string",
            "description": "Agent description or user email"
          },
          "userFavorite": {
            "type": "boolean",
            "description": "Whether the agent is a user favorite (agent mentions only)"
          }
        }
      }
    }
  }
}
```
