> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Slack Troubleshooting

## How Dust's Slack Integration Works

Dust's Slack integration has two layers: **Slack Apps** and **Features**.

### Understanding Slack Apps

A Slack app is the foundation. When you install a Slack app, it creates a bot user in your workspace. Without the app installed, there's no bot to invite. Without the bot invited, there's no feature to use.

| Slack App            | What It Creates       | What It Enables                                                                                    |
| -------------------- | --------------------- | -------------------------------------------------------------------------------------------------- |
| **Dust Data Sync**   | `@Dust Data Sync` bot | Message syncing to Dust (your channels become searchable by agents) with Dust Slack **Connection** |
| **Dust**             | `@Dust` bot           | Interactive chat with agents **directly in Slack**                                                 |
| **Dust Slack Tools** | -                     | **Slack Tool** or **Slack Bot Tool** capability in Dust                                            |

<Info>
  **Why three Slack Apps?**

  Each app has a distinct job. **Dust Data Sync** reads and indexes your messages so agents can search them later (see [Slack Connection](/docs/user-documentation/data-sources/connections)). **Dust** is the interactive bot that responds when you mention it (see [Dust in Slack](/docs/user-documentation/agents/integrations/dust-in-slack/slack-workflows)). Separating these keeps permissions clear and lets you control each independently.
</Info>

### Understanding the Features

| Feature             | Slack App Required | Additional Step                           | What Happens                                   |
| ------------------- | ------------------ | ----------------------------------------- | ---------------------------------------------- |
| **Message sync**    | Dust Data Sync     | Select channel in Dust connection manager | Messages flow into your Dust data sources      |
| **Semantic search** | Dust Data Sync     | None (automatic once synced)              | Agents search your Slack history intelligently |
| **@Dust chat**      | Dust               | Invite `@Dust` to the channel             | Chat with agents directly in Slack             |
| **Slack tools**     | Dust Slack Tools   | Personal OAuth flow in Dust               | Agents search/post Slack on your behalf        |

Now that the basics are clear, let's dive into the troubleshooting usual suspects!

## Slack Connection Issues

### Private channel not appearing

**Why this happens:** Slack apps cannot see private channels until explicitly invited. This is a Slack security feature: private means private until you grant access.

**How to fix it:**

1. Open the private channel in Slack
2. Type `/invite @Dust Data Sync` and press **Enter**
3. Wait 2–5 minutes for Slack to propagate the change
4. Refresh the connection manager in Dust

<Info>
  **Inviting is not the same as syncing**

  Inviting the bot makes the channel visible in Dust's connection manager. But messages only sync after you explicitly select that channel in **Spaces  Connections  Slack  Add / Remove data** ([Connections](/docs/user-documentation/data-sources/connections)). This gives you control over exactly what data enters Dust.
</Info>

### Channel not syncing

**Why this happens:** Either the bot isn't in the channel, or the channel isn't selected in Dust's connection manager.

**How to fix it:**

1. In Slack, type `/invite @Dust Data Sync` and press **Enter**
2. In Dust, go to **Spaces  Connections  Slack  Add / Remove data** (see [Slack Connection](/docs/user-documentation/data-sources/connections))
3. Verify the channel appears and is selected
4. If already selected but not syncing, unselect it, save, then re‑select it

**To check if the bot is in a channel:** Click the channel name in Slack, go to **Integrations**, and look for `Dust Data Sync` in the list.

### Historical messages missing

**Why this happens:** Slack's API only provides messages from after the bot joined the channel. This is a Slack platform limitation, not a Dust limitation. Slack doesn't expose historical messages to newly‑invited bots.

### "Failed to retrieve permissions" error

**Why this happens:** When you first load the connection manager on a large workspace (1000+ channels), Dust needs to cache the full channel list. This takes time, and the error appears while that cache is building.

**How to fix it:** Wait 5 minutes, then refresh the page. The cache should be populated.

### Can't see Slack integration toggle

**Why this happens:** Either you don't have admin permissions in Dust, or your Slack connection predates December 2024 and needs migration.

**How to fix it:**

* Verify you're a Dust workspace admin
* If your connection was set up before December 2024, follow the [Slack Connection setup guide](/docs/user-documentation/data-sources/connections) to create your own Slack App.
* To enable the interactive bot, go to **Workspace Management  Workspace Settings  Integrations** and toggle Slack on ([Dust in Slack](/docs/user-documentation/agents/integrations/dust-in-slack/slack-workflows)).

## @Dust Bot Issues

### @Dust not responding

**Why this happens:** The bot isn't in the channel, the Slack integration is disabled in Dust, or you're trying to use it in a DM.

**How to fix it:**

1. In Dust, go to **Workspace Management  Workspace Settings  Integrations** and verify Slack is toggled on ([Dust in Slack](/docs/user-documentation/agents/integrations/dust-in-slack/slack-workflows)).
2. In the Slack channel, type `/invite @Dust` and press **Enter**
3. Mention the bot: `@Dust your question here`

**To remove the bot from a channel:** Type `/remove @Dust` and press **Enter**.

<Info>
  **DMs are not supported**

  `@Dust` works in public and private channels only. It does not respond in direct messages ([Dust in Slack](/docs/user-documentation/agents/integrations/dust-in-slack/slack-workflows)). This is by design: channels provide shared context that makes agent responses more useful to everyone.
</Info>

### Bot doesn't see full conversation

**Why this happens:** When you mention `@Dust`, it only receives the thread it's mentioned in, not the entire channel history. This keeps responses fast and focused.

**What you can do:**

* Include relevant context directly in your message
* Use Slack threads: mention `@Dust` within a thread so it sees all the thread's messages
* Reference specific details: "Based on the pricing we discussed above, what's our discount policy?"

### Calling a specific agent

**How to do it:** Use `+` or `~` before the agent name:

```
@Dust +sales-helper What's our discount policy?
@Dust ~hr-helper What's the PTO policy?
```

**For public channels:** You can set a default agent in the agent's settings (the agent must be published). When anyone mentions `@Dust` in that channel, your chosen agent responds automatically ([Dust in Slack](/docs/user-documentation/agents/integrations/dust-in-slack/slack-workflows)).

<Warning>
  **Private channel limitation**

  You cannot set a default agent for private channels. In private channels, always use the `+agent-name` or `~agent-name` syntax to call specific agents.
</Warning>

### Auto‑reply without @mention

**Why this might not work:** Auto‑reply must be enabled per agent and per channel by a workspace admin.

**Options:**

1. **Agent settings:** In the agent's **Slack Channel Settings**, select the channel(s) and turn on **Respond to all messages in channel**. Optionally check **Top-level posts only** to skip replies within threads. Available in every workspace; see [Slack Auto-Reply without @mention](/docs/user-documentation/agents/integrations/dust-in-slack/slack-auto-reply).
2. **Slack Workflows:** Use [Slack Workflows](/docs/user-documentation/agents/integrations/dust-in-slack/slack-workflows) to trigger agents based on events like emoji reactions or schedules.

<Warning>
  **Workflows require whitelisting**

  Slack workflows must be enabled for your workspace by Dust. Contact [support@dust.tt](mailto:support@dust.tt) with your workspace URL and workflow name to request access (see [Slack Workflows](/docs/user-documentation/agents/integrations/dust-in-slack/slack-workflows)). When you contact support, include the exact name(s) of any Restricted Space used by the agent (in addition to Company Data). This is indicated by the yellow Restricted Space heads‑up in the Agent Builder.
</Warning>

## Slack Tools Issues

### Poor search results

**Why this happens:** Search quality depends on which search method is available in your Slack workspace.

| Tool                         | What It Requires        | How It Works                                           |
| ---------------------------- | ----------------------- | ------------------------------------------------------ |
| **Semantic Search Messages** | Slack AI add‑on enabled | Uses natural language understanding for better results |
| **Search Messages**          | Nothing                 | Keyword matching only, less accurate                   |

**What you can do:**

* Check if your Slack workspace has the AI add‑on enabled
* When using keyword search, be specific and exact
* Try multiple searches with different keyword combinations

### Actions appear from my name

**Why this happens:** Slack tools use your personal OAuth credentials. When an agent posts a message or performs an action, Slack sees it as coming from you. This is intentional: it means agents can only do what you're allowed to do ([Slack Tools](/docs/user-documentation/agents/tools/slack-tools)).

**If you need bot identity:** A workspace admin can enable the **Slack Bot** tool under **Admin** > **Tools**, then attach it to the relevant Space under **Spaces** > **Tools**, and add it to agents in the Agent Builder. The bot posts as a bot identity instead of you, and only works in channels where the bot has been invited.

### Tool not appearing in agent builder

**Why this happens:** You haven't connected your personal Slack credentials to Dust's tools yet.

**How to fix it:**

1. Go to **Spaces  Tools  Add Tools**
2. Select **Slack** from the list
3. Complete the OAuth flow with your Slack account
4. The Slack tools now appear when building agents ([Slack Tools](/docs/user-documentation/agents/tools/slack-tools)).

## Setup and Migration Issues

### Can't create Slack app

**Why this happens:** You don't have the required Slack permissions, the manifest was modified, or you selected the wrong workspace.

**How to fix it:**

1. Verify you're a Slack **Owner** or **Admin** (not just a member)
2. Copy the manifest exactly as provided in the Dust docs; do not edit it ([Connections](/docs/user-documentation/data-sources/connections))
3. When Slack prompts you to select a workspace, choose the correct one

**How to check your Slack role:**

1. Click your workspace name in Slack (top‑left corner)
2. Go to **Settings & administration  Manage members**
3. Search for your name; your role appears next to it

### Connection broke after editing app

**Why this happens:** Certain Slack app settings are critical to the Dust connection. Changing them breaks the authentication flow.

**Settings you must not change:**

* OAuth scopes or permissions
* Redirect URLs
* Credentials (Client ID, Client Secret, Signing Secret)

**If you rotated credentials for security reasons:** Update them immediately in **Spaces  Connections  Slack  Manage  Edit** ([Connections](/docs/user-documentation/data-sources/connections)). Enter the new credentials from your Slack app's Basic Information page. The connection should resume automatically.

### Legacy connection migration

**Why this matters:** Slack connections created before December 2024 use a shared Dust app. These connections work until **March 3, 2026**, but must be migrated to your own Slack app before that deadline ([Connections](/docs/user-documentation/data-sources/connections)).

**How to fix it:** Follow the [Slack Connection setup guide](/docs/user-documentation/data-sources/connections). The process takes about 2 minutes and involves creating your own Slack app from a manifest.

## Permission Issues

### App pending approval

**Why this happens:** Your Slack workspace has an app approval workflow enabled. New apps require admin approval before they can be used.

**How to fix it:** Ask your Slack admin to approve the app in **Slack Admin  Manage Apps  App Requests**.

### Can't see all channels

**Why this happens:** Dust has its own permission layer that controls who can select which channels for syncing.

**How to fix it:** Check **Spaces  Connections  Slack** to see access restrictions and which spaces receive which data ([Connections](/docs/user-documentation/data-sources/connections)).

### "You don't have permission" error

**Why this happens:** The action requires a Slack role you don't have.

| Action                  | Required Slack Role          |
| ----------------------- | ---------------------------- |
| Install apps            | Owner or Admin               |
| Manage existing apps    | Owner, Admin, or App Manager |
| Invite bots to channels | Any member of that channel   |

## Known Limitations

| Limitation                                 | Why It Exists                                                                                                                                                                                                                                           |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **One interactive bot per Dust workspace** | You can sync multiple Slack workspaces as data sources, but only one can have the `@Dust` bot active. This prevents confusion about which bot responds.                                                                                                 |
| **Bot messages not synced**                | Messages from `@Dust` and other bots are intentionally excluded from sync. This prevents AI‑generated content from being treated as source material, which could propagate mistakes. ([Connections](/docs/user-documentation/data-sources/connections)) |
| **No default agent in private channels**   | Slack's Terms of Service restrict certain bot behaviors in private channels. Use `@Dust +agent-name` syntax instead.                                                                                                                                    |
| **Thread links sometimes approximate**     | When messages aren't threaded, Dust links to the approximate location in the channel rather than the exact message. Use threads for precise linking. ([Connections](/docs/user-documentation/data-sources/connections))                                 |

<Info>
  **Best practice: Use threads**

  Post your topic as the first message, then continue the conversation in a thread. This improves Dust's ability to retrieve relevant context and provides accurate message links ([Connections](/docs/user-documentation/data-sources/connections)).
</Info>

## Still Stuck?

Email **[support@dust.tt](mailto:support@dust.tt)** with:

* What you did, what you expected, what happened instead
* **Dust URL where you see the issue**
* **Slack message, thread, or channel URL**
* **Any error message**
