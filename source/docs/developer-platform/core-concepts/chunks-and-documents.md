> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Chunks and Documents

## Documents

The document is the unit of ingestion in a Data Source. Documents can be inserted from the Dust interface or by API, and are identified by a unique `document_id`. Insertion is an upsertion: inserting with an existing `document_id` replaces the previous version of the document.

When a document is inserted, it is automatically pre-processed and prepared for semantic search. See [Datasources](/docs/developer-platform/core-concepts/datasources) for the full insertion lifecycle.

## Chunks

Documents are too large to fit in a language model's context window as-is, so Dust splits them into **chunks**:

* Each document is pre-processed (repeated whitespace removed) and split into chunks of at most `max_chunk_size` tokens.
* Each chunk is embedded using the embedding model set on the Data Source (`text-embedding-3-large` from OpenAI by default; Enterprise plan customers can request a different embedding model).
* Each embedding vector is indexed in a vector search database along with metadata about the document and the original chunk text.

## How chunks are retrieved

When a semantic search query runs against a Data Source:

1. The query is embedded using the same embedding model as the Data Source.
2. A vector search retrieves the most semantically relevant chunks.
3. Chunks are aggregated per document: the search returns a list of document objects, each including only the chunks that matched the search.
4. Documents are sorted by decreasing order of the maximum score of their retrieved chunks.

This structure enables Retrieval-Augmented Generation (RAG): only the most relevant chunks of information are placed into the model's context to perform a task, instead of entire documents.

## Related

* [Datasources](/docs/developer-platform/core-concepts/datasources)
* [Search the data source](/api-reference/datasources/search-the-data-source) API reference
* [Retrieve a document from a data source](/api-reference/datasources/retrieve-a-document-from-a-data-source) API reference
