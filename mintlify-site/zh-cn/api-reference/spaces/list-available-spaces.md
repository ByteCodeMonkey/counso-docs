---
title: "列出可访问的 Space"
---
列出当前已认证工作区中用户可访问的 Space。

```http
GET /api/v1/w/{wId}/spaces
```

服务地址：`https://app.counso.ai`

## 认证

在 `Authorization: Bearer <token>` 中传入工作区 API key 或用户 OAuth access token。凭据须由当前 Counso 环境签发，并有权访问目标工作区与资源。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 | 工作区的唯一字符串标识符 |
| `kinds` | 查询 | string | 否 | 要筛选的 Space 类型，以逗号分隔，可选值为 system、global、regular 和 project。默认值为 system,global,regular；如需包含 project，必须显式指定。 |

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 工作区中的 Spaces |
| 400 | 请求错误：参数无效或缺失。 |
| 401 | 未授权：身份验证令牌无效或缺失。 |
| 404 | 未找到工作区。 |
| 500 | 内部服务器错误。 |

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
    "/api/v1/w/{wId}/spaces": {
      "get": {
        "summary": "List available spaces.",
        "description": "Enumerates Spaces the authenticated user can access in the current workspace.",
        "tags": [
          "Spaces"
        ],
        "security": [
          {
            "WorkspaceApiKey": []
          },
          {
            "UserAccessToken": []
          }
        ],
        "parameters": [
          {
            "in": "path",
            "name": "wId",
            "required": true,
            "description": "Unique string identifier for the workspace",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "kinds",
            "required": false,
            "description": "Comma-separated list of space kinds to filter on, among `system`, `global`, `regular` and `project`. Defaults to `system,global,regular` — projects must be requested explicitly.",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Spaces of the workspace",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "spaces": {
                      "type": "array",
                      "items": {
                        "$ref": "#/components/schemas/Space"
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
          "404": {
            "description": "Workspace not found."
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
      "Space": {
        "type": "object",
        "properties": {
          "sId": {
            "type": "string",
            "description": "Unique string identifier for the space"
          },
          "name": {
            "type": "string",
            "description": "Name of the space"
          },
          "kind": {
            "type": "string",
            "enum": [
              "regular",
              "global",
              "system",
              "public"
            ],
            "description": "The kind of the space"
          },
          "groupIds": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "List of group IDs that have access to the space"
          },
          "isRestricted": {
            "type": "boolean",
            "description": "Whether the space is restricted to specific groups"
          }
        }
      }
    }
  }
}
```
