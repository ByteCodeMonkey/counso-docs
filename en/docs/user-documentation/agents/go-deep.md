# Go Deep

**Go Deep** is a Skill that gives an Agent a longer-running research workflow when the workspace provides it. In the documented configuration, the Skill equips the Agent with the research capabilities and instructions associated with the default Deep Dive Agent; it no longer hands the work off to a separate `@deep-dive` agent.

## Add Go Deep

For a custom Agent, open Agent Builder and add **Go Deep** from **Capabilities**, then save. The default workspace assistant may already have the Skill and can activate it when the task calls for deeper research. Availability may depend on workspace settings; an administrator can disable the capability for the workspace.

## What it can do

When enabled and configured, Go Deep can make available:

- Planning and task-execution sub-agents to coordinate complex research.
- Search and browsing across connected company data sources.
- SQL queries against supported data warehouses such as Snowflake or BigQuery.
- Web search and browsing for public information.

This combination suits a complex question that spans several sources, needs structured warehouse analysis, or requires a sustained investigation. It can take several minutes. For a short lookup or a question that needs one specific document, ordinary search is usually simpler.

Go Deep can only use sources and tools that are connected, enabled, and accessible to the Agent. Check the data scope and permissions before adding it, and review citations and coverage after a run. An administrator disabling the default Deep Dive capability removes Go Deep from Agents that would otherwise use it.
