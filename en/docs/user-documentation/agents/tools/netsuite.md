# NetSuite

The NetSuite remote MCP uses Oracle's **MCP Standard Tools SuiteApp** and OAuth 2.0. It requires a NetSuite administrator who can enable SuiteCloud features, install the SuiteApp, create a dedicated role, and register an integration. The Administrator role cannot be used with this MCP server.

## Prepare the NetSuite account

1. In **Setup → Company → Enable Features → SuiteCloud**, enable **Server SuiteScript**, **REST Web Services**, **Token-Based Authentication**, and **OAuth 2.0**.
2. In **Customization → SuiteBundler → Search & Install Bundles**, find and install **MCP Standard Tools**.
3. In **Setup → Users/Roles → Manage Roles → New**, create a dedicated role and grant **MCP Server Connection**, **Log in using OAuth 2.0 Access Tokens**, **REST Web Services**, and **Perform Search**. Assign it only to the relevant users.
4. In **Setup → Integration → Manage Integrations → New**, enable the integration and its **Authorization Code Grant**, **Public Client**, and **Dynamic Client Registration** settings. Set the application callback URL to the value shown in Counso's setup form, and select the **NetSuite AI Connector Service** scope. Save and copy the Consumer Key/Client ID and secret securely. When entering the key, omit any display prefix such as `ID` if the setup form expects only the key value.

## Connect the MCP server

In **Spaces → Tools → Add Tools → Add MCP Server**, choose **Static OAuth**. Set the server URL to the NetSuite MCP Standard Tools SuiteApp endpoint for your account:

`https://<accountid>.suitetalk.api.netsuite.com/services/mcp/v1/suiteapp/com.netsuite.mcpstandardtools`

Use your NetSuite account ID in place of `<accountid>`. The OAuth authorization endpoint is `https://<accountid>.app.netsuite.com/app/login/oauth2/authorize`; the token endpoint is `https://<accountid>.suitetalk.api.netsuite.com/services/rest/auth/oauth2/v1/token`; the scope is `mcp`. Enter the key and secret from the integration record, save, and authorize using the custom MCP role. Add the server's available tools to the approved Agent/Space.

If login fails, ensure you selected the custom role rather than Administrator. If **MCP Server Connection** is unavailable, verify the SuiteApp installation. If the key is rejected, remove a prefixed `ID` when the form expects the underlying Consumer Key. If redirect validation fails, compare the provider entry with the current Counso form callback.
