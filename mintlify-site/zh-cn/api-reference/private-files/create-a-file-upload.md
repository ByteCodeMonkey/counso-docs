---
title: "创建文件上传记录"
---
会话接口：创建文件记录并返回预签名上传 URL；随后需将文件内容上传到该地址。

```http
POST /api/w/{wId}/files
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
| `contentType` | string | 是 |
| `fileName` | string | 是 |
| `fileSize` | number | 是 |
| `useCase` | string | 是 |
| `useCaseMetadata` | object | 否 |

完整字段约束与嵌套结构见下方接口规范。

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 文件记录及上传 URL 已创建 |
| 400 | 请求无效 |
| 429 | 超出速率限制 |

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
    "/api/w/{wId}/files": {
      "post": {
        "summary": "Create a file upload",
        "description": "Private session interface. Creates the file record first, then returns a pre-signed upload URL for the content.",
        "tags": [
          "Private Files"
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
                  "contentType",
                  "fileName",
                  "fileSize",
                  "useCase"
                ],
                "properties": {
                  "contentType": {
                    "type": "string"
                  },
                  "fileName": {
                    "type": "string"
                  },
                  "fileSize": {
                    "type": "number"
                  },
                  "useCase": {
                    "type": "string",
                    "enum": [
                      "conversation",
                      "folders_document",
                      "avatar",
                      "upsert_document",
                      "upsert_table",
                      "project_context",
                      "skill_attachment",
                      "workspace_branding"
                    ]
                  },
                  "useCaseMetadata": {
                    "type": "object"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "File record created with upload URL",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "file": {
                      "$ref": "#/components/schemas/PrivateFileWithUploadUrl"
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Invalid request"
          },
          "429": {
            "description": "Rate limit exceeded"
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
      "PrivateFileWithUploadUrl": {
        "type": "object",
        "description": "File record with a pre-signed upload URL.",
        "required": [
          "sId",
          "id",
          "fileName",
          "fileSize",
          "contentType",
          "status",
          "useCase",
          "uploadUrl"
        ],
        "properties": {
          "sId": {
            "type": "string"
          },
          "id": {
            "type": "string"
          },
          "contentType": {
            "type": "string"
          },
          "fileName": {
            "type": "string"
          },
          "fileSize": {
            "type": "integer"
          },
          "version": {
            "type": "integer"
          },
          "status": {
            "type": "string",
            "enum": [
              "created",
              "failed",
              "ready"
            ]
          },
          "useCase": {
            "type": "string",
            "enum": [
              "conversation",
              "avatar",
              "tool_output",
              "upsert_document",
              "folders_document",
              "upsert_table",
              "project_context",
              "skill_attachment"
            ]
          },
          "uploadUrl": {
            "type": "string",
            "description": "Pre-signed URL for uploading the file content"
          },
          "downloadUrl": {
            "type": "string"
          },
          "publicUrl": {
            "type": "string"
          },
          "path": {
            "type": "string",
            "nullable": true,
            "description": "path when the file is ready on a mount (e.g. `project/report.pdf` or `conversation/chart.png`). Same shape as mount file listing entries."
          }
        }
      }
    }
  }
}
```
