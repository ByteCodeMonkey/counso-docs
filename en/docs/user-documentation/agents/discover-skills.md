# Let an Agent discover Skills

**Discover Skills** allows an Agent to find relevant discoverable Skills during a conversation and activate one when its description matches the request. It avoids loading every specialized instruction and capability into the Agent's initial configuration. A default workspace Agent may already include Discover Skills.

## Add it to a custom Agent

In Agent Builder, open the Agent, select **Discover Skills** from **Capabilities**, and save. For a workspace Skill to appear in discovery, its availability must allow discovery by Agents. Skills not marked discoverable are not shown to the Agent.

## What happens during a conversation

The Agent checks active workspace Skills marked as discoverable, along with any global Skills made available to it. It matches the Skill name and description to the current request, then can enable a relevant Skill for the conversation. The selected Skill's instructions, Tools, and Knowledge become available to the Agent. It stays available for later messages in the same conversation.

Discover Skills does not load every Skill up front and does not bypass workspace or Space permissions. The Agent sees only active Skills that are available to it.

## When to use it

Use Discover Skills for a general-purpose Agent serving varied requests, or when the workspace regularly adds reusable Skills for different teams. It can keep the Agent's initial setup focused while letting new discoverable procedures become available without editing each Agent. For visibility settings, see [Skill availability](skill-availability.md).
