> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Go Deep

Go Deep is a skill that enables your agents to perform in-depth analysis across company data, databases, and web sources. When enabled, it gives your agent the same research capabilities as @deep-dive: thorough investigation that may span over several minutes.

<Info>
  Go Deep used to perform a handoff to @deep-dive. This is not the case anymore, instead, it directly equips your agent with deep dive's capabilities and instructions, allowing it to conduct thorough research by itself.
</Info>

This skill gives access to your agent to the same capabilities as the [`@deep-dive`](/docs/user-documentation/agents/deep-dive-agent) global agent.

## How to add It?

The `Go Deep` skill is already included by default to the `@dust` agent, meaning that if the situation called for it, `@dust` can enable the skill and conduct thorough researches.

To add `Go Deep` to a custom agent, select the `Go Deep` skill to your agent from the Capabilities section.

## What does it do?

When the Go Deep skill is enabled, your agent gains access to:

| Capability               | Description                                                                                       |
| :----------------------- | :------------------------------------------------------------------------------------------------ |
| Sub-agents               | Planning and task execution agents for orchestrating complex research and optimize context usage. |
| Company data exploration | Full filesystem access to search and browse your connected data sources.                          |
| Data warehouses          | Ability to query SQL databases (Snowflake, BigQuery, etc.)                                        |
| Web search & browse      | Search the internet and browse web pages for external information                                 |

Your agent can use these tools to handle complex, multi-faceted questions requiring research across multiple data sources.

## When to Use?

Your agent should use `Go Deep` for:

* Complex research requiring multiple data sources.
* Questions needing deep investigation (several minutes of work).
* Tasks requiring SQL queries, web research, and company data exploration.
* In-depth analysis like market research or competitive intelligence.

## Admin Control

Workspace admins can deactivate `@deep-dive`, which removes the `Go Deep` skill from all agents. Otherwise, it's available to add to any agent with one click.

***
