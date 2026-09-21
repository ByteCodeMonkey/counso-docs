---
title: "更新智能体配置"
---
更新指定工作区中的智能体配置。

```http
PATCH /api/v1/w/{wId}/assistant/agent_configurations/{sId}
```

服务地址：`https://app.counso.ai`

## 认证

在 `Authorization: Bearer <token>` 中传入工作区 API key 或用户 OAuth access token。凭据须由当前 Counso 环境签发，并有权访问目标工作区与资源。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 | 工作区 ID |
| `sId` | 路径 | string | 是 | 智能体配置 ID |

## 请求体

`Content-Type: application/json`

| 字段 | 类型 | 必填 |
| --- | --- | --- |
| `userFavorite` | boolean | 否 |
| `agent` | object | 否 |
| `instructions` | string | 否 |
| `generation_settings` | object | 否 |
| `tags` | array[object] | 否 |
| `editors` | array[string / email] | 否 |
| `skills` | array[object] | 否 |
| `toolset` | array[object] | 否 |

完整字段约束与嵌套结构见下方接口规范。

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 已成功更新智能体配置 |
| 400 | 请求错误：参数无效或缺失。 |
| 401 | 未授权：身份验证令牌无效或缺失。 |
| 404 | 未找到智能体配置。 |
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
    "/api/v1/w/{wId}/assistant/agent_configurations/{sId}": {
      "patch": {
        "summary": "Update agent configuration",
        "description": "Applies changes to configuration {sId} within workspace {wId}.",
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
            "in": "path",
            "name": "sId",
            "required": true,
            "description": "ID of the agent configuration",
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "userFavorite": {
                    "type": "boolean"
                  },
                  "agent": {
                    "type": "object",
                    "properties": {
                      "handle": {
                        "type": "string"
                      },
                      "description": {
                        "type": "string"
                      },
                      "scope": {
                        "type": "string",
                        "enum": [
                          "visible",
                          "hidden"
                        ]
                      },
                      "avatar_url": {
                        "type": "string"
                      },
                      "max_steps_per_run": {
                        "type": "number"
                      },
                      "visualization_enabled": {
                        "type": "boolean"
                      }
                    }
                  },
                  "instructions": {
                    "type": "string"
                  },
                  "generation_settings": {
                    "type": "object",
                    "properties": {
                      "model_id": {
                        "type": "string"
                      },
                      "provider_id": {
                        "type": "string"
                      },
                      "temperature": {
                        "type": "number"
                      },
                      "reasoning_effort": {
                        "type": "string"
                      }
                    }
                  },
                  "tags": {
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "name": {
                          "type": "string"
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
                  "editors": {
                    "type": "array",
                    "description": "Emails of the workspace members to set as editors of the agent. Omitting this field keeps the current editors; providing it replaces the whole list.",
                    "items": {
                      "type": "string",
                      "format": "email"
                    },
                    "example": [
                      "alice@example.com"
                    ]
                  },
                  "skills": {
                    "type": "array",
                    "description": "Replaces the skills enabled on the agent configuration.",
                    "items": {
                      "type": "object",
                      "required": [
                        "sId",
                        "name"
                      ],
                      "properties": {
                        "sId": {
                          "type": "string"
                        },
                        "name": {
                          "type": "string"
                        }
                      }
                    }
                  },
                  "toolset": {
                    "type": "array",
                    "description": "Replaces the full set of tools on the agent. Any tool not present in this array is removed, so send the complete desired toolset. Each entry resolves an MCP server by name (see configuration.mcp_server_name). Entries that cannot be resolved are not applied and are returned in the skippedActions field of the response rather than causing the whole request to fail.",
                    "items": {
                      "type": "object",
                      "properties": {
                        "name": {
                          "type": "string"
                        },
                        "description": {
                          "type": "string"
                        },
                        "type": {
                          "type": "string",
                          "enum": [
                            "MCP"
                          ]
                        },
                        "configuration": {
                          "type": "object",
                          "properties": {
                            "mcp_server_name": {
                              "type": "string",
                              "description": "Name of the MCP server to attach. Both built-in (internal) tools and remote MCP servers are supported. A remote MCP server must first be shared to a space (global or a regular space the caller can access); it is matched by its display name, which must be unambiguous within the workspace."
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        },
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
            "description": "Successfully updated agent configuration",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "agentConfiguration": {
                      "$ref": "#/components/schemas/AgentConfiguration"
                    },
                    "skippedActions": {
                      "type": "array",
                      "description": "Toolset entries that could not be applied (e.g. the referenced MCP server was not found, is not shared to an accessible space, or the name was ambiguous). The request still succeeds; inspect this list to confirm every intended tool was attached.",
                      "items": {
                        "type": "object",
                        "properties": {
                          "name": {
                            "type": "string"
                          },
                          "reason": {
                            "type": "string"
                          }
                        }
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
            "description": "Agent configuration not found."
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
