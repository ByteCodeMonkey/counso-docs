---
title: "按名称搜索智能体"
---
按名称搜索指定工作区中的智能体配置。

```http
GET /api/v1/w/{wId}/assistant/agent_configurations/search
```

服务地址：`https://app.counso.ai`

## 认证

在 `Authorization: Bearer <token>` 中传入工作区 API key 或用户 OAuth access token。凭据须由当前 Counso 环境签发，并有权访问目标工作区与资源。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 | 工作区 ID |
| `q` | 查询 | string | 是 | 用于筛选智能体配置名称的搜索词 |

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 已成功获取智能体配置列表 |
| 400 | 请求错误：参数无效或缺失。 |
| 401 | 未授权：身份验证令牌无效或缺失。 |
| 404 | 未找到工作区。 |
| 500 | 内部服务器错误。 |

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
    "/api/v1/w/{wId}/assistant/agent_configurations/search": {
      "get": {
        "summary": "Search agents by name",
        "description": "Finds workspace {wId} agent configurations whose names match the supplied search.",
        "tags": [
          "Agents"
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
            "in": "query",
            "name": "q",
            "required": true,
            "description": "Search query for agent configuration names",
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
            "description": "Successfully retrieved agent configurations",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "agentConfigurations": {
                      "type": "array",
                      "items": {
                        "$ref": "#/components/schemas/AgentConfiguration"
                      }
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Bad Request. Invalid or missing parameters."
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
      "AgentConfiguration": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "example": 12345
          },
          "sId": {
            "type": "string",
            "description": "Unique string identifier for the agent configuration",
            "example": "7f3a9c2b1e"
          },
          "version": {
            "type": "integer",
            "example": 2
          },
          "versionCreatedAt": {
            "type": "string",
            "nullable": true,
            "description": "Timestamp of when the version was created",
            "example": "2023-06-15T14:30:00Z"
          },
          "versionAuthorId": {
            "type": "string",
            "nullable": true,
            "description": "ID of the user who created this version",
            "example": "0ec9852c2f"
          },
          "name": {
            "type": "string",
            "description": "Name of the agent configuration",
            "example": "Customer Support Agent"
          },
          "description": {
            "type": "string",
            "description": "Description of the agent configuration",
            "example": "An AI agent designed to handle customer support inquiries"
          },
          "instructions": {
            "type": "string",
            "nullable": true,
            "description": "Instructions for the agent",
            "example": "Always greet the customer politely and try to resolve their issue efficiently."
          },
          "pictureUrl": {
            "type": "string",
            "description": "URL of the agent's picture",
            "example": "https://example.com/agent-images/support-agent.png"
          },
          "status": {
            "type": "string",
            "description": "Current status of the agent configuration",
            "example": "active"
          },
          "scope": {
            "type": "string",
            "description": "Scope of the agent configuration",
            "example": "workspace"
          },
          "userFavorite": {
            "type": "boolean",
            "description": "Status of the user favorite for this configuration",
            "example": true
          },
          "model": {
            "type": "object",
            "properties": {
              "providerId": {
                "type": "string",
                "description": "ID of the model provider",
                "example": "openai"
              },
              "modelId": {
                "type": "string",
                "description": "ID of the specific model",
                "example": "gpt-4"
              },
              "temperature": {
                "type": "number",
                "example": 0.7
              }
            }
          },
          "actions": {
            "type": "array",
            "example": []
          },
          "skills": {
            "type": "array",
            "description": "Skills attached to the agent. Returned by the agent GET endpoints (list and single-agent) whatever the requested variant. Empty both for an agent with no skill and for an agent whose details were redacted for the caller (canRead false).",
            "items": {
              "$ref": "#/components/schemas/AgentSkill"
            }
          },
          "tags": {
            "type": "array",
            "description": "Tags attached to the agent",
            "items": {
              "type": "object",
              "properties": {
                "sId": {
                  "type": "string",
                  "example": "3f9d1c7a5b"
                },
                "name": {
                  "type": "string",
                  "example": "Support"
                },
                "kind": {
                  "type": "string",
                  "enum": [
                    "standard",
                    "protected"
                  ]
                }
              }
            }
          },
          "requestedSpaceIds": {
            "type": "array",
            "description": "Identifiers of the spaces the agent needs access to",
            "items": {
              "type": "string"
            },
            "example": [
              "vlt_a1b2c3d4e5"
            ]
          },
          "maxStepsPerRun": {
            "type": "integer",
            "example": 10
          },
          "templateId": {
            "type": "string",
            "nullable": true,
            "description": "ID of the template used for this configuration",
            "example": "b4e2f1a9c7"
          }
        }
      },
      "AgentSkill": {
        "type": "object",
        "description": "A skill attached to an agent configuration.",
        "properties": {
          "sId": {
            "type": "string",
            "description": "Unique string identifier for the skill",
            "example": "skill_abc123"
          },
          "name": {
            "type": "string",
            "description": "Name of the skill",
            "example": "Customer Support"
          }
        }
      }
    }
  }
}
```
