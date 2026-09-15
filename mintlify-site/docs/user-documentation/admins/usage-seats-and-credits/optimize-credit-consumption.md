---
title: "Optimize credit consumption"
---
Credit optimization means getting a useful, reliable result with the work the task requires. It is not a goal to avoid using agents. A broader search, additional tools, or a stronger model can be worthwhile when they change the quality of an important decision; they add little value when a short, focused answer would do.

## Understand what drives usage

Usage commonly changes with four parts of a workflow:

| Driver | What to review |
| --- | --- |
| Model and reasoning | A stronger model or deeper reasoning may be useful for complex work; it may be unnecessary for routine extraction or formatting. |
| Context | Long conversations and broad source access can add processing and irrelevant material. |
| Tools | Search, retrieval, data queries, file generation, and connected actions add work to an interaction. |
| Volume | Repeated runs, batch work, and scheduled workflows multiply the cost of each design choice. |

## Review workspace usage

Workspace administrators can use **Admin > Analytics** and **Admin > Usage** to inspect the views available in their subscription. Review a complete billing or usage period and compare the pace with the period elapsed. Look for contributors or workflows whose usage has changed, a sudden increase, repeated runs, and cases where higher model effort did not improve the output.

Where the current Analytics view provides them, compare members, agents, groups, models, tools, skills, sources, and daily trends. Analytics summaries generally describe usage rather than message content. Use the level of detail offered in the active Counso workspace; the available reports may change by subscription.

## Match model and depth to the work

Use a lighter model or reasoning setting for bounded tasks such as classifying a short list, extracting fields, formatting, routing, or an initial triage when the result remains reliable. Use a stronger model for work that benefits from careful reasoning, code, conflicting evidence, or consequential synthesis. If model tiers or automatic model choices are available, check their current descriptions in the model picker rather than relying on a static list.

Test changes with representative examples before changing an important agent. Compare correctness, completeness, latency, and usage—not just one successful answer. A useful pattern is a lighter first pass followed by a deeper review only when the first result identifies a real uncertainty.

## Keep context focused

- Give the agent one clear job and a concrete output format.
- Select only the data sources needed for that job, and say which source to use first.
- Use structured records or table queries for counts and numeric analysis rather than estimating from broad document search.
- Avoid pasting material the agent can already access; link or select the source instead.
- Start a new conversation when the subject changes. Continue a long thread when its history is still relevant, and use conversation summarization or compaction if the workspace provides it.

## Use tools and reusable workflows deliberately

Review the tools attached to frequently used agents. Keep those central to the task, say when to use them, and identify when the agent should answer from instructions or retrieved knowledge instead. If write operations need oversight, keep them distinct from read-only work and state when a person must approve an action.

A skill or reusable workflow can standardize a repeated method. Keep it short, procedural, and limited to the sources and tools that method needs. Review whether it improves consistency before enabling it broadly.

For a supported scheduled or automated workflow, assign an owner before increasing its volume. Test a small sample, measure result quality and failure rate, estimate expected runs, and use a limit or alert if one is available in the current workspace. Do not assume that a connector or automation shown elsewhere is enabled in this Counso workspace.

## Choose deeper research when it earns its cost

Use a deeper research mode, if available, when a task needs synthesis across multiple sources, evidence comparison, or a durable report with trade-offs. It is usually unnecessary for rewriting a short paragraph, finding one fact in a known document, or formatting simple text. Start with a focused pass; expand the investigation only when the question warrants it.

## Admin review rhythm

A lightweight review is usually enough:

- **Weekly:** check major usage changes, top agents, and unexpected increases.
- **Monthly:** choose one heavily used workflow and test a practical improvement to its model, context, tools, or instructions.
- **Quarterly:** confirm that recurring workflows have clear owners, useful outputs, and current sources; retire those no longer used.

For controls over balances, member limits, and available usage sources, see [Credit management](/docs/user-documentation/admins/usage-seats-and-credits/credit-management). For team coaching, see [Train your team on credit optimization](/docs/user-documentation/admins/usage-seats-and-credits/train-team-credit-optimization).
