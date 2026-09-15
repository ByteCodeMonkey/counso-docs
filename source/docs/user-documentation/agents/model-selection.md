> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Auto models and the model picker

> Choose a model for a conversation or agent, or let Dust maintain a model choice for you.

Every agent runs on a model. In Dust, you can choose that model in two places:

* The **model picker in the composer** changes the model for your next message in that conversation, without editing the agent.
* **"Standard" > pick your model** in the instructions of the agent builder sets the model an agent uses by default.

Both places offer three **auto models**, **Basic**, **Standard**, and **Premium**, as well as specific models from individual providers.

<Info>
  **The auto-model levels are not the same as model access tiers.** The picker’s **Basic**, **Standard**, and **Premium** are curated choices. Administrators use [model access tiers](/docs/user-documentation/admins/usage-seats-and-credits/model-access-tiers) to control individual models, reasoning efforts, and auto-model choices. The access-tier settings therefore cover more options than the three auto-model levels shown here.
</Info>

## Auto models

An auto model is a curated, ordered list of model and reasoning-effort combinations maintained by Dust. Dust periodically benchmarks the available candidates and updates each list when the preferred model changes. When you send a message, Dust uses the first candidate on the selected list that is available to your workspace.

Auto models do not analyze each request and choose a different model based on the task. They give you a maintained choice at a defined capability and cost level, so you do not need to update every agent when models change or a provider becomes unavailable.

### Basic

Basic is the lower-cost option for well-defined, repetitive, and high-volume work.

| Order | Model                 | Reasoning effort |
| ----- | --------------------- | ---------------- |
| 1     | GPT 5.6 Luna          | Light            |
| 2     | Claude Sonnet 4.6     | Light            |
| 3     | Gemini 3.7 Flash      | Light            |
| 4     | Gemini 3.1 Flash Lite | Medium           |
| 5     | Mistral Small         | None             |

### Standard

Standard is the default for most everyday work.

| Order | Model                 | Reasoning effort |
| ----- | --------------------- | ---------------- |
| 1     | GPT 5.6 Luna          | High             |
| 2     | Claude Sonnet 4.6     | Medium           |
| 3     | Gemini 3.1 Pro        | Light            |
| 4     | Gemini 3.1 Flash Lite | Light            |
| 5     | Mistral Medium 3.5    | None             |
| 6     | Mistral Small         | None             |

### Premium

Premium is for demanding work that benefits from stronger reasoning or more capable models.

| Order | Model           | Reasoning effort |
| ----- | --------------- | ---------------- |
| 1     | Claude Opus 5   | High             |
| 2     | Claude Opus 4.8 | High             |
| 3     | GPT 5.6 Sol     | Medium           |
| 4     | Gemini 3.1 Pro  | Medium           |
| 5     | Mistral Large   | None             |

The lists and their order can change as Dust benchmarks models, providers change their pricing or reliability, and new models become available. If a candidate is unavailable because of your region, plan, provider access, or administrator settings, Dust continues to the next available candidate on that list.

## What changed

1. **A model picker in the composer.** Click the model icon to choose a model for any conversation, with any agent, including the default `@dust` agent.
2. **Basic, Standard, and Premium auto models.** Dust maintains a list of preferred model and reasoning-effort combinations for each level, based on periodic benchmarking and ongoing model availability. Dust does not route each request according to the task. It keeps the list current for you, so you do not have to update models used by specific agents or change them when a provider becomes unavailable.
3. **The global model agents changed place.** They no longer appear in your agent list. Model choice now lives in the model picker.

## Were the models removed?

No. The models that powered the global model agents are still available through the model picker when your plan and administrator settings allow them. The retired agents were wrappers around a model with access to internet search, rather than full agents with their own instructions, tools, or company knowledge.

## How to use a specific model now

* **For one conversation:** Click the model icon in the composer, choose **More models**, and select the model you want. You can also type `/` in the composer and select **Pick model**.
* **For a persistent setup:** Open Agent Builder, then select a specific model in the agent's settings. That agent will keep using that model until you change it.

For most queries, we recommend **Standard**. Dust maintains and periodically reviews the candidate lists, but the selected auto model does not change based on the content of an individual request.

## Why we made this change

The retired global model agents were wrappers around a model with access to internet search, not agents with their own instructions, tools, or company knowledge. Agents and models are different things: agents combine a model with instructions, tools, and company knowledge, while the model provides the underlying intelligence. Moving model choice into the picker means any agent can use any available model, and Dust can maintain the curated auto-model lists without asking you to migrate each agent.

## My workspace has the `@dust` agent disabled

The model picker works with any agent, not only `@dust`. Use it with a custom agent, or create a simple agent in Agent Builder and choose its model there. Administrators can also re-enable `@dust` from workspace settings.

## Use the model picker in a conversation

1. Open any conversation, including one with the default `@dust` agent.
2. Click the model button in the composer, next to the send button.
3. Pick **Basic**, **Standard**, or **Premium**, or choose **More models** and select a specific model.
4. Send your message.

The picker applies to your next message in that conversation only. It does not modify the agent, affect other members, or change scheduled runs. If you do not use the picker, the agent runs on its configured model.

## What happens to existing agents?

* Custom agents where the builder selected a specific model keep that model. Nothing changes.
* Custom agents where the builder did not select a specific model previously followed the global `@dust` agent's model, but were pinned to it. They now run on **Standard**.

## Set the model of an agent

1. Open the agent in Agent Builder.
2. In the **Instructions** section, click the button named after the current model (defaults to "Standard").
3. Pick an auto model or a specific model, then save.

Choosing a specific model pins the agent to that model. Choosing an auto model means the agent follows the corresponding maintained list as Dust updates it.

## Reasoning effort

When you select a specific model, you can also choose how much reasoning effort it spends before answering:

| Effort     | Behavior                                                                     |
| ---------- | ---------------------------------------------------------------------------- |
| **None**   | No additional reasoning, for the fastest responses.                          |
| **Light**  | Light reasoning effort, for faster responses.                                |
| **Medium** | Medium reasoning effort, balancing speed and quality.                        |
| **High**   | High reasoning effort, with longer wait times and more deliberate reasoning. |

Only the levels a model supports are selectable. Reasoning effort also affects credit consumption and the [model access tier](/docs/user-documentation/admins/usage-seats-and-credits/model-access-tiers) for that model. The same model can appear in different tiers at different reasoning efforts.

Reasoning effort is part of each auto model entry, so the reasoning-effort control does not apply to **Basic**, **Standard**, or **Premium**. For example, GPT 5.6 Luna appears in Basic at Light effort and in Standard at High effort.

## Availability

* The model picker is available in the composer and Agent Builder when the feature is enabled for your workspace.
* Premium models and reasoning-effort combinations require a usage-based credit plan.
* Administrators can cap the model access tier available to each member. A cap applies to individual models, reasoning efforts, and the corresponding auto-model choice. See [Model access tiers](/docs/user-documentation/admins/usage-seats-and-credits/model-access-tiers).
* Model availability depends on your workspace, plan, region, provider availability, and administrator settings. The picker shows the options available to you.

## FAQ

### Does switching models in the composer change the agent for everyone?

No. A pick in the composer applies to your next message in that conversation only. The agent's own configuration is untouched, and no other member sees a change. To change an agent for everyone, edit it in Agent Builder.

### How does Dust choose the model behind Basic, Standard, and Premium?

Dust maintains one ordered candidate list for each auto model. The lists reflect periodic benchmarking and Dust's assessment of model quality, cost, and availability. Dust uses the first candidate on the selected list that is available to your workspace. The choice does not depend on the content of your request. If a candidate is unavailable, Dust uses the next available candidate on the same list.

### Can I pin an agent to one exact model?

Yes. In Agent Builder, on the Instructions > "Standard" or the specific model name. That agent then uses that model for every member and run, subject to plan and administrator access rules.

### What happened to the global model agents?

They were retired from the agent list. Their underlying models remain available through **More models** in the picker when your plan and administrator settings allow them.

### My agent was on a specific model. Did it move to Standard?

Agents that used the previous default model moved to **Standard**. Agents pinned to a different specific model kept that model. You can change the model powering an agent at any time in Agent Builder.

### Why is a model or auto model locked in my picker?

Your workspace may be on a legacy plan that does not include premium combinations, or your administrator may have capped your model access tier below that model or auto model. See [Model access tiers](/docs/user-documentation/admins/usage-seats-and-credits/model-access-tiers).

### What does "Model tier not enabled" mean when I run an agent?

The agent is configured to run on a model and reasoning effort above the tier your administrator allows for you. Ask your administrator to raise your tier, enable published agents to run above member tiers, or use another agent.

### Does the model picker apply to Slack, triggers, or the API?

**Slack and triggers:** A pick in the composer is scoped to that conversation in the Dust web app. An agent that runs from Slack or a trigger uses its configured model.

**The API:** [Create a new conversation](/api-reference/conversations/create-a-new-conversation) and [Create a message](/api-reference/conversations/create-a-message) accept an optional `modelSelection` object that overrides the model for the agents mentioned in that message:

```json theme={null}
{
  "modelSelection": {
    "providerId": "anthropic",
    "modelId": "claude-sonnet-4-20250514",
    "reasoningEffort": "medium"
  }
}
```

* `providerId` and `modelId` are required. `reasoningEffort` is optional.
* Omit `modelSelection` and each agent runs its configured model.
* The override applies to that message only, exactly like a pick in the composer. It does not modify the agent.
* The same access rules apply as in the app. A model that your workspace or model access tier does not allow is rejected with a `400` (`model_disabled`) rather than silently falling back to the agent's model. A malformed object also returns a `400`.
* If the model picker is not enabled for your workspace, the request returns a `403`.

## Questions?

Reach out to [support@dust.tt](mailto:support@dust.tt), or ask the `@help` agent directly in Dust.
