> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Front

## Overview

The Front MCP enables agents to interact with your Front workspace. Agents can search conversations, read messages and contact details, manage tags and assignments, and send replies or comments, supporting customer communication workflows directly from Dust.

## Connection Setup (Admin)

1. In Dust, go to **Spaces Tools** and click **Add Tools**.
2. Select **Front** from the list of available tools.
3. Paste your **Front Personal Access Token** into the field provided and save.

You can generate a Personal Access Token in Front under **Settings Integrations API**. See the [Front API documentation](https://dev.frontapp.com/reference/introduction) for details.

Once connected, the Front toolset will be available to add to agents in the spaces you grant access to.

## Authentication

Front authenticates requests using a Bearer token:

```
Authorization: Bearer <TOKEN>
```

See the [Front API Introduction](https://dev.frontapp.com/reference/introduction) for authentication details.

## Required Token Scopes

When generating a Personal Access Token in Front, enable the minimum set of scopes that match the tools you plan to use.

**Read scopes (required for read operations):**

| Scope                | Required for                                                                                                                                                 |
| :------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `conversations:read` | [List conversations](https://dev.frontapp.com/reference/list-conversations), [Search conversations](https://dev.frontapp.com/reference/search-conversations) |
| `messages:read`      | [List conversation messages](https://dev.frontapp.com/reference/list-conversation-messages)                                                                  |
| `contacts:read`      | [Get contact](https://dev.frontapp.com/reference/get-contact)                                                                                                |
| `tags:read`          | [List tags](https://dev.frontapp.com/reference/list-tags), [Get tag](https://dev.frontapp.com/reference/get-tag)                                             |
| `teammates:read`     | [List teammates](https://dev.frontapp.com/reference/list-teammates)                                                                                          |

**Write scopes (required for write operations):**

| Scope                 | Required for                                                                                     |
| :-------------------- | :----------------------------------------------------------------------------------------------- |
| `messages:send`       | [Create message / send reply](https://dev.frontapp.com/reference/create-message)                 |
| `comments:write`      | [Add comment](https://dev.frontapp.com/reference/add-comment)                                    |
| `drafts:write`        | [Create draft](https://dev.frontapp.com/reference/create-draft)                                  |
| `conversations:write` | [Update conversation](https://dev.frontapp.com/reference/update-conversation) (status, assignee) |
| `tags:write`          | Add or replace tags on conversations                                                             |

Apply only the scopes needed by the tools you enable. If your deployment only requires reading conversations, omit all write scopes.

## Available Tools

| Tool                             | Description                                                                 |
| :------------------------------- | :-------------------------------------------------------------------------- |
| **search\_conversations**        | Search conversations by query, including full-text and filter-based search. |
| **get\_conversation**            | Retrieve details of a specific conversation by ID.                          |
| **get\_conversation\_messages**  | List all messages in a conversation.                                        |
| **get\_contact**                 | Retrieve a contact's profile details.                                       |
| **get\_customer\_history**       | Retrieve conversation history for a contact.                                |
| **list\_tags**                   | List all available tags in the workspace.                                   |
| **list\_teammates**              | List all teammates (agents) in the workspace.                               |
| **list\_inboxes**                | List all inboxes the token has access to.                                   |
| **create\_conversation**         | Create a new outbound conversation.                                         |
| **create\_draft**                | Create a draft reply for a conversation.                                    |
| **add\_comment**                 | Add an internal comment to a conversation.                                  |
| **add\_tags**                    | Add tags to a conversation.                                                 |
| **add\_links**                   | Add external links to a conversation.                                       |
| **send\_message**                | Send a reply message in a conversation.                                     |
| **update\_conversation\_status** | Update the status of a conversation (e.g., archive, reopen).                |
| **assign\_conversation**         | Assign a conversation to a teammate or unassign it.                         |
