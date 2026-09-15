> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Microsoft Sharepoint and OneDrive tools

## Overview

Tool to search, read, upload and update files in your personal Sharepoint/OneDrive content.

<Info>
  **This tool uses personal credentials.** This tool interacts with
  Sharepoint/OneDrive using the user's account: it adapts to each user.
</Info>

## Admin: Setup in Dust

Go to **Spaces > Tools** in your Dust workspace, click `Add Tools`, and select Microsoft Drive.

You will then be redirected to an oAuth flow to connect an admin Microsoft Account. This account will only be used during the setup and users won't be able to query Sharepoint/OneDrive from this account.

By default this tool is added to the Company data Space, so accessible in all the workspace.

## Usage

Once the tool has been configured by the admin as described before, it can be selected on any agent in the Agent Builder.

1. Under **Spaces → Tools**, select **Add Tools**
2. Select **Microsoft Drive** from the available tools
3. When users use an agent with the Microsoft Drive tool for the first time, they will get a notification to click on the `Connect` button to connect their own Microsoft credentials. This ensures that agents only have access to the files users can personally access.

## Available Tools

| Tool                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                               |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Search In Files      | Search in files content in Microsoft OneDrive and SharePoint and returns the most relevant pieces of content.                                                                                                                                                                                                                                                                                                                             |
| Search Drive Items   | Search OneDrive and SharePoint content using Microsoft Graph Search API to find relevant files and documents. This tool returns the results in relevance order.                                                                                                                                                                                                                                                                           |
| Get File Content     | Retrieve the content of files from SharePoint/OneDrive (Powerpoint, Word, Excel, etc.). Supported mimeTypes: application/pdf, application/msword, application/vnd.ms-powerpoint, application/vnd.openxmlformats-officedocument.presentationml.presentation, application/vnd.openxmlformats-officedocument.wordprocessingml.document, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel, text/\* |
| Update Word Document | Update an existing Word document on OneDrive/SharePoint by providing a new document.xml content. Uses driveId if provided, otherwise falls back to siteId.                                                                                                                                                                                                                                                                                |
| Upload File          | Upload a file from Dust conversation to SharePoint or OneDrive. Supports files up to 250MB using the simple upload API. Automatically creates folders if they don't exist.                                                                                                                                                                                                                                                                |

## Limitations

* The tool does not return content for all file types. Please see the list above for the available file types. For example, OneNote is not supported.

## Permissions needed

If your users struggle with approval requirements, you can go in the Azure Admin portal and grant permissions at admin level.

For that go to the Azure Admin Portal, then **Enterprise applications** (you can follow this [link](https://portal.azure.com/#view/Microsoft_AAD_IAM/StartboardApplicationsMenuBlade/~/AppAppsPreview) instead), then **Dust - Tools**, then **Permissions** and click the **Grant admin consent** blue button.

**Still not working?**

Try this other process:

1. Go to this [link](https://portal.azure.com/#view/Microsoft_AAD_IAM/StartboardApplicationsMenuBlade/~/AccessRequests)
2. Click on "All (preview)"
3. Click on the "Dust - Tools" app
4. Click "Review permissions and consent" (or equivalent in your language) in the right panel
