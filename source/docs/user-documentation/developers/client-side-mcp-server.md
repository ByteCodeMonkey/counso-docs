> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Client Side MCP Server (Preview)

Client-side MCP server enables you to dynamically expose tools to Dust conversations through your client applications that interact with Dust's Conversation API. When your application creates a conversation or post a message, it can register local tools that will be available for that specific interaction. These tools execute in your client's environment (e.g., user's browser).

**Note**: All client-side MCP tools are considered low-stakes by default. This means users can choose to remember their approval choice, making subsequent tool executions frictionless.

## Important Note

Client-side MCP servers require custom development and cannot be used directly in:

* Dust Web Application
* Official Dust browser extensions

This feature is designed for developers building their own applications/extensions that integrate with Dust through our public API.

## What It Enables

This client-side integration pattern allows you to:

* Expose local tools and functionality to Dust conversations at runtime through your client applications
* Keep sensitive operations and data within your control by executing tools in your client's environment
* Dynamically register and provide tools based on the user's context or permissions
* Integrate internal services and systems with Dust while maintaining full control over the execution environment

## Key Concepts

* **Client-side Execution**: Unlike custom MCP servers that run as standalone services, client-side MCP tools execute directly in your client application's environment when it interacts with Dust through the Conversations API.
* **Dynamic Registration**: Tools are registered at runtime when your application creates or updates a conversation, allowing you to dynamically control which tools are available based on the user's context.
* **Conversation-scoped**: The tools you register are available specifically for the conversations created by your client application, ensuring proper isolation and control.

## Implementation Requirements

1. Development skills in TypeScript/JavaScript (recommended) or other languages supporting the MCP protocol
2. Access to Dust's public API with OAuth authentication

## Authentication & Security

* Only works with OAuth personal access tokens
* API Keys are not supported

## Implementation

Our [SDK](https://www.npmjs.com/package/@dust-tt/client) provides a `DustMcpServerTransport` that handles all the communication complexity with Dust. This lets you focus solely on implementing your tools' business logic. For other languages see below.

## Real-World Example: Integrating Dust in Your Application's Interface

Let's say you're building a ticketing system web application and want to expose its functionality to Dust agents directly from your application's interface. This example shows how to create a client-side MCP server that exposes the same actions available in your UI to Dust:

```typescript theme={null}
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { DustMcpServerTransport } from "@dust-tt/client";
import { z } from "zod";

// Create the server.
const server = new McpServer({
  name: "ticket-cli",
  version: "1.0.0",
});

// Expose ticket management tools.
server.tool(
  "search_tickets",
  "Search tickets in the internal system",
  {
    query: z.string().describe("Search query (e.g., 'status:open priority:high')"),
    limit: z.number().describe("Maximum number of results").default(10)
  },
  async ({ query, limit }) => {
    // Your implementation using internal ticket system API.
    const tickets = await ticketSystem.search(query, limit);
    return { tickets };
  }
);

server.tool(
  "update_ticket",
  "Update ticket status and assignee",
  {
    ticketId: z.string().describe("Ticket ID"),
    status: z.enum(["open", "in_progress", "blocked", "resolved"]),
    assignee: z.string().optional().describe("User ID to assign the ticket to"),
    comment: z.string().optional().describe("Optional comment to add")
  },
  async (params) => {
    // Your implementation using ticket system API.
    const ticket = await ticketSystem.update(params);
    return {
      ticketId: ticket.id,
      status: ticket.status,
      assignee: ticket.assignee
    };
  }
);

// Connect to Dust.
const transport = new DustMcpServerTransport(dustAPI);
await server.connect(transport);

// Get the server ID to use in conversations.
const serverId = transport.getServerId();
```

### Using the Server in Conversations/Messages

When starting a conversation or posting a message with Dust, include the server ID you received from getServerId():

```typescript theme={null}
const message = {
  content: "Can you help me find all high-priority open tickets?",
  context: {
    clientSideMCPServerIds: [serverId]
  }
};
```

Now Dust can:

* Search your ticket system
* Update ticket statuses
* Reassign tickets
* Add comments

In this example:

1. When a user opens your ticketing system UI, your application creates a new client-side MCP server instance
2. The server exposes a subset of your UI's capabilities as tools (searching and updating tickets)
3. Each client (browser tab/window) maintains its own server instance
4. When the user navigates away or closes the tab, the server instance is terminated

This means that tools are always executed in the context of the user's active session in your application, with access to the same permissions and state as your UI.

## Technical Architecture

Client-side MCP servers follow a distributed architecture where:

* **Per-Client Instances**: Each client (browser tab, application window) runs its own independent server instance
* **Session Binding**: Server instances are bound to your application's user session and execution context
* **Instance Lifecycle**: Servers exist only while your client application is running and are automatically terminated when the client closes
* **Independent Communication**: Each instance maintains its own connection with Dust through:
  * Server-Sent Events (SSE) for receiving requests
  * HTTP POST endpoints for registration, heartbeat, and sending results

While our SDK abstracts this complexity, developers using other languages will need to implement a custom  [transport](https://modelcontextprotocol.io/specification/2025-03-26/basic/transports) that maintains this per-client isolation model.

## Implementing Your Own Transport

If you're not using our TypeScript/JavaScript SDK, you'll need to implement the following protocol:

### 1. Server Registration

Each server is registered by providing a name. The server will be registered for the currently authenticated user. The registration is valid for 5 minutes unless the server continuously sends heartbeats (see endpoint documentation):

```http http theme={null}
POST /api/v1/w/:workspaceId/mcp/register
Content-Type: application/json

{
  "serverName": "your-server-name"
}
```

The response includes a `serverId` that you'll need for all subsequent calls.

### 2.Heartbeat Mechanism

To keep the server active so Dust knows that it can be used by your agent, the transport must implement heartbeat behavior. There must be no more than 5 minutes between two heartbeats. This is required so Dust knows that the server is still active and can still be used:

```http http theme={null}
POST /api/v1/w/:workspaceId/mcp/heartbeat
Content-Type: application/json

{
  "serverId": "your-server-id"
}
```

The `serverId` retrieved from the registration must be used in the body of this API call.

### 3. Listening for Requests

Connect to the SSE endpoint to receive tool execution requests:

```http http theme={null}
GET /api/v1/w/:workspaceId/mcp/requests?serverId=your-server-id
```

Every time an agent wants to use your server, events will be propagated to this endpoint and wired directly in your transport. For each event, you must call `transport.onmessage()` with the event payload.

### 4. Sending Results

To post back results, the `send` function of the transport must POST results to:

```http http theme={null}
POST /api/v1/w/:workspaceId/mcp/results
Content-Type: application/json

{
  "serverId": "your-server-id",
  "result": {
    // Your tool's execution results
  }
}
```
