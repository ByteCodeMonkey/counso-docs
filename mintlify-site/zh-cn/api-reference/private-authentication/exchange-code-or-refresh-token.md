---
title: "兑换授权码或刷新令牌"
---
在登录或续期流程中，将 WorkOS 授权码或刷新令牌换成用户访问令牌，不要求已有的 Bearer token。

```http
POST /api/workos/authenticate
```

服务地址：`https://app.counso.ai`

## 认证

可提交授权码及对应的 PKCE verifier，或提交 grant_type=refresh_token 和 refresh token 来刷新会话。无需已有的 Bearer token；支持 JSON 与表单编码请求体。

## 请求体

`Content-Type: application/json`

| 字段 | 类型 | 必填 |
| --- | --- | --- |
| `code` | string | 否 |
| `grant_type` | string | 否 |
| `refresh_token` | string | 否 |
| `code_verifier` | string | 否 |

`Content-Type: application/x-www-form-urlencoded`

| 字段 | 类型 | 必填 |
| --- | --- | --- |
| `code` | string | 否 |
| `grant_type` | string | 否 |
| `refresh_token` | string | 否 |
| `code_verifier` | string | 否 |

完整字段约束与嵌套结构见下方接口规范。

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 包含令牌的身份验证结果 |
| 400 | 请求无效 |

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
    "/api/workos/authenticate": {
      "post": {
        "summary": "Exchange code or refresh token",
        "description": "Exchanges a WorkOS authorization code or refresh token for user access tokens as part of sign-in or session renewal. An existing Bearer token is not required.",
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
                "properties": {
                  "code": {
                    "type": "string"
                  },
                  "grant_type": {
                    "type": "string",
                    "enum": [
                      "refresh_token"
                    ]
                  },
                  "refresh_token": {
                    "type": "string"
                  },
                  "code_verifier": {
                    "type": "string"
                  }
                }
              },
              "examples": {
                "authorization_code": {
                  "summary": "Exchange an authorization code",
                  "value": {
                    "code": "{{authorizationCode}}",
                    "code_verifier": "{{codeVerifier}}"
                  }
                },
                "refresh_token": {
                  "summary": "Refresh a user session",
                  "value": {
                    "grant_type": "refresh_token",
                    "refresh_token": "{{refreshToken}}"
                  }
                }
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "type": "object",
                "properties": {
                  "code": {
                    "type": "string"
                  },
                  "grant_type": {
                    "type": "string",
                    "enum": [
                      "refresh_token"
                    ]
                  },
                  "refresh_token": {
                    "type": "string"
                  },
                  "code_verifier": {
                    "type": "string"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Authentication result with tokens",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "accessToken": {
                      "type": "string"
                    },
                    "refreshToken": {
                      "type": "string"
                    },
                    "user": {
                      "type": "object"
                    },
                    "expiresIn": {
                      "type": "integer",
                      "description": "Token expiry in seconds"
                    },
                    "expirationDate": {
                      "type": "integer",
                      "description": "Token expiry date in milliseconds"
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Invalid request"
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
