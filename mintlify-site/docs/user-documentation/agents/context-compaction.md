---
title: "Compact context in a long conversation"
---
Context is the information a model can use for its next response: Agent instructions, the current request, earlier messages, and retrieved material. Capacity varies by model. Text that remains visible in the history is not necessarily sent in full to the next run.

## Inspect context usage

When the composer provides a circular context indicator, open it to inspect the usage percentage. At the configured threshold, the interface offers **Compact now**. Near the limit, it can show a warning or require compaction before another message can be sent. Follow the state shown in the current composer.

## Compact and continue the same task

1. Open the long conversation and select the context indicator in the composer.
2. Choose **Compact now** when the button is available.
3. Wait for the compaction marker to finish before sending another message.
4. Check the completion marker in the conversation. Original messages remain in the history; later runs use the concise summary and messages after the marker.
5. Restate any number, constraint, or source essential to the next step in a short message. A summary can omit details.

Compaction is useful when the same task needs to continue through a long history. It does not turn the conversation into a shared knowledge source or delete the original record.

## Start a new conversation for a new task

When the topic, source scope, or deliverable changes substantially, ask the Agent to collect the current decisions, open questions, and citations before starting a new conversation. Carry over only what the next task needs and specify its source scope again. Keep long documents in accessible knowledge sources instead of pasting them repeatedly into messages.

## Common questions

**Why is the compaction button temporarily unavailable?** An Agent may still be running, or a compaction operation may already be in progress. Wait for it to finish and inspect the indicator again.

**Does a failed compaction erase the history?** Original messages remain. Read the failure message and keep the conversation. To continue, narrow the request or start a focused conversation with the necessary records.

**Why is a detail missing after compaction?** Summaries compress information. Point to the exact detail in its original message or source and ask the Agent to correct its subsequent work.

See Model selection and Choosing sources.
