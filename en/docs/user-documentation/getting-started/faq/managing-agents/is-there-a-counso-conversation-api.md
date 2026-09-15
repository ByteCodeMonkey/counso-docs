# Is there a Counso Conversations API?

Yes. The Counso Conversations API lets an application create conversations with Counso Agents and send messages to them programmatically. It can be used to bring an Agent into a product workflow, such as a support workspace or an internal operations tool.

The public API base URL is `https://app.counso.ai`. For another Counso environment, use that environment’s base URL and keep the same route paths. The main conversation routes are:

| Operation | Method and path | Purpose |
| --- | --- | --- |
| Create a conversation | `POST /api/v1/w/{wId}/assistant/conversations` | Starts a conversation from an initial message. |
| Add a message | `POST /api/v1/w/{wId}/assistant/conversations/{cId}/messages` | Sends a message to an existing conversation. |
| Read a conversation | `GET /api/v1/w/{wId}/assistant/conversations/{cId}` | Retrieves a conversation by ID. |

Replace `{wId}` with the workspace ID and `{cId}` with the conversation ID. Requests use the JSON fields defined in the API reference.

The API works with the workspace and Agent that the calling identity is allowed to use. Your application remains responsible for its own sign-in, user permissions, and the information it sends. Do not expose a server credential in browser code or treat a conversation ID as an access-control check.

For authentication, request schemas, streaming events, and response handling, see the [developer platform overview](../../../../developer-platform/overview/developer-platform.md) and the Counso API reference.
