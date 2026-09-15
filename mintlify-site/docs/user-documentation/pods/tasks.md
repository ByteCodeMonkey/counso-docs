---
title: "Manage Pod tasks"
---
Tasks are lightweight work items in a Pod. They give a piece of work a clear brief, owner, and state; they do not replace a system of record for a business transaction.

## Before you begin

Write a self-contained description with the expected result, source material, and any approval boundary. Decide whether the task should be assigned or remain unassigned.

## Create and run a task

1. Open the Pod and choose **Tasks**.
2. Choose **Add a task**, enter the description, and optionally choose an assignee.
3. Save the task. It starts as **Open**.
4. Hover over an open task and choose the play action. Add a message or choose an agent, then start it.
5. Follow the linked conversation in **Conversations**. The task becomes **In progress**.
6. When the work is complete, mark the task **Done**. Reopen it by clearing the completion control if more work is required.

Tasks can be edited inline, reassigned, or deleted from their menu. Use **Mine** and **All** filters, and search by description when the list grows.

## Sync with another project tool

Ask an agent with the required project tool to import open items and create matching Pod tasks. For ongoing sync, define one source of truth for each field and prevent a completed item from being recreated on the next run. Test with a small set before enabling a recurring sync.

## What you should see afterward

The task is grouped by assignee and its state is visible to the Pod. Starting an agent creates a linked conversation so people can review progress and redirect the work. A completed task remains visible for history.

## Common questions

### What does Done mean?

It means the collaborative task was completed. It does not mean a payment, posting, approval, or external update happened.

### Why is my task still Open?

No agent has been started on it and no one marked it in progress. Start it or assign it to the person who owns the next step.

### Why did sync create duplicates?

The sync instructions probably lack a stable matching key or source-of-truth rule. Match on the external ID and record the link in the task before running another sync.
