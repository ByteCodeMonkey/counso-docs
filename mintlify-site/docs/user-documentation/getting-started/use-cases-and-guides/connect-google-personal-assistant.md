---
title: "Connect Google and use a personal Google assistant"
---
import { TutorialVideo } from "/snippets/tutorial-video.jsx";

Connect your own Google account to use the Google tools available to your Agent. This guide covers personal authorization and everyday use after a workspace administrator has set up the tools.

<TutorialVideo videoId="etv-cr1-8vI" title="How to Connect Your Google" language="en" />

## Before you connect

Ask your workspace administrator to make the required Google tools available. Use an Agent that can access those tools. The administrator's Google account is used for initial setup; it does not give other members access to that account's files, mail, or calendar. Administrator application setup and any required client credentials belong in the tool configuration.

For administrator setup and supported operations, see [Google Drive](/docs/user-documentation/agents/tools/google-drive), [Gmail](/docs/user-documentation/agents/tools/gmail), and [Google Calendar](/docs/user-documentation/agents/tools/google-calendar).

## Authorize your Google account

1. Open a conversation with an Agent that can use the Google tools you need, and ask it to find one known file, message, or calendar event.
2. The first time the Agent uses a tool that needs your authorization, a connection prompt or authentication error may appear. Select **Connect**.
3. Choose the Google account you intend to use and review the requested permissions before completing authorization. Each tool uses your connected identity and that account's access. Follow any separate connection prompts for Drive, Gmail, or Calendar.
4. Return to the conversation. If the Agent does not continue automatically, select **Retry** to run the request again.
5. Check the result against the original item in Google to verify that it comes from the intended account.

Personal authorization lets the tool act with your Google permissions. A managed Drive Connection that synchronizes files for search is configured separately; see [Connections](/docs/user-documentation/data-sources/connections).

## Use your personal assistant

Give the Agent a specific task and scope. For example:

- Find a named document in Google Drive and summarize its key points with a link to the source.
- Find a known Gmail message and prepare a reply draft for review.
- Summarize tomorrow's calendar events using your time zone.

Before sending a message or changing an event or file, review the proposed action, account, and recipients. Verify the result in the corresponding Google app afterward.

## If something is missing

Check that the Agent has the relevant tool, the correct Google account is connected, and that account can access the item in Google itself. If write permissions are missing, reconnect the affected tool and review the requested authorization. Ask an administrator if the tool is not available in your workspace.
