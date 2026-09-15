> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# [Beta] Import Front Conversations

This open-source script, available on GitHub at [dust-tt/dust-labs/front](https://github.com/dust-tt/dust-labs/tree/main/front) exports your Front conversations and imports them into a Dust datasource. It preserves the full conversation data and metadata, like so:

```
Conversation ID: cnv\_1a2b3c4d
Subject: Feature Request: Dark Mode Implementation
Status: archived
Assignee: John Smith (john@company.com)
Created: 2024-03-18T10:00:00.000Z
Last Updated: 2024-03-18T15:45:00.000Z

Messages:
[Customer] Sarah Johnson <sarah@client.com> - 2024-03-18T10:00:00.000Z
Hi there! I was wondering if you're planning to implement a dark mode feature?
It would really help reduce eye strain during night shifts.

[Team] John Smith <john@company.com> - 2024-03-18T10:30:00.000Z
Thanks for reaching out, Sarah! We actually have dark mode on our roadmap.
Can you tell me more about your use case? This will help us prioritize.

[Customer] Sarah Johnson <sarah@client.com> - 2024-03-18T11:15:00.000Z
Of course! Our team operates 24/7, and many of us work late shifts...

[Internal Note] John Smith <john@company.com> - 2024-03-18T15:45:00.000Z
Adding this to our Q2 planning discussion. Strong use case for healthcare clients.

Tags: feature-request, ui-ux, customer-feedback
```

The script then formats and uploads this data to Dust, maintaining the conversation structure and metadata integrity.

## How it Works

1. **Fetch Inboxes**: Retrieves all available Front inboxes
2. **Process Conversations**: For each inbox, fetches conversations (no time filtering applied)
3. **Fetch Messages**: For each conversation, retrieves all messages
4. **Create Documents**: Combines conversation metadata and messages into a single document
5. **Upload to Dust**: Stores each conversation as a document with appropriate tags

## Document Structure

Each conversation document contains:

* **Conversation Summary**: Subject, status, assignee, timestamps, message count
* **Messages Section**: All messages with sender, timestamp, direction, and content
* **Size Limits**: Total document size limited to 2MB
* **Tags**: Source, type, conversation ID, status, message count, timestamps, assignee, subject

With this data in Dust, your agents can analyze customer support responses, draft new responses based on historical conversations, and summarize common support themes.
