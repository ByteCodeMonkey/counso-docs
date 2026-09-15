---
title: "Why language models can miss exact counts and structured data"
---
Language models generate likely text; they are not inherently exact counters or spreadsheet engines. They can produce a plausible answer while missing a word occurrence, row, or relationship in a long structured file. Treat exact totals and record-level conclusions as calculations to verify.

## Counting words in a document

A request such as “How many times does this phrase appear across all files?” requires scanning the complete set and counting exact matches. A model may only see part of a long source at once, and the text it receives may be split into passages. Ask it to identify the source and scope; use a deterministic text-search or counting function for an exact count when one is available.

## Questions about CSV and tables

Rows and columns encode relationships that can be lost when a table is converted into text passages. Semantic search is useful for finding relevant passages, but it may return only the most relevant-looking rows rather than every record. This makes it a poor fit for exact counts, sums, averages, filters, and comparisons over a complete dataset.

For structured analysis, use **Query Tables** when the Agent Builder offers it. It can query supported tables with SQL before composing an answer. Select the correct table and state the date range, filters, and calculation needed. Review the returned rows or totals against the source, especially if duplicate, blank, or differently formatted values matter. See [Table queries](/docs/user-documentation/agents/knowledge/table-queries).

Use search for questions about meaning or context in unstructured documents; use table queries for calculations across structured rows. If the required query capability is unavailable, export or prepare a verifiable table and calculate the result with an appropriate spreadsheet or database tool rather than relying on a fluent guess.
