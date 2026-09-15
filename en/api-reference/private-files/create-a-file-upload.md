# Create a file upload

Private session interface. Creates the file record first, then returns a pre-signed upload URL for the content.

```http
POST /api/w/{wId}/files
```

Base URL: `https://app.counso.ai`

## Authentication

This operation requires a user OAuth access token in `Authorization: Bearer <token>`. A signed-in browser may use its Counso session cookie. A workspace API key does not supply user identity.

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
| `fileSize` | number | Yes |
| `useCase` | string | Yes |
| `useCaseMetadata` | object | No |

Field constraints and nested structures are defined in the specification below.

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | File record created with upload URL |
| 400 | Invalid request |
| 429 | Rate limit exceeded |

## Specification

Download the complete [OpenAPI / Postman](../../docs/developer-platform/counso-api-documentation/openapi-and-postman.md) files.

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
    "/api/w/{wId}/files": {
      "post": {
        "summary": "Create a file upload",
        "description": "Private session interface. Creates the file record first, then returns a pre-signed upload URL for the content.",
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
                  "contentType",
                  "fileName",
                  "fileSize",
                  "useCase"
                ],
                "properties": {
                  "contentType": {
                    "type": "string"
                  },
                  "fileName": {
                    "type": "string"
                  },
                  "fileSize": {
                    "type": "number"
                  },
                  "useCase": {
                    "type": "string",
                    "enum": [
                      "conversation",
                      "folders_document",
                      "avatar",
                      "upsert_document",
                      "upsert_table",
                      "project_context",
                      "skill_attachment",
                      "workspace_branding"
                    ]
                  },
                  "useCaseMetadata": {
                    "type": "object"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "File record created with upload URL",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "file": {
                      "$ref": "#/components/schemas/PrivateFileWithUploadUrl"
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Invalid request"
          },
          "429": {
            "description": "Rate limit exceeded"
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
      "PrivateFileWithUploadUrl": {
        "type": "object",
        "description": "File record with a pre-signed upload URL.",
        "required": [
          "sId",
          "id",
          "fileName",
          "fileSize",
          "contentType",
          "status",
          "useCase",
          "uploadUrl"
        ],
        "properties": {
          "sId": {
            "type": "string"
          },
          "id": {
            "type": "string"
          },
          "contentType": {
            "type": "string"
          },
          "fileName": {
            "type": "string"
          },
          "fileSize": {
            "type": "integer"
          },
          "version": {
            "type": "integer"
          },
          "status": {
            "type": "string",
            "enum": [
              "created",
              "failed",
              "ready"
            ]
          },
          "useCase": {
            "type": "string",
            "enum": [
              "conversation",
              "avatar",
              "tool_output",
              "upsert_document",
              "folders_document",
              "upsert_table",
              "project_context",
              "skill_attachment"
            ]
          },
          "uploadUrl": {
            "type": "string",
            "description": "Pre-signed URL for uploading the file content"
          },
          "downloadUrl": {
            "type": "string"
          },
          "publicUrl": {
            "type": "string"
          },
          "path": {
            "type": "string",
            "nullable": true,
            "description": "path when the file is ready on a mount (e.g. `project/report.pdf` or `conversation/chart.png`). Same shape as mount file listing entries."
          }
        }
      }
    }
  }
}
```
