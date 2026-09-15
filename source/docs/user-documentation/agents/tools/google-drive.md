> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Google Drive

## Overview

Search, read, create, clone, edit and comment on files in Google Drive (Docs, Sheets, Presentations).

<Info>
  **This tool uses personal credentials.** This tool interacts with Google Drive
  using the user's account: it adapts to each user.
</Info>

## Admin: Setup in Dust

Go to **Spaces > Tools** in your Dust workspace, click `Add Tools`, and select Google Drive. Fill in your Client ID & Secret.

You will then be redirected to an oAuth flow to connect an admin Google Drive Account. This account only be used during the set up and users won't be able to query Google Drive from this account.

By default this tool is added to the Company data Space, so accessible in all the workspace.

## Usage

Once the tool has been configured by the admin as described before, it can be selected on any agent: in the Agent Builder, simply click on `Add Tool` and select Google Drive.

When users use an agent with the Google Drive tool for the first time, they will get a notification to click on the `Connect` button to connect their own Google Drive credentials.

<Note>If you see an "Insufficient permissions" error when using write actions, go to Settings > Connections, disconnect Google Drive, and reconnect to grant write access.</Note>

## Available Tools

### Reading and search

| Tool                                | Description                                                                                                                                                                                                                                                           |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| List Drives                         | List all shared drives accessible by the user.                                                                                                                                                                                                                        |
| Search Files                        | Search for files in Google Drive. Can search in personal drive, all shared drives, or a specific drive.                                                                                                                                                               |
| Get File Content                    | Get the content of a Google Drive file as plain text with offset-based pagination. Supported mimeTypes: application/vnd.google-apps.document, application/vnd.google-apps.presentation, application/vnd.google-apps.spreadsheet, text/plain, text/markdown, text/csv. |
| Get Document Structure (Docs)       | Get the full structure of a Google Docs document (text, tables, formatting, indices). Use this when you need indices for updates or are working with tables.                                                                                                          |
| Get Presentation Structure (Slides) | Get the full structure of a Google Slides presentation (slides, elements, text content, object IDs). Use this when you need object IDs for updates.                                                                                                                   |
| Get Spreadsheet                     | Get metadata/properties of a Google Sheets spreadsheet (sheet names, IDs, row/column counts).                                                                                                                                                                         |
| Get Worksheet                       | Get cell values from a specific range in a Google Sheets spreadsheet.                                                                                                                                                                                                 |
| List Comments                       | List comments on a Google Drive file (Doc, Sheet, or Presentation).                                                                                                                                                                                                   |

### Create and copy

| Tool                         | Description                                                                              |
| ---------------------------- | ---------------------------------------------------------------------------------------- |
| Create Document (Docs)       | Create a new Google Docs document in the user's Drive.                                   |
| Create Spreadsheet (Sheets)  | Create a new Google Sheets spreadsheet in the user's Drive.                              |
| Create Presentation (Slides) | Create a new Google Slides presentation in the user's Drive.                             |
| Copy File                    | Copy an existing Drive file (Doc, Sheet, or Presentation) to the same or another folder. |
| Create Comment               | Add a comment to a Google Drive file (Doc, Sheet, or Presentation).                      |
| Create Reply                 | Reply to an existing comment on a Google Drive file.                                     |

### Edit and update

| Tool                           | Description                                                                                                                                                                                                |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Update Document (Docs)         | Update an existing Google Docs document (insert/delete text, work with tables, apply formatting). Tip: Call Get Document Structure first to get indices and endIndex.                                      |
| Append to Spreadsheet (Sheets) | Append rows of data to a Google Sheets spreadsheet.                                                                                                                                                        |
| Update Spreadsheet (Sheets)    | Batch update a Google Sheets spreadsheet (insert/delete/move rows/columns, merge cells, formatting, sorting, validation, filters, find/replace, etc.). Tip: Call Get Worksheet first to understand layout. |
| Update Presentation (Slides)   | Batch update an existing Google Slides presentation (create slides, insert/delete objects, replace text, update styles, tables, etc.). Tip: Call Get Presentation Structure first to get object IDs.       |

## Limitations

* The tool does not perform semantic search on your document content. If your use case requires searching through your Google Drives based on the context of your message, it is strongly recommended to use the [Google Drive Connection](/docs/user-documentation/admins/connections-management/google-drive) with our [RAG capability](/docs/user-documentation/agents/knowledge/search-data-sources).
* Maximum original file size supported: 64 MB.
* The Get File Content tool returns up to 32,000 characters per call; use offset and limit to paginate larger files.
