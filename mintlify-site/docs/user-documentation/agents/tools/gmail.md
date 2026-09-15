---
title: "Gmail"
---
The Gmail tool uses the connected user's Google identity to search and read mail and, when authorized, prepare drafts or send messages. Access follows that user's Gmail permissions; it is not automatically a shared mailbox connection.

A workspace administrator adds Gmail under **Spaces → Tools** and completes the application setup shown in the current form. The person whose mailbox should be used then authorizes the tool with their Google account. Add it to the intended Agent and start with a search or a read of one known message. Ask the Agent to identify the mailbox and message before drafting.

For email creation, prefer a draft for review. Sending requires the correct recipient, subject, body, and account identity; verify the sent message in Gmail afterward. If a user can search but cannot create a draft or send, check the granted write scope and Gmail account permissions. Do not place credentials or private message contents in Agent instructions.

## Available operations

The toolset includes `get_messages` for searching and reading messages, `get_attachment` for retrieving an attachment, `get_drafts`, `create_draft`, `create_reply_draft`, `delete_draft`, and `send_mail`. Draft and send operations require write authorization. Review the draft in Gmail before sending and check the target mailbox identity.

## Actions and approvals

`get_messages`, `get_attachment`, and `get_drafts` are read operations. `create_draft` and `create_reply_draft` prepare messages for review, `delete_draft` removes a draft, and `send_mail` sends a message. The source setup assigns Never ask to reads, Medium to draft creation, Low to draft deletion, and High to sending; administrators can adjust action stakes in the tool settings. In the documented configuration, `send_mail` may need to be enabled manually for an existing installation. Keep mail use targeted rather than using the tool for bulk campaigns.
