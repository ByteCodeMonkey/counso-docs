> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# @sidekick agent

Sidekick is an AI assistant built into the Agent Builder that helps you create new agents and improve existing ones through conversation. Instead of staring at a blank instructions field, you describe what you want your agent to do and Sidekick drafts instructions, recommends tools and skills, and suggests improvements.

* **Creating a new agent from scratch.** Describe your use case in plain language and Sidekick will draft instructions, recommend tools and skills, and suggest a model.
* **Improving an existing agent.** Open any agent in the builder and Sidekick analyzes your current configuration (including instructions, tools, and skills), checks agent feedback and usage metrics, and proposes concrete improvements.
* **Starting from a template.** When you select a template from the gallery, Sidekick uses it as a guide and walks you through building a customized version tailored to your actual workflow.
* **Turning a conversation into an agent.** Had a great conversation in Dust? Turn it into a reusable agent in one click. Sidekick pre-loads the full conversation context and drafts an agent that replicates the same workflow.

## Starting from scratch

1. Navigate to **New Agent** in the Agent Builder.
2. In the Sidekick panel, describe what you want your agent to do. For example: "I want an agent that helps my team write weekly client updates based on our CRM data and Slack channels."
3. Sidekick asks clarifying questions if needed, then drafts a full set of instructions as inline suggestions.
4. For complex use cases, Sidekick may offer to research your workspace's data sources to better understand your business requirements. This takes a few minutes but can produce more tailored results than back-and-forth questions. You'll always be asked before Sidekick takes this step.
5. Review each suggestion: click **Accept** to apply it or **Reject** to dismiss it. You can also manually edit the instructions at any time. The form is never locked.
6. Sidekick recommends tools, skills, and a model. Each recommendation appears as a one-click approval

<aside>
  You retain full control at all times. Every change Sidekick proposes appears as a reviewable diff. Nothing is applied automatically.
</aside>

## Starting from a template

When you select a template from the gallery, you’re redirected to the Agent Builder with Sidekick pre-loaded with that template’s context. Instead of applying static instructions, Sidekick walks you through a conversation to produce a version customized to your needs.

The template gallery is still the best place to discover what kinds of agents you can build. Sidekick makes the output better by adapting templates to your specific workflow.

## Improving an existing agent

Open any agent in the Agent Builder. Sidekick reads your current configuration (including unsaved changes) and proactively suggests improvements:

When you open an existing agent, Sidekick automatically reviews user feedback (thumbs-up/thumbs-down ratings) and performance metrics for that agent. This means its suggestions are grounded in how the agent is actually performing, not just what the instructions say.

* Instruction rewrites or simplifications
* Missing tools or skills that could improve the agent
* Redundant sections that could be consolidated
* Available knowledge sources worth connecting

<aside>
  Sidekick is workspace-aware. It knows what tools, skills, and knowledge sources are available in your workspace and factors them into its recommendations.
</aside>

## Turning a conversation into an agent

If you've had a successful conversation in Dust and want to reuse that workflow, you can turn it into a new agent. Look for the `Convert to agent` button in the top right of any conversation (it appears after the first agent response). Clicking it opens the Agent Builder with Sidekick pre-loaded with the full context of that conversation, so it can draft an agent that replicates the same tools, knowledge, and instructions.

Sidekick proposals appear as inline diffs in the instruction form. Each suggestion shows what would change (additions in green, removals in red) and you explicitly **Accept** or **Reject** each one.

**Key behaviors:**

* **Non-blocking editing.** You can manually edit the instruction form while Sidekick is processing. If your manual edit conflicts with a pending Sidekick suggestion, the conflicting suggestion is automatically dismissed.
* **Durable suggestions.** If you leave the Agent Builder with pending suggestions, they’ll still be there when you come back.
* **Per-editor conversations.** If multiple builders open the same agent, each gets their own Sidekick conversation. Pending suggestions from all editors are visible to everyone.

<aside>
  Sidekick conversations are session-based and not persisted between visits. However, the suggestions themselves are saved: they persist independently of the conversation.
</aside>

## What Sidekick can do

* **Draft and edit agent instructions** via inline, accept/reject diffs
* **Recommend and add/remove tools, skills, and models** with one-click approval
* **List available knowledge sources** and suggest which to connect
* **Generate workflow visualizations** (mermaid diagrams) of agent logic on request
* **Suggest use cases** when starting from scratch, informed by templates and workspace context
* **Evaluate sub-agent fit**: if your agent uses other agents as tools, Sidekick understands both the top-level agent and its sub-agents and can assess whether the configuration is correct
* **Surface quick-action buttons** for common next steps, reducing the need to type responses
* **Research company knowledge** to find answers to your business requirements in order to ensure it’s building the agent based on team standards

## Current limitations

Sidekick is designed to assist with agent building inside the Agent Builder. There are a few things it doesn't do today:

* Sidekick works inside the Agent Builder only: you can't create agents from conversations or the API
* It cannot create or edit triggers (it will explain how to set them up manually)
* It cannot draft or build skills, though it can recommend existing ones
* It evaluates each agent individually: it doesn't orchestrate multi-agent workflows or suggest building new sub-agents
* Testing still requires switching to the Preview tab

## FAQ

**Does Sidekick change my existing agents?**

No. Sidekick is purely opt-in. It only makes suggestions when you’re actively in the Agent Builder, and nothing is applied without your explicit approval. Existing agents continue working exactly as before.

**Can Sidekick break my agent?**

Every change is presented as a reviewable diff. You accept or reject each suggestion individually. Nothing is applied automatically. You retain full manual control of the form at all times.

**Does Sidekick have access to my company data?**

Sidekick can see what knowledge sources, tools, and skills are available in your workspace to make recommendations. It can also read your company data sources to provide more informed suggestions. However, it cannot access data from restricted spaces. Sidekick does not automatically add data connections to your agent. That's always a manual step.

**Is the Sidekick conversation saved?**

Conversations are session-based and not persisted between visits. But suggestions are durable: if you leave the builder with pending suggestions, they’ll be there when you come back.

**Can multiple people use Sidekick on the same agent?**

Yes. Each builder gets their own conversation thread. They can see each other’s pending and historical suggestions, but they don’t share a live conversation, which avoids confusing interleaved messages.

**How is Sidekick different from asking @dust for help with my agent?**

Sidekick is embedded directly in the Agent Builder. It can read your agent's current configuration (including unsaved changes), propose edits as reviewable inline diffs, and directly suggest tools, skills, and models, rather than producing text you'd need to copy-paste manually. Sidekick is also workspace-aware: it knows what tools, skills, and knowledge sources are available and factors them into every recommendation.

**What happens if a data source I need isn't connected?**

Sidekick will recognize that the data source is a valid integration but isn't yet connected in your workspace. It will let you know and suggest contacting your workspace admin to set up the connection. Connecting data sources is always done through the admin panel.

**Will Sidekick keep changing my instructions every time I open the builder?**

No. Sidekick avoids cosmetic changes. It only suggests modifications when it identifies a substantive gap that would tangibly improve your agent. It won't rephrase sentences just because it prefers different wording.

**Do Sidekick messages count against my message limit?**

No. Sidekick messages are free: they don't consume your workspace's credits or regular message allowance. Two fair-use limits still apply:

* A per-user daily limit on Sidekick messages: 100 messages per user per 24 hours by default, and 200 for Enterprise workspaces.
* A global fair-use cap on the total cost of free usage in your workspace, independent of the number of messages. Sidekick messages count toward this cap.

If you reach either limit, Sidekick becomes temporarily unavailable until it resets.

**Can I customize Sidekick for my workspace?**

No. There is no mechanism to customize Sidekick behavior.
