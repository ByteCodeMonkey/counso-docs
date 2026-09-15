> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Datasources

Dust's Data Sources provide a fully managed semantic search solution. A Data Source is a managed store of documents on which semantic searches can be performed. Documents can be ingested by API or uploaded manually from the Dust interface.

Once uploaded, documents are automatically chunked, embedded and indexed. Searches can be performed against the documents of a Data Source using the [Datasource block](/docs/developer-platform/legacy-dust-apps/blocks/core-blocks#datasource-block) which, given a query, automatically embeds it and performs a vector search operation to retrieve the most semantically relevant documents and associated chunks.

<Info>
  **What is semantic search?** Semantic search, generally based on embedding models, is important to large language model apps because of the limited context size of models. It enables the retrieval of chunks of valuable information that fit in context to perform a particular task. This is called *Retrieval-Augmented Generation (RAG)*.
</Info>

Data sources enable apps to perform semantic searches over large collections of documents, only retrieving the chunks of information that are the most relevant to the app's task, without having to manage the complexity of setting up a vector search database, chunking documents, embedding chunks, and finally performing vector search queries.

## Data Source creation

Creating a Data Source simply consists in providing a name and a description.

### Parameters

* `name`: string. The name of the new Data Source. It should be short and can only contain lowercase alphanumerical characters as well as `-`.
* `description`: optional string.

Data sources are created empty. Their description can be edited from the Settings panel. They cannot be renamed but they can be deleted from the same panel.

## Document insertion

Once a Data Source is created, documents can be inserted from the Dust interface or by API. When a document is inserted, the following happens automatically:

* **Chunking**: The document is pre-processed to remove repeated whitespaces (helps semantic search) and chunked using `max_chunk_size` tokens per chunk.
* **Embedding**: Each chunk is embedded (in parallel, with retries) using the embedding model `text-embedding-3-large` from OpenAI. Enterprise plan customers can ask for a different embedding model of their choice.
* **Indexing**: Each resulting embedding vector is inserted in a vector search database along with metadata about the document and the original chunk text.

The following parameters are accepted when inserting a document:

### Parameters

* `document_id`: string. A unique ID for the document. The semantics of the insertion really is an upsertion. Inserting with a `document_id` that does not exist will create that document; it will otherwise replace the previous document version (removing previous chunks from the vector search database and replacing by the updated document's).
* `text`: string.

See the [Upsert a document in a data source](/api-reference/datasources/upsert-a-document-in-a-data-source) API reference to learn how to insert documents by API. Data sources need to be created from the Dust interface.

### Uploading directories of files to your Data Source

We also have a script you can use to upload a directory's contents to your data source. Copy the following code into `upload.py` and then fill in the values for your Dust API key, the workspace ID you are in, and the data source you want to upload to. Then run `python upload.py <dir>`, where `dir` is the directory from which you want to upload the documents.

```python theme={null}
#!/usr/bin/env python
import requests
import pathlib
import pdftotext
import sys

# The three following variables need to be set with your own Dust API key (can be found in the interface),
# Workspace ID (can be found in the workspace URL) and Data Source ID:
DUST_API_KEY=""
DUST_WORKSPACE_ID=""
DUST_DATA_SOURCE_ID=""
ENDPOINT= f"https://dust.tt/api/v1/w/{DUST_WORKSPACE_ID}/data_sources/{DUST_DATA_SOURCE_ID}/documents/"

def upload(text, file):
    url = ENDPOINT + file.stem
    r = requests.post(url, headers={'Authorization': "Bearer " + DUST_API_KEY}, json={
        "text": text,
    })
    return r

directory = sys.argv[1]

# iterate through all files and upload text or pdf2text
for file in pathlib.Path(directory).rglob("*"):
    if file.is_file():
        if file.suffix == ".pdf":
            resp = upload("\n\n".join(pdftotext.PDF(file.open("rb"))) , file)
        elif file.suffix in [".txt", ".md"]:
            resp = upload(file.read_text(), file)
        else: continue
        if resp.status_code == 200:
            print("Uploaded", file)
        else:
            print("Error uploading", file)
            print(resp.text)
```

Example usage, once values are filled in: `python upload.py test_dir/`.

## Document deletion

When deleting a document, all associated chunks are automatically removed from the vector search database of the Data Source. Documents can be deleted from the Dust interface or by API.

<Note>
  Data sources can be deleted from the Dust interface. When deleted, all associated data (all documents and associated chunks) are deleted from our systems.
</Note>

See the [Delete a document from a data source](/api-reference/datasources/delete-a-document-from-a-data-source) API reference to learn how to delete documents by API.

## Querying a Data Source

Querying a Data Source is done using the [Datasource block](/docs/developer-platform/legacy-dust-apps/blocks/core-blocks#datasource-block). The `data_source` block returns a list of [Document](/api-reference/datasources/retrieve-a-document-from-a-data-source) objects. Each document may include one or more chunks (the chunks returned by the semantic search are aggregated per document). See [Chunks and Documents](/docs/developer-platform/core-concepts/chunks-and-documents) for more details.

When a query is run the following happens automatically:

* **Embedding**: The query is embedded using the embedding model set on the Data Source.
* **Search**: A vector search query is run against the embedding vectors of the Data Source's documents' chunks.
* **Union**: Most relevant chunks' documents are retrieved and chunks are associated to their original document object.
