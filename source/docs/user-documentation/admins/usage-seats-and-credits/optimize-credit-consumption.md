> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Optimize credit consumption

Credit optimization is not about using Dust less. It is about making sure each agent does the right amount of work for the value it creates.

As your team starts using Dust for real work, credit usage may increase. That can be a good sign. It often means agents are helping your team draft, search, summarize, update, route, analyze, and automate work that used to be manual.

This guide explains how to understand where usage comes from and how to keep it efficient as your workspace scales.

## What affects credit consumption

Credit consumption is usually driven by four factors:

| Factor           | What it means                                                                                                          |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Model choice** | Stronger models or higher reasoning settings can consume more credits.                                                 |
| **Context**      | Agents consume credits when they read, retrieve, and process information.                                              |
| **Tools**        | Tools let agents search, query, write, notify, create, enrich, and act. Tool-heavy workflows can consume more credits. |
| **Volume**       | A low-cost request can become expensive if it runs many times through an API, trigger, spreadsheet, or automation.     |

A good workflow uses the right model, the right context, the right tools, and the right volume for the task.

## Review usage in Analytics

Workspace admins can review credit consumption from **Admin > Analytics**. Select the current cycle, the last 7 days, the last 30 days, or the last 90 days. Then compare consumption with the workspace cap, inspect changes over time, and attribute credits to agents, members, groups, models, tools, skills, sources, or API keys. See [Analytics](/analytics) for details.

Start with these questions:

| What to review                  | What to look for                                                                           |
| ------------------------------- | ------------------------------------------------------------------------------------------ |
| **Cycle pace**                  | Is consumption on target relative to the percentage of the cycle elapsed?                  |
| **Agents and members**          | Is consumption broad across the workspace or concentrated among a few contributors?        |
| **Models, tools, and skills**   | Which workflow components account for the most credits or the highest average consumption? |
| **Sources and API keys**        | Is programmatic consumption growing or coming from an unexpected origin?                   |
| **Daily and cumulative trends** | Did consumption increase gradually, or did it spike suddenly?                              |
| **Vs Prev**                     | Which contributors changed most compared with the preceding period?                        |

Analytics exports metadata only, not message content.

## Review programmatic usage separately

Programmatic usage should be reviewed separately from regular human usage.

Dust defines programmatic usage as messages sent through a custom Dust API key, or messages that are not manually typed and sent by a person. Examples include API usage, automated workflows in Slack, Zapier or n8n, and batch operations in Google Sheets or Excel. Manually typed messages in the web app, browser extension, Slack, or Teams are not considered programmatic in the usual case.

Workspace admins can review programmatic credit consumption in **Admin > Usage** under the Programmatic usage settings. For details on how programmatic usage draws credits and how to configure the monthly cap, see [Credit management](/docs/user-documentation/admins/usage-seats-and-credits/credit-management).

When reviewing programmatic usage, check:

| What to review | What to look for                                                                              |
| -------------- | --------------------------------------------------------------------------------------------- |
| **API keys**   | Does one key drive most usage?                                                                |
| **Sources**    | Is usage coming from an API, spreadsheet, Slack workflow, Zapier, n8n, or another automation? |
| **Agents**     | Which agents are called programmatically most often?                                          |
| **Volume**     | Is the workflow running more often than expected?                                             |
| **Timing**     | Are there unexpected spikes or off-hours runs?                                                |
| **Ownership**  | Does every automation have a clear owner?                                                     |

If programmatic credits reach zero, programmatic usage is blocked until credits are added, unless Enterprise pay-as-you-go is enabled. Regular usage through the web app, Slack, or browser extension is not affected by programmatic credit depletion.

## Optimize model fit

The strongest model is not always the best default.

Stronger models are useful for complex reasoning, coding, careful synthesis, and high-stakes work. Simpler tasks such as classification, tagging, formatting, routing, extraction, deduplication, or first-pass triage may work well with lighter models when available.

The simplest way to get this right without tracking individual models is to use [auto models](/docs/user-documentation/agents/model-selection#auto-models). **Basic**, **Standard**, and **Premium** are three ordered lists of model and reasoning-effort combinations maintained by Dust at three capability and cost levels. Dust periodically benchmarks and updates the lists. You choose the level per agent, and Dust keeps the list current instead of asking you to track individual models. Dust does not choose a different level for each request based on the task.

### What to do

* Review your top agents and check whether their model matches the task.
* Use stronger models where quality clearly improves the outcome.
* Use lighter models for structured or repetitive tasks when the output remains reliable.
* Test model changes on real examples before changing an important workflow.
* Create simpler versions of popular agents when users often need quick answers.
* Cap what members can select with [model access tiers](/docs/user-documentation/admins/usage-seats-and-credits/model-access-tiers), so premium models stay reserved for the teams that need them.

### Example

If an agent classifies incoming support tickets and then writes a final customer-facing summary, the classification step may not need the strongest model. The final summary may still justify a stronger model.

## Reduce unnecessary context

More context can feel safer, but it can also make agents less focused.

Focusing on relevant, high-quality information rather than overwhelming the agent with unnecessary data leads to better results. Larger context windows can increase processing time and cost, and can introduce information overload or conflicting information. See [How to write effective instructions](/docs/user-documentation/agents/llm-best-practices/how-to-write-effective-instructions) for guidance on writing focused agent instructions.

### What to do

* Give each agent a clear job.
* Connect only the sources that matter for that job.
* Tell the agent which sources to use first.
* Remove stale or low-quality sources.
* Use structured data or table queries for numbers, counts, and metrics.
* Avoid pasting large documents if the agent already has access to the source.
* Start a new conversation when the topic changes.

### Useful instruction examples

* "Use the policy docs first for policy questions."
* "Use CRM data for account fields."
* "Use Slack only for recent discussion context."
* "Ask a clarifying question if the source is ambiguous."
* "Do not search all sources unless the first source is insufficient."

## Keep tool use intentional

Tools let agents do work beyond chat. They can search, query, update, notify, create, enrich, and act. Workspace admins can view, add, remove, and configure tools available to users from **Spaces > Tools**.

The goal is not to remove tools for the sake of removing tools. A useful tool can make an agent more efficient because it helps the agent get the right answer faster. The issue is unclear or unnecessary tool use.

### What to do

* Review the tools available to your top agents.
* Remove tools that are not central to the agent's job.
* Tell the agent when to use each tool.
* Tell the agent when not to use tools.
* Separate read-only workflows from write workflows when governance matters.
* Use structured queries for numbers and aggregations instead of asking the agent to infer metrics from broad document search.

### Useful instruction examples

* "Answer from instructions if no retrieval is needed."
* "Use the data warehouse only for numeric questions."
* "Use CRM for account metadata."
* "Do not call write tools unless the user explicitly asks."
* "Summarize retrieved data before using another tool."

## Use skills for reusable methods

Analytics attributes consumption to skills, which helps admins understand which skills account for credit usage across the workspace.

A skill is useful when an agent needs a reusable method, checklist, rubric, or process. A good skill can make a workflow more consistent because the agent knows how to approach the task.

### What to do

* Use skills for repeated methods.
* Keep skills short, specific, and procedural.
* Avoid enabling skills "just in case."
* Review whether a skill improves output quality and consistency.
* If a workflow is repeated often, consider turning the method into a reusable skill or agent.

## Use Go Deep for complex research

[Go Deep](/docs/user-documentation/agents/go-deep) gives agents the ability to conduct deeper research across company data, databases, and web sources. It includes capabilities such as sub-agents, company data exploration, data warehouse queries, and web search and browsing.

Use Go Deep when the question requires broad investigation or synthesis across multiple sources. It is best suited for complex research, market analysis, competitive intelligence, SQL-backed analysis, and work that may take several minutes.

### Good use cases for Go Deep

* Preparing a customer-ready research report.
* Analyzing adoption, risks, and opportunities across multiple sources.
* Comparing options and recommending one with trade-offs.
* Researching a market, competitor, or account.
* Creating a durable artifact such as a report, memo, or MiniApp.

### Less suitable use cases

* Rewriting a short paragraph.
* Finding one fact from one known document.
* Answering a narrow question that does not require multiple sources.
* Formatting simple text.

## Govern automations before scaling

Automations can create a lot of value, but they can also scale faster than expected.

Two settings keep them in check. [Rate limits](/docs/user-documentation/agents/triggers/webhooks/rate-limiting) cap how often a webhook trigger runs, 42 times per 24 hours by default, and its editor can adjust that. The [credit pool](/docs/user-documentation/agents/triggers/credits-usage) decides who pays: the trigger's editor, or the workspace. Put high-volume automations on the workspace pool, where you see their cost under Programmatic Usage > Automations and cap it with the monthly programmatic limit.

### Before scaling an automation

* Assign an owner.
* Use separate API keys by workflow when possible.
* Start with a small test batch.
* Measure credits per row or request.
* Check output quality.
* Check failure rate.
* Forecast daily and monthly volume.
* Define what normal usage looks like.
* Set a spike threshold.
* Review active triggers, scheduled workflows, and batch jobs regularly.

### Pre-launch checklist

* Who owns this workflow?
* What does it do?
* How often does it run?
* What does one run cost?
* What is the expected monthly volume?
* What happens when it fails?
* What volume would be surprising?
* Who should be alerted if usage spikes?

If a legitimate automation needs higher limits, workspace admins can contact Dust support with the use case and expected daily volume.

## Keep conversations clean with compaction

Long conversations are useful when the work is continuous. They become less efficient when they turn into a place for unrelated tasks.

Dust provides [context compaction](/docs/user-documentation/agents/context-compaction) to help long conversations continue with summarized context instead of replaying the full earlier history. The original messages remain stored and visible, but future agent runs use the compaction summary and the messages after the compaction marker.

Compaction is user-controlled. Dust shows a context usage indicator in the composer. The tooltip offers **Compact now** when context usage is high enough, and warnings appear as context usage increases.

### What to do

* Start a new conversation when the topic changes.
* Keep long threads for continuous work only.
* Use compaction when continuing a long conversation.
* Compact after a good answer, when the state of the work is clear.
* Turn repeated workflows into agents.
* Avoid pasting the same context repeatedly.
* Link to sources when the agent has access.

### Simple user guidance

* New topic, new conversation.
* Repeated task, use an agent.
* Same project, continue the thread and compact when useful.
* Large document, use the source instead of pasting.
* Short answer needed, ask for a short answer.

## Monthly admin checklist

Admins do not need to inspect every message. Most optimization comes from reviewing the top agents, sources, and workflows.

| Review item            | Question                                                                      |
| ---------------------- | ----------------------------------------------------------------------------- |
| **Top agents**         | Which agents are used the most?                                               |
| **Top users**          | Is usage broad or concentrated?                                               |
| **Message sources**    | Is usage coming from humans, triggers, scheduled runs, API, or integrations?  |
| **Programmatic usage** | Which API keys, agents, or sources consume the most credits?                  |
| **Tool usage**         | Which tools are used most often?                                              |
| **Skill usage**        | Which skills are used most often?                                             |
| **Go Deep usage**      | Are deep research workflows producing useful outputs?                         |
| **Automations**        | Do recurring workflows still have an owner and expected volume?               |
| **Conversations**      | Are users starting fresh when topics change and compacting long-running work? |

## Summary

Good AI adoption creates usage.

Good credit optimization makes that usage explainable, governed, and worth scaling.

The goal is not less AI. The goal is better-designed workflows.
