# Connect Microsoft

The Microsoft connection indexes selected SharePoint documents, spreadsheets, and presentations. Use an organizational Microsoft account; personal accounts are not supported.

## Authorize with an organization account

1. Open **Spaces > Connections > Microsoft** and start the connection.
2. Sign in and review the requested Microsoft permissions.
3. If your tenant requires administrator consent, submit the request. After the Entra administrator approves it, repeat the sign-in step to finish connecting.
4. Select the sites and files to synchronize.

Delegated authorization uses `Files.Read.All`, `Sites.Read.All`, `User.Read`, and `offline_access` to read files and sites, identify the user, and refresh access. Use the application identity and callback shown in your Counso setup; they belong to that deployment.

A dedicated integration account makes ongoing access easier to manage. Its direct and inherited group memberships determine the available SharePoint sites and Teams-backed files. Review public sites, private sites where the account is a member, and standard, shared, or private Teams channels it belongs to. Selecting content in Counso does not replace Microsoft permissions.

## Authorize with a service principal

If the connection offers service-principal authentication, create an Entra app registration, grant the appropriate Microsoft Graph **application** permissions, obtain administrator consent, and create a client secret. Enter its tenant ID, client ID, and secret value in Counso.

For access restricted to particular sites, use `Sites.Selected` and explicitly grant the application access to each selected site. Consent alone grants no site access. Enter the allowed site IDs in the connection when requested. Do not mix this app-only flow with the delegated permissions used for an interactive user. See [Microsoft's selected-permission model](https://learn.microsoft.com/en-us/graph/permissions-selected-overview) for the site assignment steps.

## Files and refresh behavior

Supported text-bearing documents include DOCX, PPTX, and TXT. Enable PDF indexing from the Microsoft connection's **Manage** settings when needed. XLSX workbooks are parsed into individual worksheets for table queries. Documents exceeding approximately 800 KB of extracted text are skipped.

The connection checks for changes about every five minutes. New, edited, or deleted files are reflected after synchronization, not immediately. Large batches can take longer. For a missing file, check account or application access, selected sites, supported format, and sync status.

SharePoint list custom columns are included as labels with synchronized files. They can support keyword filtering and [knowledge search](../../agents/knowledge/search-data-sources.md).
