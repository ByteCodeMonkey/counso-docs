> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Power BI

**Requirements**: Microsoft Entra admin access, a Power BI account (free tier works), and the MCP feature enabled in the Power BI admin portal.

***

### 1. Register an app in Microsoft Entra

Go to [entra.microsoft.com](https://entra.microsoft.com)  **Identity  Applications  App registrations  New registration**.

| Tool                      | Description                                      |
| ------------------------- | ------------------------------------------------ |
| `Name`                    | `Dust Power BI MCP` (or any name)                |
| `Supported account types` | *Accounts in this organizational directory only* |
| `Redirect URI`            | leave blank                                      |

Click **Register**, then note down:

* **Application (client) ID**
* **Directory (tenant) ID**

***

### 2. Configure authentication

In your app registration, go to **Authentication  Add Redirect URI  Web**.

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

Under **settings**, set **Allow public client flows** to **Enabled**. Click **Save**.

***

### 3. Create a client secret

Go to **Certificates & secrets  Client secrets  New client secret**. Add a description and expiration, then click **Add**.

**Copy the "Value" column immediately** (it won't be visible again).

***

### 4. Add API permissions

Go to **API permissions  Add a permission  APIs my organization uses**, search for **Power BI Service**, select **Delegated permissions** and check:

* `Dataset.Read.All`
* `Report.Read.All`
* `Dashboard.Read.All`
* `Workspace.Read.All`

Click **Add permissions**, then **Grant admin consent**.

***

### 5. Enable the MCP feature in Power BI

Go to [app.fabric.microsoft.com](https://app.fabric.microsoft.com)  **Settings   Admin portal  Tenant settings  Integration settings**, and enable:

* **"Users can use the Power BI Model Context Protocol server endpoint (preview)"**

***

### 6. Connect in Dust

In Dust, go to a **Space  Dev tools  MCP Servers  Add a remote MCP server**.

**Server URL**:

```
https://api.fabric.microsoft.com/v1/mcp/powerbi
```

**Authentication**: OAuth, then fill in:

| Field             | Value                                                                 |
| ----------------- | --------------------------------------------------------------------- |
| Client ID         | Your *Application (client) ID* from step 1                            |
| Client Secret     | The secret *Value* from step 3                                        |
| Token URL         | `https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token`     |
| Authorization URL | `https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/authorize` |
| Scope             | `https://analysis.windows.net/powerbi/api/.default offline_access`    |

Replace `{TENANT_ID}` with your Directory (tenant) ID.

**Important**: the scope must use `analysis.windows.net`, not `api.fabric.microsoft.com`.

The `offline_access` scope allows Dust to automatically refresh the authentication token in the background, so users don't have to re-authenticate every time the token expires (typically after one hour).

Save, authenticate with your Microsoft account, and the tools will appear.

***

### Troubleshooting

| Error                                        | Fix                                                                                               |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| **AADSTS700016**: app not found in directory | Wrong Client ID. Use "Application (client) ID", not "Secret ID" or "Object ID".                   |
| **"The feature is not available"**           | Enable the MCP feature in the Power BI admin portal (step 5).                                     |
| **"Could not get or open connection"**       | Enable XMLA endpoints in admin portal  Tenant settings  Integration settings.                     |
| **"Personal authentication required"**       | Click the authentication link in the conversation to sign in. You might need to refresh the page. |
