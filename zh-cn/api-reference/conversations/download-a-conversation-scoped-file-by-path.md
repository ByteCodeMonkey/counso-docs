# 按路径下载对话文件

使用对话内的文件路径流式下载文件。优先使用消息操作 generatedFiles 返回的规范 filePath，也支持旧版 conversation/foo.pdf 形式。属于其他对话或其他范围的路径，以及包含 .. 越界片段的路径，都会被拒绝。

```http
GET /api/v1/w/{wId}/assistant/conversations/{cId}/files/{rel}
```

服务地址：`https://app.counso.ai`

## 认证

在 `Authorization: Bearer <token>` 中传入工作区 API key 或用户 OAuth access token。凭据须由当前 Counso 环境签发，并有权访问目标工作区与资源。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 | 工作区 ID |
| `cId` | 路径 | string | 是 | 对话 ID |
| `rel` | 路径 | string | 是 | 对话文件路径：使用消息操作 generatedFiles 返回的标准 filePath，也接受旧格式 conversation/foo.pdf。属于其他对话或其他范围的路径会被拒绝；路径遍历片段（..）也会被拒绝。 |

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 文件内容已直接以流形式返回。 |
| 400 | 路径参数缺失或无效（例如，范围前缀缺失或错误）。 |
| 403 | 解析出的路径超出当前对话范围。 |
| 404 | 未找到对话或文件。 |

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
    "/api/v1/w/{wId}/assistant/conversations/{cId}/files/{rel}": {
      "get": {
        "tags": [
          "Conversations"
        ],
        "summary": "Download a conversation-scoped file by path",
        "description": "Streams a conversation-mounted file using its scoped path. Prefer the canonical filePath listed under a message action's generatedFiles; the older conversation/foo.pdf form is also accepted. Paths belonging to another conversation or scope, including traversal with .., are rejected.",
        "parameters": [
          {
            "name": "wId",
            "in": "path",
            "required": true,
            "description": "ID of the workspace",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "cId",
            "in": "path",
            "required": true,
            "description": "ID of the conversation",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "rel",
            "in": "path",
            "required": true,
            "description": "Conversation-scoped file path: the canonical `filePath` returned in a message\naction's `generatedFiles`, or the legacy `conversation/foo.pdf` form. Paths\nscoped to another conversation or to a different scope are rejected. Path\ntraversal segments (`..`) are rejected.\n",
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
        "responses": {
          "200": {
            "description": "File content streamed directly.",
            "content": {
              "application/octet-stream": {
                "schema": {
                  "type": "string",
                  "format": "binary"
                }
              }
            }
          },
          "400": {
            "description": "Missing or invalid path parameters (e.g. missing or wrong scope prefix)."
          },
          "403": {
            "description": "Resolved path is outside the conversation scope."
          },
          "404": {
            "description": "Conversation or file not found."
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
