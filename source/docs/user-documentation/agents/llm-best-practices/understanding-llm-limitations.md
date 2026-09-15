> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Understanding LLM Limitations: Counting and Parsing Structured Data

As a Dust user, you may have encountered situations where a Large Language Model (LLM), struggles with tasks that seem simple to humans. Two everyday situations you share with our team are:

1. Counting word occurrences in a document
2. Parsing a CSV or structured data file and answering specific questions about its content

Let's explore why LLMs face challenges with these tasks and how Dust's features can help you overcome these limitations.

## How LLMs Work: The "Stochastic Parrot" Dilemma

LLMs are sophisticated pattern recognition systems trained on vast amounts of text data. They operate by predicting the most likely next word in a sequence, based on patterns learned from their training data. This approach has led to remarkable capabilities in natural language processing, but it also results in some limitations.

Researcher Emily Bender coined the term "[stochastic parrots](https://en.wikipedia.org/wiki/Stochastic_parrot)" to describe LLMs, highlighting that while they can generate convincing language, they don't truly understand the meaning behind the words they produce.

The word "stochastic" derives from the ancient Greek word "stokhastikos" meaning "based on guesswork", or "randomly determined". The word "parrot" refers to the idea that LLMs merely repeat words without understanding their meaning.

This characteristic becomes particularly evident when LLMs encounter tasks requiring precise counting or structured data interpretation.

## Why LLMs Struggle with Counting and Parsing

### Counting Word Occurrences

When you ask an LLM to count how many times a word appears in a document, you're asking it to perform a task it wasn't specifically designed for. LLMs process text as a continuous stream of tokens, focusing on generating coherent responses rather than performing exact calculations. They lack the built-in ability to keep an accurate count of specific words or phrases.

Moreover, LLMs have a limited "context window" - the amount of text they can process at once. For longer documents, the model might not "see" the entire text simultaneously, making accurate counting across the whole document challenging.

### Parsing CSV Files and Answering Specific Questions

LLMs face several challenges when dealing with CSV files and structured data:

* **Sequential Processing**: LLMs are designed to process information sequentially, one token at a time. This works well for natural language but becomes problematic when dealing with multidimensional data structures like CSV files.

* **Lack of Spatial Understanding**: CSV files organize information in rows and columns, creating relationships between data points. LLMs, trained primarily on linear text, lack the inherent ability to understand these spatial relationships.

* **Training Data Bias**: This limitation extends to structured data like CSV files. LLMs are typically trained on unstructured internet data, which lacks well-labeled and structured content. This results in models that can mimic language about data but struggle with actual data interpretation and manipulation.

## Tools and Techniques for Overcoming LLM Limitations

### Table Query Overview in Dust

Table Query is a tool in Dust that addresses many of the limitations LLMs face when dealing with structured data. Here's how it works:

* **SQL Generation and Execution**: Table Query enables agents to generate and execute SQL queries on structured data before formulating a response. This capability extends to various data sources, including CSV files, Notion Databases, and Google Sheets.

* **Complement to Search Data Source**: While the Search Data Source action is excellent for retrieving relevant information, it often falls short on quantitative questions. This is because semantic search presents chunks of data ordered by relevance, making it difficult for the agent to answer numerical queries accurately. Table Query fills this gap by allowing agents to perform precise analytical operations on entire datasets.

* **Analytical Capabilities**: Because it uses SQL, Table Query lets agents answer complex analytical questions that require calculations, aggregations, and data manipulations across entire datasets.

[You can visit this page](/docs/user-documentation/getting-started/faq/troubleshooting-and-limitations/i-try-to-create-an-agent-using-the-table-query-tool-but-it-doesnt-work) if you're experiencing issues with the Table Query tool.

By following these guidelines and understanding how Table Query works, you can use this tool to overcome LLM limitations in handling structured data, enabling your agents to perform complex analytical tasks with precision.
