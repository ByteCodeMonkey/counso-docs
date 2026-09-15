> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Slab

## Overview

The Slab MCP provides agents with read access to your Slab workspace. Agents can retrieve posts, browse topics, and search content, making internal knowledge accessible directly in conversation.

## Connection Setup (Admin)

1. In Dust, go to **Spaces  Tools** and click **Add Tools**.
2. Select **Slab** from the list of available tools.
3. Paste your **Slab API access token** into the field provided and save.

You can find your API access token in Slab under **Team settings  Developer**. See the [Slab Developer Tools documentation](https://help.slab.com/en/articles/6545629-developer-tools-api-webhooks) for instructions.

Once connected, the Slab toolset will be available to add to agents in the spaces you grant access to.

## Authentication and Permissions Model

Slab's GraphQL API authenticates requests using an access token tied to a **Bot user**. Dust passes the token as:

```
Authorization: token <ACCESS_TOKEN>
```

Access to content depends entirely on **what the Bot user can access in Slab**. Before connecting, ensure the Bot user has been granted access to the topics and posts you want agents to be able to read.

**References:**

* [Slab GraphQL API (Apollo Studio)](https://studio.apollographql.com/public/Slab/variant/current/home)
* [Slab Developer Tools & API documentation](https://help.slab.com/en/articles/6545629-developer-tools-api-webhooks)

## Required Permissions

Slab does not offer granular API scopes. Access control is governed entirely by the **Bot user's permissions** within your Slab workspace:

* The Bot user must be a member of the Slab workspace.
* The Bot user must have access to the topics and posts you want agents to read.
* Private topics or posts the Bot user is not a member of will not be accessible.

Review and update the Bot user's membership in Slab's team settings to ensure the desired content is reachable.

## Available Tools

| Tool            | Description                                                |
| :-------------- | :--------------------------------------------------------- |
| **Get Post**    | Retrieve the full content of a Slab post by ID.            |
| **List Posts**  | List posts in the workspace, optionally filtered by topic. |
| **Get Topic**   | Retrieve details of a Slab topic, including its posts.     |
| **List Topics** | List all topics the Bot user has access to.                |
| **Search**      | Search posts and topics by keyword across the workspace.   |
