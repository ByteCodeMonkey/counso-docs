# 列出数据源视图

列出指定 Space 中的数据源视图。

```http
GET /api/v1/w/{wId}/spaces/{spaceId}/data_source_views
```

服务地址：`https://app.counso.ai`

## 认证

在 `Authorization: Bearer <token>` 中传入工作区 API key 或用户 OAuth access token。凭据须由当前 Counso 环境签发，并有权访问目标工作区与资源。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 | 工作区的唯一字符串标识符 |
| `spaceId` | 路径 | string | 是 | Space ID |

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 该 Space 中的数据源视图列表 |
| 400 | 请求错误：参数无效或缺失。 |
| 401 | 未授权：身份验证令牌无效或缺失。 |
| 404 | 未找到工作区。 |
| 500 | 内部服务器错误。 |

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
    "/api/v1/w/{wId}/spaces/{spaceId}/data_source_views": {
      "get": {
        "summary": "List Data Source Views",
        "description": "Enumerates the data source views configured for the selected Space.",
        "tags": [
          "DatasourceViews"
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
            "name": "spaceId",
            "required": true,
            "description": "ID of the space",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "List of data source views in the space",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "dataSourceViews": {
                      "type": "array",
                      "items": {
                        "$ref": "#/components/schemas/DatasourceView"
                      }
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Bad Request. Missing or invalid parameters."
          },
          "401": {
            "description": "Unauthorized. Invalid or missing authentication token."
          },
          "404": {
            "description": "Workspace not found."
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
    },
    "schemas": {
      "DatasourceView": {
        "type": "object",
        "properties": {
          "category": {
            "type": "string",
            "enum": [
              "managed",
              "folder",
              "website",
              "apps"
            ],
            "description": "The category of the data source view"
          },
          "createdAt": {
            "type": "number",
            "description": "Timestamp of when the data source view was created"
          },
          "dataSource": {
            "$ref": "#/components/schemas/Datasource"
          },
          "editedByUser": {
            "type": "object",
            "description": "The user who last edited the data source view",
            "properties": {
              "fullName": {
                "type": "string",
                "description": "Full name of the user"
              },
              "editedAt": {
                "type": "number",
                "description": "Timestamp of when the data source view was last edited by the user"
              }
            }
          },
          "id": {
            "type": "number",
            "description": "Unique identifier for the data source view"
          },
          "kind": {
            "type": "string",
            "enum": [
              "default",
              "custom"
            ],
            "description": "The kind of the data source view"
          },
          "parentsIn": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "List of IDs included in this view, null if complete data source is taken",
            "nullable": true
          },
          "sId": {
            "type": "string",
            "description": "Unique string identifier for the data source view"
          },
          "updatedAt": {
            "type": "number",
            "description": "Timestamp of when the data source view was last updated"
          },
          "spaceId": {
            "type": "string",
            "description": "ID of the space containing the data source view"
          }
        }
      },
      "Datasource": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "Unique identifier for the datasource",
            "example": 12345
          },
          "createdAt": {
            "type": "integer",
            "description": "Timestamp of when the datasource was created",
            "example": 1625097600
          },
          "name": {
            "type": "string",
            "description": "Name of the datasource",
            "example": "Customer Knowledge Base"
          },
          "description": {
            "type": "string",
            "description": "Description of the datasource",
            "example": "Contains all customer-related information and FAQs"
          },
          "dustAPIProjectId": {
            "type": "string",
            "description": "ID of the associated Counso API project",
            "example": "5e9d8c7b6a"
          },
          "connectorId": {
            "type": "string",
            "description": "ID of the connector used for this datasource",
            "example": "1f3e5d7c9b"
          },
          "connectorProvider": {
            "type": "string",
            "description": "Provider of the connector (e.g., 'webcrawler')",
            "example": "webcrawler"
          },
          "assistantDefaultSelected": {
            "type": "boolean",
            "description": "Whether this datasource is selected by default for agents",
            "example": true
          }
        }
      }
    }
  }
}
```
