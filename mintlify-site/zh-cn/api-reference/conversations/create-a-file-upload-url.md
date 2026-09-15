---
title: "创建文件上传地址"
---
为工作区文件创建上传记录并取得上传所需的 URL。

```http
POST /api/v1/w/{wId}/files
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
| `contentType` | string | 是 |
| `fileName` | string | 是 |
| `fileSize` | integer | 是 |
| `useCase` | string | 是 |
| `useCaseMetadata` | string | 是 |

完整字段约束与嵌套结构见下方接口规范。

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 文件上传 URL 已创建 |
| 400 | 请求无效或文件类型不受支持 |
| 401 | 未授权 |
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
    "/api/v1/w/{wId}/files": {
      "post": {
        "tags": [
          "Conversations"
        ],
        "summary": "Create a file upload URL",
        "parameters": [
          {
            "name": "wId",
            "in": "path",
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
                  "contentType",
                  "fileName",
                  "fileSize",
                  "useCase",
                  "useCaseMetadata"
                ],
                "properties": {
                  "contentType": {
                    "type": "string",
                    "description": "MIME type of the file"
                  },
                  "fileName": {
                    "type": "string",
                    "description": "Name of the file"
                  },
                  "fileSize": {
                    "type": "integer",
                    "description": "Size of the file in bytes"
                  },
                  "useCase": {
                    "type": "string",
                    "description": "Intended use case for the file, use \"conversation\""
                  },
                  "useCaseMetadata": {
                    "type": "string",
                    "description": "(optional) Metadata for the use case, for conversation useCase should be dictionary with conversationId stringified"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "File upload URL created successfully",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "file": {
                      "type": "object",
                      "properties": {
                        "sId": {
                          "type": "string",
                          "description": "Unique string identifier for the file"
                        },
                        "uploadUrl": {
                          "type": "string",
                          "description": "Upload URL for the file"
                        }
                      }
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Invalid request or unsupported file type"
          },
          "401": {
            "description": "Unauthorized"
          },
          "429": {
            "description": "Rate limit exceeded"
          }
        },
        "x-counso-auth": "workspace",
        "description": "Allocates a workspace file record and supplies the URL where its contents should be uploaded."
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
