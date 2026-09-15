---
title: "Create a content fragment"
---
Private session interface. Inserts a content fragment into an existing conversation.

```http
POST /api/w/{wId}/assistant/conversations/{cId}/content_fragment
```

Base URL: `https://app.counso.ai`

## Authentication

This operation requires a user OAuth access token in `Authorization: Bearer <token>`. A signed-in browser may use its Counso session cookie. A workspace API key does not supply user identity.

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
| `content` | string | Yes |
| `contentType` | string | Yes |
| `url` | string | No |
| `context` | object | Yes |
| `fileId` | string | No |

Field constraints and nested structures are defined in the specification below.

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | Successfully created content fragment |
| 401 | Unauthorized |

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
    "/api/w/{wId}/assistant/conversations/{cId}/content_fragment": {
      "post": {
        "summary": "Create a content fragment",
        "description": "Private session interface. Inserts a content fragment into an existing conversation.",
        "tags": [
          "Private Conversations"
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
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "title",
                  "content",
                  "contentType",
                  "context"
                ],
                "properties": {
                  "title": {
                    "type": "string"
                  },
                  "content": {
                    "type": "string"
                  },
                  "contentType": {
                    "type": "string",
                    "description": "MIME type of the content"
                  },
                  "url": {
                    "type": "string",
                    "nullable": true
                  },
                  "context": {
                    "type": "object",
                    "properties": {
                      "profilePictureUrl": {
                        "type": "string",
                        "nullable": true
                      }
                    }
                  },
                  "fileId": {
                    "type": "string",
                    "nullable": true
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Successfully created content fragment",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "contentFragment": {
                      "$ref": "#/components/schemas/PrivateContentFragment"
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
      }
    }
  }
}
```
