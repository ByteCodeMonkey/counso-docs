---
title: "更新当前用户资料"
---
会话接口：更新当前已认证用户的资料，包括姓名、job type、常用平台和头像。

```http
PATCH /api/user
```

服务地址：`https://app.counso.ai`

## 认证

此接口需要用户身份：外部客户端通过 `Authorization: Bearer <token>` 传入用户 OAuth access token；已登录的浏览器也可使用 Counso 会话 Cookie。工作区 API key 不能代替用户身份。

## 请求体

`Content-Type: application/json`

| 字段 | 类型 | 必填 |
| --- | --- | --- |
| `firstName` | string | 是 |
| `lastName` | string | 是 |
| `jobType` | string | 否 |
| `imageUrl` | string | 否 |
| `favoritePlatforms` | array[string] | 否 |
| `emailProvider` | string | 否 |
| `workspaceId` | string | 否 |

完整字段约束与嵌套结构见下方接口规范。

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 用户信息已更新 |
| 400 | 请求正文无效 |
| 404 | 未找到用户 |

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
    "/api/user": {
      "patch": {
        "summary": "Update current user",
        "description": "Private session interface. Saves profile changes for the current user, including name, job type, favorite platforms, and image.",
        "tags": [
          "Private User"
        ],
        "security": [
          {
            "UserAccessToken": []
          },
          {
            "BrowserSession": []
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "firstName",
                  "lastName"
                ],
                "properties": {
                  "firstName": {
                    "type": "string"
                  },
                  "lastName": {
                    "type": "string"
                  },
                  "jobType": {
                    "type": "string"
                  },
                  "imageUrl": {
                    "type": "string",
                    "nullable": true
                  },
                  "favoritePlatforms": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    }
                  },
                  "emailProvider": {
                    "type": "string"
                  },
                  "workspaceId": {
                    "type": "string"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "User updated successfully",
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
            "description": "Invalid request body"
          },
          "404": {
            "description": "User not found"
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
