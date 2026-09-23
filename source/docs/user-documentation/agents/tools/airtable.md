> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Airtable

## Overview

Airtable's MCP server lets your Dust assistants read and write records, explore base schemas, and interact with your Airtable data directly from conversations.

Two authentication methods are available: **Personal Access Token (PAT)** for a quick setup, and **OAuth** for a per-user authentication (recommended for teams).

***

## Method 1: Personal Access Token (PAT)

**Simpler to set up**, but all users in the workspace share the same token and the same Airtable permissions. If you need each user to authenticate with their own Airtable account, use the OAuth method below.

### 1. Create a Personal Access Token

Go to [airtable.com/create/tokens](https://airtable.com/create/tokens) and click **"Create new token"**.

* **Name**: `Dust` (or any name)
* We recommend to add the following **scopes**:
  * `data.records:read`
  * `data.records:write`
  * `data.recordComments:read`
  * `data.recordComments:write`
  * `schema.bases:read`
  * `schema.bases:write`
  * `user.email:read`
* Select the **bases** you want Dust to access
* Click **"Create token"** and **copy it immediately** (it won't be shown again)

### 2. Connect in Dust

In Dust, go to **Spaces Tools Add tools Add MCP server**.

* **Server URL**: `https://mcp.airtable.com/mcp`
* **Authentication**: Shared secret

Paste your Personal Access Token as the shared secret and save.

***

## Method 2: OAuth (Recommended)

With OAuth, each user authenticates with their own Airtable account. Airtable permissions are enforced per user.

<Info>
  [Official Airtable OAuth
  documentation](https://airtable.com/developers/web/guides/oauth-integrations)
</Info>

### 1. Create an OAuth integration in Airtable

Go to [airtable.com/create/oauth](https://airtable.com/create/oauth) and click **"Register new OAuth integration"**.

Under **"About your integration"**, fill in:

| Field            | Value                                                                                                            |
| ---------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Name**         | `Dust`                                                                                                           |
| **Homepage URL** | `https://dust.tt`                                                                                                |
| **Logo**         | Download from [dust.tt/home/brand-resources](https://dust.tt/home/brand-resources) (PNG, 200x200 to 1000x1000px) |

### 2. Add redirect URIs

Add the two redirect URLs for your Dust region:

**US workspaces:**

```
https://dust.tt/oauth/mcp_static/finalize
https://app.dust.tt/oauth/mcp_static/finalize
```

**EU workspaces:**

```
https://eu.dust.tt/oauth/mcp_static/finalize
https://app.dust.tt/oauth/mcp_static/finalize
```

### 3. Generate a client secret

On the same page, click **"Generate client secret"** and **copy it immediately** (it will not be shown again).

Note down your **Client ID** as well (visible on the page).

### 4. Add permission scopes

Under **"Permission scopes"**, we recommend to add the following scopes:

| Scope                       | Description                              |
| --------------------------- | ---------------------------------------- |
| `data.records:read`         | View record data                         |
| `data.records:write`        | Create, edit, and delete records         |
| `data.recordComments:read`  | View record comments                     |
| `data.recordComments:write` | Create, edit, and delete record comments |
| `schema.bases:read`         | View base structure (tables, fields)     |
| `schema.bases:write`        | Edit base structure                      |
| `user.email:read`           | View the authorizing user's email        |

### 5. Fill in support information

Airtable requires these fields before allowing OAuth authorization flows:

| Field                    | Value                                                                                        |
| ------------------------ | -------------------------------------------------------------------------------------------- |
| **Support email**        | `support@dust.tt`                                                                            |
| **Privacy policy URL**   | `https://dust-tt.notion.site/Terms-Conditions-2bdcf30156db4a40bcb20d27b0b1bd4e`              |
| **Terms of service URL** | `https://dust-tt.notion.site/Personal-Use-Terms-of-Service-06b764049abc4d4a9d3434245b56c765` |

Click **"Save changes"**.

### 6. Connect in Dust

In Dust, go to **Spaces Tools Add tools Add MCP server Static OAuth**.

**Server URL**:

```
https://mcp.airtable.com/mcp
```

**Authentication**: OAuth, then fill in:

| Field                          | Value                                                                                                                                          |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Client ID**                  | Your Client ID from step 3                                                                                                                     |
| **Client Secret**              | The secret from step 3                                                                                                                         |
| **Authorization URL**          | `https://airtable.com/oauth2/v1/authorize`                                                                                                     |
| **Token URL**                  | `https://airtable.com/oauth2/v1/token`                                                                                                         |
| **Scope**                      | `data.records:read data.records:write data.recordComments:read data.recordComments:write schema.bases:read schema.bases:write user.email:read` |
| **Token endpoint auth method** | `Basic Auth`                                                                                                                                   |

Save, authenticate with your Airtable account, and select the bases you want to grant access to.
