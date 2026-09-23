> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Slack workflows

Slack workflows automate routine tasks in your Slack workspace, like a message posted on a schedule or a form submitted to a channel. A workflow can also summon a Dust agent, so instead of posting a message it posts an answer.

For example:

* post `@dust +highlights What have been the highlights since yesterday?` in #general every weekday at 10 a.m.
* summon an agent in #your-channel every time someone reacts to a message with a given emoji.

## How it works

1. **Create the Slack workflow.** Define its trigger, a scheduled time or an action such as a reaction being added, and the message it posts. Slack's own guide covers this: [Build a workflow in Slack](https://slack.com/help/articles/17542172840595-Build-a-workflow--Create-a-workflow-in-Slack).
2. **Write the message so it summons an agent.** Mention `@dust` followed by the agent name, as in `@dust +agentName`, to pick which agent answers.
3. **Allow the workflow in Dust.** A workflow posts as a Slack bot rather than a person, and Dust ignores those messages until you allow the workflow. How you do that depends on your plan: see [credit-priced plans](#allow-a-workflow-on-credit-priced-plans) or [legacy plans](#allow-a-workflow-on-legacy-plans) below.

Whichever plan you are on, Dust identifies a workflow by the sender name shown in Slack on its messages, matched exactly including capitalization and emojis. Rename the workflow in Slack and it stops working until you allow it again under its new name.

Allowing a workflow also grants it a set of Spaces. It always reaches agents shared in Company Data, and any other Space has to be granted explicitly. If an agent reads data from a Space the workflow cannot reach, it stays silent when the workflow triggers it.

<Warning>
  Anyone who can run the workflow in Slack can summon agents through it, guests included. Grant a workflow only the Spaces it needs.
</Warning>

## Allow a workflow on credit-priced plans

Admins allow workflows for their teams on their own, without relying on Dust for the setup.

1. Go to **Programmatic Usage > Automations** and open the **Slack workflows** tab.
2. Click **Allow a workflow**.
3. Enter the **workflow name**, copied from the sender name on the workflow's Slack messages.
4. Under **Spaces it can reach**, add the Spaces holding the data your agent uses. Company Data is always included and cannot be removed.
5. Click **Allow**.

The workflow shows up in the table with its Spaces and the date you added it, and can summon agents from that point on.

Connect the Dust Slack bot to your workspace first. Without it, the tab prompts you to connect it and shows no table.

### Change or revoke a workflow

Click the trash icon on a row and confirm to stop that workflow from summoning agents. To change which Spaces a workflow reaches, or to follow a rename in Slack, allow it again with the updated name and Space list.

Your workspace audit log records both actions.

### Track what workflows cost

The **Slack workflows** tab reports the credits your Slack workflows consumed over the selected period, their share of total workspace consumption, and how many workflows you currently allow. Change the window with the period selector at the top of the Automations page.

## Allow a workflow on legacy plans

Legacy plans do not have the **Slack workflows** tab. The Dust team allows workflows for you instead.

Email `support@dust.tt` with the template below, filling in all three fields:

```text Whitelisting request theme={null}
Dust workspace URL: https://dust.tt/w/<your-workspace-id>
Slack workflow name: <exact name of the Slack workflow>
Spaces used by the agent: <exact names, or "Company Data" if none>
```

* **Dust workspace URL**: copy it from your browser. It contains your workspace ID, which is how we identify your workspace.
* **Slack workflow name**: we match the workflow on its name exactly as written, so copy and paste it.
* **Spaces used by the agent**: we grant the workflow access to a specific list of Spaces. If your agent uses data from any Space beyond Company Data, send us those exact names, otherwise the agent will not be allowed to answer. If it only uses Company Data, say so.

<Info>
  **Good to know**

  We allow the Slack workflow itself, so once it is validated you can change which agent it calls, or how the workflow works, without writing to us again.

  Email us again if you rename the workflow in Slack, or if you give the agent access to an additional Space.
</Info>
