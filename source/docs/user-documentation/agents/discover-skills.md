> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Discover Skills

> Let agents find and enable relevant workspace skills during a conversation.

Discover Skills lets your agent find relevant workspace and Dust-provided skills while it works. The agent can enable a skill when a request matches its description, without requiring you to add every possible skill to the agent beforehand.

<Info>
  The `@dust` agent includes Discover Skills by default.
</Info>

## How to add it

In the Agent Builder, open your custom agent and select **Discover Skills** from the **Capabilities** section. Then save the agent.

### Make workspace skills discoverable

Discover Skills only sees workspace skills marked as discoverable. Mark a skill as discoverable if you want agents with this capability to find and enable it. Skills that are not discoverable do not appear in the available skill list.

## What it does

When Discover Skills is enabled, your agent can:

| Capability                 | Description                                                                                     |
| :------------------------- | :---------------------------------------------------------------------------------------------- |
| Skill discovery            | Reviews active workspace skills marked as discoverable, along with Dust-provided global skills. |
| Relevance matching         | Uses each skill's name and description to decide whether it applies to the current request.     |
| In-conversation activation | Enables the selected skill for the current conversation.                                        |
| Capability loading         | Gains access to the enabled skill's instructions, tools, and knowledge.                         |

Discover Skills does not load every available skill into the agent at once. It keeps the agent's initial configuration focused, then adds specialized guidance and capabilities when they become relevant.

Once the agent enables a skill, that skill remains available to the same agent for subsequent messages in the conversation.

## When to use it

Add Discover Skills when:

* You are building a general-purpose agent that handles varied requests.
* Your workspace has reusable skills for different teams or workflows.
* You want agents to benefit from newly published discoverable skills without updating every agent configuration.
* Loading all specialized instructions and tools upfront would add unnecessary context.

The agent only sees active, discoverable skills that are available to it. Enabling Discover Skills does not bypass workspace or space permissions.
