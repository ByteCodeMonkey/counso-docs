---
title: "Train your team on credit optimization"
---
Teach credit optimization as a way to design better work, not as a warning to avoid using AI. A useful discussion asks which workflows produce value, and whether the same quality can be reached with a clearer request, narrower context, or simpler first pass.

## Start with good request habits

Most members do not need to learn internal usage calculations. They need to know how to describe the task, audience, sources, depth, and stopping point. For example:

| Instead of | Try |
| --- | --- |
| “Analyze this.” | “Summarize this for a finance manager in five bullets. Focus on risks, next steps, and open questions. Do not research beyond the document unless it leaves an important gap.” |
| “Do a deep dive on this account.” | “Start with a brief: company context, recent activity, open risks, and three next steps. Tell me what evidence would justify a deeper review.” |
| “Use everything you can find.” | “Check the account record and recent call notes first. Search the discussion channel only if recent context is missing.” |

A well-formed request tells the Agent what matters, where to look, how much detail to produce, and when to stop.

## Teach a light first pass, then go deeper

A deeper research mode or stronger model is useful when the question is consequential, depends on multiple sources, or requires resolving conflicting evidence. It is usually unnecessary for a short summary, simple rewrite, formatting, classification, or extracting fields from a known document.

Teach the habit: **first pass first; deeper work only when the result shows it is needed.** Members should ask for the smallest useful answer, then follow up on a real gap rather than requesting maximum detail by default. If model tiers or automatic model choices are available, explain the options currently shown in the workspace.

## Choose the right working mode

| Mode | Use it when | Example |
| --- | --- | --- |
| Agent | The task is known and can be completed in one interaction or focused conversation. | Prepare a customer meeting brief or summarize a support discussion. |
| Skill or reusable workflow | A method repeats and several people need to follow the same steps. | Apply the same review checklist to each monthly close package. |
| Manual sequence | The work is exploratory or a one-off problem whose steps are not known yet. | Compare approaches before deciding how to investigate an unusual issue. |

If the same sequence is repeated, consider turning it into a Skill or Agent. Reusable methods can reduce repeated setup, improve consistency, and avoid unnecessary tool use. Keep each method scoped to the work it serves.

## Help experienced users improve existing habits

Use real, non-sensitive examples from the workspace to show practical alternatives:

- Replace one broad default Agent with a focused Agent for a recurring task.
- Start a new conversation when an old thread carries irrelevant history.
- Test a small batch before scaling a supported workflow to a larger set.
- Use a lighter first pass for routine triage, then reserve stronger analysis for the cases that need it.

People learn faster from a side-by-side example than from a general warning about consumption.

## Train builders to design efficient Agents

Builder choices affect every later run. In a review, ask:

- Which steps can use a lighter model, and which need stronger reasoning?
- Which sources must the Agent search first, and which are unnecessary by default?
- Which tools are central to the task? Which could be removed?
- Should this be one broad Agent or a smaller set of focused Agents?
- Is this a repeated manual sequence that should become a reusable Skill or workflow?
- Does the output meet expectations on several representative examples?

Builders should use clear instructions, keep sources and tools focused, test model changes with real cases, and separate read-only tasks from changes that require human review.

## Keep manager conversations about outcomes

Questions such as “Who used the most credits?” can make useful work feel discouraged. Focus instead on workflow value and quality:

| Avoid | Ask |
| --- | --- |
| “Can we cut usage?” | “Where can we get the same reliable result with less rework?” |
| “Why is this expensive?” | “Which workflow is slow, repetitive, or too broad?” |
| “Who spent too much?” | “Where are people repeating the same task or retrying?” |
| “Is this automation worth it?” | “Who owns it, and what output or time savings does it produce?” |

## Make it a recurring practice

Use a cadence that fits the team:

- **Weekly:** review unusual usage changes and the workflows behind them.
- **Monthly:** choose one repeated task and improve its instructions, source scope, or model choice; compare a few real examples.
- **Quarterly:** review the Agent map, Skill owners, source freshness, and workflows that should be updated or retired.

Helpful training materials include an Agent map, short prompt examples, a builder checklist, and a workflow review template. Keep them aligned with the features currently enabled in Counso.

The goal is to make each interaction more useful: choose the right Agent, give it focused context, set the right depth, and formalize repeated work when it improves the outcome.
