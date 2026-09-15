---
title: "Understand retrieval-augmented answers"
---
Retrieval-augmented generation (RAG) combines a language model with selected data sources. When an Agent receives a question, it searches those sources for relevant passages, provides the retrieved material and its instructions to the model, then drafts an answer grounded in that context. The model does not need to have memorized the source material.

## What search is good at

Semantic search looks for meaning and context, not only exact words. Like a researcher locating the most useful files, it can find related information across a large collection and summarize it in natural language. It is useful for questions about a policy, topic, or explanation when the relevant answer is contained in a limited set of passages.

## What search does not guarantee

Retrieval is selective: it returns material judged relevant to the question, not every document or every occurrence. Search is therefore a poor way to answer “How many files mention this topic?” or to calculate a complete total. A fluent answer can still be incomplete if a relevant passage was not retrieved. Ask for supporting sources and check them, especially when the answer needs full coverage.

## Choose a method for the question

- Use **Search** when the Agent should find relevant passages across connected sources.
- Use **Include Data** when it should receive the newest material first until the available context is filled; this does not rank documents by relevance to each question.
- Use **Query Tables** for exact calculations across structured rows, such as counts, totals, or comparisons.
- Use **Extract Data** when you need specified fields collected from a larger set of documents according to a schema.

A clear, specific question helps search find the right material. Keep the Agent's source scope focused, ask it to cite sources, and verify totals with a structured query rather than estimating from retrieved passages. See [Search data sources](/docs/user-documentation/agents/knowledge/search-data-sources) and [Knowledge methods](/docs/user-documentation/agents/knowledge).
