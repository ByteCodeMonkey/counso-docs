---
title: "创建对话内容片段"
---
会话接口：向现有对话添加一个新的内容片段。

```http
POST /api/w/{wId}/assistant/conversations/{cId}/content_fragment
```

服务地址：`https://app.counso.ai`

## 认证

此接口需要用户身份：外部客户端通过 `Authorization: Bearer <token>` 传入用户 OAuth access token；已登录的浏览器也可使用 Counso 会话 Cookie。工作区 API key 不能代替用户身份。

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
| `content` | string | 是 |
| `contentType` | string | 是 |
| `url` | string | 否 |
| `context` | object | 是 |
| `fileId` | string | 否 |

完整字段约束与嵌套结构见下方接口规范。

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 已成功创建内容片段 |
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
    "/api/w/{wId}/assistant/conversations/{cId}/content_fragment": {
      "post": {
        "summary": "Create a content fragment",
        "description": "Private session interface. Inserts a content fragment into an existing conversation.",
        "tags": [
          "Private Conversations"
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
                  "title",
                  "content",
                  "contentType",
                  "context"
                ],
                "properties": {
                  "title": {
                    "type": "string"
                  },
                  "content": {
                    "type": "string"
                  },
                  "contentType": {
                    "type": "string",
                    "description": "MIME type of the content"
                  },
                  "url": {
                    "type": "string",
                    "nullable": true
                  },
                  "context": {
                    "type": "object",
                    "properties": {
                      "profilePictureUrl": {
                        "type": "string",
                        "nullable": true
                      }
                    }
                  },
                  "fileId": {
                    "type": "string",
                    "nullable": true
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Successfully created content fragment",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "contentFragment": {
                      "$ref": "#/components/schemas/PrivateContentFragment"
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
      "PrivateContentFragment": {
        "type": "object",
        "description": "A content fragment (file or content node attachment) in a conversation.",
        "required": [
          "type",
          "sId",
          "title",
          "contentType",
          "contentFragmentType"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "content_fragment"
            ]
          },
          "id": {
            "type": "integer"
          },
          "sId": {
            "type": "string"
          },
          "created": {
            "type": "integer"
          },
          "visibility": {
            "type": "string",
            "enum": [
              "visible",
              "deleted"
            ]
          },
          "version": {
            "type": "integer"
          },
          "rank": {
            "type": "integer"
          },
          "title": {
            "type": "string"
          },
          "contentType": {
            "type": "string",
            "description": "MIME type of the content"
          },
          "sourceUrl": {
            "type": "string",
            "nullable": true
          },
          "context": {
            "type": "object",
            "properties": {
              "username": {
                "type": "string",
                "nullable": true
              },
              "fullName": {
                "type": "string",
                "nullable": true
              },
              "email": {
                "type": "string",
                "nullable": true
              },
              "profilePictureUrl": {
                "type": "string",
                "nullable": true
              }
            }
          },
          "contentFragmentId": {
            "type": "string"
          },
          "contentFragmentVersion": {
            "type": "string",
            "enum": [
              "superseded",
              "latest"
            ]
          },
          "contentFragmentType": {
            "type": "string",
            "enum": [
              "file",
              "content_node"
            ],
            "description": "Whether this is a file upload or a content node reference"
          },
          "expiredReason": {
            "type": "string",
            "nullable": true,
            "enum": [
              "data_source_deleted"
            ]
          },
          "fileId": {
            "type": "string",
            "nullable": true,
            "description": "Present for file content fragments"
          },
          "path": {
            "type": "string",
            "nullable": true,
            "description": "Path of this file inside the sandbox conversation mount."
          },
          "processedPath": {
            "type": "string",
            "nullable": true,
            "description": "Path of the plain-text sibling of this file inside the sandbox conversation mount (e.g. an audio transcript), when it has one."
          },
          "skipFileProcessing": {
            "type": "boolean",
            "description": "Whether upload-time file processing was skipped."
          },
          "snippet": {
            "type": "string",
            "nullable": true
          },
          "textUrl": {
            "type": "string",
            "nullable": true
          },
          "textBytes": {
            "type": "integer",
            "nullable": true
          },
          "nodeId": {
            "type": "string",
            "nullable": true,
            "description": "Present for content node fragments"
          },
          "nodeDataSourceViewId": {
            "type": "string",
            "nullable": true
          }
        }
      }
    }
  }
}
```
