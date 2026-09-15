> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Zendesk

## Overview

Zendesk tools let you add to your agent the capability to interact with Zendesk support tickets using shared credentials. This provides the ability to search tickets, get tickets, and draft replies.

This document provides general information about our Zendesk tools (available tools, setup, and authentication).

## Connection Setup

The setup process requires **workspace-level Zendesk authentication** using OAuth to connect your Zendesk account to Dust.

1. Under **Spaces** > **Tools**, select **Add Tools**
2. Select **Zendesk** from the available Tools
3. Complete OAuth authorization with your Zendesk credentials

## Adding Tools to Agents

Admins can provide workspace users access to these tools by adding it to a Dust space. Users can then add the tools to an agent by selecting Zendesk in the agent builder.

## Available Tools

| Tool               | Description                                                                                                                                                                                                                                                                                           |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Get Ticket**     | Retrieve a Zendesk ticket by its ID. Returns the ticket details including subject, description, status, priority, assignee, and other metadata. Optionally include ticket metrics such as resolution times, wait times, and reply counts. Optionally include the full conversation with all comments. |
| **Search Tickets** | Search for Zendesk tickets using query syntax. Returns a list of matching tickets with their details. You can search by status, priority, assignee, tags, and other fields. Query examples: `status:open`, `priority:high`, `status:open priority:urgent`, `assignee:me`, `tags:bug`.                 |
| **Draft Reply**    | Draft a reply to a Zendesk ticket. Creates a private comment (not visible to the end user) that can be edited before being published. This is useful for preparing responses before making them public.                                                                                               |

<Info>
  Looking to import Zendesk data into Dust instead? See the [Zendesk
  connection](/docs/user-documentation/admins/connections-management/zendesk).
</Info>
