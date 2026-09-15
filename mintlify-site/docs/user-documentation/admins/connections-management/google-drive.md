---
title: "Connect Google Drive"
---
Use a Google Workspace account whose access can be managed consistently, such as a dedicated integration account. Counso can only synchronize files that this account can access. A departing employee or a permission change can interrupt synchronization, so assign an owner for the connection.

## Set up the connection

1. Open **Spaces > Connections** and select Google Drive.
2. Sign in with the designated Google account and review the requested access.
3. Choose the drives, folders, or files to synchronize and save the selection.
4. In the connection settings, enable PDF text indexing if you need searchable PDF documents.

The connected account needs the document permissions and download access required by the connector. If a file is missing from the selection tree, open its Drive sharing settings and check whether downloading, printing, or copying is disabled. Restore only the access appropriate for the files you intend to share.

## Supported content and limits

The connection can index Google Docs, Slides, DOCX, PPTX, TXT, Markdown, and PDFs containing text. Documents exceeding 2 MB of extracted text are skipped. Google spreadsheets and PDFs have a 128 MB file-size limit. Each worksheet in a Google spreadsheet can contain up to 50,000 rows for synchronization; worksheets are processed separately.

Convert native Excel workbooks to Google Sheets before using them through this connection's table queries. Google Drive can automatically convert uploaded Office files when that option is enabled in Drive settings.

Scanned, image-only documents do not provide text for this connection to index. For those PDFs, upload the file directly to a conversation and use document-reading capabilities appropriate to the file. Check the extracted result before relying on it.

## Updates and missing files

Routine additions, changes, and deletions can take a few minutes to reach Counso. The first synchronization of a large Drive can take more than a day; very large collections may take several days. Start with the folders your team needs, particularly when the account can access tens of thousands of files.

For missing content, check the connected account, selected scope, download restrictions, file format, size, and synchronization status. A file's presence in Drive alone does not mean its text has finished indexing.

## Filter by Drive labels

Drive labels become document tags that agents can use for filtering. If labels are absent, review the connection's label permissions and reconnect when additional consent is required. Updating a document causes it to be synchronized again with its current labels.
