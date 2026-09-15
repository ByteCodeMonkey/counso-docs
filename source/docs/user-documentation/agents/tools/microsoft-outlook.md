> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Microsoft Outlook

## Overview

Outlook tools let your agents work with your Microsoft 365 mailbox and calendar.
Agents can read messages and their full body, browse the folder hierarchy,
download attachments, create and delete drafts, send mail, move messages into
folders, manage contacts, and create or update calendar events.

This document covers the available tools, setup, authentication, and the scopes
Dust requests.

<Info>
  **This tool uses personal credentials.** Each user authenticates with their
  own Microsoft account, so an agent only ever sees what that user can see.
  Outlook Mail can also be installed with workspace credentials for
  platform-level automations; Outlook Calendar is personal-credentials only.
</Info>

## Admin: Setup in Dust

The setup process **requires a Microsoft Entra ID admin** ('privileged role
administrator' or 'application administrator') who is also a Dust admin. This
ensures full access to the necessary permissions.

1. Under **Spaces → Tools**, select `Add Tools`, then select `Outlook`.
2. Review the permissions. Each tool action can be set to one of four stake
   levels: high (always ask for confirmation), medium (let users save a
   confirmation for a specific input), low (users can disable confirmations
   entirely), or never ask (runs automatically) from the "Available tools"
   settings.
3. On the first connection, tick **Consent on behalf of your organization**.

Once the tool is set up, **each user must connect their own Microsoft account**
the first time an agent uses an Outlook tool on their behalf. Dust prompts them
automatically.

## Usage

After admin setup, the Outlook tool can be added to an agent by selecting it
from the agent builder. They require no additional configuration.

## Available Tools

### Outlook Mail

| Tool             | Write | Description                                                                                                                                                                                                                                                                                 |
| ---------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Get Messages     |       | Get message metadata and previews (subject, sender, date, and a \~255 character body preview, not the full body). Supports search queries and a folder path.                                                                                                                                |
| Get Message Body |       | Get the full body of a single message. Supports chunked reads for large emails.                                                                                                                                                                                                             |
| List Folders     |       | List mail folders. Returns the children of a given folder path, or top-level folders. Use it to discover the hierarchy before filtering messages by folder.                                                                                                                                 |
| List Attachments |       | List attachments on a message (metadata only: id, name, content type, size).                                                                                                                                                                                                                |
| Get Attachment   |       | Retrieve a single attachment by ID. Works for files above 4MB via a dedicated download endpoint.                                                                                                                                                                                            |
| Get Attachments  |       | Retrieve all attachments of a message at once.                                                                                                                                                                                                                                              |
| Get Drafts       |       | Get draft emails.                                                                                                                                                                                                                                                                           |
| Create Draft     | ✓     | Create a new draft, or a reply draft to an existing message. Saved in the user's account for later review.                                                                                                                                                                                  |
| Delete Draft     | ✓     | Delete a draft email.                                                                                                                                                                                                                                                                       |
| Send Mail        | ✓     | Send an email immediately, without creating a draft first.                                                                                                                                                                                                                                  |
| Move Messages    | ✓     | Move one or more messages to a destination folder, given as a path of folder names from the top level (for example `["Archive", "2026", "Receipts"]`). Folders that do not exist along the path are created automatically. Note that Microsoft Graph assigns a new message ID after a move. |
| Get Contacts     |       | Get contacts. Supports search queries.                                                                                                                                                                                                                                                      |
| Create Contact   | ✓     | Create a new contact.                                                                                                                                                                                                                                                                       |
| Update Contact   | ✓     | Update an existing contact.                                                                                                                                                                                                                                                                 |

### Outlook Calendar

| Tool                    | Write | Description                                                                                                                                         |
| ----------------------- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Get User Timezone       |       | Get the user's timezone from their mailbox settings. Called before other calendar operations for correct timezone handling.                         |
| List Calendars          |       | List all calendars accessible by the user.                                                                                                          |
| List Events             |       | List or search events. Supports filtering and searching.                                                                                            |
| Get Event               |       | Get a single event by ID.                                                                                                                           |
| Create Event            | ✓     | Create a new event, with attendees, location, and online meeting options.                                                                           |
| Update Event            | ✓     | Update an existing event.                                                                                                                           |
| Delete Event            | ✓     | Delete an event.                                                                                                                                    |
| Check Availability      |       | Compute combined free/busy availability across several participants over a date range.                                                              |
| Check Self Availability |       | Check whether the signed-in user is free during a time slot. An event blocks if its status is busy, tentative, out of office, or working elsewhere. |

## Permissions needed

Dust requests **delegated** permissions, so a user can never do more through
Dust than they can do in Outlook directly.

### Outlook Mail

| Scope                       | Required for                                                    |
| --------------------------- | --------------------------------------------------------------- |
| `Mail.ReadWrite`            | Read and modify mail, including moving messages between folders |
| `Mail.Send`                 | Send mail on behalf of the signed-in user                       |
| `User.Read`                 | Read basic profile information                                  |
| `SensitivityLabel.Read`     | Read sensitivity labels applied to messages                     |
| `offline_access`            | Maintain access without re-authentication                       |
| `Mail.ReadWrite.Shared`     | Access shared and delegated mailboxes (optional)                |
| `Mail.Send.Shared`          | Send from shared and delegated mailboxes (optional)             |
| `Contacts.ReadWrite`        | Read and modify contacts (optional)                             |
| `Contacts.ReadWrite.Shared` | Access shared contact folders (optional)                        |

<Note>
  There is no read-only Outlook Mail setup. `Mail.ReadWrite` and `Mail.Send` are
  required for the tool to function, and the shared variants imply them. Control
  what agents are allowed to do with the per-tool stake settings in the agent
  builder rather than with scopes: leave Send Mail as high stake, or simply do
  not add it to the agent.
</Note>

### Outlook Calendar

| Scope                        | Required for                                     |
| ---------------------------- | ------------------------------------------------ |
| `Calendars.ReadWrite`        | Read and modify calendar events                  |
| `User.Read`                  | Read basic profile information                   |
| `offline_access`             | Maintain access without re-authentication        |
| `Calendars.ReadWrite.Shared` | Access shared and delegated calendars (optional) |
| `MailboxSettings.Read`       | Read timezone and working hours (optional)       |

### Permissions needed

If your users struggle with approval requirements, you can go in the Azure
Admin portal and grant permissions at admin level.

For that go to the Azure Admin Portal, then **Enterprise applications** (you
can follow this [link](https://portal.azure.com/#view/Microsoft_AAD_IAM/StartboardApplicationsMenuBlade/~/AppAppsPreview)
instead), then **Dust - Tools**, then **Permissions** and click the **Grant
admin consent** blue button.

**Still not working?**

Try this other process:

1. Go to this [link](https://portal.azure.com/#view/Microsoft_AAD_IAM/StartboardApplicationsMenuBlade/~/AccessRequests)
2. Click on "All (preview)"
3. Click on the "Dust - Tools" app
4. Click "Review permissions and consent" (or equivalent in your language) in the right panel
