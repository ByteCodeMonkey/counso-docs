> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Microsoft Teams

## Overview

Tool to search, list and post messages in your personal Microsoft Teams content.

<Info>
  **This tool uses personal credentials.** This tool interacts with Microsoft
  Teams using the user's account: it adapts to each user.
</Info>

## Admin: Setup in Dust

Go to **Spaces > Tools** in your Dust workspace, click `Add Tools`, and select Microsoft Teams.

You will then be redirected to an oAuth flow to connect an admin Microsoft Account. This account will only be used during the setup and users won't be able to query Microsoft Teams from this account.

By default this tool is added to the Company data Space, so accessible in all the workspace.

## Usage

Once the tool has been configured by the admin as described before, it can be selected on any agent in the Agent Builder.

1. Under **Spaces → Tools**, select **Add Tools**
2. Select **Microsoft Teams** from the available tools
3. When users use an agent with the Microsoft Teams tool for the first time, they will get a notification to click on the `Connect` button to connect their own Microsoft credentials. This ensures that agents only have access to the channels and content users can personally access.

## Available Tools

| Tool                    | Description                                                                                                                                                           |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Search Messages Content | Search for messages content in Microsoft Teams chats and channels. Returns the results in relevance order.                                                            |
| List Teams              | List all Teams that the authenticated user has joined. Returns team details including name, description, and team ID.                                                 |
| List Users              | List all users in the organization. Returns user details including display name, email, and user ID.                                                                  |
| List Channels           | List all channels in a specific team. Returns channel details including name, description, and channel ID.                                                            |
| List Chats              | List all chats (one-on-one or group chats) for the authenticated user. Returns chat details including chat ID, topic, and participants. Can be filtered by chat type. |
| List Messages           | List all messages (and their replies) in a specific channel. Returns thread messages with their replies.                                                              |
| Post Message            | Post a message to a Teams channel, chat, or as a reply in a thread. Can send messages to channels, direct chats, or as threaded replies.                              |

## Limitations

* Microsoft API supports keyword-based search only (not semantic search)

## Permissions needed

If your users struggle with approval requirements, you can go in the Azure Admin portal and grant permissions at admin level.

For that go to the Azure Admin Portal, then **Enterprise applications** (you can follow this [link](https://portal.azure.com/#view/Microsoft_AAD_IAM/StartboardApplicationsMenuBlade/~/AppAppsPreview) instead), then **Dust - Tools**, then **Permissions** and click the **Grant admin consent** blue button.

**Still not working?**

Try this other process:

1. Go to this [link](https://portal.azure.com/#view/Microsoft_AAD_IAM/StartboardApplicationsMenuBlade/~/AccessRequests)
2. Click on "All (preview)"
3. Click on the "Dust - Tools" app
4. Click "Review permissions and consent" (or equivalent in your language) in the right panel

(Optional) Deactivate and re-activate your Teams tool if the issue persists.
