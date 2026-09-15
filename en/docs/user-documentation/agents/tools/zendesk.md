# Zendesk

The Zendesk tool uses workspace-level OAuth credentials to search and retrieve support tickets and create draft replies. A workspace administrator completes OAuth in **Spaces → Tools → Add Tools**, shares the tool with the appropriate Space, and adds it to the Agent. The shared account's Zendesk access defines which tickets are visible.

## Available operations

- **Get Ticket** reads a ticket by ID, including subject, description, status, priority, assignee, metadata, and optionally metrics or the full comment history.
- **Search Tickets** searches with Zendesk query syntax. Examples include `status:open`, `priority:high`, `assignee:me`, and `tags:bug`.
- **Draft Reply** creates a private comment that is not visible to the end user, ready for review before publication.

A Zendesk Connection used for synchronized search is separate from the live Tool. Check the shared identity and brand when a ticket is missing. Review a draft before making any reply public.
