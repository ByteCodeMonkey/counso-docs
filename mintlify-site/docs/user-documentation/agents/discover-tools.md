---
title: "Discover Tools"
---
**Discover Tools** lets an Agent find and activate specialized toolsets when a task needs them. It can keep a custom Agent's initial setup focused while making configured on-demand tools available during a conversation.

## Add Discover Tools to an Agent

If the capability is available in your workspace, open the custom Agent in Agent Builder, find **Capabilities**, select **Discover Tools**, and save the Agent. The default workspace assistant may already have dynamic tool discovery enabled; check its configuration rather than adding it twice.

Discover Tools can only list toolsets configured for on-demand availability to that Agent. Adding the capability does not connect a service, create credentials, or expand the Agent's access by itself.

## What happens during a conversation

When the Agent receives a request, Discover Tools can:

1. Review the names and descriptions of toolsets available to it.
2. Match a toolset to the request.
3. Enable the selected toolset in the current conversation.
4. Call its actions to read live data or make changes in an external application, if the tool and authorization allow it.

After activation, that toolset remains available to the same Agent for later messages in the conversation. It still follows its existing Space permissions and authentication settings.

## When to use it

Use Discover Tools when an Agent may need live or private data that is not indexed in Knowledge, or actions such as posting a message, creating a page, or updating an issue. It can also help a general-purpose Agent work with several configured applications without loading every tool at the start.

For information already indexed in connected sources, use **Discover Knowledge**. Discover Tools is for configured actions and live integrations. Review the action and destination before allowing an external change.
