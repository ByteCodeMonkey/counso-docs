# Computer

Computer gives an Agent a safe, temporary workspace where it can inspect files, run code, transform data, and return finished artifacts to the conversation. It is useful when a task needs exact calculations or a real output file; it is usually unnecessary for a short answer or simple summary. Files on the user's laptop are not available unless uploaded through an approved interface.

## File work

Computer can clean or calculate from Excel and CSV files, update existing workbooks, create or edit PowerPoint decks, update Word documents, extract text from PDFs, analyze images, process ZIP archives, and produce artifacts such as reports, charts, CSV exports, or converted files. For spreadsheets, describe which rows, columns, formulas, and formats must remain; ask it to check totals. For a deck, upload a template and specify which slides or sections to update. If a template matters, edit the original copy instead of rebuilding it. Review the final file before sending it outside the workspace.

Computer can also use code to compute an exact answer from every row in a large spreadsheet or structured file and return a concise result without returning the raw data. Keep intermediate work in the temporary workspace and explicitly request the final file or text you need.

## Network and secrets

Outbound internet access is restricted by a workspace allowlist. Administrators can approve exact domains or wildcard subdomains. If enabled, an Agent may request one-time access to a domain for the current Computer session; this does not change the workspace allowlist. A blocked-domain error is different from an external service's 401/403 response, which usually points to credentials or provider permissions.

Administrators can provide non-sensitive configuration values as environment variables. Credentials belong in HTTPS secrets, scoped to the domains that may receive them. Computer sees a placeholder rather than the raw secret; never paste API keys into a prompt or store credentials in ordinary variables. Configuration values are loaded when a Computer starts, so an existing session does not necessarily see later changes.

## Output and persistence

Computer's working area is temporary. Ask the Agent to attach the finished `.xlsx`, `.pptx`, PDF, or other artifact to the conversation, or save it to a connected location using the appropriate provider tool. A file left only in the temporary work area is not a shared persistent file. Open and inspect the returned artifact; confirm formulas, layout, page breaks, and important figures before relying on it.
