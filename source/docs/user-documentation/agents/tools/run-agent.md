> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Run agent

The `run_agent` tool enables your agents to run other agent as a tool. Two modes of executions are available:

### Default: Agent runs in background

The selected agent runs in a separate conversation and returns its output to the main agent, which then continues processing. This is particularly useful to:

* **Share behaviors across agents**: Factor specialized capabilities into dedicated custom agents that can be reused by multiple higher-level agents. This creates a modular architecture where lower-level agents handle specific tasks, improving maintainability and consistency.
* **Delegate in long-running loops**: When an agent needs to perform complex, multi-step tasks, delegating subtasks to sub-agents in separate conversations prevents context exhaustion. Each sub-agent operates with a fresh context window, enabling longer and more complex agentic workflows.

### New: agent responds in  conversation

The selected agent takes over and responds directly to the user instead of the main agent. This is a complete handoff. Useful to:

* **Route to specialized agents**: Direct users to the most appropriate agent based on their request type, domain, or required expertise.
* **Use specialized tools or knowledge**: Hand off to an agent with access to specific toolsets, data sources, or domain expertise that the main agent doesn't have, ensuring the user gets a direct response from the most capable agent.

The tool is configured as a regular tool in the agent builder and consists in selecting the agent to call.

You can provide context in the agent instructions about when to call the agent and what information to provide when doing so.

When your agent calls another agent you will be able to access the query and response (as well as agent thoughts) in the action detail panel. A link is also present to introspect the sub-conversation created and the actions taken by the sub-agent there.

We enforce a maximum recursion depth of 4 for calling sub-agents. Beyond this depth the action will return an error to the agent attempting it.
