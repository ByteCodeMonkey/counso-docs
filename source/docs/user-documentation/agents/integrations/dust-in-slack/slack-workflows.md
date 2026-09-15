> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Slack workflows

## Overview

Slack workflows allow you to automate routine tasks and interactions within your Slack workspace. You can integrate Dust agents into these workflows.

For example:

* create a Slack workflow sending a message every day at 10a.m. in the #general channel: [\`@dust](https://github.com/dust) +highlights\` What have been the highlights since yesterday?
* trigger a Dust agent in the #your-channel channel every time a member adds the  emoji to a Slack message.

## Setting up a Slack Workflow with a Dust agent

1. **Create a Slack workflow.** This includes defining the workflow trigger, for example a scheduled time (e.g., daily at 10a.m.) or an action (e.g., adding a  emoji to a message). You can find more details about how to create a Slack workflow [here](https://slack.com/help/articles/17542172840595-Build-a-workflow--Create-a-workflow-in-Slack).
2. **Whitelist your Slack workflow with the Dust team.** Dust must whitelist your Slack workflow before a Dust agent can reply to messages posted by the workflow Slackbot.

   <Warning>
     **Contact Dust support to get your workflow whitelisted**

     Email `support@dust.tt` with the template below. Those informations are crucial for us to proceed with the whitelisting ;

     ```text Whitelisting request theme={null}
     Dust workspace URL: https://dust.tt/w/<your-workspace-id>
     Slack workflow name: <exact name of the Slack workflow>
     Restricted Spaces / Pods used by the agent: <exact names, or "workspace" if none>
     ```
   </Warning>

   What each field means:

   * **Full Dust workspace URL** — copy it directly from your browser. It contains your workspace ID, which is what we use to identify your workspace.
   * **Exact Slack workflow name** — we match the workflow on its name, exactly as written, so copy and paste it (capitalization, spacing, emojis included).
   * **Restricted Spaces / Pods used by the agent** — whitelisting grants the workflow access to a specific list of Spaces and Pods. **If your agent uses data from any Restricted Space or private Pod, we need their exact names**, otherwise the agent will not be allowed to answer when triggered by the workflow. If the agent only uses Company Data and open Spaces or Pods, simply write `workspace`.

   <Info>
     **Good to know**

     The **whitelisting is at the Slack workflow level,** so you can change the name of the agent called inside anytime once validated, or even how the workflow work.

     However, the whitelisting is tied to the **exact workflow name**: if you rename the Slack workflow, the whitelisting no longer applies and you have to email `support@dust.tt` again with the new name.

     If you later give the agent access to an additional Restricted Space or private Pod, contact us again so we can add it to the whitelist.
   </Info>
3. **Invoke @dust and the Dust Agent of your choice in the Slack workflow message.** Specify which Dust agent to use in a workflow by including the agent's name following this message format: `@dust +agentName`. This will ensure that the correct Dust agent responds to the workflow-triggered messages.
