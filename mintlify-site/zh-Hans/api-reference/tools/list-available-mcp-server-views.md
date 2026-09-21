---
title: "列出可用 MCP 服务器视图"
---
列出当前已认证工作区指定 Space 中已启用的 MCP 服务器视图（即工具）。

```http
GET /api/v1/w/{wId}/spaces/{spaceId}/mcp_server_views
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
| 200 | 该 Space 的 MCP 服务器视图 |
| 400 | 请求错误：参数无效或缺失。 |
| 401 | 未授权：身份验证令牌无效或缺失。 |
| 404 | 未找到工作区。 |
| 500 | 内部服务器错误。 |

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
    "/api/v1/w/{wId}/spaces/{spaceId}/mcp_server_views": {
      "get": {
        "summary": "List available MCP server views.",
        "description": "Shows the enabled MCP server views (tools) available in a selected Space for this workspace.",
        "tags": [
          "Tools"
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
            "description": "MCP server views of the space",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "spaces": {
                      "type": "array",
                      "items": {
                        "$ref": "#/components/schemas/MCPServerView"
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
      "MCPServerView": {
        "type": "object",
        "required": [
          "isRestrictedToSkills"
        ],
        "properties": {
          "id": {
            "type": "integer",
            "description": "Unique identifier for the MCP server view",
            "example": 123
          },
          "sId": {
            "type": "string",
            "description": "Unique string identifier for the MCP server view",
            "example": "mcp_sv_abc123"
          },
          "name": {
            "type": "string",
            "nullable": true,
            "description": "Custom name for the MCP server view (null if not set)",
            "example": "My Custom MCP Server"
          },
          "description": {
            "type": "string",
            "nullable": true,
            "description": "Custom description for the MCP server view (null if not set)",
            "example": "This MCP server handles customer data operations"
          },
          "createdAt": {
            "type": "number",
            "description": "Unix timestamp of when the MCP server view was created",
            "example": 1625097600
          },
          "updatedAt": {
            "type": "number",
            "description": "Unix timestamp of when the MCP server view was last updated",
            "example": 1625184000
          },
          "spaceId": {
            "type": "string",
            "description": "ID of the space containing the MCP server view",
            "example": "spc_xyz789"
          },
          "serverType": {
            "type": "string",
            "enum": [
              "remote",
              "internal"
            ],
            "description": "Type of the MCP server",
            "example": "remote"
          },
          "server": {
            "type": "object",
            "properties": {
              "sId": {
                "type": "string",
                "description": "Unique string identifier for the MCP server",
                "example": "mcp_srv_def456"
              },
              "name": {
                "type": "string",
                "description": "Name of the MCP server",
                "example": "Customer Data Server"
              },
              "version": {
                "type": "string",
                "description": "Version of the MCP server",
                "example": "1.0.0"
              },
              "description": {
                "type": "string",
                "description": "Description of the MCP server",
                "example": "Handles customer data operations and queries"
              },
              "icon": {
                "type": "string",
                "description": "Icon identifier for the MCP server",
                "example": "database"
              },
              "authorization": {
                "type": "object",
                "nullable": true,
                "properties": {
                  "provider": {
                    "type": "string",
                    "description": "OAuth provider for authorization",
                    "example": "github"
                  },
                  "supported_use_cases": {
                    "type": "array",
                    "items": {
                      "type": "string",
                      "enum": [
                        "platform_actions",
                        "personal_actions"
                      ]
                    },
                    "description": "Supported use cases for the authorization",
                    "example": [
                      "platform_actions"
                    ]
                  },
                  "scope": {
                    "type": "string",
                    "description": "OAuth scope required",
                    "example": "repo:read"
                  }
                }
              },
              "tools": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "name": {
                      "type": "string",
                      "description": "Name of the tool",
                      "example": "query_customers"
                    },
                    "description": {
                      "type": "string",
                      "description": "Description of what the tool does",
                      "example": "Query customer database for information"
                    },
                    "inputSchema": {
                      "type": "object",
                      "description": "JSON Schema for the tool's input parameters",
                      "example": {
                        "type": "object",
                        "properties": {
                          "customerId": {
                            "type": "string"
                          }
                        }
                      }
                    }
                  }
                }
              },
              "availability": {
                "type": "string",
                "description": "Availability status of the MCP server",
                "example": "production"
              },
              "allowMultipleInstances": {
                "type": "boolean",
                "description": "Whether multiple instances of this server can be created",
                "example": false
              },
              "documentationUrl": {
                "type": "string",
                "nullable": true,
                "description": "URL to the server's documentation",
                "example": "https://docs.example.com/mcp-server"
              }
            }
          },
          "oAuthUseCase": {
            "type": "string",
            "nullable": true,
            "enum": [
              "platform_actions",
              "personal_actions"
            ],
            "description": "OAuth use case for the MCP server view",
            "example": "platform_actions"
          },
          "isRestrictedToSkills": {
            "type": "boolean",
            "description": "Whether the MCP server view can only be used through skills",
            "example": false
          },
          "editedByUser": {
            "type": "object",
            "nullable": true,
            "description": "Information about the user who last edited the MCP server view",
            "properties": {
              "editedAt": {
                "type": "number",
                "nullable": true,
                "description": "Unix timestamp of when the edit occurred",
                "example": 1625184000
              },
              "fullName": {
                "type": "string",
                "nullable": true,
                "description": "Full name of the editor",
                "example": "John Doe"
              },
              "imageUrl": {
                "type": "string",
                "nullable": true,
                "description": "Profile image URL of the editor",
                "example": "https://example.com/profile/johndoe.jpg"
              }
            }
          }
        }
      }
    }
  }
}
```
