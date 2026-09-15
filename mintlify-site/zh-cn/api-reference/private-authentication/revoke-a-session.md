---
title: "撤销登录会话"
---
按 session_id 撤销对应的 WorkOS 会话，使该会话退出登录。此接口不要求 Bearer token。

```http
POST /api/workos/revoke-session
```

服务地址：`https://app.counso.ai`

## 认证

提交要撤销的 session_id，以结束该用户会话。此退出登录接口不要求 Bearer token。

## 请求体

`Content-Type: application/json`

| 字段 | 类型 | 必填 |
| --- | --- | --- |
| `session_id` | string | 是 |

完整字段约束与嵌套结构见下方接口规范。

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 会话已撤销 |
| 400 | session_id 无效 |

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
    "/api/workos/revoke-session": {
      "post": {
        "summary": "Revoke a session",
        "description": "Revokes the WorkOS session named in session_id to sign that session out. This endpoint does not require a Bearer token.",
        "tags": [
          "Private Authentication"
        ],
        "security": [],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "session_id"
                ],
                "properties": {
                  "session_id": {
                    "type": "string"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Session revoked successfully",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "success": {
                      "type": "boolean"
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Invalid session_id"
          }
        },
        "x-counso-auth": "login"
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
