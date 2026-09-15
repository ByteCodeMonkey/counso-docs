# Data sources

A data source is a managed collection of documents that Counso indexes for semantic search. Create one in the Counso interface by providing a short name and an optional description. The name can contain lowercase letters, numbers, and hyphens; a new data source starts empty. You can edit its description or delete it in Settings, but you cannot rename it.

Add documents through the interface or API. During ingestion, Counso removes repeated whitespace, splits the text into chunks using the configured `max_chunk_size`, embeds the chunks, and indexes their vectors with the document metadata and original text. The default embedding model is `text-embedding-3-large`; a different model can be used where the workspace supports it.

Use a stable `document_id` when inserting or updating a document. With `baseUrl` set to `https://app.counso.ai`, an upsert uses `POST {baseUrl}/api/v1/w/{wId}/spaces/{spaceId}/data_sources/{dsId}/documents/{documentId}` with a JSON body containing `text`. A new ID creates a document; an existing ID replaces its previous version and indexed chunks. Searching uses `GET {baseUrl}/api/v1/w/{wId}/spaces/{spaceId}/data_sources/{dsId}/search`. Deleting a document removes its associated chunks; deleting the data source removes all documents and chunks in it. Confirm the target before either delete operation.

For a directory import, a script can read PDF, TXT, and Markdown files and upsert each document. This example uses Python, `requests`, and `pdftotext`; provide workspace, Space, data source, and credential values through environment variables. It derives each document ID from the file’s relative path, so files in different folders keep separate identities.

```python
import os
import pathlib
import sys
from urllib.parse import quote
import requests
import pdftotext

base_url = os.getenv("COUNSO_BASE_URL", "https://app.counso.ai")
workspace_id = os.environ["COUNSO_WORKSPACE_ID"]
space_id = os.environ["COUNSO_SPACE_ID"]
data_source_id = os.environ["COUNSO_DATA_SOURCE_ID"]
api_key = os.environ["COUNSO_API_KEY"]

def upload(text, file):
    document_id = file.relative_to(directory).as_posix()
    url = (f"{base_url}/api/v1/w/{workspace_id}/spaces/{space_id}"
           f"/data_sources/{data_source_id}/documents/{quote(document_id, safe='')}")
    return requests.post(
        url,
        headers={"Authorization": f"Bearer {api_key}"},
        json={"text": text},
    )

directory = pathlib.Path(sys.argv[1])
for file in directory.rglob("*"):
    if not file.is_file():
        continue
    if file.suffix.lower() == ".pdf":
        with file.open("rb") as source:
            text = "\n\n".join(pdftotext.PDF(source))
    elif file.suffix.lower() in {".txt", ".md"}:
        text = file.read_text()
    else:
        continue
    response = upload(text, file)
    if response.status_code != 200:
        print("Import failed:", file, response.status_code, response.text)
    else:
        print("Imported:", file)
```

Save the script as `upload.py`, install `requests` and `pdftotext`, set the environment variables above, then run `python upload.py <directory-to-import>`.

Check the response for each file and review the indexed content in Counso. Use `https://app.counso.ai` as the default `baseUrl`, or substitute your environment’s base URL.

When an Agent searches a data source, Counso embeds the query and retrieves relevant chunks. Results are grouped by original document, so an Agent can use relevant passages without loading every full document into context. This retrieval pattern is called retrieval-augmented generation (RAG). For chunking and result ordering, see [Chunks and documents](chunks-and-documents.md).
