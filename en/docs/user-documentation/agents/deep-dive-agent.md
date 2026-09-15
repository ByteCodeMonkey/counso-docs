# Deep Dive Agent

If your Counso workspace includes a **Deep Dive** Agent (it may be called `@deep-dive`), use it for questions that need a broad investigation across several available sources. It can spend longer on planning, research, and synthesis than a quick-answer Agent. Availability and the exact sources depend on workspace configuration.

To use it, select or mention the Deep Dive Agent in a conversation and state the question, the period or entities to cover, and the evidence you need in the answer. For a simple lookup, use an ordinary Agent with a focused search instead.

## How it investigates

For a straightforward question, Deep Dive may answer directly. For a more involved task, the workflow can include:

1. Planning the investigation and identifying distinct research questions.
2. Delegating parts of the work to specialist agents, such as document search, web research, or database analysis.
3. Running independent research tasks in parallel, with up to six sub-agent tasks at once.
4. Combining results into a structured response with citations.

Long investigations can take several minutes. Follow the visible progress and review sources, coverage, and assumptions before relying on the synthesis.

## Sources and capabilities

Depending on what is connected and enabled for the Agent, a Deep Dive workflow may use:

- **Knowledge search and browsing:** search relevant passages, navigate a source hierarchy, and read full documents in sections.
- **Data warehouses:** inspect available schemas and query supported databases such as Snowflake or BigQuery.
- **Web search and browsing:** find current public information and inspect relevant pages.
- **Discoverable tools:** use a workspace tool when the task needs a supported integration and the required access is configured.
- **Frames:** create a chart or interactive view when that makes the findings easier to understand.
- **Sub-agents:** divide a complex investigation into independent parts, then synthesize the results.

These capabilities are not automatic guarantees. A connection must be available, the Agent must have the required access, and the relevant tool must be enabled. Ask for citations and the source coverage when completeness matters.

## Permissions and limitations

The default Deep Dive Agent uses Knowledge and Tools from **Company Data**, subject to the current user's permissions. It cannot access **Restricted Spaces** or the separate **Table Query** action used for spreadsheet and Notion tables. Its data warehouse queries are a different capability. Tools with Personal authentication use the current user's connected account, and sub-agents inherit the same access limits. Workspace administrators can disable the default Deep Dive Agent.

Use Deep Dive for research and synthesis. Review its conclusions against source records before making a decision or updating another system.
