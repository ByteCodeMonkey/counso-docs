> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# @deep-dive Agent

## What is `@deep-dive` and how to use it?

`@deep-dive` is a default agent in your workspace designed to tackle complex, multi-faceted questions that require thorough investigation. Unlike quick-answer agents, @deep-dive takes its time (running for 10 to 30 minutes when needed) to deliver comprehensive, well-researched results.

`@deep-dive` has full access to all your Knowledge and Tools from the Company Data Space. When you need to analyze hundreds of documents, query multiple data sources, synthesize internal and external information, or investigate complex questions across your entire knowledge base, this agent allocates substantially more time and compute to answer thoroughly.

Simply mention it using `@deep-dive` on the composer and ask your question!

## How `@deep-dive` Works

`@deep-dive` adapts its approach based on your question's complexity.

**Simple questions:** If your question can be answered with a quick search or a simple semantic search, `@deep-dive` handles it directly with no unnecessary overhead.

**Complex questions:** When the work requires depth, `@deep-dive` transforms into a research coordinator.

1. **Plans the investigation**: Creates a research plan and consults the planning agent to optimize the approach. For this we use a model with high-thinking settings.
2. **Delegates to specialists**: Spawns sub-agents to handle specific tasks (browsing web pages, reading documents, querying databases).
3. **Runs tasks in parallel**: Executes up to 6 sub-agent tasks simultaneously for faster results.
4. **Synthesizes findings**: Combines all the research into a comprehensive, well-structured answer or report.

You'll see `@deep-dive`'s reasoning process in real-time as it works through your question, so you always know what it's doing.

## Tools & Capabilities

`@deep-dive` has access to all Knowledge and tools in Company Data:

### Advanced search

`@deep-dive` can explore your Knowledge data using our Advanced search tool,  a **file system-like interface** that works across all your connected sources.

**What it can do:**

* **Navigate hierarchies**: Browse through Slack channels, Notion workspaces, GitHub repos, and other data sources like a file system.
* **Search intelligently**: Run semantic searches to find relevant information based on meaning, not just keywords.
* **Read documents**: Access full document contents in manageable chunks, even for very large files.
* **Find by name**: Search for specific documents or files across your entire knowledge base.
* **Locate in context**: Understand where documents sit within your organization's structure.

### Data Warehouses

`@deep-dive` can also explore your data warehouses (Snowflake, BigQuery) to answer quantitative questions with precision.

**What it can do:**

* **Explore available data**: Discover tables, schemas, and databases across your warehouses.
* **Understand structure**: Examine schemas, column types, relationships, and example rows.
* **Execute queries**: Run SQL queries with automatic dialect detection.
* **Join across sources**: Combine data from multiple tables or even different data sources.

You don't need to know which tables contain the data. `@deep-dive` explores your warehouse dynamically and finds what it needs.

### Web Search & Browse

`@deep-dive` can search the web and read web pages to gather up-to-date information and external knowledge. It uses AI-generated summaries for efficient browsing, then reads full content for important pages when needed.

### Dynamic Tool Discovery

`@deep-dive` can discover and use additional capabilities during an investigation. When a task requires a specific tool (GitHub, Salesforce, Monday.com, etc.), it spawns a sub-agent with access to that toolset. This means @deep-dive adapts to what your workspace has available.

### MiniApps

When text isn't enough, `@deep-dive` can create interactive visualizations with charts, graphs, and dynamic dashboards using our "Create MiniApps" tool. It only creates interactive content when it genuinely enhances the answer, defaulting to clear, comprehensive written reports for most questions.

### Sub-Agents

`@deep-dive` spawns specialized sub-agents that tackle different aspects of your question independently, working in parallel (up to 6 at once) to dramatically speed up complex investigations.

`@deep-dive`first consults a specialized planning agent that reviews and improves the investigation strategy, suggesting which steps should run in parallel versus sequentially and ensuring the plan is realistic and executable. Each sub-agent receives clear, self-contained instructions and returns concise results that `@deep-dive` synthesizes into your final answer.

## When to Use `@deep-dive`

Use `@deep-dive` when you need:

* **Comprehensive analysis** across multiple data sources (internal docs + data warehouse + web).
* **Competitive intelligence** synthesizing internal strategy with external market data.
* **Regulatory or legal research** combining internal policies with up-to-date external sources.
* **Technical investigations** spanning code repositories, documentation, and database metrics.
* **Cross-system exploration** that requires querying databases, reading documents, and browsing the web.
* **Exhaustive document analysis** when you need insights from hundreds or thousands of files.

## What to Expect

When you ask a complex question, here's what happens:

1. **Planning phase** (30 seconds - 2 minutes): `@deep-dive` asks a private agent @dust-planning to create a research plan and consults the planning agent.
2. **Research phase** (5-20 minutes): `@deep-dive`spawns many private @dust-task sub-agents to gather information in parallel.
3. **Synthesis phase** (1-3 minutes): `@deep-dive` combines findings into a comprehensive answer.

You'll see real-time updates showing `@deep-dive`'s and its sub-agents reasoning and which sub-agents are working on what. For simple questions, Deep Dive works much faster, typically under a minute.

### Output Format

`@deep-dive` adapts its output to match your question:

* **Simple questions**: Concise, natural answers with proper citations
* **Complex investigations**: Comprehensive research reports with clear sections, headings, and narrative flow
* **Data analysis**: May include tables, charts, or interactive visualizations

All answers include citations to sources (your internal documents, web pages, or data queries) so you can verify the information.

### Permissions & Security

`@deep-dive` respects your workspace's access controls. It only accesses data you're authorized to see, operates under your identity when using tools with Personal authentication, and respects space-level and query-level permissions. Sub-agents inherit the same permissions, ensuring secure research across your organization.

It can be deactivated in the workspace by an admin as any other default agent.

### Limitations

* `@deep-dive` cannot access data from the Table Query tool, meaning it cannot query spreadsheet or Notion tables.
* `@deep-dive` cannot access data from Restricted Spaces.

***

**Updated** October 2025
