> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Microsoft Excel

## Overview

Make your agents search and edit Excel files in your Sharepoint/OneDrive.

<Info>
  **This tool uses personal credentials.** This tool interacts with your
  Microsoft Excel files using the user's account: it adapts to each user.
</Info>

## Admin: Setup in Dust

Go to **Spaces > Tools** in your Dust workspace, click `Add Tools`, and select Microsoft Excel.

You will then be redirected to an oAuth flow to connect an admin Microsoft Account. This account will only be used during the setup and users won't be able to query SharePoint/OneDrive from this account.

By default this tool is added to the Company data Space, so accessible in all the workspace.

## Usage

Once the tool has been configured by the admin as described before, it can be selected on any agent in the Agent Builder.

1. Under **Spaces → Tools**, select **Add Tools**
2. Select **Microsoft Excel** from the available tools
3. When users use an agent with the Microsoft Excel tool for the first time, they will get a notification to click on the `Connect` button to connect their own Microsoft credentials. This ensures that agents only have access to the Excel files users can personally access.

## Available Tools

| Tool             | Description                                                                                |
| ---------------- | ------------------------------------------------------------------------------------------ |
| List Excel Files | List Excel files (.xlsx, .xlsm) from SharePoint or OneDrive.                               |
| Get Worksheets   | Get a list of all worksheets (sheets/tabs) in an Excel workbook stored in SharePoint.      |
| Read Worksheet   | Read data from a specific range or entire worksheet in an Excel file stored in SharePoint. |
| Write Worksheet  | Write data to a specific range in an Excel worksheet stored in SharePoint.                 |
| Create Worksheet | Create a new worksheet (sheet/tab) in an Excel workbook stored in SharePoint.              |
| Clear Range      | Clear data from a specific range in an Excel worksheet stored in SharePoint.               |

## Permissions needed

If your users struggle with approval requirements, you can go in the Azure Admin portal and grant permissions at admin level.

For that go to the Azure Admin Portal, then **Enterprise applications** (you can follow this [link](https://portal.azure.com/#view/Microsoft_AAD_IAM/StartboardApplicationsMenuBlade/~/AppAppsPreview) instead), then **Dust - Tools**, then **Permissions** and click the **Grant admin consent** blue button.

**Still not working?**

Try this other process:

1. Go to this [link](https://portal.azure.com/#view/Microsoft_AAD_IAM/StartboardApplicationsMenuBlade/~/AccessRequests)
2. Click on "All (preview)"
3. Click on the "Dust - Tools" app
4. Click "Review permissions and consent" (or equivalent in your language) in the right panel
