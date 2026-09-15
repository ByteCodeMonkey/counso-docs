---
title: "Microsoft Outlook"
---
Outlook tools can search and read mail, inspect folders and attachments, create drafts, send or move messages, manage contacts, and create or update calendar events. Mail and calendar permissions are separate; request only the capabilities the Agent needs.

A Microsoft Entra administrator and workspace administrator configure the tool in **Spaces → Tools** and grant the delegated permissions required by the current form. The acting user then connects their Microsoft account. Mail operations generally require `Mail.ReadWrite`, with `Mail.Send` for sending; shared mailboxes may require `Mail.ReadWrite.Shared` and `Mail.Send.Shared`. Contact operations may require `Contacts.ReadWrite` and, for shared contacts, `Contacts.ReadWrite.Shared`. Calendar access requires `Calendars.ReadWrite`, with shared calendar permission as needed, plus account and mailbox settings access.

Start with a read or draft. Confirm which mailbox, folder, calendar, and user identity the Agent is using. Before sending or changing an event, review recipient/time details; afterward verify the same message or event in Outlook. If read works but write does not, check delegated consent and the target mailbox's permission separately.

## Available operations

Mail operations include **Get Messages**, **Get Message Body**, **List Folders**, **List Attachments**, **Get Attachment**, **Get Attachments**, **Get Drafts**, **Create Draft**, **Delete Draft**, **Send Mail**, and **Move Messages**. Message previews are shorter than full message bodies; large messages can be read in chunks. Attachment listing returns metadata, while retrieval fetches the file.

Contact operations include **Get Contacts**, **Create Contact**, and **Update Contact**. Calendar operations include **Get User Timezone**, **List Calendars**, **List Events**, **Get Event**, **Create Event**, **Update Event**, **Delete Event**, **Check Availability**, and **Check Self Availability**. Calendar tools use personal credentials; shared-mailbox scenarios apply to mail, not necessarily calendar access.

Mail uses delegated `Mail.ReadWrite`, `Mail.Send`, `User.Read`, `SensitivityLabel.Read`, and `offline_access` as needed. Shared mailbox operations may require `Mail.ReadWrite.Shared` and `Mail.Send.Shared`; contacts may require `Contacts.ReadWrite` and `Contacts.ReadWrite.Shared`. Calendar requires `Calendars.ReadWrite`, optionally `Calendars.ReadWrite.Shared`, plus `MailboxSettings.Read`, `User.Read`, and `offline_access`. Review the actual consent request and enabled actions.

## Action confirmation

Review the action-level confirmation setting in the tool's **Available tools** panel. The source interface describes High actions as requiring approval each time, Medium as allowing a saved confirmation for a specific input, Low as allowing confirmations to be disabled by users, and Never ask as automatic. Sending mail or changing calendar entries should not be treated like read-only searches; choose confirmation settings that match the organisation's policy.
