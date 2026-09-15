# Client-side MCP servers

A client-side MCP server lets an application provide tools to a Counso conversation while the tools themselves run in the application’s environment, such as an authenticated browser session. This is useful when an Agent needs to work with information or actions that should stay in the context of the user’s application—for example, looking up a ticket or preparing an update through an internal service. It is designed for custom applications built on the Counso Conversations API; it is not a setting that adds tools to the Counso web app or its extensions.

The application controls which tools are available for a conversation and implements each tool’s behavior. It can choose tools based on the current user and task, then include the active server ID in the conversation context as `clientSideMCPServerIds`. Tools run with the application’s local session and state. Keep the tool list narrow, and check the user’s authorization again when each operation runs. Conversation-level registration helps scope tools but does not replace your application’s access checks.

Because execution happens in the client, each browser tab or application window has its own server instance, and a tool is available only while that client session can serve requests. Plan for a closed tab, lost connection, or expired user session, and return clear errors when a tool cannot complete. Client-side MCP tools are treated as low-stakes by default, so users may choose to remember an approval decision; enforce your own authorization for every operation.

## Registering and serving a client-side server

MCP registration requires an OAuth access token for the signed-in user. API keys are not supported for these routes. Use `https://app.counso.ai` as the default `baseUrl`; substitute the base URL of the Counso environment used by your application when needed.

| Step | Method and route | Request or response |
| --- | --- | --- |
| Register | `POST {baseUrl}/api/v1/w/{wId}/mcp/register` | Send `{"serverName":"ticket-tools"}`; retain the returned `serverId` and `expiresAt`. |
| Keep active | `POST {baseUrl}/api/v1/w/{wId}/mcp/heartbeat` | Send `{"serverId":"..."}` before the registration expires. |
| Receive tool requests | `GET {baseUrl}/api/v1/w/{wId}/mcp/requests?serverId={serverId}` | Keep the `text/event-stream` connection open to receive requests. `lastEventId` can be supplied when resuming. |
| Return a result | `POST {baseUrl}/api/v1/w/{wId}/mcp/results` | Send `{"serverId":"...","result":{...}}` after executing the requested tool. |
| Deregister | `POST {baseUrl}/api/v1/w/{wId}/mcp/deregister` | Send `{"serverId":"..."}` when the client server shuts down. |

Registration is scoped to the authenticated user and workspace. It expires after five minutes unless renewed; send heartbeats no more than five minutes apart and use `expiresAt` to track the active registration. On the `requests` event stream, dispatch each tool request to the MCP server transport; the transport sends the tool result to the `results` endpoint. Deregister the server when the client closes.

An SDK transport can manage this registration and message flow for you. If you implement another transport, keep the per-client isolation model: register under the signed-in user, listen for requests over Server-Sent Events, deliver each event to the MCP transport, and post the execution result. See the [Counso API reference](../../developer-platform/counso-api-documentation/openapi-and-postman.md) for the endpoint schemas.
