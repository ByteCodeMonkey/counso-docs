> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# [Deprecated] Google Sheets

## Overview

<Warning>
  **Deprecated - Use the Google Drive tool for Google Sheets workflows**.
</Warning>

The Google Sheets tool is deprecated. Migrate to the Google Drive tool, which supports reading and editing Google Sheets via tools like Get Spreadsheet, Get Worksheet, Append to Spreadsheet, and Update Spreadsheet.

<Info>This tool uses personal credentials.</Info>
This tool interacts with Google Sheets using the user accounts: it adapts to
each user.

**Migrate to the Google Drive tool**: /docs/user-documentation/admins/connections-management/google-drive
Common replacements:

* **List Spreadsheets** Use Google Drive: Search Files (filter to spreadsheets) or Get Spreadsheet when you know the ID.
* **Get Spreadsheet / Get Worksheet** Use Google Drive: Get Spreadsheet / Get Worksheet.
* **Append Data / Update Cells / Format Cells / Clear Range / Copy Sheet / Add/Delete/Rename/Move Worksheet** Use Google Drive: Append to Spreadsheet / Update Spreadsheet.

## Admin: Setup in Google Cloud

A Google Workspace account is required for the following steps.

### Create a Client App

Go to [Google Cloud](https://console.cloud.google.com). Pick one of your project or create a new one. Then in the search bar, type "*Google Auth platform*" and pick "Clients".

Create a new client:

**Fill in basic information**

* Application type: "Web application".
* External Client App Name: "Dust Gsheets Integration".
* Authorized javascript origins: [https://dust.tt](https://dust.tt) and [https://eu.dust.tt](https://eu.dust.tt)
* Authorized redirect URIs: [https://app.dust.tt/oauth/gmail/finalize](https://app.dust.tt/oauth/gmail/finalize) and [https://app.dust.tt/oauth/gmail/finalize](https://app.dust.tt/oauth/gmail/finalize)

## Admin: Setup in Dust

Pick Create and on the next screen, copy the Client ID and Client Secret (you'll need them for the Dust setup):

Go to Spaces > Tools in your Dust workspace, click `Add Tools`, and select Google Sheets.

You will then be redirected to an oAuth flow to connect an admin Google Sheets Account. This account only be used during the set up and users won't be able to query Google Sheets from this account.

By default this tool is added to the Company data Space, so accessible in all the workspace.

## Available Tools

| Tool               | Description                                                                                                                        |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| List Spreadsheets  | List Google Sheets spreadsheets accessible by the user from both personal drive and shared drives. Supports pagination and search. |
| Get Spreadsheet    | Get metadata and properties of a specific Google Sheets spreadsheet.                                                               |
| Get Worksheet      | Get data from a specific worksheet in a Google Sheets spreadsheet.                                                                 |
| Update Cells       | Update cells in a Google Sheets spreadsheet.                                                                                       |
| Append Data        | Append data to a Google Sheets spreadsheet.                                                                                        |
| Clear Range        | Clear values from a range in a Google Sheets spreadsheet.                                                                          |
| Create Spreadsheet | Create a new Google Sheets spreadsheet.                                                                                            |
| Add Worksheet      | Add a new worksheet to an existing Google Sheets spreadsheet.                                                                      |
| Delete Worksheet   | Delete a worksheet from a Google Sheets spreadsheet.                                                                               |
| Format Cells       | Apply formatting to cells in a Google Sheets spreadsheet.                                                                          |
| Copy Sheet         | Copy a sheet from one Google Sheets spreadsheet to another spreadsheet.                                                            |
| Rename Worksheet   | Rename a worksheet in a Google Sheets spreadsheet.                                                                                 |
| Move Worksheet     | Move a worksheet to a new position in a Google Sheets spreadsheet.                                                                 |

## Usage

Once the tool has been configured by the admin as described before, it can be configured for any agent. In the Agent Builder, simply click on `Add Tool` and select Google Sheets.

When users use an agent with the Google Sheets tool for the first time, they will get this notification:

They will have to click on the `Connect` button to connect their own Google Calendar credentials. After it will look like this:

And they can click on the `Retry` button to replay the agent answer if not done automatically.
