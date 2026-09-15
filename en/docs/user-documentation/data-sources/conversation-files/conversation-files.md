# Conversation files

Attach files to a conversation when an Agent needs temporary context for a task. The Agent can read supported documents, analyze tables, inspect images where the selected model supports vision, transcribe audio/video, or use the material to create a new artifact. Conversation attachments are scoped to that conversation; they are not added to workspace search or automatically available in other conversations.

Typical limits documented for the upload flow are 5 MB for images, 25 MB for audio, 50 MB for documents and code, and 50 MB for delimited files such as CSV, TSV, XLS, and XLSX. Supported types and limits can vary by workspace and are shown by the attachment control.

For a useful result, state what to inspect, the relevant pages/sheets/date range, the fields or calculation rules, and the output format. For example, ask the Agent to compare two policies and list changed clauses with page and section, or to total a named worksheet while retaining the original currency and showing excluded rows.

Check the response against the uploaded source before sharing. To reuse material later, save it in a suitable shared location with the right access boundary. Generating a file in the conversation does not itself save it to a shared Folder or provider drive.
