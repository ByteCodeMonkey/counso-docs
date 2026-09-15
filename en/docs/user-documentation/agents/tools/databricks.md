# Databricks

Databricks offers separate MCP tools for **Databricks SQL** and **Databricks Genie**. SQL can explore permitted Unity Catalog data and query a SQL warehouse; Genie works with the Genie resources and underlying data permitted to the user. Unity Catalog permissions are enforced on requests.

## Create the Databricks app connection

Use the workspace URL where notebooks run—not the Account Console URL. In Databricks Account Console, open **Settings → App Connections**, create an OAuth app connection, and add the callback URL displayed by Counso's setup form. Keep client-secret generation enabled, then copy the client ID and secret securely. Add `sql` and `offline_access` for SQL, `genie` and `offline_access` for Genie, or both sets when using both tools.

Before connecting, confirm that the users can access the required Genie resources or, for SQL, the intended Unity Catalog catalogs, schemas, tables, and SQL warehouse. If the workspace uses IP access lists, allow the outbound access required for the service.

## Connect the tool

In **Spaces → Tools → Add Tools**, choose Databricks SQL or Databricks Genie. Enter the workspace URL and app connection credentials, then authorize. The provider endpoint is derived from the workspace hostname: `/api/2.0/mcp/sql` for SQL or `/api/2.0/mcp/genie` for Genie. Add the tool to an Agent and begin with a bounded read from one known resource.
