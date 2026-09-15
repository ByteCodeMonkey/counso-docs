---
title: "上传工具文件"
---
将 MCP 服务器工具返回的文件下载后上传到工作区。

```http
POST /api/v1/w/{wId}/search/tools/upload
```

服务地址：`https://app.counso.ai`

## 认证

在 `Authorization: Bearer <token>` 中传入工作区 API key 或用户 OAuth access token。凭据须由当前 Counso 环境签发，并有权访问目标工作区与资源。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 | 工作区 ID |

## 请求体

`Content-Type: application/json`

| 字段 | 类型 | 必填 |
| --- | --- | --- |
| `serverViewId` | string | 是 |
| `externalId` | string | 是 |
| `conversationId` | string | 否 |
| `serverName` | string | 否 |
| `serverIcon` | string | 否 |

完整字段约束与嵌套结构见下方接口规范。

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 文件已上传 |
| 400 | 请求错误 |
| 401 | 未授权 |
| 500 | 内部服务器错误 |

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
    "/api/v1/w/{wId}/search/tools/upload": {
      "post": {
        "summary": "Upload a tool file",
        "description": "Moves a file returned by an MCP server tool into the workspace by downloading and uploading its contents.",
        "tags": [
          "Search"
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
            "WorkspaceApiKey": []
          },
          {
            "UserAccessToken": []
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "serverViewId",
                  "externalId"
                ],
                "properties": {
                  "serverViewId": {
                    "type": "string",
                    "description": "The MCP server view ID"
                  },
                  "externalId": {
                    "type": "string",
                    "description": "The external ID of the file in the tool"
                  },
                  "conversationId": {
                    "type": "string",
                    "description": "Optional conversation ID for context"
                  },
                  "serverName": {
                    "type": "string",
                    "description": "Optional name of the MCP server (e.g., \"Notion\", \"GitHub\")"
                  },
                  "serverIcon": {
                    "type": "string",
                    "description": "Optional icon identifier for the MCP server"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "File uploaded successfully"
          },
          "400": {
            "description": "Bad request"
          },
          "401": {
            "description": "Unauthorized"
          },
          "500": {
            "description": "Internal server error"
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
    }
  }
}
```
