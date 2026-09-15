> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Slack Auto-Reply without @mention

Dust agents can automatically reply in selected Slack channels without anyone mentioning the `@Dust` Slack app. This is useful for dedicated support or Q\&A channels where every message should get an agent answer without extra steps.

This feature is available in every workspace using the [Dust in Slack](https://dust.tt/home/slack/slack-integration) integration.

## How it works

When auto-reply is enabled for a channel, the agent set as the channel's default agent responds to messages posted in the channel, not just to `@Dust` mentions. Two modes are available:

* **All messages**: the agent replies to every message in the channel, including replies inside threads.
* **Top-level posts only**: the agent replies only to new channel messages, not to replies within threads.

Messages that explicitly mention `@Dust` follow the standard mention behavior, and messages posted by bots are ignored.

## Set it up

Auto-reply is configured per agent from its Slack channel settings. Only workspace admins can change these settings, and the agent must be published.

1. In the Agent Builder, open the agent's **Slack Channel Settings**.
2. Select the channel(s) where the agent should reply by default.
3. Turn on **Respond to all messages in channel**.
4. (Optional) Check **Top-level posts only** to skip replies within threads.
5. Save.

<Info>
  **Private channels**

  Private channels you belong to appear in the channel list after you add the Slack tool to the agent, connect your personal Slack account, and invite `@Dust` to the channel.
</Info>

## Related

* [Slack workflows](/docs/user-documentation/agents/integrations/dust-in-slack/slack-workflows)
* [\[Beta\] Slack Auto-Join](/docs/user-documentation/agents/integrations/dust-in-slack/slack-auto-join)
