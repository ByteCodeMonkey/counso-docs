> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# JIT tools

## Overview

With JIT tools, you can activate and configure tools directly from the composer when you need them, without editing the agent in the builder. These settings are conversation‑scoped (ephemeral) and do not change the saved agent configuration for everyone.

## When to use JIT tools

* One‑off or time‑boxed tasks where you don't want to modify the shared agent
* Least‑privilege usage: enable only the tool(s) needed for the current question
* Faster iteration: avoid a trip to the agent builder for ad‑hoc work

## How to add a tool from the composer

1. In a conversation, open the composer tool picker
2. Search for the tool you need (e.g., "Notion") and click Configure
3. Complete any required authentication/permissions
4. Confirm the configuration. The tool becomes available to the agent for this conversation

Tip: Be explicit in your prompt about how the tool should be used (scope, sources, timeframe, and expected output).

## What happens under the hood (scope & persistence)

* Conversation‑scoped: enabled tools apply to this conversation only
* No change to the saved agent: your agent's builder configuration remains intact
* Same credentials and permissions model as when added in the builder

## What tools work well JIT

* Retrieval/Search (RAG) for contextual answers from your data sources /docs/user-documentation/agents/llm-best-practices/understanding-rag
* Web Search & Browse for up‑to‑date public information /docs/user-documentation/agents/tools/web-search-and-browse
* Structured lookups (Table Queries / Extract Data) when you need exact numbers or bulk extraction see sections in the RAG guide above
* Running another agent as a tool for a focused sub‑task (e.g., drafting, translation, summarization) /docs/user-documentation/agents/tools/index

## Best practices

* Keep scope narrow: specify exact sources or repositories when relevant
* Prefer structured methods (Table Queries, Extract Data) for quantitative tasks
* Start a new conversation if you want a clean context before enabling tools

## Related docs

* Tools overview /docs/user-documentation/agents/tools/index
* Data sources overview /docs/user-documentation/data-sources/overview
* Conversation files & dynamic tools /docs/user-documentation/data-sources/folders
* Web Search & Browse /docs/user-documentation/agents/tools/web-search-and-browse
* RAG overview/guidance /docs/user-documentation/agents/llm-best-practices/understanding-rag
