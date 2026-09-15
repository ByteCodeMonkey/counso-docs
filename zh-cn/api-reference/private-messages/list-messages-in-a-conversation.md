# 列出对话消息

会话接口：分页读取指定对话中的消息。

```http
GET /api/w/{wId}/assistant/conversations/{cId}/messages
```

服务地址：`https://app.counso.ai`

## 认证

此接口需要用户身份：外部客户端通过 `Authorization: Bearer <token>` 传入用户 OAuth access token；已登录的浏览器也可使用 Counso 会话 Cookie。工作区 API key 不能代替用户身份。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 | 工作区 ID |
| `cId` | 路径 | string | 是 | 对话 ID |

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 已成功获取消息列表 |
| 401 | 未授权 |

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
    "/api/w/{wId}/assistant/conversations/{cId}/messages": {
      "get": {
        "summary": "List messages in a conversation",
        "description": "Private session interface. Pages through the messages belonging to a selected conversation.",
        "tags": [
          "Private Messages"
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
        "responses": {
          "200": {
            "description": "Successfully retrieved messages",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "messages": {
                      "type": "array",
                      "items": {
                        "oneOf": [
                          {
                            "$ref": "#/components/schemas/PrivateUserMessage"
                          },
                          {
                            "$ref": "#/components/schemas/PrivateLightAgentMessage"
                          },
                          {
                            "$ref": "#/components/schemas/PrivateContentFragment"
                          }
                        ]
                      }
                    },
                    "hasMore": {
                      "type": "boolean"
                    },
                    "lastValue": {
                      "type": "integer",
                      "nullable": true
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
      },
      "PrivateLightAgentMessage": {
        "type": "object",
        "description": "A lighter agent message used in paginated message list responses.",
        "required": [
          "type",
          "sId",
          "version",
          "rank",
          "status",
          "parentMessageId",
          "configuration"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "agent_message"
            ]
          },
          "sId": {
            "type": "string"
          },
          "created": {
            "type": "integer"
          },
          "completedTs": {
            "type": "integer",
            "nullable": true
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
          "branchId": {
            "type": "string",
            "nullable": true,
            "description": "Legacy, always null. Branches were removed."
          },
          "parentMessageId": {
            "type": "string"
          },
          "parentAgentMessageId": {
            "type": "string",
            "nullable": true
          },
          "status": {
            "type": "string",
            "enum": [
              "created",
              "succeeded",
              "failed",
              "cancelled"
            ]
          },
          "content": {
            "type": "string",
            "nullable": true
          },
          "chainOfThought": {
            "type": "string",
            "nullable": true
          },
          "error": {
            "type": "object",
            "nullable": true,
            "properties": {
              "code": {
                "type": "string"
              },
              "message": {
                "type": "string"
              },
              "metadata": {
                "type": "object",
                "nullable": true
              }
            }
          },
          "configuration": {
            "type": "object",
            "description": "Minimal agent configuration info",
            "properties": {
              "sId": {
                "type": "string"
              },
              "name": {
                "type": "string"
              },
              "pictureUrl": {
                "type": "string"
              },
              "status": {
                "type": "string"
              },
              "canRead": {
                "type": "boolean"
              }
            }
          },
          "citations": {
            "type": "object",
            "additionalProperties": {
              "$ref": "#/components/schemas/PrivateCitation"
            }
          },
          "generatedFiles": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "fileId": {
                  "type": "string",
                  "nullable": true,
                  "description": "Counso file id for DB-backed files, or null for path-backed files."
                },
                "filePath": {
                  "type": "string",
                  "description": "Canonical scoped path for path-backed files."
                },
                "title": {
                  "type": "string"
                },
                "contentType": {
                  "type": "string"
                },
                "publicUrl": {
                  "type": "string"
                }
              }
            }
          },
          "richMentions": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PrivateRichMentionWithStatus"
            }
          },
          "completionDurationMs": {
            "type": "integer",
            "nullable": true
          },
          "costCredits": {
            "type": "integer",
            "nullable": true,
            "description": "Cost of producing this agent message, in credits (intelligence + tool credits). Null when no billable usage is attributed to the message."
          },
          "subAgentCostCredits": {
            "type": "number",
            "nullable": true,
            "description": "Aggregated credit cost of all sub-agents (run_agent / agent_handover) spawned recursively by this message. Computed only on single-message fetches. Null otherwise."
          },
          "resolvedModel": {
            "type": "object",
            "nullable": true,
            "description": "Model triplet used to generate the message. Null when the agent ran its configured model (legacy).",
            "properties": {
              "providerId": {
                "type": "string"
              },
              "modelId": {
                "type": "string"
              },
              "reasoningEffort": {
                "type": "string"
              }
            }
          },
          "modelResolutionMethod": {
            "type": "string",
            "nullable": true,
            "enum": [
              "agent",
              "user",
              "auto",
              "auto_fast",
              "auto_complex",
              "fair_use_downgrade"
            ],
            "description": "How resolvedModel was chosen - agent (configured model), user (per-message picker), auto/auto_fast/auto_complex (routed through a model stream), or fair_use_downgrade (premium allowance spent, ran the Standard stream instead). Null (legacy)."
          },
          "activitySteps": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "type": {
                  "type": "string",
                  "enum": [
                    "thinking",
                    "action"
                  ]
                },
                "content": {
                  "type": "string",
                  "description": "Chain of thought text (thinking steps only)"
                },
                "label": {
                  "type": "string",
                  "description": "Action display label (action steps only)"
                },
                "id": {
                  "type": "string"
                },
                "actionId": {
                  "type": "string",
                  "description": "Action string identifier (action steps only)"
                }
              }
            }
          },
          "reactions": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PrivateReaction"
            }
          }
        }
      },
      "PrivateCitation": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string"
          },
          "description": {
            "type": "string"
          },
          "href": {
            "type": "string"
          },
          "provider": {
            "type": "string"
          },
          "contentType": {
            "type": "string"
          }
        }
      },
      "PrivateReaction": {
        "type": "object",
        "description": "A reaction on a message.",
        "required": [
          "emoji",
          "users"
        ],
        "properties": {
          "emoji": {
            "type": "string"
          },
          "users": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "userId": {
                  "type": "string",
                  "nullable": true
                },
                "username": {
                  "type": "string"
                },
                "fullName": {
                  "type": "string",
                  "nullable": true
                }
              }
            }
          }
        }
      },
      "PrivateRichMentionWithStatus": {
        "type": "object",
        "description": "A rich mention with approval status, used in message responses.",
        "required": [
          "id",
          "type",
          "label",
          "pictureUrl",
          "description",
          "dismissed",
          "status"
        ],
        "properties": {
          "id": {
            "type": "string"
          },
          "type": {
            "type": "string",
            "enum": [
              "agent",
              "user"
            ]
          },
          "label": {
            "type": "string"
          },
          "pictureUrl": {
            "type": "string"
          },
          "description": {
            "type": "string"
          },
          "userFavorite": {
            "type": "boolean"
          },
          "dismissed": {
            "type": "boolean"
          },
          "status": {
            "type": "string",
            "enum": [
              "pending_conversation_access",
              "pending_project_membership",
              "approved",
              "rejected",
              "user_restricted_by_conversation_access",
              "agent_restricted_by_space_usage"
            ]
          }
        }
      },
      "PrivateUserMessage": {
        "type": "object",
        "description": "A user message in a conversation.",
        "required": [
          "type",
          "sId",
          "content",
          "version",
          "rank",
          "created"
        ],
        "properties": {
          "id": {
            "type": "integer"
          },
          "type": {
            "type": "string",
            "enum": [
              "user_message"
            ]
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
          "branchId": {
            "type": "string",
            "nullable": true,
            "description": "Legacy, always null. Branches were removed."
          },
          "user": {
            "type": "object",
            "nullable": true,
            "description": "The user who sent the message",
            "properties": {
              "sId": {
                "type": "string"
              },
              "username": {
                "type": "string"
              },
              "fullName": {
                "type": "string"
              },
              "image": {
                "type": "string",
                "nullable": true
              }
            }
          },
          "mentions": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PrivateMention"
            }
          },
          "richMentions": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PrivateRichMentionWithStatus"
            }
          },
          "content": {
            "type": "string"
          },
          "context": {
            "$ref": "#/components/schemas/PrivateUserMessageContext"
          },
          "reactions": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PrivateReaction"
            }
          }
        }
      },
      "PrivateMention": {
        "type": "object",
        "description": "A mention in a message (agent or user).",
        "properties": {
          "configurationId": {
            "type": "string",
            "description": "Agent configuration sId (for agent mentions)"
          },
          "type": {
            "type": "string",
            "enum": [
              "user"
            ],
            "description": "Present only for user mentions"
          },
          "userId": {
            "type": "string",
            "description": "User sId (for user mentions)"
          }
        }
      },
      "PrivateUserMessageContext": {
        "type": "object",
        "description": "Context metadata for a user message.",
        "required": [
          "username",
          "timezone",
          "origin"
        ],
        "properties": {
          "username": {
            "type": "string"
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
          },
          "timezone": {
            "type": "string"
          },
          "origin": {
            "type": "string",
            "enum": [
              "web",
              "project_kickoff",
              "extension",
              "agent_sidekick",
              "analytics_panel",
              "api",
              "cli",
              "cli_programmatic",
              "email",
              "excel",
              "gsheet",
              "make",
              "n8n",
              "powerpoint",
              "raycast",
              "slack",
              "slack_workflow",
              "teams",
              "transcript",
              "triggered_programmatic",
              "triggered",
              "wakeup",
              "zapier",
              "zendesk",
              "onboarding_conversation"
            ]
          },
          "selectedSpaceIds": {
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        }
      }
    }
  }
}
```
