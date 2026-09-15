# 为对话选择 Space

会话接口：将常规 Space 追加到对话明确选择的数据范围中。

```http
POST /api/w/{wId}/assistant/conversations/{cId}/selected_spaces
```

服务地址：`https://app.counso.ai`

## 认证

此接口需要用户身份：外部客户端通过 `Authorization: Bearer <token>` 传入用户 OAuth access token；已登录的浏览器也可使用 Counso 会话 Cookie。工作区 API key 不能代替用户身份。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 |  |
| `cId` | 路径 | string | 是 |  |

## 请求体

`Content-Type: application/json`

| 字段 | 类型 | 必填 |
| --- | --- | --- |
| `mode` | string | 是 |
| `spaceIds` | array[string] | 是 |

完整字段约束与嵌套结构见下方接口规范。

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 已选 Spaces 和有效 ACL 摘要。 |
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
    "/api/w/{wId}/assistant/conversations/{cId}/selected_spaces": {
      "post": {
        "summary": "Select Spaces for a conversation",
        "description": "Private session interface. Adds regular Spaces to the conversation's explicitly selected scope.",
        "tags": [
          "Private Conversations"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "wId",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "path",
            "name": "cId",
            "required": true,
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
                  "mode",
                  "spaceIds"
                ],
                "properties": {
                  "mode": {
                    "type": "string",
                    "enum": [
                      "add"
                    ]
                  },
                  "spaceIds": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    }
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Selected Spaces and effective ACL summary.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "selectedSpaces": {
                      "type": "array",
                      "items": {
                        "allOf": [
                          {
                            "$ref": "#/components/schemas/PrivateSpace"
                          },
                          {
                            "type": "object",
                            "properties": {
                              "selected": {
                                "type": "boolean"
                              }
                            }
                          }
                        ]
                      }
                    },
                    "effectiveAcl": {
                      "type": "object",
                      "properties": {
                        "spaceIds": {
                          "type": "array",
                          "items": {
                            "type": "string"
                          }
                        },
                        "viewerMustHaveAll": {
                          "type": "boolean"
                        }
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
