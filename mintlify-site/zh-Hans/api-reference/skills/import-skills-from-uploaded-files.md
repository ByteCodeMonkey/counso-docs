---
title: "从上传文件导入 Skills"
---
从已上传的文件或 ZIP 压缩包导入 Skills。

```http
POST /api/v1/w/{wId}/skills
```

服务地址：`https://app.counso.ai`

## 认证

在 `Authorization: Bearer <token>` 中传入工作区 API key 或用户 OAuth access token。凭据须由当前 Counso 环境签发，并有权访问目标工作区与资源。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 | 工作区的唯一字符串标识符 |

## 请求体

`Content-Type: multipart/form-data`

| 字段 | 类型 | 必填 |
| --- | --- | --- |
| `files` | array[string / binary] | 是 |
| `names` | array[string] | 否 |
| `onConflict` | string | 否 |
| `editors` | array[string / email] | 否 |
| `availability` | string | 否 |

完整字段约束与嵌套结构见下方接口规范。

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | Skills 导入结果。 |
| 400 | 请求错误：上传文件无效或缺失。 |
| 401 | 未授权：身份验证令牌无效或缺失。 |
| 404 | 未找到工作区。 |

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
    "/api/v1/w/{wId}/skills": {
      "post": {
        "summary": "Import skills from uploaded files",
        "description": "Adds Skills to the workspace from uploaded files or a ZIP archive.",
        "tags": [
          "Skills"
        ],
        "security": [
          {
            "WorkspaceApiKey": []
          },
          {
            "UserAccessToken": []
          }
        ],
        "parameters": [
          {
            "in": "path",
            "name": "wId",
            "required": true,
            "description": "Unique string identifier for the workspace",
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "multipart/form-data": {
              "schema": {
                "type": "object",
                "required": [
                  "files"
                ],
                "properties": {
                  "files": {
                    "type": "array",
                    "items": {
                      "type": "string",
                      "format": "binary"
                    },
                    "description": "Skill files or ZIP archives to import."
                  },
                  "names": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    },
                    "description": "Optional skill names to import from the uploaded files."
                  },
                  "onConflict": {
                    "type": "string",
                    "enum": [
                      "error",
                      "skip",
                      "override"
                    ],
                    "description": "Conflict handling strategy. Defaults to error."
                  },
                  "editors": {
                    "type": "array",
                    "items": {
                      "type": "string",
                      "format": "email"
                    },
                    "description": "Optional editor email addresses to add to imported or updated skills. Editors must be active workspace builders. Existing skills keep their current editors."
                  },
                  "availability": {
                    "type": "string",
                    "enum": [
                      "editors",
                      "workspace_users",
                      "users_and_agents"
                    ],
                    "description": "Optional availability to apply to imported or updated skills. editors is unpublished, workspace_users is published, and users_and_agents is discoverable. New skills default to editors and existing skills keep their current availability when omitted."
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Skills import result.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "imported": {
                      "type": "array",
                      "items": {
                        "$ref": "#/components/schemas/Skill"
                      }
                    },
                    "updated": {
                      "type": "array",
                      "items": {
                        "$ref": "#/components/schemas/Skill"
                      }
                    },
                    "skipped": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "name": {
                            "type": "string"
                          },
                          "message": {
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
            "description": "Bad Request. Missing or invalid uploaded files."
          },
          "401": {
            "description": "Unauthorized. Invalid or missing authentication token."
          },
          "404": {
            "description": "Workspace not found."
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
      "Skill": {
        "type": "object",
        "properties": {
          "sId": {
            "type": "string",
            "description": "Unique string identifier for the skill",
            "example": "skill_abc123"
          },
          "createdAt": {
            "type": "number",
            "nullable": true,
            "description": "Timestamp of when the skill was created"
          },
          "updatedAt": {
            "type": "number",
            "nullable": true,
            "description": "Timestamp of when the skill was last updated"
          },
          "editedBy": {
            "type": "integer",
            "nullable": true,
            "description": "Numeric identifier of the last editor"
          },
          "status": {
            "type": "string",
            "enum": [
              "active",
              "archived",
              "suggested"
            ],
            "description": "Current status of the skill",
            "example": "active"
          },
          "name": {
            "type": "string",
            "description": "Name of the skill",
            "example": "Customer Support"
          },
          "agentFacingDescription": {
            "type": "string",
            "description": "Description shown to agents when selecting or using the skill",
            "example": "Use this skill to answer customer support questions."
          },
          "userFacingDescription": {
            "type": "string",
            "description": "Description shown to workspace users",
            "example": "Answers support questions with the right workspace context."
          },
          "icon": {
            "type": "string",
            "nullable": true,
            "description": "Icon identifier for the skill",
            "example": "ActionRobotIcon"
          },
          "source": {
            "type": "string",
            "nullable": true,
            "enum": [
              "web_app",
              "github",
              "api",
              "local_file"
            ],
            "description": "Source used to create or import the skill"
          },
          "sourceMetadata": {
            "type": "object",
            "nullable": true,
            "allOf": [
              {
                "$ref": "#/components/schemas/SkillSourceMetadata"
              }
            ]
          },
          "reinforcement": {
            "type": "string",
            "enum": [
              "auto",
              "on",
              "off"
            ],
            "description": "Reinforcement setting for the skill"
          },
          "lastReinforcementAnalysisAt": {
            "type": "string",
            "nullable": true,
            "description": "Timestamp of the last reinforcement analysis, when available"
          },
          "requestedSpaceIds": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Space identifiers the skill needs access to"
          },
          "manuallyRequestedSpaceIds": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Subset of requestedSpaceIds that was selected by hand rather than derived from the skill's tools, knowledge or nested skills\n"
          },
          "fileAttachments": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "fileId": {
                  "type": "string",
                  "description": "Unique string identifier for the attached file"
                },
                "fileName": {
                  "type": "string",
                  "description": "Name of the attached file"
                }
              }
            }
          },
          "canRead": {
            "type": "boolean",
            "description": "Whether the authenticated actor can read the skill's instructions, tools and files. False when they were redacted for a workspace admin who is not a member of every space the skill requires."
          },
          "canWrite": {
            "type": "boolean",
            "description": "Whether the authenticated actor can edit the skill"
          },
          "isDefault": {
            "type": "boolean",
            "deprecated": true,
            "description": "Whether this skill is enabled by default. Deprecated, use availability instead."
          },
          "availability": {
            "type": "string",
            "enum": [
              "editors",
              "workspace_users",
              "users_and_agents"
            ],
            "description": "Who the skill is available to (users_and_agents makes it discoverable by agents)"
          },
          "instructions": {
            "type": "string",
            "nullable": true,
            "description": "Instructions used by the agent when running the skill"
          },
          "instructionsHtml": {
            "type": "string",
            "nullable": true,
            "description": "HTML representation of the skill instructions"
          },
          "tools": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/MCPServerView"
            }
          }
        }
      },
      "MCPServerView": {
        "type": "object",
        "required": [
          "isRestrictedToSkills"
        ],
        "properties": {
          "id": {
            "type": "integer",
            "description": "Unique identifier for the MCP server view",
            "example": 123
          },
          "sId": {
            "type": "string",
            "description": "Unique string identifier for the MCP server view",
            "example": "mcp_sv_abc123"
          },
          "name": {
            "type": "string",
            "nullable": true,
            "description": "Custom name for the MCP server view (null if not set)",
            "example": "My Custom MCP Server"
          },
          "description": {
            "type": "string",
            "nullable": true,
            "description": "Custom description for the MCP server view (null if not set)",
            "example": "This MCP server handles customer data operations"
          },
          "createdAt": {
            "type": "number",
            "description": "Unix timestamp of when the MCP server view was created",
            "example": 1625097600
          },
          "updatedAt": {
            "type": "number",
            "description": "Unix timestamp of when the MCP server view was last updated",
            "example": 1625184000
          },
          "spaceId": {
            "type": "string",
            "description": "ID of the space containing the MCP server view",
            "example": "spc_xyz789"
          },
          "serverType": {
            "type": "string",
            "enum": [
              "remote",
              "internal"
            ],
            "description": "Type of the MCP server",
            "example": "remote"
          },
          "server": {
            "type": "object",
            "properties": {
              "sId": {
                "type": "string",
                "description": "Unique string identifier for the MCP server",
                "example": "mcp_srv_def456"
              },
              "name": {
                "type": "string",
                "description": "Name of the MCP server",
                "example": "Customer Data Server"
              },
              "version": {
                "type": "string",
                "description": "Version of the MCP server",
                "example": "1.0.0"
              },
              "description": {
                "type": "string",
                "description": "Description of the MCP server",
                "example": "Handles customer data operations and queries"
              },
              "icon": {
                "type": "string",
                "description": "Icon identifier for the MCP server",
                "example": "database"
              },
              "authorization": {
                "type": "object",
                "nullable": true,
                "properties": {
                  "provider": {
                    "type": "string",
                    "description": "OAuth provider for authorization",
                    "example": "github"
                  },
                  "supported_use_cases": {
                    "type": "array",
                    "items": {
                      "type": "string",
                      "enum": [
                        "platform_actions",
                        "personal_actions"
                      ]
                    },
                    "description": "Supported use cases for the authorization",
                    "example": [
                      "platform_actions"
                    ]
                  },
                  "scope": {
                    "type": "string",
                    "description": "OAuth scope required",
                    "example": "repo:read"
                  }
                }
              },
              "tools": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "name": {
                      "type": "string",
                      "description": "Name of the tool",
                      "example": "query_customers"
                    },
                    "description": {
                      "type": "string",
                      "description": "Description of what the tool does",
                      "example": "Query customer database for information"
                    },
                    "inputSchema": {
                      "type": "object",
                      "description": "JSON Schema for the tool's input parameters",
                      "example": {
                        "type": "object",
                        "properties": {
                          "customerId": {
                            "type": "string"
                          }
                        }
                      }
                    }
                  }
                }
              },
              "availability": {
                "type": "string",
                "description": "Availability status of the MCP server",
                "example": "production"
              },
              "allowMultipleInstances": {
                "type": "boolean",
                "description": "Whether multiple instances of this server can be created",
                "example": false
              },
              "documentationUrl": {
                "type": "string",
                "nullable": true,
                "description": "URL to the server's documentation",
                "example": "https://docs.example.com/mcp-server"
              }
            }
          },
          "oAuthUseCase": {
            "type": "string",
            "nullable": true,
            "enum": [
              "platform_actions",
              "personal_actions"
            ],
            "description": "OAuth use case for the MCP server view",
            "example": "platform_actions"
          },
          "isRestrictedToSkills": {
            "type": "boolean",
            "description": "Whether the MCP server view can only be used through skills",
            "example": false
          },
          "editedByUser": {
            "type": "object",
            "nullable": true,
            "description": "Information about the user who last edited the MCP server view",
            "properties": {
              "editedAt": {
                "type": "number",
                "nullable": true,
                "description": "Unix timestamp of when the edit occurred",
                "example": 1625184000
              },
              "fullName": {
                "type": "string",
                "nullable": true,
                "description": "Full name of the editor",
                "example": "John Doe"
              },
              "imageUrl": {
                "type": "string",
                "nullable": true,
                "description": "Profile image URL of the editor",
                "example": "https://example.com/profile/johndoe.jpg"
              }
            }
          }
        }
      },
      "SkillSourceMetadata": {
        "type": "object",
        "properties": {
          "repoUrl": {
            "type": "string",
            "description": "URL of the source repository, when applicable",
            "example": "https://github.com/example/agent-skills"
          },
          "filePath": {
            "type": "string",
            "description": "Path to the source skill file",
            "example": "support/SKILL.md"
          }
        }
      }
    }
  }
}
```
