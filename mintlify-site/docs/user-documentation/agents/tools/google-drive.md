---
title: "Google Drive"
---
The Google Drive tool performs live operations on files that the acting user can access. It is a personal-credential tool: a workspace administrator completes app setup, then each user connects their own Google account. It is distinct from a Drive Connection, which synchronizes selected files for search, and from the deprecated standalone Sheets tool.

An administrator opens **Spaces → Tools → Add Tools → Google Drive**, enters the client ID and secret requested by the form, and completes initial OAuth. Add the tool to the Agent; the first user then selects **Connect** to authorize their Google account. If write actions return an insufficient-permissions error, reconnect Google Drive and grant the requested write access.

## Available operations

- **List Drives** and **Search Files** locate personal-drive or Shared Drive content.
- **Get File Content** reads supported Docs, Sheets, Slides, text, Markdown, and CSV content. Large responses use offset/limit pagination.
- **Get Document Structure**, **Get Spreadsheet**, **Get Worksheet**, and **Get Presentation Structure** inspect document elements, spreadsheet properties/cell ranges, or slide objects before editing.
- **List Comments**, **Create Comment**, and **Create Reply** handle file comments.
- **Create Document**, **Create Spreadsheet**, **Create Presentation**, and **Copy File** create or duplicate files.
- **Update Document**, **Append to Spreadsheet**, **Update Spreadsheet**, and **Update Presentation** perform edits. Read the current structure first so indices, ranges, and object IDs are correct.

The tool does not provide semantic search over all Drive content. Use a Drive Connection for indexed retrieval. The source documentation sets an original-file limit of 64 MB and a 32,000-character content response per call; use pagination for larger text and check the current form for updated limits. After an edit, reopen the same file and range in Drive.
