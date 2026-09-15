# 创建内容片段

在指定工作区的对话中创建新的内容片段。

```http
POST /api/v1/w/{wId}/assistant/conversations/{cId}/content_fragments
```

服务地址：`https://app.counso.ai`

## 认证

在 `Authorization: Bearer <token>` 中传入工作区 API key 或用户 OAuth access token。凭据须由当前 Counso 环境签发，并有权访问目标工作区与资源。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 | 工作区 ID |
| `cId` | 路径 | string | 是 | 对话 ID |

## 请求体

`Content-Type: application/json`

| 字段 | 类型 | 必填 |
| --- | --- | --- |
| `title` | string | 是 |
| `content` | string | 否 |
| `contentType` | string | 否 |
| `url` | string | 否 |
| `fileId` | string | 否 |
| `path` | string | 否 |
| `processedPath` | string | 否 |
| `skipFileProcessing` | boolean | 否 |
| `nodeId` | string | 否 |
| `nodeDataSourceViewId` | string | 否 |
| `context` | object | 否 |

完整字段约束与嵌套结构见下方接口规范。

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 内容片段已创建。 |
| 400 | 请求错误：参数无效或缺失。 |
| 401 | 未授权：身份验证令牌无效或缺失。 |
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
    "/api/v1/w/{wId}/assistant/conversations/{cId}/content_fragments": {
      "post": {
        "summary": "Create a content fragment",
        "description": "Adds a newly created content fragment to a conversation in workspace {wId}.",
        "tags": [
          "Conversations"
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
            "name": "cId",
            "required": true,
            "description": "ID of the conversation",
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
                "$ref": "#/components/schemas/ContentFragment"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Content fragment created successfully.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ContentFragment"
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
      "ContentFragment": {
        "type": "object",
        "required": [
          "title"
        ],
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the content fragment",
            "example": "My content fragment"
          },
          "content": {
            "type": "string",
            "description": "The content of the content fragment (optional if `fileId` is set)",
            "example": "This is my content fragment extracted text"
          },
          "contentType": {
            "type": "string",
            "description": "The content type of the content fragment (optional if `fileId` is set)",
            "example": "text/plain"
          },
          "url": {
            "type": "string",
            "description": "The URL of the content fragment",
            "example": "https://example.com/content"
          },
          "fileId": {
            "type": "string",
            "description": "The id of the previously uploaded file (optional if `content` and `contentType` are set)",
            "example": "fil_123456"
          },
          "path": {
            "type": "string",
            "nullable": true,
            "description": "Path of this file inside the sandbox conversation mount.",
            "example": "conversation/report.csv"
          },
          "processedPath": {
            "type": "string",
            "nullable": true,
            "description": "Path of the plain-text sibling of this file inside the sandbox conversation mount (e.g. an audio transcript), when it has one.",
            "example": "conversation/voice.processed.txt"
          },
          "skipFileProcessing": {
            "type": "boolean",
            "description": "Whether upload-time file processing was skipped."
          },
          "nodeId": {
            "type": "string",
            "description": "The id of the content node (optional if `content` and `contentType` are set)",
            "example": "node_123456"
          },
          "nodeDataSourceViewId": {
            "type": "string",
            "description": "The id of the data source view (optional if `content` and `contentType` are set)",
            "example": "dsv_123456"
          },
          "context": {
            "$ref": "#/components/schemas/Context"
          }
        }
      },
      "Context": {
        "type": "object",
        "required": [
          "username",
          "timezone"
        ],
        "properties": {
          "username": {
            "type": "string",
            "description": "Username in the current context",
            "example": "johndoe123"
          },
          "timezone": {
            "type": "string",
            "description": "User's timezone",
            "example": "America/New_York"
          },
          "fullName": {
            "type": "string",
            "description": "User's full name in the current context",
            "example": "John Doe"
          },
          "email": {
            "type": "string",
            "description": "User's email in the current context",
            "example": "john.doe@example.com"
          },
          "profilePictureUrl": {
            "type": "string",
            "description": "URL of the user's profile picture",
            "example": "https://example.com/profiles/johndoe123.jpg"
          },
          "selectedSpaceIds": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "agenticMessageData": {
            "type": "object",
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "run_agent",
                  "agent_handover"
                ],
                "description": "Type of the agentic message"
              },
              "originMessageId": {
                "type": "string",
                "description": "ID of the origin message",
                "example": "2b8e4f6a0c"
              }
            }
          }
        }
      }
    }
  }
}
```
