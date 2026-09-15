---
title: "Review Skill improvement suggestions"
---
When **Self-improving Skills** is enabled, the workspace can analyze conversations where Skills were used and suggest changes to those Skills. Signals may include explicit feedback, corrections to an Agent's answer, a capability that was not used when needed, or a conversation that went off track. Suggestions are intended to help Skill editors improve recurring guidance; they do not update a Skill until an editor approves a change.

## Review a suggestion

1. Open the Skill in Skill Builder and inspect the suggestions in the side panel.
2. Read the proposed diff and identify the behavior it would change.
3. Choose **Approve** to apply the change, or **Decline** to dismiss it.
4. After approval, test the updated Skill on a representative task and review its new version in history.

Suggestions may propose revised instructions or changes to the Tools used by a Skill. Consider whether the proposal is correct for the Skill's audience and access scope before accepting it.

## Control the feature

The feature is optional. An administrator can turn it off in workspace settings; an individual Skill may also have its own self-improvement control. Disabling the workspace feature stops conversation analysis and new suggestions. Disabling it for one Skill leaves the workspace setting unchanged.

## Data and processing

The analysis may use conversation messages, Tool calls and Agent responses, user feedback, and the current Skill instructions and Tools. It uses the model providers configured for the workspace. Enable it only after reviewing the workspace's applicable data-processing, notice, access, and retention requirements. Suggestions and analysis records are stored within the workspace's governance scope. This feature proposes changes to workspace Skills; it is not intended to train a general-purpose model on the conversations.

## Processing modes and credits

Analysis is scheduled nightly. The default batch mode sends work for asynchronous processing; providers may take up to 24 hours to complete a batch. Suggestions therefore do not necessarily appear immediately after feedback.

Batch processing temporarily stores requests and results with the provider. Do not assume that a zero-data-retention arrangement for interactive calls also covers batch jobs. If the workspace offers the batch-mode control, an administrator can turn batch mode off while keeping Skill improvement active; analysis then uses synchronous streaming calls. Whether those calls qualify for zero data retention depends on the provider and your workspace agreement. For a strict requirement, confirm that configuration or disable self-improvement.

Analysis consumes workspace credits. Check Usage and the workspace's current pricing for the charge; streaming and batch processing can have different costs.

## Keep human review in the loop

A suggestion can generalize from a particular conversation or reflect a one-off preference. Accept it only when the change expresses a repeatable rule for the Skill's intended users. Continue to review unusual outcomes manually, and use Skill history to understand or reverse a change.
