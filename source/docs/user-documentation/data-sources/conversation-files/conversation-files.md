> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Conversation Files

## Overview

You can attach files directly to a conversation to give agents ad-hoc context without setting up a data source. Agents can read the content, answer questions about it, extract information, run analysis on tabular data, and generate new files from it.

Conversation files are scoped to the conversation: they are not indexed in your workspace data sources and are only available where you uploaded them.

## Supported files and size limits

| File type       | Examples                | Limit |
| --------------- | ----------------------- | ----- |
| Images          | .jpg, .png, .gif, .webp | 5 MB  |
| Audio files     | .mp3, .wav, .m4a        | 25 MB |
| Data files      | .txt, .pdf, .doc, .json | 50 MB |
| Code files      | .py, .js, .ts, etc.     | 50 MB |
| Delimited files | .csv, .tsv, .xls, .xlsx | 50 MB |

## Working with conversation files

* **Documents** (PDF, Word, text): agents extract and use the text content to answer questions or produce summaries.
* **Tabular files** (CSV, Excel): agents can query and analyze the data, compute aggregates, and produce charts or reports.
* **Images**: agents can view and analyze images in conversations.
* **Audio and video files**: automatically transcribed so agents can work with the transcript.

## Generating files

Agents can also produce new files in a conversation (PDF, Word, Excel, CSV, and more) using the [File Generation tool](/docs/user-documentation/agents/tools/file-generation).
