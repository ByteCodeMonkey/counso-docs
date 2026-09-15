> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Discover Tools

> Let agents find and enable specialized tools when a task requires them.

Discover Tools lets your agent find specialized toolsets available in your workspace and enable them when needed. This gives a custom agent access to a broad range of actions without loading every tool into its initial configuration.

<Info>
  The `@dust` agent already includes dynamic tool discovery. Add Discover Tools to give a custom agent the same on-demand access pattern.
</Info>

## How to add it

In the Agent Builder, open your custom agent and select **Discover Tools** from the **Capabilities** section. Then save the agent.

## What it does

When Discover Tools is enabled, your agent can:

| Capability                 | Description                                                                                          |
| :------------------------- | :--------------------------------------------------------------------------------------------------- |
| Toolset discovery          | Reviews the names and descriptions of specialized toolsets available to the agent.                   |
| Relevance matching         | Selects a toolset that fits the current request.                                                     |
| In-conversation activation | Enables the selected toolset for the current conversation.                                           |
| Tool use                   | Calls the enabled toolset's actions to read live data or perform changes in an external application. |

Once enabled, a toolset remains available to the same agent for subsequent messages in the conversation.

Discover Tools only lists tools configured for on-demand availability. The tools still follow their existing space permissions and authentication settings.

## When to use it

Add Discover Tools when your agent may need to:

* Perform actions such as posting a message, creating a page, or updating an issue.
* Retrieve live or private data that is not indexed in company data.
* Work across several applications without loading every integration upfront.
* Adapt to new workspace tools without updating its configuration each time.

For retrieving information that is already indexed in your company's connected data sources, use [Discover Knowledge](/docs/user-documentation/agents/discover-knowledge). Use Discover Tools for write actions, live data, or sources that are not indexed.
