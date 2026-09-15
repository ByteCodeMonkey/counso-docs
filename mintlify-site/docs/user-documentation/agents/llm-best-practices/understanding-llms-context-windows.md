---
title: "Understand context windows"
---
A context window is the amount of information a language model can process for one response. It includes the conversation, Agent instructions, retrieved or attached data, and the response being generated. A longer thread or larger set of files leaves less room for new material.

## Why the limit matters

When a conversation grows, older details may no longer fit in the model's active context. When an Agent includes recent documents, only as much material as the configured context allows can be considered. A larger context can help with long documents, but it can also take longer, consume more resources, and introduce irrelevant or conflicting information. Bigger is not automatically better.

## Work with the limit

- Give the Agent a focused source set and clear instructions rather than attaching everything.
- Start a new conversation for a separate task so unrelated history does not compete for context.
- Use a file or table query for large source material instead of pasting a long extract into chat.
- When a long task continues, summarize the decisions and open questions before moving to a fresh conversation.
- Choose a model and data approach suited to the task; model context limits and feature-specific limits may differ.

If a response misses an earlier fact, provide the relevant source or restate the key detail and ask the Agent to verify it. For managing a long conversation, see [Context compaction](/docs/user-documentation/agents/context-compaction).
