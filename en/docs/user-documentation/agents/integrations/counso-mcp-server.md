# Connect an MCP client to Counso

Connect a compatible external application to Counso to work with Agents, conversations, Knowledge, and Pod material through your Counso account. A deployment administrator must enable the MCP service and its OAuth connection before users connect a client.

To give a Counso Agent access to a third-party service instead, see [Add a remote MCP server](../../admins/tools-management/adding-an-mcp-server.md).

## Connect your application

1. Get the MCP server address for your deployment from the workspace administrator. Use the supplied service address rather than a documentation page or a guessed domain.
2. In the application's MCP settings, add a remote server with that address. The client must support remote MCP with OAuth.
3. Follow the authorization prompt, sign in to Counso, and select the workspace.
4. Start with a simple request, such as identifying the workspace or listing the Agents you can access.

The connection uses OAuth. A workspace API key is not a substitute for this sign-in flow.

## Use the connected workspace

The client discovers the tools exposed by the server. Depending on the service configuration, these can include Agent requests, conversations, Knowledge searches, and Pod files or tasks. Use the actual tool list to determine which operations are available; it does not automatically contain every third-party Tool configured in Counso.

Authorization uses your Counso identity and access scope. Review any requested action before changing or sharing workspace content from an external application.

## Troubleshoot sign-in

Check the server address, client OAuth support, and account selection. If a callback is rejected or access is disabled, ask the administrator to check the MCP service settings and permitted redirect addresses. An application failing before the sign-in page may need its MCP or OAuth support updated.
