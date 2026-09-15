> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Discover Knowledge

> Give agents access to company documents and data warehouse analysis.

Discover Knowledge lets your agent search and analyze the company documents and data warehouse tables available to it. The agent can move from broad discovery to source reading or SQL analysis without requiring you to configure each source as a separate tool.

<Info>
  The `@dust` agent includes Discover Knowledge by default.
</Info>

## How to add it

In the Agent Builder, open your custom agent and select **Discover Knowledge** from the **Capabilities** section. Then save the agent.

## What it does

When Discover Knowledge is enabled, your agent gains access to:

| Capability            | Description                                                                                                           |
| :-------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| Semantic search       | Finds relevant content across connected company data, even when the source uses different wording from your question. |
| Browse and find       | Explores source hierarchies and locates folders, documents, pages, schemas, and tables by name.                       |
| Source reading        | Reads the contents of a known document or page and identifies its location in the source hierarchy.                   |
| Warehouse exploration | Lists databases, schemas, and tables, then inspects columns, types, and sample values.                                |
| SQL analysis          | Queries known warehouse tables to calculate counts, trends, rankings, joins, and other structured results.            |

The agent usually starts with semantic search for document-based questions. It can switch to browsing when it needs to understand a folder or inspect a complete collection.

For warehouse questions, the agent can combine SQL results with company documents. This helps it find metric definitions, table documentation, or other business context before interpreting the data.

## When to use it

Add Discover Knowledge when your agent needs to:

* Answer questions from company documents across multiple connected sources.
* Explore a known folder, document collection, or data source hierarchy.
* Find and read a document when you do not know its exact title or location.
* Discover warehouse tables and query them with SQL.
* Combine qualitative context from documents with quantitative warehouse data.

Discover Knowledge follows the user's permissions and the spaces available to the agent. It does not provide write actions in third-party applications. For those tasks, use [Discover Tools](/docs/user-documentation/agents/discover-tools).
