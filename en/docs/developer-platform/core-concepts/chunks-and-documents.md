# Chunks and documents

A document is the unit of content stored in a data source. It has a unique `document_id` and may be added through the Counso interface or API. When a document is inserted or updated, Counso prepares it for search and divides its text into chunks so that relevant passages can be retrieved without sending the entire document to a model.

Counso removes repeated whitespace, then splits a document into chunks of at most the configured `max_chunk_size` tokens. Each chunk is embedded using the model configured for its data source (`text-embedding-3-large` by default) and indexed with document metadata and the original chunk text. Keep related information together and use clear headings so retrieved passages retain their context.

For a semantic search, Counso embeds the query using the data source’s embedding model, retrieves the most relevant chunks, and groups matching chunks by original document. A returned document can contain only the passages that matched, rather than its full text. Results are ordered by each document’s highest-scoring retrieved chunk.

This structure supports retrieval-augmented generation (RAG): an Agent uses selected passages from a larger collection to answer a request. For document insertion, replacement, and deletion behavior, see [Data sources](datasources.md).
