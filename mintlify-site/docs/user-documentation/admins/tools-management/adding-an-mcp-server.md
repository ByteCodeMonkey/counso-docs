---
title: "Add a remote MCP server"
---
A remote MCP server exposes a provider's tools to Agents through the Model Context Protocol. Counso connects to the server as an MCP client. The provider manages the tools and their permissions.

## Add and share a server

1. Open **Spaces → Tools → Add Tools → Add MCP Server**.
2. Enter the server name and endpoint URL supplied by the provider or your integration owner. Check the server identity and transport details before saving.
3. Choose the authentication method the server supports: automatic OAuth, a bearer token, or static OAuth. The form may offer only a subset for a given server.
4. For OAuth, use the callback URL displayed in the Counso form when registering the client with the provider. Do not copy a callback from another environment. For bearer authentication, store the provider token as a protected credential; never include it in Agent instructions.
5. Save the server, complete authorization, review the available tools, and share it only with the Spaces that need them.
6. Add selected tools to an Agent and test a read against a known record before enabling write operations.

## Authentication choices

**Automatic OAuth** is the simplest option when the provider's server supports a standard discovery flow; the user authorizes the provider account in the browser. **Bearer token** is appropriate when the provider issues a scoped token. Calls made through that server use the third-party account represented by the token; the token does not become each Counso member’s personal identity. If users need separate provider identities, configure a server per person and share each only with that person’s Restricted Space. **Static OAuth** is for a provider app whose client ID, secret, authorization URL, token URL, scopes, or token endpoint method must be entered by an administrator.

## Custom server checks

For a server you operate, use a stable HTTPS endpoint, document the tool names and side effects, and restrict its provider credentials to the minimum required scope. Check the server's authentication and network requirements with the current form, then verify that the expected tools appear after authorization. A connection screen alone does not prove that a tool can access the intended provider object. Read the same object back after any test write.
