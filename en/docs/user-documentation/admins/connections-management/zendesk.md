# Connect Zendesk

This connection imports Support tickets and Guide Help Center articles into Counso knowledge. It does not install a chat assistant inside Zendesk.

## Connect and choose brands

Use an administrator with access to both Counso and Zendesk Support and Guide. Open **Spaces > Connections > Zendesk**, enter your Zendesk subdomain, and authorize the connection. The subdomain is the part before `.zendesk.com` in your Zendesk address.

You can select a brand's tickets alone or select the whole brand, including its Help Center. For articles, select individual categories or an entire Help Center. Only published articles in the selected scope are indexed. Select the whole Help Center if newly created categories should be included automatically.

## Configure ticket synchronization

Open **Manage** on the Zendesk connection to adjust these options:

| Option | Effect |
| --- | --- |
| Sync Unresolved Tickets | Includes tickets that are not yet solved or closed. This can increase volume and introduce unfinished support discussions into search. |
| Hide Customer Information | Omits customer names and email addresses from attached metadata. It does not redact those details from ticket messages. |
| Data Retention Period | Determines how long tickets remain eligible. Check the current configured value before estimating coverage. |
| Ticket Tag Filters | Includes or excludes tickets using their tags. |
| Organization Tag Filters | Includes or excludes tickets using the associated organization's tags. |
| Custom Field Tags | Adds selected custom-field values as `fieldName:value` labels. Find the numeric field ID in Zendesk Admin's Fields settings and use **Add Field**. |
| Rate Limit Transactions Per Second | Caps connector requests to fit Zendesk rate limits. Leaving it empty disables this additional cap, not Zendesk's own limits. |

By default, the connection focuses on solved or closed tickets within the relevant time window. Inclusion and exclusion tag filters apply to future synchronization; they do not remove previously indexed tickets retroactively. Expired or unselected tickets are cleaned daily.

## What is included

Tickets include comments, available author metadata, tags, priority, type, channel, organization and group IDs, satisfaction feedback, and due dates. Search is designed to find relevant ticket content. Do not treat semantic search as a complete counting system for questions such as how many tickets were assigned to a person.

Articles include the title and body, category and section descriptions, author metadata, labels, and vote balance. The customer-information setting controls included identity metadata, so enabling it also removes identity context from agent answers.

## Refresh and labels

Selecting content starts synchronization; duration depends on the amount of data. A newly solved or deleted ticket, or a newly published article, can take up to about 30 minutes to be reflected. Deleted or unselected articles and expired tickets are cleaned on the daily cycle.

Ticket tags and labels such as `priority`, `ticketType`, `channel`, `status`, `groupId`, `organizationId`, `dueDate`, `satisfactionRating`, and `hasIncidents` can narrow [knowledge searches](../../agents/knowledge/search-data-sources.md).
