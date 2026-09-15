---
title: "Steer a running conversation"
---
When the workspace supports live Agent progress, you can follow a run as it proceeds and redirect it without starting over. Progress may show steps such as searches, tool calls, and file operations. Select a step to inspect its details when that view is available.

## Send a correction while the Agent is working

You can send a message before the current run has finished. The message appears as pending. The Agent completes its current round of actions first—for example, it finishes the current group of parallel searches—then reads your message with the conversation context and continues in the new direction.

You can send more than one message while the Agent is working. They are queued and picked up together after the current round. Use a short correction to narrow the source, add context, or change the requested output; you do not need to cancel the run just to steer it.

## One Agent at a time

The live-steering behavior is scoped to one active Agent in a conversation. The active Agent is shown in the composer. To reliably direct the run, continue with that Agent rather than starting a second one in the same conversation.

## Stop a run

If you stop the Agent, work already completed remains in the conversation; stopping ends the work still to come. Inspect the completed steps and result before deciding whether to continue with a correction or start a separate conversation.

## Use steering to refine the task

A correction is most useful when it identifies what should change while preserving work that is still relevant. For example, if an Agent is collecting a monthly summary and you decide to include a region breakdown, send that request while it is running. It will finish its current action round, then incorporate the added requirement. Check that it actually applied the correction in the final response.
