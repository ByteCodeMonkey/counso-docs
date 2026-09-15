---
title: "获取 Space 详情"
---
会话接口：读取指定 Space 的详情，包括分类、成员和权限。

```http
GET /api/w/{wId}/spaces/{spaceId}
```

服务地址：`https://app.counso.ai`

## 认证

此接口需要用户身份：外部客户端通过 `Authorization: Bearer <token>` 传入用户 OAuth access token；已登录的浏览器也可使用 Counso 会话 Cookie。工作区 API key 不能代替用户身份。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 | 工作区 ID |
| `spaceId` | 路径 | string | 是 | Space ID |
| `includeAllMembers` | 查询 | string | 否 | 包含所有成员（包括非活跃成员） 可选值：`true` |

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 成功 |
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
    "/api/w/{wId}/spaces/{spaceId}": {
      "get": {
        "summary": "Get a space",
        "description": "Private session interface. Returns a Space record with its categories, members, and permissions.",
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
          },
          {
            "in": "path",
            "name": "spaceId",
            "required": true,
            "description": "ID of the space",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "includeAllMembers",
            "required": false,
            "description": "Include all members (including inactive)",
            "schema": {
              "type": "string",
              "enum": [
                "true"
              ]
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
                    "space": {
                      "allOf": [
                        {
                          "$ref": "#/components/schemas/PrivateSpace"
                        },
                        {
                          "type": "object",
                          "properties": {
                            "groupIds": {
                              "type": "array",
                              "items": {
                                "type": "string"
                              }
                            },
                            "isRestricted": {
                              "type": "boolean"
                            },
                            "categories": {
                              "type": "object",
                              "additionalProperties": {
                                "type": "object",
                                "properties": {
                                  "count": {
                                    "type": "integer"
                                  },
                                  "usage": {
                                    "type": "object",
                                    "properties": {
                                      "count": {
                                        "type": "integer"
                                      },
                                      "agents": {
                                        "type": "array",
                                        "items": {
                                          "type": "object"
                                        }
                                      }
                                    }
                                  }
                                }
                              }
                            },
                            "canWrite": {
                              "type": "boolean"
                            },
                            "canRead": {
                              "type": "boolean"
                            },
                            "isMember": {
                              "type": "boolean"
                            },
                            "isEditor": {
                              "type": "boolean"
                            },
                            "members": {
                              "type": "array",
                              "items": {
                                "type": "object"
                              }
                            },
                            "groups": {
                              "type": "array",
                              "description": "The groups given access to the space, with the role their grant confers.",
                              "items": {
                                "type": "object",
                                "properties": {
                                  "sId": {
                                    "type": "string"
                                  },
                                  "name": {
                                    "type": "string"
                                  },
                                  "kind": {
                                    "type": "string"
                                  },
                                  "role": {
                                    "type": "string",
                                    "enum": [
                                      "member",
                                      "editor"
                                    ]
                                  }
                                }
                              }
                            },
                            "description": {
                              "type": "string",
                              "nullable": true
                            },
                            "archivedAt": {
                              "type": "integer",
                              "nullable": true
                            },
                            "todoGenerationEnabled": {
                              "type": "boolean",
                              "description": "Whether automatic todo suggestions from project activity are enabled."
                            },
                            "lastTodoAnalysisAt": {
                              "type": "integer",
                              "nullable": true,
                              "description": "Unix timestamp (ms) of the last automatic todo suggestion scan, if any."
                            },
                            "pinnedFramePath": {
                              "type": "string",
                              "nullable": true,
                              "description": "Scoped path to the frame file pinned as the Pod banner."
                            },
                            "frameTabs": {
                              "type": "array",
                              "description": "Frames promoted as custom Pod tabs.",
                              "items": {
                                "type": "object",
                                "properties": {
                                  "path": {
                                    "type": "string"
                                  },
                                  "title": {
                                    "type": "string"
                                  },
                                  "icon": {
                                    "type": "string"
                                  }
                                }
                              }
                            },
                            "tabsOrder": {
                              "type": "array",
                              "description": "Interleaved system tab ids and frame paths before Settings.",
                              "items": {
                                "type": "string"
                              }
                            }
                          }
                        }
                      ]
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
