---
title: "Create a file upload URL"
---
Allocates a workspace file record and supplies the URL where its contents should be uploaded.

```http
POST /api/v1/w/{wId}/files
```

Base URL: `https://app.counso.ai`

## Authentication

Send a workspace API key or a user OAuth access token in `Authorization: Bearer <token>`. The credential must belong to this Counso deployment and have access to the requested workspace and resources.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes | ID of the workspace |

## Request body

`Content-Type: application/json`

| Field | Type | Required |
| --- | --- | --- |
| `contentType` | string | Yes |
| `fileName` | string | Yes |
| `fileSize` | integer | Yes |
| `useCase` | string | Yes |
| `useCaseMetadata` | string | Yes |

Field constraints and nested structures are defined in the specification below.

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | File upload URL created successfully |
| 400 | Invalid request or unsupported file type |
| 401 | Unauthorized |
| 429 | Rate limit exceeded |

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
