---
title: "Upload file content"
---
Private session interface. Processes the supplied file bytes and saves the resulting content.

```http
POST /api/w/{wId}/files/{fileId}
```

Base URL: `https://app.counso.ai`

## Authentication

This operation requires a user OAuth access token in `Authorization: Bearer <token>`. A signed-in browser may use its Counso session cookie. A workspace API key does not supply user identity.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes | ID of the workspace |
| `fileId` | path | string | Yes | ID of the file |

## Request body

`Content-Type: multipart/form-data`

| Field | Type | Required |
| --- | --- | --- |
| `file` | string / binary | No |

Field constraints and nested structures are defined in the specification below.

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | File processed successfully |
| 400 | Invalid file content (e.g. a CSV with an unsupported encoding) |
| 403 | Permission denied |
| 404 | File not found |

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
    "/api/w/{wId}/files/{fileId}": {
      "post": {
        "summary": "Upload file content",
        "description": "Private session interface. Processes the supplied file bytes and saves the resulting content.",
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
          },
          {
            "in": "path",
            "name": "fileId",
            "required": true,
            "description": "ID of the file",
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
            "multipart/form-data": {
              "schema": {
                "type": "object",
                "properties": {
                  "file": {
                    "type": "string",
                    "format": "binary"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "File processed successfully",
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
            "description": "Invalid file content (e.g. a CSV with an unsupported encoding)"
          },
          "403": {
            "description": "Permission denied"
          },
          "404": {
            "description": "File not found"
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
