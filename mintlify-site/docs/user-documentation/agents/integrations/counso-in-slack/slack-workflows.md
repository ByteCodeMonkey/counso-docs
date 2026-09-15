---
title: "Use an Agent in Slack workflows"
---
A Slack workflow can send a message that invokes an Agent when an event occurs, such as a scheduled time or a reaction added to a message. This is useful for routine summaries or routing, where the Agent's answer should appear in a shared channel.

## Set up the workflow

1. In Slack, create a workflow and choose its trigger, such as a schedule or an emoji reaction.
2. Add a step that posts the prompt to the channel where the Agent should respond. Address the configured Counso app and name the Agent in the message, for example `@Counso +weekly-summary Summarize the updates since yesterday`. If the workspace uses another mention label, select the app from Slack's mention picker.
3. Ask a workspace administrator to register the exact workflow name and the restricted Spaces used by the Agent. Provide the workspace identifier requested by the approval process.
4. Run a test with a harmless prompt and confirm that the expected Agent replies in the intended channel.

Approval may be tied to the exact workflow name and the Agent's restricted data scope. Renaming the workflow or adding a restricted Space may require the administrator to update its approval. The deployment administrator manages workflow authorization for the workspace.

Before sharing a workflow broadly, confirm that every channel participant is an intended recipient of the Agent's answer and that the Agent can access only the sources needed for the task.
