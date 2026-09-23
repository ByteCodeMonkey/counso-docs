# Knowledge for Agents

Knowledge settings determine what material an Agent can use and how it retrieves that material. Choose the method that fits the question; availability and source types depend on the workspace configuration.

| Method | Use it for | What it does |
|---|---|---|
| **Search** | Finding relevant passages across connected sources | Searches selected content by meaning and returns relevant passages for the response. It is the usual starting point for questions about policies, topics, or context. |
| **Include Data** | Supplying recent source material on every run | Adds the newest available documents first until its context limit is reached. It does not rank documents by relevance to the current question. |
| **Query Tables** | Counts, totals, filters, comparisons, and other structured analysis | Queries selected structured tables, where available, before the Agent explains the result. |
| **Extract Data** | Collecting specific fields across documents | Searches selected sources and extracts information into a defined or generated schema. |
| **Find in data sources** | Browsing connected data by folder, path, or document title | Lists folders, opens a document by path, locates a document by title, and reports its place in the hierarchy. It complements semantic search when source structure matters. |

In Agent Builder, select the required data sources and explain their contents so the Agent can choose the appropriate action. Search and Include Data work with selected documents; Query Tables is for structured rows; Extract Data is for fields that need to be gathered consistently across sources.

For exact procedures, see [Search data sources](search-data-sources.md), [Include Data](include-data.md), [Table queries](table-queries.md), and [Extract data](extract-data.md). Find in data sources is available with supported Search configurations and does not require a separate source selection.
