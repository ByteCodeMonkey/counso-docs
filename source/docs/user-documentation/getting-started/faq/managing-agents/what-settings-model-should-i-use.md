> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# What settings / model should I use?

* **Instructions**: write clear, detailed prompts for the agent. Check [Prompting 101: How to Talk to Your Agents](/docs/user-documentation/agents/llm-best-practices/how-to-write-effective-instructions) for more advice.
* **Advanced** > **Model selection**: choose the model the agent runs on, and its reasoning effort.

## Which model should I choose?

Start with an auto model, and use **Standard** unless you have a reason not to. The [auto models](/docs/user-documentation/agents/model-selection#auto-models) page explains which one to use for different kinds of work.

Pick a specific model only when you need a guarantee that the agent always runs on one exact model, for example to reproduce a known output.

## What reasoning effort should I set?

Reasoning effort only applies when you pick a specific model, and only the levels that model supports are selectable. See [Reasoning effort](/docs/user-documentation/agents/model-selection#reasoning-effort) for the levels and their tradeoffs.

## Can I change the model without editing the agent?

Yes. Use the model picker in the composer. It applies to your next message in that conversation only and leaves the agent untouched.
