---
title: "查看或下载文件"
---
会话接口：查看或下载文件；读取 Skill 附件需要对关联 Skill 有读取权限。可用 version 参数选择 original、processed 或 public 版本，并用 action 指定 view 或 download。

```http
GET /api/w/{wId}/files/{fileId}
```

服务地址：`https://app.counso.ai`

## 认证

此接口需要用户身份：外部客户端通过 `Authorization: Bearer <token>` 传入用户 OAuth access token；已登录的浏览器也可使用 Counso 会话 Cookie。工作区 API key 不能代替用户身份。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 | 工作区 ID |
| `fileId` | 路径 | string | 是 | 文件 ID |
| `version` | 查询 | string | 否 | 要获取的文件版本 可选值：`original`, `processed`, `public` |
| `action` | 查询 | string | 否 | 要执行的操作 可选值：`view`, `download` |

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 文件内容，或用于下载的重定向 URL |
| 302 | 重定向到签名下载 URL |
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
      "get": {
        "summary": "Get or download a file",
        "description": "Private session interface. Opens or downloads a file. Reading a Skill attachment requires read access to that Skill; version (original, processed, public) and action (view, download) select the returned content and operation.",
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
          },
          {
            "in": "query",
            "name": "version",
            "required": false,
            "description": "File version to retrieve",
            "schema": {
              "type": "string",
              "enum": [
                "original",
                "processed",
                "public"
              ]
            }
          },
          {
            "in": "query",
            "name": "action",
            "required": false,
            "description": "Action to perform",
            "schema": {
              "type": "string",
              "enum": [
                "view",
                "download"
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
            "description": "File content or redirect to download URL",
            "content": {
              "application/octet-stream": {
                "schema": {
                  "type": "string",
                  "format": "binary"
                }
              }
            }
          },
          "302": {
            "description": "Redirect to signed download URL"
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
    }
  }
}
```
