---
title: "Delete a row"
---
Removes row {rId} from table {tId} in data source {dsId}, within workspace {wId}.

```http
DELETE /api/v1/w/{wId}/spaces/{spaceId}/data_sources/{dsId}/tables/{tId}/rows/{rId}
```

Base URL: `https://app.counso.ai`

## Authentication

Send a workspace API key or a user OAuth access token in `Authorization: Bearer <token>`. The credential must belong to this Counso deployment and have access to the requested workspace and resources.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes | Unique string identifier for the workspace |
| `spaceId` | path | string | Yes | ID of the space |
| `dsId` | path | string | Yes | ID of the data source |
| `tId` | path | string | Yes | ID of the table |
| `rId` | path | string | Yes | ID of the row |

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | The row was deleted |
| 404 | The row was not found |
| 429 | Too many pending table updates are queued for this table. Retry later. |

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
    "/api/v1/w/{wId}/spaces/{spaceId}/data_sources/{dsId}/tables/{tId}/rows/{rId}": {
      "delete": {
        "summary": "Delete a row",
        "description": "Removes row {rId} from table {tId} in data source {dsId}, within workspace {wId}.",
        "tags": [
          "Datasources"
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
          },
          {
            "in": "path",
            "name": "spaceId",
            "required": true,
            "description": "ID of the space",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "path",
            "name": "dsId",
            "required": true,
            "description": "ID of the data source",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "path",
            "name": "tId",
            "required": true,
            "description": "ID of the table",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "path",
            "name": "rId",
            "required": true,
            "description": "ID of the row",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "The row was deleted"
          },
          "404": {
            "description": "The row was not found"
          },
          "429": {
            "description": "Too many pending table updates are queued for this table. Retry later."
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
    }
  }
}
```
