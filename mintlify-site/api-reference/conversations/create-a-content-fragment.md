---
title: "Create a content fragment"
---
Adds a newly created content fragment to a conversation in workspace {wId}.

```http
POST /api/v1/w/{wId}/assistant/conversations/{cId}/content_fragments
```

Base URL: `https://app.counso.ai`

## Authentication

Send a workspace API key or a user OAuth access token in `Authorization: Bearer <token>`. The credential must belong to this Counso deployment and have access to the requested workspace and resources.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes | ID of the workspace |
| `cId` | path | string | Yes | ID of the conversation |

## Request body

`Content-Type: application/json`

| Field | Type | Required |
| --- | --- | --- |
| `title` | string | Yes |
| `content` | string | No |
| `contentType` | string | No |
| `url` | string | No |
| `fileId` | string | No |
| `path` | string | No |
| `processedPath` | string | No |
| `skipFileProcessing` | boolean | No |
| `nodeId` | string | No |
| `nodeDataSourceViewId` | string | No |
| `context` | object | No |

Field constraints and nested structures are defined in the specification below.

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | Content fragment created successfully. |
| 400 | Bad Request. Missing or invalid parameters. |
| 401 | Unauthorized. Invalid or missing authentication token. |
| 500 | Internal Server Error. |

## Specification

Download the complete [OpenAPI / Postman](/docs/developer-platform/counso-api-documentation/openapi-and-postman) files.

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
    "/api/v1/w/{wId}/assistant/conversations/{cId}/content_fragments": {
      "post": {
        "summary": "Create a content fragment",
        "description": "Adds a newly created content fragment to a conversation in workspace {wId}.",
        "tags": [
          "Conversations"
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
                "$ref": "#/components/schemas/ContentFragment"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Content fragment created successfully.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ContentFragment"
                }
              }
            }
          },
          "400": {
            "description": "Bad Request. Missing or invalid parameters."
          },
          "401": {
            "description": "Unauthorized. Invalid or missing authentication token."
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
      "ContentFragment": {
        "type": "object",
        "required": [
          "title"
        ],
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the content fragment",
            "example": "My content fragment"
          },
          "content": {
            "type": "string",
            "description": "The content of the content fragment (optional if `fileId` is set)",
            "example": "This is my content fragment extracted text"
          },
          "contentType": {
            "type": "string",
            "description": "The content type of the content fragment (optional if `fileId` is set)",
            "example": "text/plain"
          },
          "url": {
            "type": "string",
            "description": "The URL of the content fragment",
            "example": "https://example.com/content"
          },
          "fileId": {
            "type": "string",
            "description": "The id of the previously uploaded file (optional if `content` and `contentType` are set)",
            "example": "fil_123456"
          },
          "path": {
            "type": "string",
            "nullable": true,
            "description": "Path of this file inside the sandbox conversation mount.",
            "example": "conversation/report.csv"
          },
          "processedPath": {
            "type": "string",
            "nullable": true,
            "description": "Path of the plain-text sibling of this file inside the sandbox conversation mount (e.g. an audio transcript), when it has one.",
            "example": "conversation/voice.processed.txt"
          },
          "skipFileProcessing": {
            "type": "boolean",
            "description": "Whether upload-time file processing was skipped."
          },
          "nodeId": {
            "type": "string",
            "description": "The id of the content node (optional if `content` and `contentType` are set)",
            "example": "node_123456"
          },
          "nodeDataSourceViewId": {
            "type": "string",
            "description": "The id of the data source view (optional if `content` and `contentType` are set)",
            "example": "dsv_123456"
          },
          "context": {
            "$ref": "#/components/schemas/Context"
          }
        }
      },
      "Context": {
        "type": "object",
        "required": [
          "username",
          "timezone"
        ],
        "properties": {
          "username": {
            "type": "string",
            "description": "Username in the current context",
            "example": "johndoe123"
          },
          "timezone": {
            "type": "string",
            "description": "User's timezone",
            "example": "America/New_York"
          },
          "fullName": {
            "type": "string",
            "description": "User's full name in the current context",
            "example": "John Doe"
          },
          "email": {
            "type": "string",
            "description": "User's email in the current context",
            "example": "john.doe@example.com"
          },
          "profilePictureUrl": {
            "type": "string",
            "description": "URL of the user's profile picture",
            "example": "https://example.com/profiles/johndoe123.jpg"
          },
          "selectedSpaceIds": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "agenticMessageData": {
            "type": "object",
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "run_agent",
                  "agent_handover"
                ],
                "description": "Type of the agentic message"
              },
              "originMessageId": {
                "type": "string",
                "description": "ID of the origin message",
                "example": "2b8e4f6a0c"
              }
            }
          }
        }
      }
    }
  }
}
```
