# Move Google Sheets work to Google Drive

The standalone Google Sheets tool described by this older setup is deprecated. Use the Google Drive tool for supported spreadsheet reading and editing instead. This page is retained only to help workspace owners recognize the older tool and move existing Agent configurations.

## Migration steps

1. In the Agent builder, remove the deprecated Google Sheets capability from Agents that use it.
2. Ask a workspace administrator to configure the native Google Drive tool using the current setup form.
3. Add Google Drive to the relevant Agent and connect the Google account that owns or can access the target spreadsheets.
4. Update the Agent instructions to name the spreadsheet, worksheet, and range and to read the data back after edits.
5. Test against one known spreadsheet, verify the returned values in Google Drive, then remove the old tool configuration if it is no longer used.

Keep the Google Drive Connection and live Drive Tool distinct: a Connection supports synchronized search; the Tool performs precise live file and spreadsheet operations. If the Drive tool is unavailable in the workspace, check its current enablement with an administrator before relying on the deprecated path.
