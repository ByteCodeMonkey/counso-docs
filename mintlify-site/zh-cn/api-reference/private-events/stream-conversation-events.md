---
title: "实时接收对话事件"
---
会话接口：通过 SSE 实时接收对话事件；SSE 流量会转发到 /api/sse/。

```http
GET /api/w/{wId}/assistant/conversations/{cId}/events
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
| 200 | SSE 事件流。每个事件以 data: {json}\n\n 形式发送，并通过 type 字段区分事件类型。 |
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
    "/api/w/{wId}/assistant/conversations/{cId}/events": {
      "get": {
        "summary": "Stream conversation events",
        "description": "Private session interface. Delivers conversation events in real time through SSE, routed via /api/sse/.",
        "tags": [
          "Private Events"
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
            "description": "SSE event stream. Each event is sent as `data: {json}\\n\\n`.\nEvents are discriminated by the `type` field.\n",
            "content": {
              "text/event-stream": {
                "schema": {
                  "$ref": "#/components/schemas/PrivateConversationEvent"
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
      "PrivateConversationEvent": {
        "type": "object",
        "description": "Server-Sent Event for conversation-level streaming. Discriminated on the `type` field.",
        "discriminator": {
          "propertyName": "type"
        },
        "oneOf": [
          {
            "$ref": "#/components/schemas/PrivateUserMessageNewEvent"
          },
          {
            "$ref": "#/components/schemas/PrivateAgentMessageNewEvent"
          },
          {
            "$ref": "#/components/schemas/PrivateAgentMessageConsumptionUpdatedEvent"
          },
          {
            "$ref": "#/components/schemas/PrivateAgentMessageDoneEvent"
          },
          {
            "$ref": "#/components/schemas/PrivateCompactionMessageNewEvent"
          },
          {
            "$ref": "#/components/schemas/PrivateCompactionMessageDoneEvent"
          },
          {
            "$ref": "#/components/schemas/PrivateConversationForkPreparedEvent"
          },
          {
            "$ref": "#/components/schemas/PrivateConversationTitleEvent"
          },
          {
            "$ref": "#/components/schemas/PrivateWakeUpUpdatedEvent"
          }
        ]
      },
      "PrivateAgentMessageConsumptionUpdatedEvent": {
        "type": "object",
        "required": [
          "type",
          "created",
          "conversationId",
          "messageId",
          "costCredits"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "agent_message_consumption_updated"
            ]
          },
          "created": {
            "type": "integer"
          },
          "conversationId": {
            "type": "string"
          },
          "messageId": {
            "type": "string"
          },
          "costCredits": {
            "type": "number",
            "nullable": true
          }
        }
      },
      "PrivateAgentMessageDoneEvent": {
        "type": "object",
        "required": [
          "type",
          "created",
          "conversationId",
          "configurationId",
          "messageId",
          "status"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "agent_message_done"
            ]
          },
          "created": {
            "type": "integer"
          },
          "conversationId": {
            "type": "string"
          },
          "configurationId": {
            "type": "string"
          },
          "messageId": {
            "type": "string"
          },
          "status": {
            "type": "string",
            "enum": [
              "success",
              "error"
            ]
          }
        }
      },
      "PrivateAgentMessageNewEvent": {
        "type": "object",
        "required": [
          "type",
          "created",
          "configurationId",
          "messageId",
          "message"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "agent_message_new"
            ]
          },
          "created": {
            "type": "integer"
          },
          "configurationId": {
            "type": "string"
          },
          "messageId": {
            "type": "string"
          },
          "message": {
            "$ref": "#/components/schemas/PrivateAgentMessage"
          }
        }
      },
      "PrivateAgentMessage": {
        "type": "object",
        "description": "An agent message in a conversation.",
        "required": [
          "type",
          "sId",
          "version",
          "rank",
          "status",
          "parentMessageId"
        ],
        "properties": {
          "id": {
            "type": "integer"
          },
          "agentMessageId": {
            "type": "integer"
          },
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
            "nullable": true,
            "description": "If handover, the agent message that summoned this agent"
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
            "$ref": "#/components/schemas/PrivateLightAgentConfiguration"
          },
          "actions": {
            "type": "array",
            "items": {
              "type": "object"
            },
            "description": "MCP actions executed by the agent"
          },
          "contents": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "step": {
                  "type": "integer"
                },
                "content": {
                  "type": "object"
                }
              }
            }
          },
          "skipToolsValidation": {
            "type": "boolean"
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
          "reactions": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PrivateReaction"
            }
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
          }
        }
      },
      "PrivateCompactionMessageDoneEvent": {
        "type": "object",
        "required": [
          "type",
          "created",
          "messageId",
          "message"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "compaction_message_done"
            ]
          },
          "created": {
            "type": "integer"
          },
          "messageId": {
            "type": "string"
          },
          "message": {
            "$ref": "#/components/schemas/PrivateCompactionMessage"
          }
        }
      },
      "PrivateCompactionMessage": {
        "type": "object",
        "description": "A compaction message summarizing earlier conversation content.",
        "required": [
          "type",
          "sId",
          "status",
          "version",
          "rank",
          "created"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "compaction_message"
            ]
          },
          "id": {
            "type": "integer"
          },
          "compactionMessageId": {
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
          "branchId": {
            "type": "string",
            "nullable": true,
            "description": "Legacy, always null. Branches were removed."
          },
          "sourceConversationId": {
            "type": "string",
            "nullable": true
          },
          "status": {
            "type": "string",
            "enum": [
              "created",
              "succeeded",
              "failed"
            ]
          },
          "content": {
            "type": "string",
            "nullable": true,
            "description": "Compacted summary. Null while status is \"created\"."
          }
        }
      },
      "PrivateCompactionMessageNewEvent": {
        "type": "object",
        "required": [
          "type",
          "created",
          "messageId",
          "message"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "compaction_message_new"
            ]
          },
          "created": {
            "type": "integer"
          },
          "messageId": {
            "type": "string"
          },
          "message": {
            "$ref": "#/components/schemas/PrivateCompactionMessage"
          }
        }
      },
      "PrivateConversationForkPreparedEvent": {
        "type": "object",
        "required": [
          "type",
          "created"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "conversation_fork_prepared"
            ]
          },
          "created": {
            "type": "integer"
          }
        }
      },
      "PrivateConversationTitleEvent": {
        "type": "object",
        "required": [
          "type",
          "created",
          "title"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "conversation_title"
            ]
          },
          "created": {
            "type": "integer"
          },
          "title": {
            "type": "string"
          }
        }
      },
      "PrivateLightAgentConfiguration": {
        "type": "object",
        "description": "Agent configuration as returned by the private list endpoint.",
        "required": [
          "id",
          "sId",
          "version",
          "name",
          "description",
          "pictureUrl",
          "status",
          "scope",
          "model",
          "maxStepsPerRun",
          "tags"
        ],
        "properties": {
          "id": {
            "type": "integer"
          },
          "sId": {
            "type": "string"
          },
          "version": {
            "type": "integer"
          },
          "versionCreatedAt": {
            "type": "string",
            "nullable": true
          },
          "versionAuthorId": {
            "type": "integer",
            "nullable": true
          },
          "name": {
            "type": "string"
          },
          "description": {
            "type": "string"
          },
          "instructions": {
            "type": "string",
            "nullable": true
          },
          "pictureUrl": {
            "type": "string"
          },
          "status": {
            "type": "string",
            "description": "Agent status",
            "enum": [
              "active",
              "archived",
              "draft",
              "pending",
              "disabled_by_admin",
              "disabled_missing_datasource",
              "disabled_free_workspace"
            ]
          },
          "scope": {
            "type": "string",
            "enum": [
              "global",
              "visible",
              "hidden"
            ]
          },
          "userFavorite": {
            "type": "boolean"
          },
          "model": {
            "type": "object",
            "properties": {
              "providerId": {
                "type": "string"
              },
              "modelId": {
                "type": "string"
              },
              "temperature": {
                "type": "number"
              },
              "reasoningEffort": {
                "type": "string",
                "enum": [
                  "none",
                  "light",
                  "medium",
                  "high"
                ]
              }
            }
          },
          "maxStepsPerRun": {
            "type": "integer"
          },
          "tags": {
            "type": "array",
            "items": {
              "type": "object",
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
          "templateId": {
            "type": "string",
            "nullable": true
          },
          "requestedGroupIds": {
            "type": "array",
            "items": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          "requestedSpaceIds": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "canRead": {
            "type": "boolean"
          },
          "canEdit": {
            "type": "boolean"
          },
          "lastAuthors": {
            "type": "array",
            "description": "Optional, returned when withAuthors query param is set",
            "items": {
              "type": "string"
            }
          },
          "editors": {
            "type": "array",
            "description": "Optional, returned when withEditors query param is set",
            "items": {
              "type": "object",
              "properties": {
                "sId": {
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
            }
          },
          "usage": {
            "type": "object",
            "description": "Optional, returned when withUsage query param is set",
            "properties": {
              "messageCount": {
                "type": "integer"
              },
              "conversationCount": {
                "type": "integer"
              },
              "userCount": {
                "type": "integer"
              },
              "timePeriodSec": {
                "type": "integer"
              }
            }
          },
          "feedbacks": {
            "type": "object",
            "description": "Optional, returned when withFeedbacks query param is set",
            "properties": {
              "up": {
                "type": "integer"
              },
              "down": {
                "type": "integer"
              }
            }
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
      "PrivateUserMessageNewEvent": {
        "type": "object",
        "required": [
          "type",
          "created",
          "messageId",
          "message"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "user_message_new"
            ]
          },
          "created": {
            "type": "integer"
          },
          "messageId": {
            "type": "string"
          },
          "message": {
            "$ref": "#/components/schemas/PrivateUserMessage"
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
      },
      "PrivateWakeUpUpdatedEvent": {
        "type": "object",
        "required": [
          "type",
          "created",
          "conversationId",
          "wakeUpId",
          "userId"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "wake_up_updated"
            ]
          },
          "created": {
            "type": "integer"
          },
          "conversationId": {
            "type": "string"
          },
          "wakeUpId": {
            "type": "string"
          },
          "userId": {
            "type": "string",
            "description": "sId of the user who owns the wake-up."
          }
        }
      }
    }
  }
}
```
