> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# [Beta] Import Jira issues

## Jira Issues Importer for Dust

This script imports recently updated Jira issues into a Dust datasource.

This open-source script, **available on GitHub at[dust-tt/dust-labs/jira](https://github.com/dust-tt/dust-labs/tree/main/jira)**, automates the process of exporting issues updated in the last 24 hours from Jira and importing them into a Dust datasource. It fetches full issue details, like so:

```
Issue Key: KAN-3
ID: 10002
URL: https://dust4ai.atlassian.net/rest/api/3/issue/10002
Summary: Nice task to do
Description:
What do you think about this description

Issue Type: Task
Status: To Do
Priority: Medium
Assignee: Alban Dumouilla (alban@dust.tt)
Reporter: Alban Dumouilla (alban@dust.tt)
Project: My Kanban Project (KAN)
Created: 2024-08-20T15:51:58.901+0200
Updated: 2024-08-20T16:26:36.215+0200
Resolution: Unresolved
Resolution Date: N/A
Labels: test
Components:
Sprint: N/A
Epic: N/A
Time Tracking:
  Original Estimate: N/A
  Remaining Estimate: N/A
  Time Spent: N/A
Votes: 0
Watches: 1
Fix Versions:
Affected Versions:
Subtasks:
Issue Links: Blocks KAN-1: This is a todo card
Attachments:

Comments:

[2024-08-20T16:26:36.076+0200] Author: Alban Dumouilla (alban@dust.tt)
This is the first comment of the issue
```

The script then formats and uploads this data to Dust.

The script only exports issues updated in the last 24 hours, so schedule it to run daily to keep your Dust knowledge base up to date with Jira. Your agents can then use the issue data to analyze support trends, response times, and customer service quality. The script uses rate limiting and error handling to stay reliable with large volumes of Jira issues.
