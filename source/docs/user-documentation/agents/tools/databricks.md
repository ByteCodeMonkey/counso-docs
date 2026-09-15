> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Databricks

## **Setup in Databricks**

### 1. Find your Databricks workspace URL

The workspace hostname is the domain you see in your browser when you are logged into your Databricks workspace, for example `dbc-a1b2c3d4-e5f6.cloud.databricks.com`.

You can also find it from the Account Console:

1. Go to the [Databricks Account Console](https://accounts.cloud.databricks.com/) (on Azure, use the Azure portal).
2. In the left sidebar, click **Workspaces**.
3. Click the workspace you want to connect.
4. On the **Configuration** tab, the workspace URL is displayed at the top of the page, next to the workspace status. It also appears under **Networking > Connectivity > Per-workspace URL**.
5. Copy the URL without the trailing slash, for example `https://dbc-a1b2c3d4-e5f6.cloud.databricks.com`.

<Info>
  Use the **workspace** URL (where you open notebooks), not the Account Console URL (`accounts.cloud.databricks.com`). If your organization has several workspaces, pick the one containing the data you want to expose to agents.
</Info>

### **2. Create an App Connection**

1. Open the [**Databricks Account Console**](https://accounts.cloud.databricks.com/ "https://accounts.cloud.databricks.com/").

2. Go to **Settings > App Connections**.

3. Click **Add connection**.

4. Give the connection a descriptive name, such as `Dust MCP`.

5. Add the Dust OAuth redirect URL: `https://dust.tt/oauth/mcp_static/finalize`

6. Keep **Generate a client secret** enabled. Dust uses the client ID and client secret when connecting to Databricks.

7. Add the scopes required by the tools you want to use:
   * **Databricks SQL**: `sql` and `offline_access`
   * **Databricks Genie**: `genie` and `offline_access`
   * If you use both tools, add both `sql` and `genie`, together with `offline_access`.

8. Create the connection and copy its **client ID** and **client secret**. You will enter them in Dust.

Databricks documents OAuth app connections under **Settings > App Connections**. OAuth applications with a client secret are confidential clients, which is the configuration required by the Dust presets.

### **3. Verify Databricks permissions**

Make sure the users authenticating through Dust can access the relevant Databricks resources:

* For **Databricks Genie**, the relevant Genie resources and underlying data.
* For **Databricks SQL**, the required Unity Catalog catalogs, schemas, tables, and SQL warehouses.

Unity Catalog permissions are enforced on every request.

## **Setup in Dust**

1. In your Dust workspace, go to **Spaces > Tools > Add Tools**.
2. Select **Databricks SQL** or **Databricks Genie**.
3. Enter your Databricks workspace URL, for example: `https://your-workspace.cloud.databricks.com`
4. Enter the **client ID** and **client secret** from the Databricks App Connection.
5. Click **Connect**.

Dust derives the OAuth authorization endpoint, token endpoint, and MCP server URL from the workspace URL:

* SQL: `https://<workspace-hostname>/api/2.0/mcp/sql`
* Genie: `https://<workspace-hostname>/api/2.0/mcp/genie`

The OAuth endpoints are derived automatically, so they do not need to be entered manually.

If your Databricks workspace uses IP access lists, also make sure that Dust’s outbound IP addresses are allowed to connect to the workspace.
