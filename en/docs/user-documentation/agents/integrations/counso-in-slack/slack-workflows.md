# Use an Agent in Slack workflows

Slack workflows automate routine tasks such as scheduled messages or form submissions. A workflow can mention a Counso Agent so that the Agent's answer is posted to the selected channel.

For example, a workflow can:

- ask a highlights Agent for a summary every weekday morning;
- invoke an Agent whenever someone reacts to a message with a selected emoji.

## How it works

1. In Slack, create a workflow and choose a trigger such as a schedule, form submission, or reaction.
2. Add a message step. Mention the configured Counso app and the Agent name, for example `@Counso +highlights Summarize the updates since yesterday`.
3. Allow the workflow in Counso and grant it only the Spaces needed by the Agent.
4. Run a harmless test and confirm that the expected Agent responds in the intended channel.

Counso identifies a workflow by the sender name shown on its Slack messages. The match includes capitalization and emoji. If the workflow is renamed in Slack, allow it again under the new name.

The workflow can always reach Agents and data made available through Company Data. Other Spaces must be granted explicitly. If an Agent needs a Space the workflow cannot reach, it will not answer the workflow message.

<Warning>
  Anyone who can run the Slack workflow, including guests, may be able to invoke the selected Agent. Grant the workflow only the Spaces it needs, and make sure the destination channel is appropriate for the answer.
</Warning>

## Allow a workflow

If the workspace provides self-service workflow controls:

1. Open **Programmatic Usage > Automations**.
2. Select the **Slack workflows** tab.
3. Click **Allow a workflow**.
4. Enter the exact workflow sender name from Slack.
5. Under **Spaces it can reach**, add the Spaces containing the data required by the Agent. Company Data is always included.
6. Save the workflow and test it from Slack.

The table shows the allowed workflows, their Space access, and when they were added. The page may also report the credits consumed by Slack workflows for the selected period.

If the Slack workflows tab is not available in the current deployment, ask the deployment administrator to register the workflow name and its allowed Spaces. Do not send workspace identifiers or access information to an upstream vendor.

## Change or revoke access

Remove a workflow from the table to prevent it from invoking Agents. To change its name or Space access, register it again with the updated values. If audit logging is enabled, workflow authorization changes appear in the workspace audit log.
