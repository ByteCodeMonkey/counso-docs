> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# [Beta] Import Linear Issues

## Linear Issues Importer for Dust

This script synchronizes your Linear issues with a Dust datasource.

This open-source script, **available on GitHub at[dust-tt/dust-labs/linear](https://github.com/dust-tt/dust-labs/tree/main/linear)**, automates the process of exporting all issues from Linear, along with related metadata such as comments, attachments, and history. It fetches full issue metadata, like so:

```
Issue Summary for ENG-123: Implement new authentication flow

Metadata:
Issue Details:
ID: abc123
Number: 123
Identifier: ENG-123
URL: https://linear.app/company/issue/ENG-123

Team & Project:
Team: Engineering (ENG)
Project: Authentication Overhaul
State: In Progress (Active)

Dates & Times:
Created: 2024-03-18T10:00:00.000Z
Updated: 2024-03-18T15:30:00.000Z
Started: 2024-03-18T11:00:00.000Z
Due Date: 2024-03-25

People:
Creator: Jane Smith (jane@company.com)
Assignee: John Doe (john@company.com)
Subscribers: Alice Brown (alice@company.com), Bob Wilson (bob@company.com)

Planning:
Priority: 2 (High)
Estimate: 5 points
Cycle: Sprint 45 (2024-03-18T00:00:00.000Z to 2024-03-29T23:59:59.999Z)
Labels: security, authentication

Description:
Implement new OAuth2-based authentication flow with support for multiple providers.
- Add OAuth2 client implementation
- Support Google and GitHub providers
- Implement token refresh logic
- Add user session management

Comments:
Comment by Alice Brown (alice@company.com) - 2024-03-18T12:00:00.000Z
Should we also consider adding Microsoft OAuth support?
Reactions: : 2, : 1

Comment by John Doe (john@company.com) - 2024-03-18T13:15:00.000Z
Good suggestion. I'll create a follow-up ticket for that.

Recent History:
2024-03-18T11:00:00.000Z - John Doe
Changed status from "Todo" to "In Progress"
```

The script then formats and uploads this data to Dust.

With this data in Dust, you can build agents that analyze trends, response times, and response quality across your Linear issues. The script includes rate limiting, filtering, and error handling, and handles large volumes of Linear issues reliably.
