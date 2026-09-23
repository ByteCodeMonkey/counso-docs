---
title: "Model access tiers"
---
If the **Models tier** controls are available in your workspace, administrators can limit which models and reasoning settings members can select. This is a ceiling on model choice, not a seat or credit allocation. It can help reserve higher-capability options for work that needs them while leaving routine work on the options appropriate to the team.

## Understand the tiers

The workspace may group model and reasoning combinations into ordered tiers such as **Basic**, **Standard**, and **Premium**. The current model picker and its tier information show which combinations belong to each level. These assignments can change as model availability and workspace configuration change; use the live list rather than a copied model inventory.

A tier can apply to a specific model and reasoning setting together. The same model may therefore be available at one reasoning level and restricted at another. The ceiling may also apply to the corresponding automatic model choice, not just to named models.

## Current options in each tier

The following list reflects the model-tier information panel as of September 14, 2026. Provider availability and workspace configuration can change it. An asterisk marks an option that may depend on workspace configuration or plan eligibility; use the live picker as the final source of truth.

### Basic

| Model | Reasoning efforts in this tier |
| --- | --- |
| Claude 4.5 Haiku | Light, Medium, High |
| Claude Sonnet 4.6 | Light |
| Claude Sonnet 5 | Light |
| DeepSeek V4.1 Flash (Fireworks) | None, Light, Medium, High |
| Gemini 3.1 Flash Lite | None, Light, Medium |
| Gemini 3.5 Flash Lite | None, Light, Medium |
| Mistral Codestral | None |
| Mistral Small | None |
| GPT-5.4 Mini | None, Light, Medium, High |
| GPT-5.4 Nano | None, Light, Medium, High |
| GPT 5.6 Luna | None, Light |
| GLM-5.3 Flash (Fireworks) | Light, Medium, High |

### Standard

| Model | Reasoning efforts in this tier |
| --- | --- |
| Claude Sonnet 4.6 | Medium |
| Claude Sonnet 5 | Medium |
| Inkling (Fireworks) | Light, Medium, High |
| Kimi K3 (Fireworks) | Light |
| GLM-5.3 (Fireworks) | Light, Medium, High |
| Gemini 3.1 Flash Lite | High |
| Gemini 3.1 Pro (Preview) | Light |
| Gemini 3.5 Flash Lite | High |
| Gemini 3.7 Flash | Light, Medium |
| Gemini 3.8 Flash | Light, Medium |
| Mistral Large | None |
| Mistral Medium 3.5 | None |
| GPT 5.6 Luna | Medium, High |
| GPT 5.6 Sol\* | None |
| GPT 5.6 Terra | None, Light, Medium, High |
| Grok 4.5\* | Light, Medium, High |
| Grok 4.6\* | Light, Medium |

### Premium

| Model | Reasoning efforts in this tier |
| --- | --- |
| Claude Opus 4.6 | Light, Medium, High |
| Claude Sonnet 4.6 | High |
| Claude Sonnet 5 | High |
| Kimi K3 (Fireworks) | Medium, High |
| Gemini 3.1 Pro (Preview) | Medium, High |
| Gemini 3.7 Flash | High |
| Gemini 3.8 Flash | High |
| Mistral Medium 3.5 | High |
| GPT 6 Astra\* | Light, Medium, High |
| GPT 5.6 Sol\* | Light, Medium, High |
| GPT 5.6 Terra (long context)\* | None, Light, Medium, High |
| Grok 4.6\* | High |

## Set the workspace ceiling

1. Open **Admin > Usage** and find **Models tier**, if available.
2. Set **Workspace access** to the highest level members should be able to select.
3. Leave groups or individual members on **Inherit** to use the next applicable setting.

A workspace setting applies to members without a more specific override. Check the options presented in the workspace before changing the ceiling; the available tiers depend on current plan and model configuration.

## Set group or member overrides

On the same page, use the groups table to set a ceiling for a team. **Inherited from workspace** means the group uses the workspace setting. Use the members table to apply a setting to one person; **Inherit** means the member follows their group or, if none applies, the workspace.

The effective ceiling is resolved as follows:

1. A member-specific override takes precedence.
2. Otherwise, if the member belongs to groups with overrides, the highest of those tiers applies.
3. Otherwise, the workspace ceiling applies.

A group override grants that level to its members; it does not lower the ceiling for members who belong to another, higher-tier group. Set a member override when one person needs a different limit.

## Published agents

A member below an agent's configured model tier may be prevented from running that agent. If the **Published agents** option is available and enabled, published agents can run for members even when their configured model exceeds the member's personal selection ceiling. Members still cannot select that higher model themselves; unpublished or personal agents remain subject to the ceiling, and creating or editing an agent above it may be blocked.

Before relying on this exception, review who can publish agents and confirm that the published workflow is appropriate for its audience.

## What members see and how to review changes

Models or reasoning settings above a member's ceiling may appear locked in the picker. Automatic model choices above the ceiling may also be locked rather than silently choosing a lower level. An attempt to run an agent above the permitted ceiling can show a model-access warning.

Changes to workspace, group, or member ceilings may appear in the audit log if that feature is enabled. Review the entry after making a change, then test the affected selection with a member in the relevant group.

Model tiers limit which models members can choose; they do not by themselves set a credit budget or guarantee a particular reduction in usage. See [Optimize credit consumption](/docs/user-documentation/admins/usage-seats-and-credits/optimize-credit-consumption) for other controls.
