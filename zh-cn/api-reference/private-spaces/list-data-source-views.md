# 列出数据源视图

会话接口：列出指定 Space 中的全部数据源视图。

```http
GET /api/w/{wId}/spaces/{spaceId}/data_source_views
```

服务地址：`https://app.counso.ai`

## 认证

此接口需要用户身份：外部客户端通过 `Authorization: Bearer <token>` 传入用户 OAuth access token；已登录的浏览器也可使用 Counso 会话 Cookie。工作区 API key 不能代替用户身份。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 | 工作区 ID |
| `spaceId` | 路径 | string | 是 | Space ID |
| `category` | 查询 | string | 否 | 按数据源视图类别筛选 可选值：`managed`, `folder`, `website`, `apps` |
| `withDetails` | 查询 | string | 否 | 包含用量和连接器详情（需要同时指定 category） 可选值：`true` |
| `includeEditedBy` | 查询 | string | 否 | 包含 editedByUser 信息 可选值：`true` |

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 成功 |
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
    "/api/w/{wId}/spaces/{spaceId}/data_source_views": {
      "get": {
        "summary": "List data source views",
        "description": "Private session interface. Lists every data source view attached to the chosen Space.",
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
            "name": "category",
            "required": false,
            "description": "Filter by data source view category",
            "schema": {
              "type": "string",
              "enum": [
                "managed",
                "folder",
                "website",
                "apps"
              ]
            }
          },
          {
            "in": "query",
            "name": "withDetails",
            "required": false,
            "description": "Include usage and connector details (requires category)",
            "schema": {
              "type": "string",
              "enum": [
                "true"
              ]
            }
          },
          {
            "in": "query",
            "name": "includeEditedBy",
            "required": false,
            "description": "Include editedByUser information",
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
                    "dataSourceViews": {
                      "type": "array",
                      "items": {
                        "$ref": "#/components/schemas/PrivateDataSourceView"
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
      "PrivateDataSourceView": {
        "type": "object",
        "description": "A view on a data source within a space.",
        "required": [
          "sId",
          "id",
          "category",
          "kind",
          "spaceId",
          "dataSource"
        ],
        "properties": {
          "sId": {
            "type": "string"
          },
          "id": {
            "type": "integer"
          },
          "category": {
            "type": "string",
            "enum": [
              "managed",
              "folder",
              "website",
              "apps"
            ]
          },
          "kind": {
            "type": "string",
            "enum": [
              "default",
              "custom"
            ]
          },
          "spaceId": {
            "type": "string"
          },
          "createdAt": {
            "type": "integer"
          },
          "updatedAt": {
            "type": "integer"
          },
          "parentsIn": {
            "type": "array",
            "nullable": true,
            "items": {
              "type": "string"
            },
            "description": "List of parent IDs included in this view, null if the full data source is used"
          },
          "dataSource": {
            "$ref": "#/components/schemas/PrivateDataSource"
          },
          "editedByUser": {
            "type": "object",
            "nullable": true,
            "properties": {
              "editedAt": {
                "type": "integer",
                "nullable": true
              },
              "fullName": {
                "type": "string",
                "nullable": true
              },
              "imageUrl": {
                "type": "string",
                "nullable": true
              },
              "email": {
                "type": "string",
                "nullable": true
              },
              "userId": {
                "type": "string",
                "nullable": true
              }
            }
          },
          "usage": {
            "type": "object",
            "description": "Present when the view was fetched with usage details (withDetails query param). Counts agents and skills that use this data source view.",
            "properties": {
              "count": {
                "type": "integer"
              },
              "agents": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "sId": {
                      "type": "string"
                    },
                    "name": {
                      "type": "string"
                    },
                    "pictureUrl": {
                      "type": "string"
                    }
                  }
                }
              },
              "skills": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "sId": {
                      "type": "string"
                    },
                    "name": {
                      "type": "string"
                    },
                    "icon": {
                      "type": "string",
                      "nullable": true
                    }
                  }
                }
              }
            }
          }
        }
      },
      "PrivateDataSource": {
        "type": "object",
        "description": "A data source in the workspace.",
        "required": [
          "sId",
          "id",
          "name"
        ],
        "properties": {
          "sId": {
            "type": "string"
          },
          "id": {
            "type": "integer"
          },
          "createdAt": {
            "type": "integer"
          },
          "name": {
            "type": "string"
          },
          "description": {
            "type": "string",
            "nullable": true
          },
          "assistantDefaultSelected": {
            "type": "boolean"
          },
          "dustAPIProjectId": {
            "type": "string"
          },
          "dustAPIDataSourceId": {
            "type": "string"
          },
          "connectorId": {
            "type": "string",
            "nullable": true
          },
          "connectorProvider": {
            "type": "string",
            "nullable": true
          }
        }
      }
    }
  }
}
```
