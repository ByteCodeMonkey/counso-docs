# 更新数据源视图

会话接口：更新指定数据源视图。

```http
PATCH /api/w/{wId}/spaces/{spaceId}/data_source_views/{dsvId}
```

服务地址：`https://app.counso.ai`

## 认证

此接口需要用户身份：外部客户端通过 `Authorization: Bearer <token>` 传入用户 OAuth access token；已登录的浏览器也可使用 Counso 会话 Cookie。工作区 API key 不能代替用户身份。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 | 工作区 ID |
| `spaceId` | 路径 | string | 是 | Space ID |
| `dsvId` | 路径 | string | 是 | 数据源视图 ID |

## 请求体

`Content-Type: application/json`

| 字段 | 类型 | 必填 |
| --- | --- | --- |
| `parentsIn` | array[string] | 否 |

完整字段约束与嵌套结构见下方接口规范。

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
    "/api/w/{wId}/spaces/{spaceId}/data_source_views/{dsvId}": {
      "patch": {
        "summary": "Update a data source view",
        "description": "Private session interface. Modifies the selected data source view.",
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
            "in": "path",
            "name": "dsvId",
            "required": true,
            "description": "ID of the data source view",
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
                "properties": {
                  "parentsIn": {
                    "type": "array",
                    "nullable": true,
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
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "dataSourceView": {
                      "$ref": "#/components/schemas/PrivateDataSourceView"
                    },
                    "connector": {
                      "type": "object",
                      "nullable": true
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
