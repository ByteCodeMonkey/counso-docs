---
title: "发起 WorkOS 登录"
---
通过重定向到 WorkOS AuthKit 开始用户登录。客户端可以传入 PKCE 参数，不要求已有的 Bearer token。

```http
GET /api/workos/login
```

服务地址：`https://app.counso.ai`

## 认证

此接口用于开始用户登录，不要求已有的 Bearer token。使用 PKCE 的客户端提交已登记的回调地址与 code challenge，响应会将用户重定向至身份服务。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `redirect_uri` | 查询 | string | 否 | 自定义重定向 URI（扩展程序用于 PKCE 流程） |
| `code_challenge` | 查询 | string | 否 | PKCE code challenge |
| `code_challenge_method` | 查询 | string | 否 | PKCE code challenge 方法（S256） |

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 登录页 HTML |
| 302 | 重定向到 WorkOS 授权 URL |
| 400 | 请求错误 |

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
    "/api/workos/login": {
      "get": {
        "summary": "Initiate WorkOS login",
        "description": "Starts authentication by redirecting the user to WorkOS AuthKit. Clients can supply PKCE parameters; no existing Bearer token is needed.",
        "tags": [
          "Private Authentication"
        ],
        "security": [],
        "parameters": [
          {
            "in": "query",
            "name": "redirect_uri",
            "required": false,
            "description": "Custom redirect URI (used by extensions for PKCE flow)",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "code_challenge",
            "required": false,
            "description": "PKCE code challenge",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "code_challenge_method",
            "required": false,
            "description": "PKCE code challenge method (S256)",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Login page HTML"
          },
          "302": {
            "description": "Redirect to WorkOS authorization URL"
          },
          "400": {
            "description": "Bad request"
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
