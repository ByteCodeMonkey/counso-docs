> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Model access tiers

> Restrict which models and reasoning efforts your members can select, for the whole workspace, a group, or one member.

Members can pick the model an agent runs on from the composer and Agent Builder. See [Auto models and the model picker](/docs/user-documentation/agents/model-selection).

As an administrator, you can cap how far up the model list each member can go. This lets you keep everyday work within a defined cost range while reserving higher-cost options for members who need them.

<Info>
  **Model access tiers are broader than the auto-model levels in the picker.** Here, **Basic**, **Standard**, and **Premium** are administrator controls that apply to individual models, reasoning-effort combinations, and the corresponding auto models. The picker’s **Basic**, **Standard**, and **Premium** are curated auto-model choices, not the complete set of models and reasoning efforts that these controls cover. For the curated auto-model lists, see [Auto models and the model picker](/docs/user-documentation/agents/model-selection).
</Info>

## The three tiers

Every model and supported reasoning effort belongs to one tier. The same model can appear in more than one tier because its tier can change with the reasoning effort.

| Tier         | What it contains                                                                         |
| ------------ | ---------------------------------------------------------------------------------------- |
| **Basic**    | Lower-cost model and reasoning-effort combinations for well-defined and repetitive work. |
| **Standard** | Everyday model and reasoning-effort combinations for most work.                          |
| **Premium**  | Higher-cost combinations for demanding work that benefits from stronger capabilities.    |

Tiers are cumulative. **Up to Standard** grants access to Basic and Standard. **Up to Premium** grants access to all three tiers, which is the default for every workspace.

<Note>
  The selector applies to every option in the selected category, not only to the three auto-model rows. It controls individual models, their supported reasoning efforts, and the corresponding Basic, Standard, or Premium auto model. A model can remain selectable at one reasoning effort while another effort on the same model is disabled.
</Note>

## Current options in each tier

The lists below match the model options shown by the model-tier information panel as of September 14, 2026. They include the model and reasoning-effort combinations currently assigned to each tier. Dust can change these assignments as providers release models, update pricing, or change availability.

*Asterisks mark models that depend on workspace configuration or plan eligibility.*

### Basic

| Model                           | Reasoning efforts in this tier |
| ------------------------------- | ------------------------------ |
| Claude 4.5 Haiku                | Light, Medium, High            |
| Claude Sonnet 4.6               | Light                          |
| Claude Sonnet 5                 | Light                          |
| DeepSeek V4.1 Flash (Fireworks) | None, Light, Medium, High      |
| Gemini 3.1 Flash Lite           | None, Light, Medium            |
| Gemini 3.5 Flash Lite           | None, Light, Medium            |
| Mistral Codestral               | None                           |
| Mistral Small                   | None                           |
| GPT-5.4 Mini                    | None, Light, Medium, High      |
| GPT-5.4 Nano                    | None, Light, Medium, High      |
| GPT 5.6 Luna                    | None, Light                    |
| GLM-5.3 Flash (Fireworks)       | Light, Medium, High            |

### Standard

| Model                    | Reasoning efforts in this tier |
| ------------------------ | ------------------------------ |
| Claude Sonnet 4.6        | Medium                         |
| Claude Sonnet 5          | Medium                         |
| Inkling (Fireworks)      | Light, Medium, High            |
| Kimi K3 (Fireworks)      | Light                          |
| GLM-5.3 (Fireworks)      | Light, Medium, High            |
| Gemini 3.1 Flash Lite    | High                           |
| Gemini 3.1 Pro (Preview) | Light                          |
| Gemini 3.5 Flash Lite    | High                           |
| Gemini 3.7 Flash         | Light, Medium                  |
| Gemini 3.8 Flash         | Light, Medium                  |
| Mistral Large            | None                           |
| Mistral Medium 3.5       | None                           |
| GPT 5.6 Luna             | Medium, High                   |
| GPT 5.6 Sol\*            | None                           |
| GPT 5.6 Terra            | None, Light, Medium, High      |
| Grok 4.5\*               | Light, Medium, High            |
| Grok 4.6\*               | Light, Medium                  |

### Premium

| Model                          | Reasoning efforts in this tier |
| ------------------------------ | ------------------------------ |
| Claude Opus 4.8\*              | Light, Medium, High            |
| Claude Opus 5\*                | Light, Medium, High            |
| Claude Sonnet 4.6              | High                           |
| Claude Sonnet 5                | High                           |
| Kimi K3 (Fireworks)            | Medium, High                   |
| Gemini 3.1 Pro (Preview)       | Medium, High                   |
| Gemini 3.7 Flash               | High                           |
| Gemini 3.8 Flash               | High                           |
| Mistral Medium 3.5             | High                           |
| GPT 6 Astra\*                  | Light, Medium, High            |
| GPT 5.6 Sol\*                  | Light, Medium, High            |
| GPT 5.6 Terra (long context)\* | None, Light, Medium, High      |
| Grok 4.6\*                     | High                           |

The three auto models are separate curated choices in the picker. **Basic** corresponds to the lower-cost auto model, **Standard** to the default auto model, and **Premium** to the higher-capability auto model. They are also gated by the member's maximum tier.

## Set the workspace ceiling

1. Go to **Admin** > **Usage**.
2. In the **Models tier** section, set **Workspace access** to the highest tier available to members of the workspace.
3. The change applies to every member who has no group or personal override.

The default is **Up to Premium**, so nothing is restricted until you lower it.

## Override for a group

On the same **Usage** page, the groups table lets you set a tier per group. A group set to **Inherited from workspace** follows the workspace ceiling.

Group overrides let you give a specific team access to Premium options while the rest of the workspace stays on Standard.

## Override for a member

The members table on the **Usage** page lets you set a tier for one member. Leaving a member on **Inherit** makes them follow their groups, or the workspace if they have no group override.

## How the ceiling is resolved

Dust resolves one ceiling per member, in this order:

1. **Member override**, if set. It wins over everything else.
2. **Group overrides**, if the member belongs to at least one group with an override. When a member is in several such groups, the highest of those tiers applies.
3. **Workspace access**, otherwise.

## Let members run published agents above their tier

Restricting a member also restricts the agents they can run. If an agent is configured on a model and reasoning effort above the member's ceiling, the run is blocked with **Model tier not enabled**.

That can be too strict for a well-built shared agent that deliberately uses a stronger model. In the **Models tier** section, enable **Published agents** to let every member run published agents regardless of the agent's model tier, while still capping what they can select themselves.

With **Published agents** enabled:

* Published agents run normally for everyone.
* Unpublished and personal agents remain restricted to the member's ceiling.
* Creating or editing an agent on a model above the member's ceiling remains blocked.

## What members see

* In the model picker, individual models and reasoning efforts above their ceiling are visible but locked, with a tooltip telling them to contact their administrator.
* Auto-model rows above their ceiling are also locked. They do not silently downgrade to another auto model.
* When members try to run an agent above their ceiling, they get a **Model tier not enabled** message naming the agent.

## Audit trail

Changes to model tier settings are recorded in your [audit logs](/docs/user-documentation/admins/audit-logs/audit-logs), so you can see who changed a workspace, group, or member ceiling and when.

## Availability

Model access tiers are available on usage-based credit plans. On legacy plans, premium model and reasoning-effort combinations are not selectable through the model picker, and there is no tier setting to configure.

## FAQ

### Do I have to configure anything for members to use the latest models?

No. Every workspace starts at **Up to Premium**, which restricts nothing. Configure tiers only if you want to limit what members can select.

### Why does the same model appear in more than one tier?

A tier applies to a model and a reasoning effort together. For example, Claude Sonnet 4.6 is Basic at Light effort, Standard at Medium effort, and Premium at High effort.

### Does the selector disable only the auto-model choices?

No. The tier ceiling applies to every model and reasoning-effort combination in that category, as well as to the corresponding auto model. If you cap a member at Standard, Premium model combinations and the Premium auto model are unavailable to that member.

### Does restricting tiers break agents that were already built on Premium models?

The agents keep their configuration. What changes is who can run them: a member below the required tier is blocked unless the agent is published and you have enabled **Published agents**.

### What happens when a member belongs to two groups with different tiers?

The highest of the two applies. Group overrides grant access; they do not subtract it. To cap one specific person below their groups, set a member override.

### Can I restrict a single person rather than a group?

Yes. Set a tier directly on that member in the members table on the **Usage** page. A member override takes precedence over their groups and the workspace ceiling.

### Does this reduce credit consumption?

It caps the most expensive model and reasoning-effort combinations members can select on their own, which removes one source of unplanned spend. It is one lever among several. See [Optimize credit consumption](/docs/user-documentation/admins/usage-seats-and-credits/optimize-credit-consumption).
