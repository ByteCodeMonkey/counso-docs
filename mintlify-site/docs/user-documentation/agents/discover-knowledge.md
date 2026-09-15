---
title: "Add Discover Knowledge to an Agent"
---
**Discover Knowledge** lets an Agent search connected company documents and, where configured, explore structured data sources without requiring you to add a separate search tool for every source. A default workspace Agent may already include it.

## Add the capability

In Agent Builder, open a custom Agent, select **Discover Knowledge** from **Capabilities**, and save. The Agent can use only the sources available to it through the relevant Spaces and permissions.

## What it can do

Depending on the connected sources and workspace configuration, Discover Knowledge can:

- search documents by meaning across connected sources;
- browse a source hierarchy to find folders, pages, schemas, or tables;
- open and read a known document or page;
- inspect warehouse databases, schemas, tables, columns, types, or sample values; and
- query known warehouse tables to calculate counts, trends, rankings, or joins.

For document questions, the Agent can start with semantic search and then browse or read a complete source when more context is needed. For data questions, it can combine a query result with related business definitions in documents. Results depend on the source connector and access actually provided.

## When to use it

Add Discover Knowledge to a general-purpose Agent that needs to find information across several connected sources, locate a document whose exact path is unknown, or combine written context with structured analysis. It is for finding and analyzing information, not writing to third-party applications. Use [Discover Tools](/docs/user-documentation/agents/discover-tools) when the Agent needs to take actions in those applications.
