---
title: "Write effective Agent instructions"
---
Instructions describe how an Agent should handle a recurring task. Write them as if you were briefing a capable colleague who does not already know your process: be direct, give relevant context, and say what a useful result looks like. Sidekick can help draft or refine instructions, but review every suggestion before saving it.

## A practical structure

Include the parts that matter for your use case:

- **Role and goal:** who the Agent is helping and what it should accomplish.
- **Process:** the steps to follow, if the work has a repeatable sequence.
- **Expertise and context:** the policies, definitions, audience, or examples the Agent needs.
- **Constraints:** what sources to use, what not to assume, and what to do when evidence is missing or inconsistent.
- **Output:** the format, level of detail, and fields the answer should contain.

For example, instead of “review these invoices,” specify which period and files to review, the fields to compare, how to report discrepancies, and which conclusions must be left for a person to confirm.

## Keep instructions usable

Use specific language rather than a string of search keywords. Give only context that changes the answer; a longer instruction is not automatically better. Examples are useful when they show a preferred format or distinguish a correct answer from a weak one. Break a complex process into clear steps, but avoid writing hidden-reasoning requests.

## Test and revise

Try several representative requests, including one with incomplete information. Check whether the Agent uses the intended sources, follows the requested format, and asks for clarification where needed. If it misses, change one part of the instructions at a time and repeat the test. Keep the instructions focused on the Agent's intended user and task.

For the initial build flow, see [Create your first Agent](/docs/user-documentation/agents/create-your-first-agent).
