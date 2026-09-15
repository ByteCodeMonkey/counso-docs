---
title: "Search connected data sources"
---
The Search capability finds passages in the data sources selected for an Agent and supplies relevant material to its response. It uses meaning and context, not only exact keyword matches. The Agent can search only sources and locations that have been made available to it.

## Choose what the Agent can search

In Agent Builder, select the relevant connected sources, folders, websites, channels, or other locations offered by the workspace. Narrow the selection to the task. A focused source set makes results easier to interpret and can reduce unrelated matches. The underlying source must be connected and available in an appropriate Space.

## Filter by labels

Where a source supports labels, use them to narrow the searchable documents. A must-have rule includes a document only when it has at least one required label. A must-not-have rule excludes a document if it has any excluded label. If in-conversation label filtering is available, the Agent can use exact label values from the request; spell the label exactly as it is stored.

## What semantic search does

For a question such as “What should I prepare for parental leave?”, semantic search can find passages about leave policy even when those passages do not use the exact wording of the question. The Agent then uses the retrieved passages with the question to draft a response and link back to sources when available. Search returns relevant material; it does not guarantee that every matching file or row was examined.

## Advanced search

If the Agent Builder offers **Advanced settings** for Search, enabling the advanced mode may allow the Agent to browse folders and read files by path as well as search passages. This can help when folder structure is meaningful or the Agent needs a complete file. It may require additional tool calls and take longer.

Use Search for questions about meaning, policy, or context in connected documents. For exact totals or calculations across structured rows, use [Table queries](/docs/user-documentation/agents/knowledge/table-queries).
