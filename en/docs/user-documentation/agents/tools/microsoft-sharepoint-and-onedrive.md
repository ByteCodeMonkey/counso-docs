# Microsoft SharePoint and OneDrive tools

The SharePoint and OneDrive tool lets an Agent find and read sites, drives, folders, and files that the acting Microsoft user can access. Depending on configuration, it may also upload or update files. It is a live tool and is separate from a synchronized Microsoft Connection.

A Microsoft Entra administrator and workspace administrator add the tool under **Spaces → Tools** and grant the delegated scopes required by the current form. The documented permissions include `User.Read`, `Files.ReadWrite.All`, `Sites.Read.All`, `ExternalItem.Read.All`, and `offline_access`; use the current consent screen as the source of truth. The acting user completes sign-in and must already have access to the intended site or drive.

Add the tool to an Agent and start with a known site, library, and file. Before an upload or update, read the destination and confirm the target path. Verify the same file ID and content after the write. If a file is missing, check group-based site membership as well as direct permission; if it is visible in a Connection but not in the Tool, compare the service account and acting user's access.

## Available operations and limits

The tool list includes **Search In Files**, **Search Drive Items**, **Get File Content**, **Update Word Document**, and **Upload File**. Search returns files visible to the user's Microsoft identity; reading and uploading require access to the particular site, drive, or folder. The tool focuses on files and does not replace a SharePoint Connection for synchronized retrieval.

`Files.ReadWrite.All`, `Sites.Read.All`, `ExternalItem.Read.All`, `User.Read`, and `offline_access` are the recorded delegated scopes, subject to the current admin consent form. A user's group-based SharePoint membership can affect visibility as well as direct site permissions. For external data sets, the user and tenant must support the required permission.
