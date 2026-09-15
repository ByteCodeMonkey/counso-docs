---
title: "归档 Skill"
---
软归档工作区中的自定义 Skill。

```http
DELETE /api/v1/w/{wId}/skills/{skillId}
```

服务地址：`https://app.counso.ai`

## 认证

在 `Authorization: Bearer <token>` 中传入工作区 API key 或用户 OAuth access token。凭据须由当前 Counso 环境签发，并有权访问目标工作区与资源。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 | 工作区的唯一字符串标识符 |
| `skillId` | 路径 | string | 是 | 自定义 Skill 的唯一字符串标识符 |

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | Skill 已归档。 |
| 401 | 未授权：身份验证令牌无效或缺失。 |
| 403 | 禁止访问：调用者无权归档 Skills。 |
| 404 | 未找到 Skill。 |
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
    "/api/v1/w/{wId}/skills/{skillId}": {
      "delete": {
        "summary": "Archive a skill",
        "description": "Marks a custom workspace Skill as archived without permanently deleting it.",
        "tags": [
          "Skills"
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
            "in": "path",
            "name": "skillId",
            "required": true,
            "description": "Unique string identifier for the custom skill",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Skill archived successfully.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "required": [
                    "success"
                  ],
                  "properties": {
                    "success": {
                      "type": "boolean"
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
            "description": "Forbidden. The caller is not allowed to archive skills."
          },
          "404": {
            "description": "Skill not found."
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
    }
  }
}
```
