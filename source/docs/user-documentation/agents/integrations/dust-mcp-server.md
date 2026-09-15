> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Dust MCP Server

Dust can expose your workspace as a remote MCP Server, so compatible MCP clients can use Dust where you already work. This lets tools such as IDEs and AI assistants call Dust to search workspace knowledge, work with conversations, and access files or Pods through the Model Context Protocol.

Use this page when you want to connect an MCP client to Dust. If you want to add an external MCP Server as a tool inside Dust, see [Adding an MCP Server](/docs/user-documentation/admins/tools-management/adding-an-mcp-server) instead.

## Server URL

Choose the URL that matches your Dust region:

| Region      | MCP Server URL           |
| ----------- | ------------------------ |
| Global / US | `https://dust.tt/mcp`    |
| EU          | `https://eu.dust.tt/mcp` |

Add this URL in any compatible MCP client that supports remote MCP servers with OAuth authentication. Client-specific setup steps vary by product and are not covered in this page.

## What it enables

Once connected, the Dust MCP Server lets your MCP client work with Dust on behalf of the authenticated user. The first version exposes tools to:

* identify the current Dust user and workspace;
* list available agents;
* list conversations, create conversations, create messages, and retrieve conversation messages;
* retrieve Pod information and Pod tasks;
* list, read, create, search, and resolve files scoped to conversations or Pods;
* search across workspace Spaces.

The exact tools exposed by the server may evolve over time. The Dust MCP Server does not proxy every third-party tool configured in your Dust workspace.

## Authentication and permissions

The Dust MCP Server uses OAuth. In most compatible clients, authentication starts automatically after you add the MCP Server URL. You will be asked to sign in to Dust and select the workspace to connect.

The connected client acts as the authenticated Dust user. It can only access the Dust data, Spaces, conversations, Pods, and files that this user can access in Dust. Tokens issued for the MCP Server are scoped to MCP usage and are not Dust API keys.

**Note:** API keys are not used to connect to the Dust MCP Server. Use the OAuth flow initiated by your MCP client.

### OAuth client registration

Dust supports the OAuth client registration mechanisms used by MCP clients:

* **Dynamic Client Registration (DCR)**, for clients that register dynamically with the authorization server during setup.
* **Client ID Metadata Documents (CIMD)**, for clients that identify themselves through a client metadata document.

### Required `resource` parameter

MCP clients must include the OAuth `resource` parameter in both authorization and token requests. This parameter identifies the MCP Server the token is intended for and allows Dust to issue tokens scoped to the Dust MCP Server.

Clients that omit the `resource` parameter are not supported. If your client fails during OAuth, check whether it follows the MCP authorization specification for resource parameters: [Model Context Protocol authorization specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization#resource-parameter-implementation).

## Admin controls

Workspace admins can disable Dust MCP Server access for their workspace. Admins can also control which redirect URIs are allowed during client authentication.

If a user cannot connect, check that the Dust MCP Server is enabled for the workspace and that the MCP client's redirect URI is allowed.

## Compatibility

The Dust MCP Server is designed for clients that support remote MCP servers and the latest MCP authorization flow, including OAuth resource parameters.

Some MCP clients may not work if they do not implement the expected OAuth metadata discovery or required authorization parameters. If authentication fails before the Dust login screen, update the client and confirm that it supports remote MCP servers with OAuth, including the `resource` parameter.

## Troubleshooting

If the connection does not work:

1. Confirm that you are using the correct region URL, either `https://dust.tt/mcp` or `https://eu.dust.tt/mcp`.
2. Confirm that your MCP client supports remote MCP servers with OAuth authentication.
3. Confirm that your MCP client includes the OAuth `resource` parameter in authorization and token requests.
4. Ask a Dust workspace admin to confirm that Dust MCP Server access is enabled for the workspace.
5. If the client shows a redirect URI or OAuth error, ask an admin to verify that the redirect URI is allowed.

## Related pages

* [Adding an MCP Server](/docs/user-documentation/admins/tools-management/adding-an-mcp-server), for adding external MCP servers as tools inside Dust.
* [Client-side MCP Server](/docs/user-documentation/developers/client-side-mcp-server), for developers exposing local client-side tools to Dust conversations.
* [Access Controls and Permissions](/docs/user-documentation/admins/admin-governance/access-controls-and-permissions), for how Dust workspace roles and Spaces control access.
* [Model Context Protocol authorization specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization), for the OAuth requirements implemented by MCP clients and servers.
