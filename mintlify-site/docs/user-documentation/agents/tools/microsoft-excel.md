---
title: "Microsoft Excel"
---
The Excel tool lets an Agent work with Excel workbooks stored in Microsoft 365 locations available to the acting user. It can inspect workbooks and worksheets, read ranges, and update supported cell ranges. This is a live tool, not a file-sync Connection.

A Microsoft Entra administrator and workspace administrator add Excel under **Spaces → Tools** and approve delegated permissions shown by the current setup form. The recorded scopes include `User.Read`, `Files.ReadWrite.All`, `Sites.Read.All`, and `offline_access`. The user who will perform the work signs in with their own Microsoft identity and needs permission to the target workbook.

For a query, identify the workbook, worksheet, and exact range. Ask the Agent to inspect the sheet before writing and to preserve formulas and formats outside the requested cells. After an update, reopen the same workbook and range and check values, formulas, and the workbook identity. If Excel cannot find or update a workbook, check whether it is in an accessible OneDrive or SharePoint location and whether the user's Microsoft permissions allow the operation.

## Available operations

The tool list includes **List Excel Files** (`.xlsx` and `.xlsm`), **Get Worksheets**, **Read Worksheet**, **Write Worksheet**, **Create Worksheet**, and **Clear Range**. Files are read from SharePoint or OneDrive locations the acting user can access. A write requires Microsoft file-edit permission in addition to successful tool setup.

Use **Get Worksheets** before specifying a sheet, then read the exact range before writing. If the workbook or range is missing, check whether the file is stored in the user's accessible SharePoint or OneDrive, and whether the user has edit permission. The delegated scopes recorded for setup include `User.Read`, `Files.ReadWrite.All`, `Sites.Read.All`, and `offline_access`; confirm them in the current consent form.
