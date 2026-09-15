# Front

The Front MCP tool lets an Agent search conversations, read messages and contacts, inspect inboxes and teammates, create drafts or conversations, add comments and tags, assign conversations, and send replies. It uses a Personal Access Token configured for the workspace, so the token owner's Front access is shared with users who may invoke the tool.

## Connect Front

In **Front → Settings → Integrations → API**, create a Personal Access Token for the intended account. Grant read scopes only as needed: `conversations:read`, `messages:read`, `contacts:read`, `tags:read`, and `teammates:read`. For writes, add only the matching scopes: `messages:send`, `comments:write`, `drafts:write`, `conversations:write`, or `tags:write`. A read-only Agent should not receive write scopes.

In **Spaces → Tools**, add Front, enter the token, and share it with the relevant Space. Add Front to an Agent and begin with an inbox and a known conversation. Check that the token owner can access the inbox.

## Available operations

Read/discovery operations include `search_conversations`, `get_conversation`, `get_conversation_messages`, `get_contact`, `get_customer_history`, `list_tags`, `list_teammates`, and `list_inboxes`. Write operations include `create_conversation`, `create_draft`, `add_comment`, `add_tags`, `add_links`, `send_message`, `update_conversation_status`, and `assign_conversation`.

Match write scopes to actions. If drafts are sufficient, do not grant message sending. Distinguish an internal comment or draft from a sent customer reply. For a reply, check the recipient and body and confirm the message in Front afterward.
