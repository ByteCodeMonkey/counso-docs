> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Slack tools

<Danger>
  **Warning**

  On May 29, 2025, Slack implemented significant API and policy changes that affect third‑party integrations:

  * Marketplace requirement: commercial apps must be listed on the Slack Marketplace to maintain full API access.
  * Rate limiting: non‑Marketplace and shared apps face drastically reduced limits on key endpoints.
  * Data indexing restrictions: Slack's updated terms prohibit bulk data indexing and enterprise search of Slack content.
    Current status (January 2026):
  * Slack MCP tools are fully available (GA). They provide real‑time search and messaging via your personal Slack credentials. Semantic search is available when your workspace has Slack AI enabled (Business+/Enterprise+ plans); otherwise, tools use keyword search.
  * Slack's Real‑Time Search API remains in closed beta for approved partners, with broader availability expected summer 2026.
  * If you need Slack as a synchronized data source, use the self‑created Slack app flow documented in "Slack connection."
    See our Status Report Page for ongoing updates.
</Danger>

For data synchronization and higher rate limits via a self‑created Slack app, see the Slack connection guide.

## Overview

Slack tools let you add to your agent the capability to interact with Slack content using your personal credentials. This provides the ability to search Slack messages, post messages, and access workspace information.

This document provides general information about our Slack tools (available tools, setup, and authentication).

Since this uses personal credentials, all actions performed by agents will appear as if you performed them directly.

<Info>
  **Another way to integrate Dust inside Slack**

  If you are looking to call Dust directly from Slack, please check [Dust in Slack](/docs/user-documentation/agents/integrations/dust-in-slack/slack-workflows#/)
</Info>

## :gear: Connection Setup

The setup process requires **personal Slack authentication** and uses OAuth to connect your individual Slack account to Dust. This ensures that agents only have access to the channels and content that you can personally access.

1. Under **Spaces** -> **Tools**, select **Add Tools**
2. Select **Slack** from the available MCP servers
3. Complete OAuth authorization with your personal Slack credentials.

## :ok\_person: Adding Tools to Agents

Admins can provide workspace users access to these tools by adding it to a Dust space. Users can then add the tools to an agent by selecting Slack in the agent builder.

## Available Tools

### Search Messages

Search messages across all channels and direct messages accessible to your user account.

**Parameters**: Keywords, time frame, channel filters, user filters
**Limitations**: Keyword-based search (not semantic)

### Semantic Search Messages

*(Conditionally available when Slack AI is enabled)*

Use semantic search to find messages across public channels, private channels, DMs, and group DMs where the current user is a member.

**Parameters**: Query, channels, user filters, time frame

### Post Message

Post a message to a channel or send a direct message.

**Parameters**: Recipient (channel/user), message content, optional thread timestamp, optional file ID to attach
**Formatting**: Supports Slack-flavored markdown

### Schedule Message

Schedule a message to be posted to a channel at a future time.

**Parameters**: Recipient, message content, scheduled time (Unix timestamp), optional thread timestamp
**Limitations**: Messages can be scheduled up to 120 days in advance. Maximum of 30 scheduled messages per 5 minutes per channel. File attachments are not supported for scheduled messages due to Slack API constraints. Use Post Message to send messages with files.

### List Users

Retrieve all users in the workspace with optional name filtering.

### Get User

Get user information given a Slack user ID.

**Parameters**: User ID

### Search Channels

Search for channels the user can access (public, private, DMs and group DMs are resolved by ID/name). Supports free‑text filtering and returns relevant channel metadata for targeting other tools.

### List Threads

List threads for a given channel, private channel, or DM. Returns thread headers with timestamps.

**Parameters**: Channel (name, ID, or user ID), optional oldest timestamp

### Read Thread Messages

Read all messages in a specific thread from public channels, private channels, or DMs.

**Parameters**: Channel, thread timestamp, optional limit/cursor/oldest/latest for pagination

## Advanced Features

### Thread Support

* Reply to existing message threads using thread timestamps
* Maintain conversation context within Slack threads
* Find thread IDs through message search functionality

### User and Channel References

* Mention users using \<@USER\_ID> format
* Reference channels using \<#CHANNEL\_ID> format
* Never use plain names as they won't be parsed correctly

## Limitations & Considerations

* Standard Slack API limits apply
* Search mode depends on your Slack plan: semantic search when Slack AI is enabled; keyword search otherwise.
* Scheduled messages cannot include file attachments (Slack API limitation). Use Post Message to include files.

**Using bot credentials instead of personal credentials?**
If you need actions to appear as coming from a bot rather than your personal account, see the Slack Bot MCP tool. A workspace admin can enable it under **Admin** > **Tools**, then attach it to the relevant Space under **Spaces** > **Tools**, and add it to agents in the Agent Builder.
