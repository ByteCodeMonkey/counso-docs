---
title: "创建 Space"
---
会话接口：在工作区中创建 Space。

```http
POST /api/w/{wId}/spaces
```

服务地址：`https://app.counso.ai`

## 认证

此接口需要用户身份：外部客户端通过 `Authorization: Bearer <token>` 传入用户 OAuth access token；已登录的浏览器也可使用 Counso 会话 Cookie。工作区 API key 不能代替用户身份。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 | 工作区 ID |

## 请求体

`Content-Type: application/json`

| 字段 | 类型 | 必填 |
| --- | --- | --- |
| `isRestricted` | boolean | 是 |
| `name` | string | 是 |
| `spaceKind` | string | 是 |
| `memberIds` | array[string] | 否 |
| `groupIds` | array[string] | 否 |

完整字段约束与嵌套结构见下方接口规范。

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 201 | 已成功创建 Space |
| 401 | 未授权 |

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
    "/api/w/{wId}/spaces": {
      "post": {
        "summary": "Create a space",
        "description": "Private session interface. Creates a Space inside the workspace.",
        "tags": [
          "Private Spaces"
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
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "isRestricted",
                  "name",
                  "spaceKind"
                ],
                "properties": {
                  "isRestricted": {
                    "type": "boolean"
                  },
                  "name": {
                    "type": "string"
                  },
                  "spaceKind": {
                    "type": "string",
                    "enum": [
                      "regular",
                      "project"
                    ]
                  },
                  "memberIds": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    },
                    "description": "The space's manual member list. Omitted or empty means the space starts with no manual member."
                  },
                  "groupIds": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    },
                    "description": "The groups given access to the space. Omitted or empty means no group has access to it."
                  }
                }
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Successfully created space",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "space": {
                      "$ref": "#/components/schemas/PrivateSpace"
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
      "PrivateSpace": {
        "type": "object",
        "description": "A space in the workspace.",
        "required": [
          "sId",
          "name",
          "kind"
        ],
        "properties": {
          "sId": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "kind": {
            "type": "string",
            "enum": [
              "global",
              "system",
              "conversations",
              "regular",
              "project"
            ]
          },
          "createdAt": {
            "type": "integer"
          },
          "updatedAt": {
            "type": "integer"
          }
        }
      }
    }
  }
}
```
