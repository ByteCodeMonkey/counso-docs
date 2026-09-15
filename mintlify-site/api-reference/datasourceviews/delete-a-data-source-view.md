---
title: "Delete a data source view"
---
Removes the selected data source view from its Space.

```http
DELETE /api/v1/w/{wId}/spaces/{spaceId}/data_source_views/{dsvId}
```

Base URL: `https://app.counso.ai`

## Authentication

Send a workspace API key or a user OAuth access token in `Authorization: Bearer <token>`. The credential must belong to this Counso deployment and have access to the requested workspace and resources.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes |  |
| `spaceId` | path | string | Yes |  |
| `dsvId` | path | string | Yes |  |

## Responses

| HTTP status | Description |
| --- | --- |
| 204 | Data source view successfully deleted |
| 401 | Unauthorized - The data source view is in use and cannot be deleted |
| 403 | Forbidden - Only admins or builders can delete data source views |
| 404 | Data source view not found |

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
    "/api/v1/w/{wId}/spaces/{spaceId}/data_source_views/{dsvId}": {
      "delete": {
        "tags": [
          "DatasourceViews"
        ],
        "security": [
          {
            "WorkspaceApiKey": []
          },
          {
            "UserAccessToken": []
          }
        ],
        "summary": "Delete a data source view",
        "parameters": [
          {
            "name": "wId",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "spaceId",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "dsvId",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "204": {
            "description": "Data source view successfully deleted"
          },
          "401": {
            "description": "Unauthorized - The data source view is in use and cannot be deleted"
          },
          "403": {
            "description": "Forbidden - Only admins or builders can delete data source views"
          },
          "404": {
            "description": "Data source view not found"
          }
        },
        "x-counso-auth": "workspace",
        "description": "Removes the selected data source view from its Space."
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
