> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Salesloft

## Overview

The Salesloft MCP lets agents read cadence actions and related context directly from your Salesloft workspace, supporting sales workflow automation. Agents can retrieve the actions and tasks needed for daily cadence execution without switching between tools.

## Connection Setup (Admin)

1. In Dust, go to **Spaces  Tools** and click **Add Tools**.
2. Select **Salesloft** from the list of available tools.
3. Paste your **Salesloft API Key** (Personal Access Token) into the field provided and save.

Once connected, the Salesloft toolset will be available to add to agents in the spaces you grant access to.

## Authentication

Salesloft authenticates requests using a Bearer token. Dust passes the API key as:

```
Authorization: Bearer <API_KEY>
```

See the official [Salesloft API Key Authentication documentation](https://developers.salesloft.com/docs/platform/api-basics/api-key-authentication/) for details on creating Personal Access Tokens.

## Required API Key Scopes

When creating or editing a Personal Access Token in Salesloft, apply the **least-privilege READ scopes** that match the endpoints used by the server. At minimum:

| Scope           | Required for                                                    |
| :-------------- | :-------------------------------------------------------------- |
| `cadences:read` | Listing and retrieving cadence actions via the Actions endpoint |
| `people:read`   | Reading people/prospect data associated with actions            |
| `team:read`     | Retrieving team and user context                                |
| `calls:read`    | Retrieving phone-type actions.                                  |

If your deployment also fetches cadence step details or other related entities, enable any additional required read scopes to match those endpoints.

**References:**

* [Scopes overview](https://developers.salesloft.com/docs/platform/api-basics/scopes/)
* [List Actions endpoint](https://developers.salesloft.com/docs/api/actions-index/)

## Available Tools

| Tool             | Description                                                                                  |
| :--------------- | :------------------------------------------------------------------------------------------- |
| **List Actions** | List cadence actions filtered by type, status, assignee, or date range.                      |
| **Get Action**   | Retrieve details of a specific action, including associated person and cadence step context. |
