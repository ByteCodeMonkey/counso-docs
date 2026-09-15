# 获取提及建议

根据搜索词获取可用的智能体和用户提及建议。

```http
GET /api/v1/w/{wId}/assistant/mentions/suggestions
```

服务地址：`https://app.counso.ai`

## 认证

在 `Authorization: Bearer <token>` 中传入工作区 API key 或用户 OAuth access token。凭据须由当前 Counso 环境签发，并有权访问目标工作区与资源。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 | 工作区 ID |
| `query` | 查询 | string | 是 | 用于筛选提及建议的搜索词 |
| `select` | 查询 | array[string] | 否 | 要包含的提及类型列表。可填 agents、users 或两者；未提供时默认包含 agents 和 users。 |
| `current` | 查询 | boolean | 否 | 是否在建议中包含当前用户 |

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 提及建议列表 |
| 400 | 请求错误：参数无效或缺失。 |
| 401 | 未授权：身份验证令牌无效或缺失。 |
| 500 | 内部服务器错误。 |

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
    "/api/v1/w/{wId}/assistant/mentions/suggestions": {
      "get": {
        "summary": "Get mention suggestions",
        "description": "Returns agent and user mention candidates matching the supplied query.",
        "tags": [
          "Mentions"
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
            "required": true,
            "description": "Search query string to filter suggestions",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "select",
            "required": false,
            "description": "Array of mention types to include. Can be \"agents\", \"users\", or both. If not provided, defaults to agents and users.",
            "schema": {
              "type": "array",
              "items": {
                "type": "string",
                "enum": [
                  "agents",
                  "users"
                ]
              }
            }
          },
          {
            "in": "query",
            "name": "current",
            "required": false,
            "description": "Whether to include the current user in the suggestions.",
            "schema": {
              "type": "boolean"
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
        "responses": {
          "200": {
            "description": "List of mention suggestions",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "suggestions": {
                      "type": "array",
                      "items": {
                        "$ref": "#/components/schemas/RichMention"
                      }
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Bad Request. Missing or invalid parameters."
          },
          "401": {
            "description": "Unauthorized. Invalid or missing authentication token."
          },
          "500": {
            "description": "Internal Server Error."
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
      "RichMention": {
        "type": "object",
        "description": "A rich mention suggestion containing detailed information about an agent or user",
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
            "description": "Unique identifier for the mention (agent sId or user sId)",
            "example": "7f3a9c2b1e"
          },
          "type": {
            "type": "string",
            "enum": [
              "agent",
              "user"
            ],
            "description": "Type of the mention",
            "example": "agent"
          },
          "label": {
            "type": "string",
            "description": "Display label for the mention",
            "example": "My Assistant"
          },
          "pictureUrl": {
            "type": "string",
            "description": "URL of the profile picture",
            "example": "https://example.com/avatar.png"
          },
          "description": {
            "type": "string",
            "description": "Description of the mention (agent description or user email)",
            "example": "A helpful AI assistant"
          },
          "userFavorite": {
            "type": "boolean",
            "nullable": true,
            "description": "Whether the agent is marked as a favorite by the user (only for agent mentions)",
            "example": true
          }
        }
      }
    }
  }
}
```
