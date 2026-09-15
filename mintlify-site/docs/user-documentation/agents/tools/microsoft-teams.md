---
title: "Microsoft Teams"
---
The Teams tool gives an Agent access to Teams data and messaging using a Microsoft identity. Depending on permissions it can find teams and channels, search or read chats and messages, and send messages. A Teams Bot or channel integration is a separate feature with a separate identity and event configuration.

A Microsoft Entra administrator and workspace administrator add the Teams tool under **Spaces → Tools** and approve the delegated permissions required by the current form. The recorded scope set includes team and channel basics, chat and message read/write permissions, message sending, user profile access, and `offline_access`; exact requirements depend on enabled actions. Each user authorizes their own account if the form uses personal credentials.

Add the tool to an Agent and test a channel or chat the user can already access. Before sending, confirm the target team, channel or chat, recipients, and message body. Verify the result in Teams. If messages appear under an unexpected identity or a channel is missing, distinguish the live tool from the Teams Bot and check the acting user's membership and admin consent.

## Available operations and limitation

The tool list includes **Search Messages Content**, **List Teams**, **List Users**, **List Channels**, **List Chats**, **List Messages**, and **Post Message**. Search is keyword-based rather than semantic. The authenticated user must belong to a team or chat to see its content.

The required delegated permissions depend on the enabled actions and can include `Team.ReadBasic.All`, `Channel.ReadBasic.All`, `Chat.Read`, `Chat.ReadWrite`, `ChatMessage.Read`, `ChatMessage.Send`, `ChannelMessage.Read.All`, `ChannelMessage.Send`, `User.Read`, `User.ReadBasic.All`, and `offline_access`. An Entra administrator may need to grant consent in the enterprise application's permissions panel or approve the pending consent request.

## Messaging and search

`Search Messages Content` uses keyword search rather than semantic retrieval. **List Teams**, **List Channels**, and **List Chats** help identify a target; **List Messages** reads a channel thread and replies; **List Users** identifies recipients; **Post Message** writes to a channel, chat, or thread. Use the acting user's accessible team/chat, and specify the destination before sending.
