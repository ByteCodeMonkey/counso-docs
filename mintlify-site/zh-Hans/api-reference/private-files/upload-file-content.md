---
title: "上传文件内容"
---
会话接口：处理并保存已上传的文件内容。

```http
POST /api/w/{wId}/files/{fileId}
```

服务地址：`https://app.counso.ai`

## 认证

此接口需要用户身份：外部客户端通过 `Authorization: Bearer <token>` 传入用户 OAuth access token；已登录的浏览器也可使用 Counso 会话 Cookie。工作区 API key 不能代替用户身份。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 | 工作区 ID |
| `fileId` | 路径 | string | 是 | 文件 ID |

## 请求体

`Content-Type: multipart/form-data`

| 字段 | 类型 | 必填 |
| --- | --- | --- |
| `file` | string / binary | 否 |

完整字段约束与嵌套结构见下方接口规范。

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 文件已处理 |
| 400 | 文件内容无效（例如，CSV 使用了不受支持的编码） |
| 403 | 权限被拒绝 |
| 404 | 未找到文件 |

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
    "/api/w/{wId}/files/{fileId}": {
      "post": {
        "summary": "Upload file content",
        "description": "Private session interface. Processes the supplied file bytes and saves the resulting content.",
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
          },
          {
            "in": "path",
            "name": "fileId",
            "required": true,
            "description": "ID of the file",
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
            "multipart/form-data": {
              "schema": {
                "type": "object",
                "properties": {
                  "file": {
                    "type": "string",
                    "format": "binary"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "File processed successfully",
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
            "description": "Invalid file content (e.g. a CSV with an unsupported encoding)"
          },
          "403": {
            "description": "Permission denied"
          },
          "404": {
            "description": "File not found"
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
