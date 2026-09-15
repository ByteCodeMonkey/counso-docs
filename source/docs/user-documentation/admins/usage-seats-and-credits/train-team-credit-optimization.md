> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Train your team on credit optimization

Credit optimization is the practice of getting the best possible output from every credit spent. It is about matching the right model, context, tools, and workflow design to each task so that your team maximizes results without waste.

This guide covers how to train employees, builders, managers, and admins on the habits that make AI usage efficient at scale: prompting defaults, model selection, workflow formalization, builder standards, and recurring review rhythms.

## Frame the training around output quality

The framing of credit optimization training determines how people behave afterward.

If the training is positioned as cost control, people hesitate before using useful agents, builders avoid ambitious workflows, and managers treat high consumption as suspicious before understanding whether the workflow is valuable.

Position it instead as workflow quality: getting better results from better-designed interactions with agents.

| Avoid this framing          | Use this framing                                     |
| --------------------------- | ---------------------------------------------------- |
| "You used too many credits" | "Which workflows are producing the most value?"      |
| "Who spent the credits?"    | "Which agents are driving the best outcomes?"        |
| "Can we cut usage?"         | "Where can we get the same result more efficiently?" |
| "Why is this expensive?"    | "Is the model and depth matched to the task?"        |

## Teach prompting defaults before teaching the dashboard

Most employees do not need to understand tokens, model pricing, or retrieval mechanics. They need a simple mental model:

AI consumption is shaped by workflow design.

A vague request makes the agent do more guessing. A broad agent may retrieve more noise. A long conversation can carry irrelevant context. A deep workflow does more work than a lightweight first pass. An automation multiplies whatever design choices were made before it launched.

Once people understand that, credit optimization becomes a question of shaping the work better, not spending less.

### What to teach

For new users, teach concrete prompting defaults.

| Instead of                         | Train                                                                                                                                                                                                |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "Analyze this."                    | "Summarize this in 5 bullets for a sales manager. Focus only on risks, next steps, and open questions. Do not do extra research unless the document is insufficient."                                |
| "Do a deep dive on this customer." | "Give me a lightweight account brief first: company context, recent interactions, open risks, and 3 suggested next steps. If the signal is weak, tell me what would justify a deeper investigation." |
| "Use everything you can find."     | "Use CRM and call notes first. Only search Slack if the answer is missing recent context."                                                                                                           |

These prompts produce better output. They tell the agent what work matters, where to look, how much depth to use, and when to stop. See [How to write effective instructions](/docs/user-documentation/agents/llm-best-practices/how-to-write-effective-instructions) for more guidance.

### Simple user guidance

| Situation                | Habit                                   |
| ------------------------ | --------------------------------------- |
| New topic                | Start a new conversation                |
| Repeated task            | Use an agent                            |
| Same project, continuing | Keep the thread, compact when useful    |
| Large document           | Use the source instead of pasting       |
| Short answer needed      | Ask for a short answer                  |
| Complex investigation    | Use Go Deep or a stronger model         |
| Simple task              | Use a lighter model or a standard agent |

## Teach when to go deep

Deep workflows produce high-value output. They also consume more credits by design.

A deep dive should be treated like sending a senior analyst into a problem, not like asking for a quick summary. It is the right choice when the question is complex, the answer depends on multiple sources, the stakes are high, or the user needs synthesis rather than retrieval.

[Go Deep](/docs/user-documentation/agents/go-deep) gives agents the ability to conduct in-depth research across company data, databases, and web sources. It includes sub-agents, company data exploration, data warehouse queries, and web search and browsing.

### Good reasons to use deep research or a stronger model

* Preparing for a high-stakes customer meeting.
* Investigating a complex support issue across multiple sources.
* Synthesizing conflicting evidence.
* Drafting executive-ready recommendations.
* Comparing strategic options with tradeoffs.
* Turning a messy set of inputs into a clear decision memo.

### Less suitable use cases

* Summarizing a short document.
* Rewriting a message.
* Formatting notes.
* Classifying a list.
* Extracting fields from a document.
* Asking for a first-pass opinion.

### The habit to train

**First pass first. Deep dive second.**

Start lightweight, then escalate only if the first pass shows the problem deserves it. A stronger model is a tool for a class of work. If the task is simple, it may produce a slightly more polished answer at a higher cost without changing the business outcome. See [What settings and model should I use?](/docs/user-documentation/getting-started/faq/managing-agents/what-settings-model-should-i-use) for guidance on model selection.

## Teach when to use a skill, an agent, or a chain

As teams get more advanced, users start chaining things manually. They ask one agent to search, then another to summarize, then another to rewrite, then paste the output into a new conversation for a final draft.

Sometimes this is useful exploration. Often, it is a sign that the workflow should be formalized.

### Three modes to distinguish

| Mode                           | When to use                     | Example                                                                                              |
| ------------------------------ | ------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **Normal agent**               | The task is known and contained | "Prepare a customer meeting brief," "summarize this support thread," "draft a follow-up email"       |
| **Skill or reusable workflow** | The process is repeatable       | The same sequence happens every week, or multiple people are chaining the same steps                 |
| **Chaining**                   | The work is exploratory         | The user is figuring out the problem, comparing approaches, or doing a one-off complex investigation |

### Simple rule

If you chain it twice, consider turning it into a workflow. If a team chains it repeatedly, formalize it.

Manual chaining often hides cost. Each step can add context, trigger tools, use a strong model, or create another long conversation. A reusable workflow can be designed more carefully: lighter models for simple steps, better source scoping, clearer tool usage, and a cleaner output.

[Skills](/docs/user-documentation/agents/skills/skill-examples) in Dust are reusable packages of instructions, knowledge, and tools that you can share across multiple agents. When you update a skill's instructions, every agent using that skill automatically gets the improvement.

## Retrain existing users on better habits

Existing users already have habits, and many of those habits were rational when they formed. They use the general agent because it worked. They paste documents because they want to be sure the agent has context. They reuse long conversations because it feels convenient. They ask for deep research because they associate depth with quality.

The goal is to help them refine those habits as usage scales.

### What to do

Use real examples from your workspace to show better alternatives:

| Current pattern                                      | Better alternative                                                             |
| ---------------------------------------------------- | ------------------------------------------------------------------------------ |
| A broad agent used as the default for too many tasks | A specialized agent that gets to a better answer faster                        |
| A long thread carrying old context                   | A fresh conversation that produces a more focused result                       |
| An automation that worked on ten rows                | An automation with an owner and volume estimate before running on ten thousand |
| A premium model used for simple triage               | A workflow split into a lighter first pass and a stronger final synthesis      |

People learn faster from patterns than from policy.

## Train builders with a deeper curriculum

End-user habits matter, but builder habits scale further.

A user can make one conversation inefficient. A builder can make hundreds of future runs inefficient by choosing the wrong model, attaching too many sources, giving an agent too many tools, or leaving instructions too vague.

### Builder training checklist

| Question to ask                                                      | What it covers         |
| -------------------------------------------------------------------- | ---------------------- |
| Which steps are simple enough for a lighter model?                   | Model routing          |
| Which steps genuinely need a stronger model?                         | Model routing          |
| Which sources should be searched first?                              | Data scoping           |
| Which sources should not be attached by default?                     | Data scoping           |
| Which tools are central to the workflow?                             | Tool discipline        |
| Which tools are just there "in case"?                                | Tool discipline        |
| Should this be one broad agent, or two narrower agents?              | Agent design           |
| Should this be a reusable skill instead of repeated manual chaining? | Workflow formalization |
| What does a good output look like on 10 real examples?               | Testing                |

For builders, credit optimization is product design. Every agent has a usage profile. Every model choice, data source, tool, and instruction changes that profile. See [How to write effective instructions](/docs/user-documentation/agents/llm-best-practices/how-to-write-effective-instructions), [model settings](/docs/user-documentation/getting-started/faq/managing-agents/what-settings-model-should-i-use), and [agent troubleshooting](/docs/user-documentation/agents/troubleshooting-your-agent) for details.

### Builder best practices

* Use lighter models for structured or repetitive tasks when the output remains reliable.
* Connect only the sources that matter for the agent's job.
* Remove tools that are not central to the workflow.
* Write clear, specific instructions; vague instructions make agents do more guessing. See [How to write effective instructions](/docs/user-documentation/agents/llm-best-practices/how-to-write-effective-instructions).
* Test model changes on real examples before changing an important workflow.
* Use [skills](/docs/user-documentation/agents/skills/skill-examples) to share instructions and tools across multiple agents.

## Help managers focus on workflow quality

Managers set the tone for how the team approaches credit optimization.

If they frame it as cost control, people become cautious. If they frame it as workflow quality, people become more intentional about how they use agents.

### Better manager questions

| Instead of asking              | Ask                                                                    |
| ------------------------------ | ---------------------------------------------------------------------- |
| "Who used the credits?"        | "Which workflows are creating the most value?"                         |
| "Why is this expensive?"       | "Which agents are slow, repetitive, or too broad?"                     |
| "Who is spending too much?"    | "Where are people retrying the same task?"                             |
| "Can we cut usage?"            | "Where are people manually chaining steps that should become a skill?" |
| "Is this automation worth it?" | "Which automations need an owner before they scale?"                   |

These questions keep the conversation focused on work design and make optimization collaborative.

## Make credit optimization a recurring ritual

Credit optimization should be a normal operating habit, not a reaction to a surprise.

| Cadence       | What to do                                                                                                                                                                                                                                                                      |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Weekly**    | Admins review the shape of usage: top agents, top sources, programmatic growth, expensive model usage, deep research usage, and sudden changes. See [Analytics](/analytics) and [Credit management](/docs/user-documentation/admins/usage-seats-and-credits/credit-management). |
| **Monthly**   | Inspect the top workflows and identify one concrete improvement.                                                                                                                                                                                                                |
| **Quarterly** | Refresh the agent map, review automation ownership, retire unused agents, and retrain teams on the habits that matter most.                                                                                                                                                     |

## Training assets to create

Keep the assets simple and practical.

| Asset                       | What it contains                                                                                                                                                                |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Agent map**               | Which agent to use for which workflow, so employees always know where to start.                                                                                                 |
| **User cheat sheet**        | Examples of lightweight prompts, deep-dive prompts, and "when to start fresh" guidance.                                                                                         |
| **Builder checklist**       | Model choice, data scope, tools, instructions, output length, test examples, and whether a repeated chain should become a skill.                                                |
| **Automation checklist**    | Owner, expected volume, test batch, cost per run, failure behavior, and monitoring. See [trigger rate limits](/docs/user-documentation/agents/triggers/webhooks/rate-limiting). |
| **Monthly review template** | A standard format so credit optimization becomes a normal operating habit rather than a one-off investigation.                                                                  |

## Summary

Credit optimization is learned behavior. People learn it through onboarding, examples, manager language, builder standards, and recurring rituals.

The goal is not to reduce AI usage. It is to maximize the value of every interaction: use the right agent, ask the right-sized question, choose depth intentionally, turn repeated chains into workflows, and match the model to the task.

Credit optimization is what AI adoption needs once it starts working.
