> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Changelog

> New updates and improvements to Dust

<Update label="September 10th, 2026" tags={["Added"]}>
  ## Assign Admin and Manager roles from any workspace group

  Admins can now assign the Admin or Manager role to any workspace group from Settings & Governance → Roles, without relying on groups named `dust-admins` or `dust-managers`. This supports manually managed groups as well as groups provisioned from your identity provider.

  Existing `dust-admins` and `dust-managers` groups are migrated automatically, so current role assignments continue to work. Available to all workspace admins.
</Update>

<Update label="September 8th, 2026" tags={["Added"]}>
  ## Flexible space and pod permissions

  You can now manage access to spaces and pods with individual members and groups at the same time. Spaces no longer require choosing between member-based or group-based access, and pods can be managed with groups as well as individual users.

  Use the member and group management controls in your space or pod settings to configure access as your teams grow.
</Update>

<Update label="September 5th, 2026" tags={["Added"]}>
  ## GPT6 Astra

  GPT6 Astra is now available in Dust. You can select it when choosing a model for your agents and conversations.
</Update>

<Update label="August 26th, 2026" tags={["Added"]}>
  ## Credit pool usage for triggers

  Triggers can now run on the workspace pool of credits on credit-priced plans and on the programmatic usage pool on seat-based plans. Admins can control who can use these pools, while trigger editors can choose the pool in the trigger edition sheet and track usage from the Automations page. This gives you more granular control over credit allocation.
</Update>

<Update label="August 14th, 2026" tags={["Added"]}>
  ## Slack auto-replies without an @mention

  You can now configure a Dust agent to reply in a Slack channel without requiring the @Dust app mention. Set the agent to respond to every message or only the first message in a new thread, depending on how much automation you want in that channel. Available to every workspace.
</Update>

<Update label="August 10th, 2026" tags={["Added"]}>
  ## Choose the model from the composer

  [Watch the model demo](https://github.com/user-attachments/assets/50fae19e-f5e5-42ec-803b-6d5af30a9071)

  You can now choose which model runs your agent directly from the message composer. Click the model icon to choose a specific model or one of Dust's three auto models: **Basic**, **Standard**, and **Premium**.

  Each auto model is an ordered list of model and reasoning-effort combinations maintained by Dust. We periodically benchmark the candidates and update the lists when the preferred model changes. Dust does not route each request to a different model based on the task. When you send a message, Dust uses the first candidate on the selected list that is available to your workspace. If a candidate is unavailable, Dust continues to the next one.

  The model picker works with any agent, including the default `@dust` agent. A selection in the composer applies to your next message in that conversation only. To make a persistent choice, set the model in Agent Builder.

  The global model agents no longer appear in your agent list, but the models that powered them remain available through **More models** in the picker when your plan and administrator settings allow them. These agents were wrappers around a model with access to internet search, rather than full agents with their own instructions, tools, or company knowledge.

  Custom agents pinned to a specific model keep that model. Custom agents that previously followed the default model now run on **Standard**.

  The model picker is available in every workspace where the feature is enabled. Legacy pricing workspaces cannot select Premium models.
</Update>

<Update label="August 10th, 2026" tags={["Added"]}>
  ## Restrict access to model tiers

  Admins can now cap members at **Basic**, **Standard**, or **Premium** to control which model and reasoning-effort combinations they can select. The setting applies to every model option in the selected tier, not only to the auto-model rows. Models and reasoning efforts above a member's ceiling are locked in the picker, and agents configured with an unpermitted option show an error instead of running.

  Open the information panel beside the model-tier setting to see the current model and reasoning-effort options in each tier. The list changes as Dust updates its model catalog, pricing, and availability.

  Available in every new credit-based workspace.
</Update>

<Update label="August 4th, 2026" tags={["Added"]}>
  ## Modjo MCP is now available

  The official Modjo MCP is now available in all Dust workspaces. Your agents can connect to Modjo to retrieve call transcripts, deal details, and other company information, then use that context in agent answers and workflows. Modjo combines call transcripts with CRM capabilities, so you can bring both conversation and revenue context into Dust. Available to all Dust users.
</Update>

<Update label="July 31st, 2026" tags={["Added"]}>
  ## Workspaces can now choose a skill’s availability

  You can now set a skill’s availability at the workspace level. Choose Editors only to limit discovery to editors while keeping the skill usable through agents and other skills, All members to make it available through the input bar and agent builder to everyone, or Members and agents to include agents with Discover Skills enabled. Admins and managers can control who changes this setting.
</Update>

<Update label="July 30th, 2026" tags={["Added"]}>
  ## Restrict a tool to skills

  Workspace admins can now restrict a tool so agents and conversations can use it only through a skill, rather than adding it directly. This adds a governance layer for tools that need workspace-specific query guidance or safety rules, helping prevent inefficient repeated calls and unsafe use. The setting is available to every workspace admin.
</Update>

<Update label="July 29th, 2026" tags={["Added"]}>
  ## Admin governance controls

  Dust now lets admins manage user groups and assign granular permissions across the workspace. You can create groups manually or provision them, control which groups can create or publish agents, manage public MiniApp sharing, and use the new manager role as the builder role is deprecated.

  Available to everyone now.
</Update>

<Update label="July 27th, 2026" tags={["Added"]}>
  ## Kimi K3 via Fireworks AI

  You can now use Kimi K3 through Fireworks AI, bringing a strong open-weights model to Dust. It delivers quality close to Claude Fable and GPT 5.6 Sol, with a similar cost per task to GPT Sol.

  Available to everyone with access to US-based models.
</Update>

<Update label="July 22nd, 2026" tags={["Added"]}>
  ## Connect your personal Zendesk account

  You can now connect your own Zendesk account to the Zendesk tool, alongside the workspace connection. Actions run under your identity, so updates and replies are attributed to you instead of a shared workspace account.

  The subdomain comes from the workspace connection, so you only authenticate once. Open the Zendesk tool settings to connect your personal account. Available in all workspaces with Zendesk configured.
</Update>

<Update label="July 10th, 2026" tags={["Added"]}>
  ## Slack MCP Improvements: Reactions, Status Updates, and Optional "Sent by Agent" Footer

  🎯 What is it?

  Your agents can now do more when working through the Slack integration. They can add and remove emoji reactions, update Slack status, and, when an admin allows it, send messages without the "sent by agent" footer that normally appears with personal authentication.

  💡 Why is it useful?

  Until now, these were hard limitations of the Slack integration: agents couldn't react to messages, change status, or send messages that looked fully native. These additions let your agents interact in Slack in a more natural way, and give you finer control over how agent-sent messages appear to your teams.

  ⚙ How does it work?

  Reactions and status updates are available to everyone out of the box. The "sent by agent" footer can be turned off on a per-message basis, but only if an admin has enabled that option for your workspace, so you stay in control of transparency.

  ✨ Concrete Use Cases

  Here's how you could use it:

  * **Acknowledging messages**: An agent monitoring a support channel can add a ✅ reaction once it has picked up and handled a request, giving your team an instant visual cue.
  * **Signaling availability**: An agent can update a user's Slack status (for example, "In a meeting" or "Focusing") based on calendar events or workflow triggers.
  * **Cleaner notifications**: For internal broadcast messages where the footer adds noise, an admin-approved agent can post updates that read more naturally to recipients.

  📈 Benefits for you

  Agents feel more like real teammates inside Slack, interactions are smoother, and admins keep control over both transparency and how agent messages are presented.

  🚀 How to access it?

  Reactions and status updates are available now to everyone using the Slack integration, no setup needed. To allow users to remove the "sent by agent" footer, an admin needs to enable the corresponding toggle in your workspace settings first.
</Update>

<Update label="July 10th, 2026" tags={["Added"]}>
  ## GPT-5.6 Sol, Terra & Luna Are Now Available on Dust

  🎯 What is it?

  We've added OpenAI's newest GPT-5.6 model family to Dust. It comes in three tiers, each tuned for a different balance of speed, cost, and capability: **Sol** (the most capable), **Terra** (the balanced middle-ground), and **Luna** (the fastest). All three can be selected directly when building or editing an agent.

  💡 Why is it useful?

  Not every task needs the most powerful model, and not every task can afford to wait. Until now, choosing a model often meant trading off speed against depth of reasoning. With three clearly defined tiers, you can now match the right model to the right job, getting fast responses where you need throughput and deeper reasoning where the task demands it, without paying for more than you need.

  ⚙️ How does it work?

  Each tier is designed for a specific profile:

  * **Sol**: the most capable, built for complex, long-horizon agentic workflows.
  * **Terra**: strong reasoning at a reasonable cost, a solid default for most use cases.
  * **Luna**: optimized for high-throughput, low-latency tasks where speed matters most.

  📈 Benefits for you

  More control and flexibility: you can optimize each agent for speed, cost, or depth depending on its purpose, improving both efficiency and results across your workspace.

  🚀 How to access it?

  The three models are available to all users right now. Open the agent builder, go to the model picker, and select **Sol**, **Terra**, or **Luna** to start using them.
</Update>

<Update label="July 8th, 2026" tags={["Added"]}>
  ## 🔔 Sound Notification When an Agent Needs Your Approval

  🎯 What is it?

  Dust can now play a sound alert whenever one of your agents pauses and waits for you to approve or decline a tool action. The sound only plays when you're not actively viewing that particular conversation, so you're notified precisely when your attention is needed elsewhere.

  💡 Why is it useful?

  When an agent runs a task that requires manual approval (for example, before it performs a sensitive action), it pauses until you respond. If you've switched to another tab or you're working on something else, it was easy to miss these moments and leave an agent waiting. This audio alert ensures you can step away or multitask without losing track of pending approvals.

  ⚙️ How does it work?

  Once enabled, Dust plays your configured sound whenever an agent is waiting for approval or decline of a tool, and only if you're not currently looking at that conversation. Sound notifications are off by default, so you're fully in control of whether you use them.

  ✨ Concrete Use Cases

  Here's how you could use it:

  * **Multitasking across tabs**: You launch an agent on a long task, switch to your inbox, and get an audible cue the moment it needs your go-ahead, no need to keep checking back.
  * **Running several agents at once**: While monitoring multiple conversations, you're alerted as soon as any one of them pauses for approval, so none of them sit idle.

  📈 Benefits for you

  Less time spent checking on agents, faster response to approval requests, and smoother multitasking. Your agents spend less time waiting, which keeps your workflows moving.

  🚀 How to access it?

  Sound notifications are off by default. To turn them on, go to **Personal Settings → Notifications** and enable the sound alert (you can also configure which sound plays).
</Update>

<Update label="July 8th, 2026" tags={["Added"]}>
  ## Set Default Skills in Pods

  🎯 What is it?

  Pod editors can now select a set of default skills directly from their Pod settings. Once configured, these skills automatically appear in the input bar of every new conversation started in that Pod, exactly as if each user had added them manually via the "/" command or the dropdown menu.

  💡 Why is it useful?

  Until now, if you wanted to use skills that aren't attached to a specific agent, you had to add them by hand every time you started a new conversation. This created repetitive friction, especially for teams relying on the same set of skills day to day. Default skills remove that step, ensuring the right capabilities are always ready from the very first message.

  ⚙ How does it work?

  A Pod editor opens the Pod settings and selects the skills they want available by default. From that point on, every new conversation in the Pod automatically loads those skills into the input bar. Users can still add or remove skills per conversation as needed.

  ✨ Concrete Use Cases

  Here's how you could use it:

  * **Standardizing team workflows**: A Pod dedicated to customer support can have your knowledge-search and ticket-handling skills preloaded, so every agent starts with the same toolkit.
  * **User onboarding and activation**: Set helpful skills as defaults to guide new members and help them get value from the Pod immediately, without needing to know which skills to add.

  📈 Benefits for you

  You save time by eliminating repetitive setup, ensure consistency across conversations in a Pod, and make it easier for new users to get productive right away with the most relevant skills already in place.

  🚀 How to access it?

  This is available to all users. If you're a Pod editor, head to your Pod settings, select the skills you'd like to set as defaults, and they'll automatically appear in every new conversation started in that Pod.
</Update>

<Update label="July 6th, 2026" tags={["Added"]}>
  ## Select a Custom Default Agent in Pods

  🎯 What is it?

  You can now choose a default agent for an entire Pod. Once set by a Pod editor, every new conversation started in that Pod will automatically begin with the selected agent, instead of the standard default. This setting lives directly in your Pod settings.

  💡 Why is it useful?

  Teams often rely on a specific agent that already has the right context, skills, and connected data for their work. Until now, members had to manually pick that agent each time they started a conversation, an easy step to forget and a source of inconsistency across a team. Setting a default agent at the Pod level removes that friction and ensures everyone starts from the same, well-prepared assistant.

  ⚙️ How does it work?

  An editor of the Pod opens the Pod settings and selects the agent they want as the default. From that point on, all new conversations created in the Pod open with this agent already selected.

  ✨ Concrete Use Cases

  Here's how you could use it:

  * **Support team Pod**: Set a customer-support agent as the default so every new conversation is handled by an agent that already knows your product documentation and support tone.
  * **Sales team Pod**: Default to an agent connected to your CRM and sales playbooks, so account managers immediately get relevant, context-aware answers without any setup.

  📈 Benefits for you

  * Consistency across your team: everyone talks to the same specialized agent by default.
  * Time saved: no need to manually select the right agent for each new conversation.
  * Better answers from the start: conversations begin with the context, skills, and data your team actually needs.

  🚀 How to access it?

  This is available to all users. If you're an editor of a Pod, open your **Pod settings** and select the agent you'd like to set as the default for new conversations. Existing conversations are unaffected.
</Update>

<Update label="July 3rd, 2026" tags={["Added"]}>
  ## Triggers Now Run Inside Pods

  🎯 What is it?

  When a trigger fires, the conversation it creates now lives directly inside the Pod you've selected. This means every automated run lands in the right workspace context from the start, rather than sitting outside your team's organized spaces.

  💡 Why is it useful?

  Automated work can quickly become hard to track when it's scattered outside your team's normal environment. By routing triggered conversations into a Pod, everything stays organized, easy to find, and shareable with the right people, automatically placed where the relevant context already lives.

  ⚙️ How does it work?

  When you set up a trigger, you select the Pod where its conversations should run. From then on, each time the trigger fires, the resulting conversation is created inside that Pod alongside your team's related work.

  ✨ Concrete Use Cases

  Here's how you could use it:

  * **Recurring reporting**: A daily trigger that generates a summary now posts its conversation straight into your team's reporting Pod, where everyone already looks for updates.
  * **Automated monitoring**: A trigger watching for specific events creates its conversations inside the dedicated project Pod, so the whole team can review and act on them in context.

  📈 Benefits for you

  Less time spent hunting for automated runs, better visibility for your team, and cleaner organization of all triggered work: each conversation lands exactly where it belongs, with the right people able to access it.

  🚀 How to access it?

  This is available to all users. Open your trigger configuration and select the Pod where you'd like the triggered conversations to run.
</Update>

<Update label="June 30th, 2026" tags={["Added"]}>
  ## Claude Sonnet 5 is Now Available on Dust

  🎯 What is it?

  We've added Anthropic's latest model, Claude Sonnet 5, to Dust. The `claude-sonnet` global agent now runs on Sonnet 5 automatically, and you can also select Sonnet 5 directly when building your own agents.

  💡 Why is it useful?

  You get access to the newest generation of the Sonnet model, with its improvements in reasoning, quality, and overall performance, without having to change any of your existing setups. The upgrade happens automatically behind the global agent.

  ⚙ How does it work?

  The `claude-sonnet` global agent has been updated to point to Sonnet 5, so it's already using the new model. In the agent builder, Sonnet 5 now appears as an option in the model picker, ready to be assigned to any agent you create or edit.

  ✨ Concrete Use Cases

  Here's how you could use it:

  * **Upgrade an existing agent**: Edit one of your custom agents and switch its model to Sonnet 5 to benefit from the latest improvements.
  * **Quick everyday tasks**: Use the `claude-sonnet` global agent. It already runs on Sonnet 5, no configuration needed.

  📈 Benefits for you

  Access to a more capable model for your agents, improved output quality, and a smooth transition since your current configurations keep working as-is.

  🚀 How to access it?

  If your workspace is on a paid plan, Sonnet 5 is already available, no feature flag required. Use it through the `claude-sonnet` global agent, or select it in the model picker within the agent builder.

  ⚠ Please note: Sonnet 5 is not yet available for workspaces with EU data residency. We'll keep you informed as soon as that changes.
</Update>

<Update label="June 30th, 2026" tags={["Added"]}>
  ## Youtrust Remote MCP Server Now Available in Dust

  🎯 **What is it?**

  You can now connect your Dust workspace directly to Youtrust, an e-signature platform, through our Remote MCP Servers catalog. Once connected, your agents can search signature requests, use existing templates, and trigger signing flows, all without leaving Dust.

  💡 **Why is it useful?**

  Managing contracts and signature requests often means juggling multiple tools and manual handoffs between drafting a document and getting it signed. This integration removes that friction by letting your agents interact with Youtrust on your behalf, so signature workflows can run end to end inside Dust.

  ⚙ **How does it work?**

  Youtrust is available as a Remote MCP Server, which is a secure way for Dust to connect to an external service. The connection uses standard, secure authentication (OAuth), so your agents can act on your Youtrust account safely once it's set up.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  * **Contract drafting and sending**: Have an agent draft a contract and send it for signature in one continuous flow, with no manual copy-paste or switching tools.
  * **Automated follow-ups**: Set up an agent to monitor pending signature requests and automatically follow up when a deadline is approaching, so nothing slips through the cracks.

  📈 **Benefits for you**

  Less manual work, faster turnaround on signatures, and fewer forgotten follow-ups. Your team can spend less time chasing documents and more time on higher-value work.

  🚀 **How to access it?**

  If your team uses Youtrust, head to the Remote MCP Servers catalog in your Dust workspace, select Youtrust, and connect your account using the guided authentication flow. Once connected, the Youtrust capabilities can be added to your agents.

  ***

  *Note: this integration is available to anyone using Youtrust. If you'd like help setting up a specific use case, your Customer Success contact is happy to assist.*
</Update>

<Update label="June 30th, 2026" tags={["Added"]}>
  ## Agents Can Now Ask You Clarifying Questions: Available Everywhere

  🎯 **What is it?**

  The "Ask user question" capability is now built into every agent by default. This means any agent can pause mid-task to ask you a clarifying question when it needs more information, instead of guessing or proceeding with incomplete instructions. Previously, this had to be manually enabled on a per-agent basis.

  💡 **Why is it useful?**

  Until now, this capability was opt-in, which made it hard to discover and easy to forget when building a custom agent. By making it a default for all agents, you get more reliable, conversational interactions out of the box: agents can check in with you before heading in the wrong direction.

  ⚙️ **How does it work?**

  When an agent encounters ambiguity or needs a decision from you, it can now ask you directly during a task. You answer, and the agent continues with the right context. No setup or configuration is needed.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  * **Ambiguous requests**: You ask an agent to "draft the email to the client". Instead of assuming which client, it asks you to confirm before writing.
  * **Missing details**: An agent working on a report notices a required figure is missing and asks you for it, rather than leaving a gap or inventing a value.

  📈 **Benefits for you**

  More accurate results, fewer back-and-forth corrections, and a smoother collaboration with your agents, especially for custom agents where this previously had to be configured manually.

  🚀 **How to access it?**

  There's nothing to set up. This is now active by default for all agents across your workspace, including any custom agents you've already built.
</Update>

<Update label="June 30th, 2026" tags={["Added"]}>
  ## The Computer: Let Your Agents Work Safely with Files, Code, and More

  🎯 What is it?

  The [Computer](/docs/user-documentation/agents/tools/computer) is a new capability that gives your agents access to an isolated, secure environment where they can work directly with files, run calculations, execute code and handle larger multi-step workflows. Optionally, you can authorize your Computer environment to make network requests to specific destinations.

  💡 Why is it useful?

  Until now, agents were limited when it came to tasks that required actually processing files, running code, or chaining together more complex operations. The Computer removes those limits by giving agents a safe, sandboxed space to get hands-on work done, so they can support richer and more demanding tasks end to end.

  ⚙️ How does it work?

  Agents operate inside an isolated environment where they can safely manipulate files, perform computations, run code, and connect to external resources. Because the environment is sandboxed, this work happens securely without affecting your other systems. This also adds support for most external agent skills.

  ✨ Concrete Use Cases

  Here's how you could use it:

  * **File processing**: Have an agent extract text from a PDF, clean up a spreadsheet, or convert and reorganize a set of documents.
  * **Calculations & data work**: Ask an agent to run numerical analysis or process a dataset and return the results.
  * **Code execution**: Let an agent write and run code to automate a task or test a quick script.
  * **Larger workflows**: Combine several steps, such as fetching data via a network request, transforming it, and producing a final output, in a single agent run.

  📈 Benefits for you

  More capable agents and more efficient workflows. Tasks that previously required manual effort or couldn't be handled at all can now be completed directly by your agents, with broader support for external agent skills.

  🚀 How to access it?

  The Computer is available to everyone, with one exception: Enterprise workspaces that were not part of the beta. If that's your case, you can opt in at any time, and every workspace will automatically receive the feature within the next 2 weeks. You can learn more in the [documentation](/docs/user-documentation/agents/tools/computer).
</Update>

<Update label="June 24th, 2026" tags={["Added"]}>
  ## Pods Now Apply Your AGENTS.md to Every Conversation

  🎯 What is it?

  Pod editors can now manage an `AGENTS.md` file directly from their Pod settings. Once set, Dust automatically adds its content to the system prompt of every conversation that happens within that Pod, so your guidelines and workflows are always in effect.

  💡 Why is it useful?

  Previously, keeping behavior consistent across multiple conversations often meant copy-pasting the same instructions over and over. This feature lets you define your Pod-level rules and workflows once, in a single place, and have them applied everywhere automatically, ensuring consistency across every run without the manual overhead.

  ⚙ How does it work?

  Editors update the `AGENTS.md` file from the Pod settings, and Dust injects it into the system prompt for all conversations in that Pod. Oversized files are now handled more safely, so large instruction sets won't cause issues.

  ✨ Concrete Use Cases

  Here's how you could use it:

  * **Consistent tone and formatting**: Define how agents should respond (language, style, structure) so every conversation in the Pod follows the same standards.
  * **Shared workflows and guardrails**: Document the steps, do's and don'ts, or compliance rules your team must follow, and have them automatically enforced in each conversation.

  📈 Benefits for you

  You save time by setting your rules once instead of repeating them, you reduce the risk of inconsistent behavior across conversations, and you gain a single, easy-to-maintain source of truth for how your Pod should operate.

  🚀 How to access it?

  This is available to all Pod users for Pod conversations, no feature flag required. Pod editors can open their Pod settings and edit the `AGENTS.md` file to get started.
</Update>

<Update label="June 17th, 2026" tags={["Added"]}>
  ## Adomik Integration: Ad Revenue Analytics & Knowledge, Directly in Dust

  🎯 What is it?

  Adomik is now available as a default integration in Dust, connected securely via OAuth. Once enabled, your builders can give agents read-only access to Adomik's tools, allowing them to analyze your programmatic advertising and monetization data, as well as search and retrieve pages from your Adomik knowledge base, all without leaving Dust.

  💡 Why is it useful?

  If your teams work with programmatic advertising, investigating revenue movements or pricing shifts often means jumping between tools and manually pulling reports. This integration brings that data and knowledge directly into your agents, so you can run monetization investigations and draft analyses in one place.

  ⚙️ How does it work?

  Adomik connects as a remote integration through a secure OAuth login. The tools are strictly read-only, meaning agents can analyze and retrieve your data but cannot modify anything on the Adomik side.

  ✨ Concrete Use Cases

  Here's how you could use it:

  * **Revenue investigation**: Ask an agent to identify and explain sudden CPC/CPM shifts or revenue movements across your programmatic inventory.
  * **Report drafting**: Have an agent pull the relevant monetization figures and draft a first version of a performance report for your team.
  * **Knowledge lookup**: Let an agent search your Adomik knowledge base to quickly answer process or methodology questions.

  📈 Benefits for you

  You save time by consolidating ad data analysis and knowledge retrieval into your existing Dust agents, reduce manual back-and-forth between platforms, and give your teams faster, data-backed answers on monetization questions.

  🚀 How to access it?

  An admin first connects Adomik from **Spaces → Tools**. Once connected, your builders can add the Adomik tools to any relevant agent.
</Update>

<Update label="June 17th, 2026" tags={["Added"]}>
  ## Lemlist MCP Server Now Available

  🎯 **What is it?**

  The Lemlist MCP Server is now available across all Dust workspaces. It connects your Dust agents directly to Lemlist, giving them access to your leads, verified contacts, and multichannel outreach sequences. In short, your agents can now help you manage your outbound workflow without you having to switch tools.

  💡 **Why is it useful?**

  Outbound prospecting often means juggling several tools and repeating the same manual steps: pulling lead lists, checking contact details, updating sequences. By bringing Lemlist into Dust, you can hand those tasks to an agent and keep your focus on strategy and conversations that matter.

  ⚙️ **How does it work?**

  Once enabled, an agent can query and act on your Lemlist data through the connection: retrieving leads, accessing verified contact information, and working with your multichannel sequences. You ask the agent in natural language, and it interacts with Lemlist on your behalf.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  * **Lead review:** Ask an agent to pull a list of leads from a given Lemlist campaign and summarize who's worth prioritizing.
  * **Contact enrichment:** Have an agent retrieve verified contact details for a set of prospects before you reach out.
  * **Sequence management:** Ask an agent to check the status of your multichannel sequences or help you organize prospects across channels.

  📈 **Benefits for you**

  Less tool-switching, faster access to your outbound data, and the ability to delegate repetitive prospecting tasks to an agent. The result is a smoother outbound workflow and more time for high-value selling.

  🚀 **How to access it?**

  The Lemlist MCP Server is available in all Dust workspaces. You can add it as a tool when building or editing an agent, then connect your Lemlist account to start using it. If you're a Lemlist user, it's ready for you to set up today.
</Update>

<Update label="June 17th, 2026" tags={["Added"]}>
  ## GLM 5.2 Now Available in Dust

  🎯 What is it?

  GLM 5.2 is a new AI model developed by the lab Z.ai, now available within Dust. It performs at a frontier level on many agentic benchmarks, with results comparable to leading models like Opus 4.8 and GPT 5.5. The model is hosted in the United States by Fireworks.

  💡 Why is it useful?

  Having access to a broad range of high-performing models means you're never locked into a single provider. GLM 5.2 expands your options with a model that delivers top-tier performance on agentic tasks, giving you more flexibility to choose the right model for your specific needs and use cases.

  ⚙️ How does it work?

  GLM 5.2 is available as a model option when building or configuring your agents. You select it from the list of available models, just as you would with any other supported model. Although developed by Z.ai, it is hosted in the US by Fireworks.

  ✨ Concrete Use Cases

  Here's how you could use it:

  * **Agentic workflows**: Power agents that handle multi-step tasks and tool use, where GLM 5.2's strong agentic benchmark performance shines.
  * **Model comparison**: Test GLM 5.2 against your current models on your own use cases to see which delivers the best results for your team.

  📈 Benefits for you

  More choice, more flexibility. You gain access to an additional frontier-level model, allowing you to optimize your agents for performance while diversifying beyond a single model provider.

  🚀 How to access it?

  GLM 5.2 is now available in the model selection menu when creating or editing an agent. Choose it as your model to start testing it on your workflows.
</Update>

<Update label="June 16th, 2026" tags={["Added"]}>
  ## Email Threads Now Stay in a Single Conversation

  📌 Context

  When you interact with a Dust agent over email, each reply used to start a brand-new Dust conversation. So if an agent answered your email and you replied back, that reply was treated as a separate, disconnected conversation, losing the continuity of the exchange.

  We've changed this behavior: an email thread now maps to a single Dust conversation. Every reply within the same email thread continues in the same conversation, preserving the full context of the discussion. This change was driven both by product best practices and by popular demand from users.

  🔄 Impact on Dust

  Dust now recognizes when an incoming email belongs to an existing thread and routes it to the matching conversation automatically. The agent keeps the full history of the exchange in context, so each reply builds on what came before rather than starting from scratch.

  👤 Impact for you

  This is a positive change with no downside. When you email back and forth with an agent, the conversation stays coherent: the agent remembers the earlier messages in the thread, giving you more relevant and context-aware responses. You no longer end up with a scattered set of one-off conversations for what is really a single discussion.

  ✅ Actions required

  No action required on your part. The improvement is live and applies to everyone automatically. Just reply within the same email thread as usual, and the conversation will continue where it left off.
</Update>

<Update label="June 16th, 2026" tags={["Added"]}>
  ## Clari Copilot Integration Now Available for All Workspaces

  🎯 What is it?

  Your agents can now connect directly to Clari Copilot to search and analyze your sales calls. Without leaving Dust, an agent can pull up call transcripts, AI-generated summaries, discussed topics, action items, and competitor mentions. You can also filter calls by attendee email to zero in on specific conversations.

  💡 Why is it useful?

  Sales call intelligence usually lives in a separate tool, which means manually exporting or copy/pasting transcripts whenever you want to act on them. This integration removes that friction: the insights captured in your calls become directly usable inside your Dust workflows, so nothing gets lost between the conversation and the follow-up.

  ⚙️ How does it work?

  Dust connects to Clari Copilot through a dedicated integration secured with your Clari API credentials. Once connected, your agents can query call data on demand, just like they would search any other connected source.

  ✨ Concrete Use Cases

  Here's how you could use it:

  * **Account recaps**: Ask an agent to summarize all recent calls with a given account before a renewal conversation or QBR.
  * **Sales-to-CS handoffs**: Generate a clean handoff brief from the latest sales calls, including action items and key topics, so Customer Success starts fully informed.
  * **Meeting follow-ups**: Draft follow-up emails based on what was actually said and committed to during a call.
  * **Voice of Customer analysis**: Surface recurring themes and competitor mentions across calls to feed product and go-to-market decisions.

  📈 Benefits for you

  Less manual exporting and copy/pasting, faster and more accurate follow-ups, and smoother handoffs between teams. Your call data stops being a static archive and becomes something your agents can act on in real time.

  🚀 How to access it?

  The integration is now generally available to all workspaces. To set it up, add the Clari Copilot MCP server in your workspace tools and configure it with your Clari `X-Api-Key` and `X-Api-Password`. Once connected, you can add the Clari Copilot tools to any agent. Reach out to us if you'd like a hand getting it configured.
</Update>

<Update label="June 15th, 2026" tags={["Added"]}>
  ## Dust is now a remote MCP server

  🎯 **What is it?**

  Dust can now be connected to any MCP-capable client as a remote MCP server. This means you can access your Dust building blocks (workspace knowledge, Pods, conversations, and files) directly from the other tools you already use, without having to open Dust itself.

  💡 **Why is it useful?**

  Until now, reusing your Dust knowledge and artifacts in another tool often meant copy/pasting content back and forth or constantly switching between apps. By making Dust available as a remote MCP server, your trusted context travels with you, so the same knowledge and outputs can be tapped into wherever you work.

  ⚙️ **How does it work?**

  MCP (Model Context Protocol) is a standard way for applications to securely connect to external sources of context. Any client that supports MCP can now authenticate to Dust and pull in your building blocks on demand. Full setup instructions are available in the [documentation](/docs/user-documentation/agents/integrations/dust-mcp-server).

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  * **Working in an MCP-capable coding or writing tool:** Pull in relevant workspace knowledge or a past conversation directly into your working environment, without leaving the app you're in.
  * **Reusing existing artifacts:** Reference files or Pod content from Dust inside another client, so your team relies on a single, trusted source instead of duplicated copies.

  📈 **Benefits for you**

  Less copy/pasting, fewer app switches, and more consistency. Your teams can reuse the same trusted knowledge and artifacts across tools, which saves time and reduces the risk of working from outdated or fragmented information.

  🚀 **How to access it?**

  This is available now to everyone, no feature flag required. To get started, follow the connection steps in the [documentation](/docs/user-documentation/agents/integrations/dust-mcp-server).

  A note for workspace admins: you stay in control of access. You can disable MCP server access for the entire workspace, and you can restrict which redirect URIs are allowed during client authentication.
</Update>

<Update label="June 8th, 2026" tags={["Added"]}>
  ## Gamma MCP now available in Dust

  🎯 What is it?

  You can now connect Gamma to Dust as a Remote MCP Server. Once connected, your Dust agents can interact directly with Gamma to create and manage AI-powered presentations and documents from within your conversations.

  💡 Why is it useful?

  Creating presentations usually means switching between tools: drafting content in one place, then manually building slides in another. With the Gamma integration, your agents can handle the full process in one flow, from generating the content to producing a polished presentation, without you leaving Dust.

  ⚙️ How does it work?

  Gamma connects as a Remote MCP Server via OAuth. Once an admin sets it up in Spaces → Tools, the Gamma capabilities become available to any agent in the workspace.

  ✨ Concrete Use Cases

  * **One-click presentations**: Ask an agent to turn a brief or a set of notes into a ready-to-share Gamma presentation.
  * **Document generation**: Generate polished Gamma documents directly from your Dust conversations, without copy-pasting.

  📈 Benefits for you

  Faster content creation, fewer tool switches, and the ability to produce professional presentations and documents as part of any agent workflow.

  🚀 How to access it?

  Go to **Spaces → Tools** and add Gamma as a Remote MCP Server. Once connected, add the Gamma tools to any of your agents.
</Update>

<Update label="June 8th, 2026" tags={["Added"]}>
  ## Skills in Skills: Compose Skills and Tools Directly Within Your Instructions

  ## 🎯 What is it?

  You can now reference skills and tools directly inside your skill instructions, the same way you already reference knowledge. Skills can call on other skills, letting you build richer, more modular capabilities by combining existing building blocks. As part of this change, the separate "tools" section has been removed, and tools are now inserted inline wherever you need them.

  ## 💡 Why is it useful?

  Until now, skills stood on their own and couldn't draw on one another, which often meant duplicating the same logic across multiple skills. This update responds to a widely requested ability to compose skills, so you can assemble specialized capabilities into more complete workflows without rebuilding them each time.

  ## ⚙️ How does it work?

  When editing a skill's instructions, you use a dropdown to insert a reference to another skill or to a tool inline, exactly as you would when adding knowledge. The referenced skill or tool becomes part of that skill's behavior, so capabilities can be layered and reused.

  ## ✨ Concrete Use Cases

  Here's how you could use it:

  * **Building on existing skills**: Create a "Weekly Report" skill that references your existing "Data Retrieval" and "Summarization" skills, rather than duplicating that logic.
  * **Inline tool placement**: Insert a specific tool exactly at the point in your instructions where it's needed, making the skill's behavior clearer and easier to maintain.

  ## 📈 Benefits for you

  Less duplication, easier maintenance, and far more flexibility when designing skills. By composing skills from smaller, reusable pieces, you can build sophisticated agents faster and keep them consistent over time.

  ## 🚀 How to access it?

  The feature is available to everyone. When editing a skill, use the dropdown within the instructions to insert a reference to another skill or a tool. Your existing skills have already been updated automatically: the list of tools previously associated with a skill now appears at the top of its instructions, so nothing is lost in the transition.

  ***

  *No action is required on your part, your existing skills continue to work as before. This is simply a new way to compose and reuse them going forward.*
</Update>

<Update label="June 8th, 2026" tags={["Added"]}>
  ## @dust can now build skills

  Builders can now ask the @dust agent to create or edit skills directly from a conversation, no need to open the Skill Builder. Describe the workflow you want to capture, and @dust handles the rest.

  <br />
</Update>

<Update label="June 5th, 2026" tags={["Added"]}>
  ## Dust Support: Get Instant, Grounded Support Answers from @dust

  🎯 **What is it?**

  We've introduced a new discoverable skill that turns @dust into your first line of support. When you ask a support-related question, the agent detects your intent, answers it directly, and grounds its response in trusted sources so you can rely on what it tells you.

  💡 **Why is it useful?**

  Until now, getting a support answer often meant leaving your workspace to search documentation, browse community threads, or file a request and wait. This skill brings accurate support answers to you instantly, right where you already work, so you spend less time hunting for help and more time getting things done.

  ⚙️ **How does it work?**

  The skill recognizes when you're asking a support question and responds with answers grounded in real, up-to-date sources: the public [dust-tt/dust GitHub issues](https://github.com/dust-tt/dust/issues) and the [Dust community](https://community.dust.tt). This means responses reflect documented known issues and community knowledge rather than guesswork.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  * **Troubleshooting a behavior**: Ask "Why is my agent not picking up the latest documents from my connected data source?" and get an answer grounded in known issues and community discussions.
  * **Checking a known issue**: Ask "Is there a reported problem with PDF parsing right now?" and find out whether it's a documented issue with a workaround or fix already discussed.

  📈 **Benefits for you**

  Faster, more accurate answers without leaving Dust. You get reliable support grounded in real sources, reduce the back-and-forth of opening tickets, and resolve questions in the flow of your work.

  🚀 **How to access it?**

  The skill is discoverable and available to every user. Mention @dust and ask your support question. The agent will detect that you need support and respond with a grounded answer.
</Update>

<Update label="June 4th, 2026" tags={["Added"]}>
  ## Speech-to-Text for Audio & Video Files

  🎯 What is it?

  A new speech-to-text tool is now available in Dust, allowing your agents to transcribe spoken content from both audio and video sources. You can transcribe content from supported URLs or by uploading files directly, with support for most common formats (mp3, mp4, wav, m4a, mov, webm, aac, flac, and more).

  💡 Why is it useful?

  Audio and video content is everywhere (meeting recordings, interviews, webinars, voice notes), but the information locked inside it is hard to search, reuse, or act on. Transcription has been a recurring request, and with Dust's expanded processing capabilities, your agents can now turn spoken content into text that can be summarized, analyzed, and integrated into your workflows.

  ⚙️ How does it work?

  Your agent can transcribe content in two ways: from a URL (within an approved list of domains) or from a file you upload directly. Once transcribed, the text becomes available for the agent to work with: summarizing, extracting key points, or feeding into other tasks.

  ✨ Concrete Use Cases

  Here's how you could use it:

  * **Meeting follow-ups**: Upload a recording of a call and ask your agent to produce a clean summary with action items and decisions.
  * **Content repurposing**: Transcribe a webinar or podcast episode, then have your agent draft a blog post, social snippets, or an internal recap.
  * **Interview analysis**: Turn recorded user interviews into searchable text and extract recurring themes or quotes.

  📈 Benefits for you

  Significant time savings on manual transcription, easier reuse of audio/video content, and the ability to make spoken information searchable and actionable, all within your existing Dust workflows.

  🚀 How to access it?

  The feature is available to everyone now, no activation needed. Provide a supported URL or upload an audio/video file in your conversation, and ask your agent to transcribe it.
</Update>

<Update label="May 29th, 2026" tags={["Added"]}>
  ## Pods: A Shared Workspace for Your Team and Your Agents

  🎯 **What is it?**

  Pods are dedicated collaborative spaces where your team and your agents work together on a shared initiative. Each Pod brings **Conversations**, **Files**, and **Tasks** into one place, continuously indexed so that agents build on what was already discussed, without you having to re-explain context every time.

  💡 **Why is it useful?**

  Work in most teams is fragmented: conversations are scattered across individual feeds, files live in different tools, and every new interaction starts from scratch. Pods solve this by making context persistent and shared, so the next conversation starts smarter than the last, and nothing gets lost between sessions.

  ⚙️ **How does it work?**

  When you create a Pod, you get a shared environment with four core components:

  * **Conversations**: All threads related to the initiative stay in one place, and are continuously indexed so agents can reference past decisions automatically.
  * **Files**: Upload documents or connect Company Data directly into the Pod. Everyone, humans and agents alike, works from the same shared context.
  * **Tasks**: Create to-dos, assign them to teammates, or launch agent-run task conversations with the right context preloaded.
  * **Governance**: Pods can be **open** (anyone in the workspace can join) or **invite-only** (editors manage membership).

  ✨ **Concrete Use Cases**

  **Running a client project**: Create a Pod for the account, add the relevant files and data sources, and let your agents reuse every past decision and conversation thread. No more copy-pasting context into each new chat.

  **Managing a recurring initiative**: Use Tasks to assign work to teammates or trigger agent-run conversations at the right moment, with all the background knowledge already loaded in the Pod.

  📈 **Benefits for you**

  * **No more context re-pasting**: agents remember what was discussed and build on it automatically.
  * **One place for everything**: files, conversations, and tasks are co-located and shared across your team.
  * **Agents as true teammates**: they can read files, reference past conversations, create and update tasks, and manage Pod members.
  * **Flexible permissions**: open collaboration or controlled access, depending on what your initiative requires.

  🚀 **How to access it?**

  Pods are available to **everyone**: no feature flag, no opt-in required. Look for the **Pods** section in your Dust sidebar. Documentation is at [/docs/user-documentation/pods/overview](/docs/user-documentation/pods/overview).
</Update>

<Update label="May 28th, 2026" tags={["Added"]}>
  ## Claude Opus 4.8 Now Available in the Agent Builder

  🎯 **What is it?**

  Claude Opus 4.8, Anthropic's latest and most advanced reasoning model, is now available in Dust's agent builder. Enterprise customers can select it as the underlying model when creating custom agents, giving them access to Anthropic's most capable model to date.

  💡 **Why is it useful?**

  Opus models sit at the top of Anthropic's model family: they're designed for tasks that demand deep reasoning, sustained multi-step thinking, and the highest quality outputs. Opus 4.8 is no exception, and it's now within reach directly from your Dust workspace.

  ⚙️ **How does it work?**

  When building or editing a custom agent in Dust, you can now select **Claude Opus 4.8** as the model powering that agent. The model is not set as a default. It's a deliberate choice available to those who want the highest level of reasoning for specific, demanding use cases.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  * **Complex analysis & synthesis**: Build an agent that processes lengthy, nuanced documents (legal contracts, research reports, financial filings) and produces high-quality structured summaries or recommendations.
  * **Advanced code generation & review**: Set up a coding agent that not only generates code but critically evaluates logic, identifies edge cases, and suggests architectural improvements across long codebases.

  📈 **Benefits for you**

  Access to Opus 4.8 means your most demanding workflows no longer require trade-offs between speed and quality: you can configure dedicated agents that bring the best reasoning available to bear on your hardest problems, while keeping lighter models for everyday tasks.

  🚀 **How to access it?**

  This feature is available to **Enterprise customers**. Go to the **Agent Builder**, create or edit a custom agent, and choose **Claude Opus 4.8** in the model selection step.
</Update>

<Update label="May 28th, 2026" tags={["Added"]}>
  ## [Apify MCP Is Now Available in Dust](https://apify.com/store/categories/mcp-servers)

  🎯 **What is it?**

  Dust agents can now connect to Apify as a remote MCP (Model Context Protocol) server. This means your agents can trigger Apify Actors (pre-built web scraping and automation tools) directly from a Dust conversation, and pull the resulting data back in real time.

  💡 **Why is it useful?**

  Getting fresh data from the web or automating repetitive data-collection workflows has historically required custom-built scrapers, dedicated infrastructure, or manual copy-paste work. With Apify connected to Dust, agents can tap into thousands of ready-made scraping and automation tools on demand: no custom code, no glue scripts, no maintenance overhead.

  ⚙️ **How does it work?**

  Apify is connected as a remote MCP server inside Dust. Once set up, agents can call any Apify Actor (a self-contained unit for scraping or automating tasks on a specific platform or website), wait for it to run, and fetch the structured output directly into the conversation. Authentication is handled via OAuth.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  * **Competitive intelligence**: Ask an agent to scrape a competitor's pricing page or product listings on a weekly basis and summarize changes, no manual browsing required.
  * **Lead enrichment**: Trigger an Apify Actor to pull public company data, LinkedIn profiles, or job postings and feed the results directly into your CRM workflow through Dust.
  * **Social media monitoring**: Run an Actor to collect recent posts or mentions from a specific platform and have an agent analyze sentiment or flag trending topics.

  📈 **Benefits for you**

  Access to live, structured web data without engineering effort. Your agents become significantly more autonomous on research, monitoring, and data-gathering tasks, eliminating the round-trip between Dust and external scraping tools.

  🚀 **How to access it?**

  Available now for teams already using Apify. Connect it in **Spaces → Tools**, using OAuth to authenticate. Once added, it can be assigned to any agent in your workspace.
</Update>

<Update label="May 28th, 2026" tags={["Added"]}>
  ## Six New Integrations Now Available in Dust

  🎯 **What is it?**

  Dust just added six new MCP (Model Context Protocol) integrations: **Monday.com**, **Snowflake**, **Luma**, **Confluence**, **Contentsquare**, and **Praiz** are now available for all workspaces. Each integration lets your agents connect directly to these tools and take action: no tab-switching, no copy-pasting, no manual data gathering.

  💡 **Why is it useful?**

  Your tools hold critical data: project statuses, warehouse queries, event records, meeting transcripts, wiki pages, digital experience metrics. Until now, getting that data into a Dust workflow meant leaving the conversation. With MCP integrations, agents can reach directly into these tools and surface exactly what you need, right where you're working.

  ⚙️ **How does it work?**

  Each integration is set up once by an admin in **Spaces → Tools**. After that, any team member can add the tool to their agents. Authentication is handled via OAuth: secure, and no API key management required.

  ✨ **Concrete Use Cases**

  * **Monday.com**: Let agents track project statuses, pull board items, and surface blockers across your team's work.
  * **Snowflake**: Query your data warehouse directly from a conversation.
  * **Luma**: Access event details, attendee lists, and registration data.
  * **Confluence**: Search, read, create and update pages and spaces.
  * **Contentsquare**: Query site metrics, funnels, user journeys, and conversion impact data.
  * **Praiz**: Search meetings, pull full transcripts, access timelines, comments, and participants.

  📈 **Benefits for you**

  Less context-switching. Faster workflows. Your agents can now pull live data from the tools your teams already use daily.

  🚀 **How to access it?**

  Go to **Spaces → Tools** in your Dust workspace and look for any of these integrations in the MCP catalog. Available to all workspaces today.
</Update>

<Update label="May 27th, 2026" tags={["Added"]}>
  ## Costory MCP Now Available in Dust

  🎯 **What is it?**

  Dust now supports Costory as a remote MCP (Model Context Protocol) server. This means your Dust agents can connect directly to Costory to query cloud costs, compare spending across periods, and generate reports or alerts, all without leaving Dust.

  💡 **Why is it useful?**

  FinOps questions ("What changed in our cloud spend this month?", "Which service drove the cost spike?") typically require jumping between billing dashboards, pulling exports, and chasing down the right person. With this integration, agents can answer those questions in seconds, directly in Dust.

  ⚙️ **How does it work?**

  Costory is connected to Dust as a remote MCP server, authenticated via OAuth. Once connected, any agent in your workspace can call Costory's tools to fetch, analyze, and compare cloud spending data.

  ✨ **Concrete Use Cases**

  * **Cloud cost monitoring**: Ask "What were our top 5 cost drivers last week compared to the week before?" and get an instant, structured breakdown.
  * **Automated cost alerts**: Build an agent that runs on a schedule, detects unusual spend variations in Costory, and posts a summary directly to Slack.

  📈 **Benefits for you**

  * FinOps questions get answered in seconds, not hours
  * Engineering and Ops teams stay unblocked
  * Agents can combine Costory data with other sources in Dust

  🚀 **How to access it?**

  Go to **Spaces → Tools**, click **Add Tools**, search for Costory, and authenticate via OAuth. Once connected, add Costory tools to any of your agents.
</Update>

<Update label="May 27th, 2026" tags={["Added"]}>
  ## Praiz is Now Available as a Remote MCP Tool in Dust

  🎯 **What is it?**

  Dust now supports Praiz as a connected remote MCP tool. Praiz is a meeting intelligence platform that records, transcribes, and analyzes your calls using AI, and you can now connect it directly to your Dust workspace. Once connected, your Dust agents can search meetings and retrieve full transcripts along with rich metadata: timelines, participant details, comments, templates, and usage statistics.

  💡 **Why is it useful?**

  Sales calls, customer success check-ins, and product interviews hold valuable insights, but those insights are usually locked inside recordings that no one goes back to read. With the Praiz integration, your Dust agents can tap into that conversation data on-demand, without you having to switch tools, copy-paste transcripts, or manually dig through recordings.

  ⚙️ **How does it work?**

  Connect Praiz as a remote MCP server via OAuth in your Dust workspace. Once authenticated, any Dust agent you configure will be able to search your Praiz meetings and pull structured data from them (transcripts, timelines, participants, and more) directly within a Dust conversation or workflow.

  ✨ **Concrete Use Cases**

  * **Account briefs**: Ask a Dust agent to summarize everything discussed with a specific account over the last 3 months (objections raised, commitments made, open questions) and get a ready-to-use brief in seconds.
  * **Automated follow-up drafts**: After a sales or CS call, trigger a Dust agent to retrieve the Praiz transcript, extract key action items and next steps, and generate a personalized follow-up email.
  * **CRM note generation**: Use a Dust agent to pull structured data from a Praiz meeting and draft a CRM update ready to be pasted or pushed via another integration.

  📈 **Benefits for you**

  Your call data stops being a passive archive and becomes an active part of your AI workflows.

  🚀 **How to access it?**

  1. Go to **Spaces → Tools** in your Dust workspace
  2. Search for **Praiz** in the available remote MCP tools
  3. Connect via **OAuth**, available to all workspaces

  > **Note:** You'll need an active Praiz account to authenticate.
</Update>

<Update label="May 27th, 2026" tags={["Added"]}>
  ## Monday.com MCP: Now Available for All Workspaces

  🎯 **What is it?**

  The Monday.com MCP (Model Context Protocol) server is now generally available across all Dust workspaces. Your agents can now interact directly with your Monday.com boards (reading, creating, updating, and commenting), all from within your Dust conversations.

  💡 **Why is it useful?**

  Project management data often lives in silos, forcing teams to manually check boards, copy-paste updates, or switch between tools to stay on top of work. With the Monday.com MCP, your agents become active participants in your workflows: no more context switching, no more stale information.

  ⚙️ **How does it work?**

  Once an admin connects the Monday.com integration in your Space settings, agents equipped with the tool can query your Monday.com workspace in real time. They can read board and item data, create or update items, assign tasks, change statuses, and post comments, directly from a conversation.

  ✨ **Concrete Use Cases**

  **Project status summaries**: Ask your agent "What's the current status of our Q3 launch items?" and get an instant, structured overview pulled directly from your Monday.com boards.

  **Task creation from conversations**: After a meeting recap, have an agent automatically create Monday.com items, assign them to the right people, and set the appropriate status.

  **Cross-tool workflows**: Combine Monday.com data with your other connected tools (Slack, Notion, CRM) to build agents that can triage, prioritize, and act on work across your entire stack.

  📈 **Benefits for you**

  * **Save time** on manual status updates and task creation
  * **Keep your boards up to date** without leaving your conversations
  * **Let your team** interact with Monday.com through natural language

  🚀 **How to access it?**

  1. **Admins**: Go to **Spaces > Tools** and connect the Monday.com integration
  2. **Everyone**: Add the Monday.com tool to any of your agents and start using it
</Update>

<Update label="May 27th, 2026" tags={["Added"]}>
  ## Confluence MCP is Now Generally Available

  🎯 **What is it?**

  The Confluence MCP Server is now available to all Dust workspaces, no preview access needed. This integration allows your agents to interact directly and dynamically with your Confluence instance: reading, searching, and even writing content, all from within Dust.

  💡 **Why is it useful?**

  Until now, Dust could connect to Confluence as a read-only data source, syncing pages so agents could search them. With the MCP Server, agents go further: they can now act on Confluence in real time. Agents can fetch the latest version of a page, pull a comment thread, or draft and publish new content, becoming active contributors to your knowledge base, not just readers.

  ⚙️ **How does it work?**

  Once a workspace admin connects Confluence via **Spaces > Tools**, the integration becomes available to all members. Anyone can then add the Confluence tool to their agents. From there, agents can call Confluence directly during conversations: searching pages, reading history, creating or updating content, and leaving inline comments.

  ✨ **Concrete Use Cases**

  * **Knowledge base maintenance**: Ask an agent to find an outdated onboarding page and update it directly in Confluence.
  * **Meeting follow-ups**: Have an agent create a new Confluence page with summary, action items, and decisions.
  * **Documentation Q\&A**: Ask "What does our runbook say about database rollbacks?" and the agent searches Confluence in real time.
  * **Audit & review**: Have an agent pull the edit history of a critical page and summarize what changed.

  📈 **Benefits for you**

  * Agents that write, not just read
  * Always up-to-date responses (live queries, not cached snapshots)
  * Reduced context-switching
  * Collaboration at scale via inline comments

  🚀 **How to access it?**

  1. **Admin setup**: Go to **Spaces > Tools** and connect your Confluence account
  2. **Agent setup**: Add the Confluence tool to your agents from the agent builder
</Update>

<Update label="May 27th, 2026" tags={["Added"]}>
  ## Luma MCP Server: Now Generally Available

  🎯 **What is it?**

  The Luma MCP Server is now available to all Dust workspaces. It connects your Dust agents directly to Luma, your event management platform, giving them the ability to interact with your events, calendars, guest lists, and attendee communications, all from within a conversation.

  💡 **Why is it useful?**

  Managing events involves a lot of back-and-forth: checking RSVPs, updating event details, reaching out to attendees. With the Luma MCP Server, your agents can handle these tasks directly, without switching between tools or copying information manually.

  ⚙️ **How does it work?**

  Once an admin connects Luma via an API Key in Spaces > Tools, any agent in the workspace can be configured to use Luma capabilities. The agent can then search, read, and manage your Luma data conversationally.

  ✨ **Concrete Use Cases**

  * **Event preparation**: Ask your agent "Who has RSVP'd to our June 12th webinar?" and get an up-to-date guest list instantly.
  * **Event management**: Have your agent create a new event, update its description, or send a message to all registered attendees.

  📈 **Benefits for you**

  Save time on repetitive event management tasks, reduce context-switching, and let your team get event information or take action without needing direct Luma access.

  🚀 **How to access it?**

  1. Go to **Spaces > Tools** in your Dust workspace
  2. Add the **Luma MCP Server** using your Luma API Key
  3. Enable the tool on any agent

  > Only workspace admins can set up the integration. Once configured, all members can use it through their agents.
</Update>

<Update label="May 27th, 2026" tags={["Added"]}>
  ## Snowflake MCP Server: Now Generally Available

  🎯 **What is it?**

  The Snowflake MCP (Model Context Protocol) Server is now available to all Dust workspaces. Your agents can connect directly to Snowflake and interact with your data (listing databases, schemas, and tables, running SQL queries, inspecting column definitions, and retrieving results), all within a conversation.

  💡 **Why is it useful?**

  Until now, getting insights from Snowflake required switching between tools, writing queries manually, or relying on data teams. With this integration, your agents can query your Snowflake data warehouse on the fly, turning natural language questions into structured data results without ever leaving Dust.

  ⚙️ **How does it work?**

  Once configured by an admin, the Snowflake MCP Server is available as a tool that any agent can use. Ask your agent a data-related question, and it will query Snowflake, retrieve the relevant results, and surface them directly in the conversation.

  ✨ **Concrete Use Cases**

  * **Sales reporting**: Ask your agent "What were our top 10 accounts by revenue last quarter?" and it queries Snowflake and returns the answer instantly.
  * **Data exploration**: Ask "What tables are available in our analytics schema?" to understand what data exists before diving deeper.

  📈 **Benefits for you**

  * Faster access to data insights without switching tools
  * No SQL expertise required for end users
  * Enables data-driven conversations directly in Dust

  🚀 **How to access it?**

  Admins can set up the Snowflake MCP Server in **Spaces → Tools**. Once configured, it becomes available for any agent in your workspace.
</Update>

<Update label="May 26th, 2026" tags={["Added"]}>
  ## Contentsquare Remote MCP Now Available in Dust

  🎯 **What is it?**

  Dust now integrates Contentsquare as a remote MCP (Model Context Protocol) server, available directly in the Dust tool catalog. Your agents can now query Contentsquare data (site metrics, funnels, user journeys, page comparisons, errors, and conversion impact) straight from a Dust conversation, without ever leaving the platform.

  💡 **Why is it useful?**

  Analyzing digital experience data typically means logging into Contentsquare, navigating multiple dashboards, cross-referencing views, and manually synthesizing insights. This integration collapses that process into a simple conversational workflow: ask a question, get the answer, decide what to do next.

  ⚙️ **How does it work?**

  Once an admin connects Contentsquare via OAuth in **Spaces > Tools**, the MCP server becomes available as a tool for agents in your workspace. Any agent equipped with this tool can then query Contentsquare's key DEX (Digital Experience) signals in real time.

  ✨ **Concrete Use Cases**

  * **Conversion investigation**: Ask "Which steps in the checkout funnel had the highest drop-off last week?" and get an instant answer.
  * **Error impact analysis**: Ask "What is the conversion impact of the JavaScript errors on our homepage?" and get a business impact summary.

  📈 **Benefits for you**

  Turn hours of manual dashboard exploration into a fast, natural-language Q\&A workflow. Anyone, not just analytics experts, can access Contentsquare insights through their agents.

  🚀 **How to access it?**

  1. Go to **Spaces > Tools** in your Dust workspace
  2. Find Contentsquare in the MCP catalog
  3. Connect via **OAuth** (admin rights required)
  4. Add the tool to any agent
</Update>

<Update label="May 23rd, 2026" tags={["Added"]}>
  ## Collapsing Input Bar on Mobile for Better Reading

  🎯 **What is it?**

  On mobile, the input bar now automatically collapses into a compact pill as you scroll through a conversation. Voice input remains always visible and accessible, so you can interact with your agents without typing a single character.

  💡 **Why is it useful?**

  Mobile screens are limited in space. When you're reading through a conversation, the input bar used to take up valuable vertical real estate. This update lets you focus on the content while keeping voice input just a thumb-tap away, making the mobile experience genuinely hands-free.

  ⚙️ **How does it work?**

  As you scroll down in a conversation on mobile, the input bar shrinks into a small pill: unobtrusive, but always present. The voice input button remains accessible at all times. When you're ready to respond, just tap the pill to expand it back to full size, or go straight to voice.

  ✨ **Concrete Use Cases**

  * **Reading long conversations on the go**: Scroll through a lengthy thread without the input bar eating into your screen, then jump straight into a voice reply when you're ready.
  * **Hands-free interaction**: Commuting or multitasking? Trigger voice input instantly from any point in the conversation without scrolling back to the bottom.

  📈 **Benefits for you**

  More readable conversations on mobile, a more natural scrolling experience, and frictionless access to voice input, all without any setup. This is a step toward a fully no-typing mobile experience with Dust.

  🚀 **How to access it?**

  No action needed. This update is live for **all mobile web users**: just open Dust on your mobile browser and start scrolling.
</Update>

<Update label="May 22nd, 2026" tags={["Added"]}>
  ## Agents Can Now Export MiniApps as PDF or PNG

  🎯 **What is it?**

  Agents can now export any MiniApp (the interactive visualizations and dashboards they generate) directly as a PDF or PNG file. This means any visual output produced during a conversation can be saved and shared in a universally accessible format.

  💡 **Why is it useful?**

  Until now, MiniApps were only viewable inside a Dust conversation. If you wanted to share a report or dashboard with someone outside of Dust, you had to rely on screenshots or manual exports. This feature closes that gap and makes it easier to bring Dust's outputs into your broader workflows.

  ⚙️ **How does it work?**

  When an agent generates a MiniApp in a conversation, it can now trigger an export directly, producing a clean, ready-to-share PDF or PNG file. Agents can also use this capability to inspect and reason about the visual output they just created, enabling smarter, more iterative work.

  ✨ **Concrete Use Cases**

  * **Sharing a report with stakeholders**: Ask an agent to build a weekly performance dashboard as a MiniApp, then export it as a PDF to include in an email or slide deck.
  * **Automated document generation**: Have an agent create a formatted visual summary, export it as a PNG, and attach it directly to a Notion page or Slack message.

  📈 **Benefits for you**

  * Save time by eliminating manual export steps
  * Share polished, professional visuals directly from your conversations
  * Enable agents to work more autonomously by reasoning on their own visual outputs

  🚀 **How to access it?**

  This is available to everyone, right now. Ask an agent to build a MiniApp and request an export. The agent will handle the rest.
</Update>

<Update label="May 22nd, 2026" tags={["Added"]}>
  ## Inline Text Editing in MiniApps: Tweak Your Content Without Reprompting

  🎯 **What is it?**

  You can now double-click any static text inside a MiniApp to edit it directly, without having to reprompt the agent. Previously, correcting a word, tweaking a label, or adjusting any text in a MiniApp required going back to the conversation and asking the agent to make the change. Now you can just click and type.

  💡 **Why is it useful?**

  MiniApps are designed to produce polished, ready-to-use outputs: documents, tables, dashboards, reports. But a great first draft rarely needs zero edits. Being able to fix text in place, without re-running the agent, makes the editing loop faster and puts you in control of the final result.

  ⚙️ **How does it work?**

  When viewing a MiniApp in a conversation, any static text element can now be double-clicked to enter edit mode. You can type your changes and they apply immediately, just like editing a document.

  ✨ **Concrete Use Cases**

  * **Quick copy fixes**: You asked for a report summary but the agent used slightly off-brand wording. Double-click and correct it in seconds.
  * **Number tweaks**: The agent drafted a slide with a placeholder figure. You have the real number now. Just double-click and type it in.
  * **Label adjustments**: A chart label or table header doesn't quite fit. Edit it directly without re-running anything.

  📈 **Benefits for you**

  Fewer roundtrips to the agent for small edits, faster time from first draft to final output, and more direct control over the content you share.

  🚀 **How to access it?**

  This is available to everyone, now. Open any MiniApp in a conversation and double-click on a text element to start editing.
</Update>

<Update label="May 20th, 2026" tags={["Added"]}>
  ## Gemini 3.5 Flash Now Available on Dust

  🎯 **What is it?**

  Gemini 3.5 Flash, Google's latest AI model, is now available on Dust. It is designed for speed and delivers frontier-level performance across a wide range of tasks, making it one of the fastest capable models available on the platform.

  💡 **Why is it useful?**

  When working with agents that handle high volumes of requests, or when you need quick turnaround on complex tasks, model speed matters. Gemini 3.5 Flash combines the responsiveness you'd expect from a fast model with the quality benchmarks of a frontier one, a combination that's rarely available in one package.

  ⚙️ **How does it work?**

  Gemini 3.5 Flash can be selected as the underlying model when configuring any agent on Dust, just like other available models. It fits into your existing workflows with no additional setup required.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  * **High-volume support agents**: Handle large numbers of customer queries faster, without sacrificing response quality.
  * **Real-time drafting agents**: Speed up content generation workflows where low latency makes a meaningful difference in team productivity.

  📈 **Benefits for you**

  Faster responses, frontier-level quality, and no trade-offs on accuracy. Gemini 3.5 Flash gives your agents more horsepower for time-sensitive or high-throughput use cases.

  🚀 **How to access it?**

  Gemini 3.5 Flash is available to **all users** today. To use it, open any agent's settings, navigate to the model selection section, and choose **Gemini 3.5 Flash** from the list.
</Update>

<Update label="May 19th, 2026" tags={["Added"]}>
  ## LLM Model Refresh: Grok 4.3 Upgrade and Anthropic Model Migrations

  📌 **Context**

  Two of our LLM providers are making changes to their model lineups, and this affects the models available in Dust. Here’s what’s changing and when.

  **Grok 4.3 upgrade (happening now)**: xAI has deprecated Grok 3 and replaced it with Grok 4.3, at the same price point but with significantly better performance. This upgrade is live now. If you were using Grok 3, your agents will automatically switch to Grok 4.3, no action needed.

  **Anthropic model migrations (deadline: July 31, 2025)**: Anthropic is deprecating older Claude models. Here’s the mapping of legacy models to their recommended replacements:

  | Legacy model               | Replacement       |
  | -------------------------- | ----------------- |
  | claude-3-5-sonnet-20240620 | claude-sonnet-4-5 |
  | claude-3-5-haiku-20241022  | claude-haiku-4-5  |
  | claude-3-opus-20240229     | claude-opus-4-5   |
  | claude-3-5-sonnet-20241022 | claude-sonnet-4-5 |

  **Deadline: July 31, 2025.** After that date, Anthropic will stop serving these legacy models.

  🔄 **Impact on Dust**

  Dust’s pre-built "global" agents (like @claude-sonnet) already run on the latest models and are unaffected. The risk is **only for custom agents** that were manually configured to use a specific legacy model ID.

  👤 **Impact for you**

  If you or your team have built custom agents on one of the legacy Anthropic models listed above, **those agents will stop working after July 31, 2025**. Check your custom agents and switch them to a supported model before the deadline.

  ✅ **Actions required**

  Review your custom agents before July 31. You can do this from the **Agent Builder** in Dust: go to your agent list, open any custom agent, and check the model it’s configured to use. If it’s one of the deprecated models, update it to the recommended replacement.

  Needs to be done by **July 31, 2025**.
</Update>

<Update label="May 11th, 2026" tags={["Added"]}>
  ## Branching Conversations

  🎯 **What is it?**

  You can now create a "branch" from any existing conversation. This creates a new conversation that inherits key context from the original (like a summary of what happened, attachments, and tool outputs) without carrying over the full message history.

  💡 **Why is it useful?**

  As conversations evolve, you often reach a point where you need to split work into parallel streams or share results without exposing all the back-and-forth. Branching lets you divide complex projects into focused workstreams, or collaborate on outcomes while keeping the messy details contained.

  ⚙ **How does it work?**

  Access the conversation menu (top right of the screen or next to the conversation title in the left sidebar) and select the branching option. The new conversation is created in 10-20 seconds with a compacted summary of the original conversation, plus copies of any attachments and tool outputs. The branch inherits the same access permissions as the original conversation at the time of creation.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Split a project into parallel workstreams**: Your conversation outlines a plan for building a new feature with three components. Branch into three separate conversations (one for each technical design) so teams can work independently without cluttering a single thread.

  **Share results, not process**: You've built a detailed data frame after hours of iteration and refinement. Branch the conversation so collaborators can access the final output and continue refining it, without wading through all the trial and error.

  📈 **Benefits for you**

  * **Better organization**: Keep complex projects manageable by splitting them into focused conversations
  * **Cleaner collaboration**: Share outcomes and context without overwhelming teammates with unnecessary details
  * **Flexible workflows**: Move from planning to execution across multiple parallel efforts

  🚀 **How to access it?**

  Look for the conversation menu in the top right corner of your screen, or next to the conversation title in your left sidebar. The branching option is available to everyone. Try it on your next multi-part project!
</Update>

<Update label="May 11th, 2026" tags={["Added"]}>
  ## Asana MCP update

  📌 Context

  Asana has shut down their MCP (Model Context Protocol) V1 server and migrated to V2. The old connection will stop working. If your workspace uses the Asana MCP tool in Dust, this is an action required update.

  🔄 Impact on Dust

  Dust has updated the Asana integration to support the V2 API. The new connection is fully compatible and ready to use.

  👤 Impact for you

  If your workspace currently uses the Asana MCP tool, the existing connection will break once Asana fully switches off V1. You’ll need to reconnect Asana using the new V2 setup.

  ✅ Actions required

  1. Go to **Spaces → Tools** in your Dust workspace
  2. Find the Asana MCP connection
  3. Reconnect it following the updated setup instructions

  This only affects workspaces that currently have Asana connected via MCP. If you haven’t set up the Asana integration yet, you can follow the new V2 instructions when you do.
</Update>

<Update label="May 7th, 2026" tags={["Added"]}>
  ## 🔒 Audit Logs for Enterprise Workspaces

  🎯 **What is it?**

  Enterprise workspace administrators now have access to detailed audit logs directly in the admin panel. These logs track all agent executions, tool calls, and administrative actions across your workspace. Additionally, you can stream these logs in real-time to your existing Security Information and Event Management (SIEM) platforms like Datadog, Splunk, or any custom HTTPS endpoint.

  💡 **Why is it useful?**

  Security and compliance teams need complete visibility into workspace activities for several critical purposes: responding to security incidents, meeting regulatory compliance requirements, conducting internal audits, and distinguishing between actions taken by users versus those performed by agents. Until now, this level of detailed activity tracking wasn't available in Dust.

  ⚙ **How does it work?**

  Audit logs are accessible through your admin panel with real-time updates. You can view the complete history of activities, filter by type (agent executions, tool calls, admin actions), and configure streaming to your preferred SIEM platform or custom endpoint for centralized security monitoring.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Security Incident Investigation**: When investigating a potential security event, quickly review which agents were executed, what tools they used, and which users or agents performed specific actions during the relevant timeframe.

  **Compliance Reporting**: Generate audit reports for compliance certifications (SOC 2, ISO 27001, GDPR) by exporting complete activity logs showing data access patterns, administrative changes, and agent behaviors.

  **Separation of Concerns**: Clearly distinguish between actions initiated by human users and those performed autonomously by agents, helping you understand and control automated workflows in your environment.

  📈 **Benefits for you**

  * **Stronger Security Posture**: Complete visibility into all workspace activities enables faster threat detection and incident response
  * **Simplified Compliance**: Meet regulatory requirements with complete, exportable audit trails
  * **Operational Intelligence**: Understand how agents and users interact with your Dust workspace to optimize workflows
  * **Centralized Monitoring**: Integrate with your existing security infrastructure for unified monitoring across all enterprise tools

  🚀 **How to access it?**

  This feature is available exclusively for Enterprise plan workspaces. Workspace administrators can access audit logs by navigating to the admin panel. For detailed setup instructions, including SIEM streaming configuration, visit our documentation at [/docs/user-documentation/admins/audit-logs/audit-logs](/docs/user-documentation/admins/audit-logs/audit-logs)
</Update>

<Update label="May 7th, 2026" tags={["Added"]}>
  ## Agents can now see images returned by MCP tools

  🎯 **What is it?**

  We've shipped a new file system for conversations. The first thing it enables: agents can now see images returned by MCP tools. When a tool produces an image (JPEG, PNG, GIF, WebP), the agent receives the actual visual content and can interpret, analyze, and describe it.

  💡 **Why is it useful?**

  Until now, when an MCP tool returned an image, agents were blind to it. They could acknowledge the file existed but couldn't look at it. This was a real gap: screenshots from Microsoft Drive, charts from data tools, visual outputs from external integrations, all invisible to the agent. That's now fixed.

  ⚙ **How does it work?**

  Behind the scenes, all conversation files are now organized in a unified, structured system. When an agent needs to access an image returned by an MCP tool, it receives the actual visual content instead of just metadata.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Screenshot analysis**: Have an agent interpret a screenshot returned by a Drive or browser tool, without manually describing what's on screen.

  **Chart and graph reading:** Ask an agent to extract trends or key metrics from a chart generated by a data tool.

  **Visual tool output review:** Any MCP tool that produces images can now have its output directly analyzed by the agent in context.
</Update>

<Update label="May 6th, 2026" tags={["Added"]}>
  ## Context Compaction: Keep Your Agents Sharp in Long Conversations

  🎯 **What is it?**

  Context Compaction is a new feature that automatically summarizes earlier parts of long conversations with your agents. Instead of losing context or hitting limits, Dust intelligently condenses the conversation history while preserving the essential information your agent needs to continue working effectively.

  💡 **Why is it useful?**

  During extended work sessions (like analyzing complex documents, iterating on code, or working through multi-step projects), conversations can become very long. Previously, this could degrade agent performance or force you to start a new conversation and lose your working context. Context Compaction solves this by maintaining quality throughout long interactions while keeping your full conversational context available in summarized form.

  ⚙ **How does it work?**

  A new usage indicator appears in your input bar showing how much context is being used. The system guides you through three stages: at 30% usage, compaction becomes available; at 70%, you'll see a helpful reminder to compact; and at 80%, the system will pause new messages until you run compaction to ensure optimal performance.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Complex Analysis Projects**: You're working with an agent to analyze multiple quarterly reports over several hours. Instead of splitting your work across multiple conversations, Context Compaction lets you maintain the full analytical thread while summarizing earlier findings.

  **Iterative Development**: You're collaborating with an agent on code development with many iterations and refinements. The conversation naturally grows long, but compaction preserves all your decisions and context without performance degradation.

  📈 **Benefits for you**

  Save time by never needing to restart conversations or re-explain context. Maintain better continuity in complex projects. Work confidently knowing your agent has access to the full conversation history in an optimized format.

  🚀 **How to access it?**

  Context Compaction is now available to all users. Watch for the context usage indicator in your input bar. When it appears, you'll be guided through the process automatically. Learn more in our [documentation](/docs/user-documentation/agents/context-compaction).
</Update>

<Update label="May 4th, 2026" tags={["Added"]}>
  ## GMail Labels Management and Email Archiving

  🎯 **What is it?**

  Your agents can now apply labels to emails and archive messages directly in Gmail. These new capabilities extend the existing Gmail tools, giving your agents more control over inbox management.

  💡 **Why is it useful?**

  Many workflows require not just reading emails, but organizing them too. Agents can now triage customer requests, categorize vendor communications, or clean up your inbox automatically, no manual sorting required. Combined with Wake-ups (scheduled agent runs), you can fully automate inbox maintenance.

  ⚙ **How does it work?**

  Agents with access to the Gmail tools can now use new actions to apply any of your existing Gmail labels and move emails to archive. These actions work alongside the existing Gmail capabilities your agents already have.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Automated inbox triage**: Set up an agent that runs every morning via Wake-ups, reviews new emails, applies labels like "Urgent", "Follow-up", or "Read Later", and archives low-priority messages.

  **Customer support categorization**: Have an agent automatically label incoming support emails by topic (Billing, Technical, Feature Request) and archive resolved threads, keeping your team's shared inbox organized.

  **Vendor communication management**: Create an agent that identifies invoices, contracts, and purchase orders in your email, applies the appropriate labels, and archives them after filing the information in your system.

  📈 **Benefits for you**

  * **Save time**: Eliminate manual email sorting and filing
  * **Stay organized**: Maintain a clean, well-labeled inbox automatically
  * **Enable new workflows**: Combine with Wake-ups for fully autonomous inbox management
  * **Reduce noise**: Archive processed emails so you can focus on what matters

  🚀 **How to access it?**

  The new label and archive capabilities require additional Gmail permissions. To enable them:

  1. Go to **Personal Settings** (bottom left of Dust)
  2. Find your Gmail connection and **disconnect** it
  3. The next time an agent needs Gmail access, you'll be prompted to **re-authenticate** with the updated permissions

  Once re-authenticated, your agents will automatically have access to the new label management and archiving tools.
</Update>

<Update label="April 29th, 2026" tags={["Added"]}>
  ## Wake-ups: Agents can now schedule themselves to continue work later

  🎯 **What is it?**

  Agents can now set their own wake-up schedules to resume work at a future time within an ongoing conversation. Think of it as giving your agent the ability to "set a reminder" for itself to check back on something, run a recurring task, or wait for a response before continuing.

  💡 **Why is it useful?**

  Sometimes work doesn't happen all at once. You might need to wait for someone to respond, check if a condition has changed, or simply run the same process every day at 9 AM. Until now, you'd have to manually come back and prompt the agent again. With wake-ups, the agent handles the timing for you automatically.

  ⚙ **How does it work?**

  Agents have access to a wake-up tool that lets them schedule themselves to continue the conversation at a specific time or on a regular schedule (daily, weekly, etc.). Once scheduled, the agent will automatically "wake up" and continue where it left off.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Follow-up automation**: Ask an agent to send an email to a colleague and check back in 2 hours to see if they've responded, then proceed with next steps based on their answer.

  **Recurring updates**: Have an agent refresh a data dashboard every Monday at 9 AM, or check project status every Friday afternoon and send you a summary.

  **Real-time monitoring**: Set an agent to check an external system every 30 minutes until a specific condition is met (like a deployment completing or a document being approved).

  📈 **Benefits for you**

  No more manual follow-ups or remembering to re-prompt your agents. You can now set up truly autonomous workflows that span hours, days, or weeks, with the agent managing its own schedule and keeping work moving forward without your intervention.

  🚀 **How to access it?**

  Wake-ups are now available to all users. Ask your agent to "check back in \[time]" or "run this every \[schedule]" and it will use the wake-up tool automatically. For more details on how to configure wake-up schedules, check out the documentation: [/docs/user-documentation/agents/tools/wake-ups](/docs/user-documentation/agents/tools/wake-ups)
</Update>

<Update label="April 28th, 2026" tags={["Added"]}>
  ## Gong Tools Integration via MCP

  🎯 **What is it?**

  You can now connect Gong to Dust through our MCP (Model Context Protocol) integration. This allows your agents to access call transcripts and notes directly during conversations and workflows, without leaving Dust.

  💡 **Why is it useful?**

  Sales and customer success teams have valuable insights locked in Gong recordings. By connecting Gong as a live tool, your agents can pull context from customer calls on-demand, right when you need it: preparing for a meeting, writing follow-ups, or analyzing trends.

  ⚙️ **How does it work?**

  Once connected, Gong becomes available as a tool that your agents can use. When an agent needs information from a call, it queries Gong in real-time and retrieves the relevant transcript or notes to inform its response.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Pre-meeting preparation**: Ask an agent to "Summarize the last 3 calls with Acme Corp" and get instant context before your next meeting.

  **Customer insight synthesis**: Create a workflow that pulls key objections or feature requests from recent calls and compiles them into a weekly report.

  **Follow-up automation**: Have an agent draft personalized follow-up emails that reference specific points discussed in the most recent Gong call.

  📈 **Benefits for you**

  * **Instant access**: No manual searching through Gong. Your agents retrieve exactly what they need
  * **Better context**: Agents can reference actual customer conversations to provide more relevant responses
  * **Time savings**: Eliminate copy-pasting between tools and cut steps from your workflow

  🚀 **How to access it?**

  This feature is available to all workspaces. Check out our documentation to set up the integration: [/docs/user-documentation/agents/tools/gong](/docs/user-documentation/agents/tools/gong)

  **Note**: This is a live, tool-based integration. If you're looking to synchronize transcripts into Dust for semantic search across all your data, use the Gong connector instead.
</Update>

<Update label="April 28th, 2026" tags={["Added"]}>
  ## Slash Commands Now Available in the Input Bar

  🎯 **What is it?**

  You can now type `/` directly in the conversation input bar to quickly access and add capabilities to your conversations. A searchable dropdown appears instantly, listing all available skills and MCP tools, which you can filter and select using your keyboard or mouse.

  💡 **Why is it useful?**

  Previously, accessing capabilities required navigating through the toolbar, which could interrupt your workflow. This new slash command feature removes that detour, letting you stay focused on the conversation while quickly adding the tools you need, similar to how modern text editors and communication tools work.

  ⚙ **How does it work?**

  Type `/` in the input bar, and a dropdown menu appears with all your available capabilities. Continue typing to filter results using fuzzy matching (you don't need to type exact names), then select what you need with your keyboard (arrows, Enter, Tab) or mouse. Press Escape to close the menu.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  * **Quick data analysis**: Type `/` then "calc" to instantly find and add calculator or data processing tools without breaking your thought process
  * **Adding specialized skills mid-conversation**: Type `/` then start typing a skill name like "research" to quickly enable research capabilities when you realize you need them

  📈 **Benefits for you**

  This feature saves time and keeps you in flow. Instead of moving your cursor to the toolbar, you can access everything through keyboard shortcuts, making conversations with agents faster and more efficient, especially valuable when you're working through multiple tasks quickly.

  🚀 **How to access it?**

  The feature is available to everyone right now. Just type `/` in any conversation input bar to try it out.
</Update>

<Update label="April 24th, 2026" tags={["Added"]}>
  ## GPT 5.5 now available on Dust

  🎯 **What is it?**

  OpenAI's latest model, GPT 5.5, is now available on Dust. You can select it when building custom agents or use it directly through the global agent interface.

  💡 **Why is it useful?**

  GPT 5.5 represents OpenAI's newest advancement, offering improved performance over the previous GPT 5.4 model. This means better reasoning, more accurate responses, and more capable agents.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  * **Better analysis agents**: Build agents that handle complex research, data analysis, or strategic planning with improved reasoning capabilities
  * **Improved conversational agents**: Create customer-facing or internal support agents that provide more nuanced and accurate responses

  📈 **Benefits for you**

  Access to OpenAI's latest model means your agents can deliver higher quality outputs, handle more sophisticated tasks, and provide better assistance to your team.

  🚀 **How to access it?**

  * **For custom agents**: Open the agent builder and select "GPT 5.5" from the model dropdown menu
  * **For quick tasks**: Use the global agent which now runs on GPT 5.5 by default
</Update>

<Update label="April 22nd, 2026" tags={["Added"]}>
  ## GPT Image 2: Enhanced Image Generation Now Default on Dust

  🎯 **What is it?**

  OpenAI has released GPT Image 2, a new image generation model that's now the default for all image creation on Dust. This model brings significant improvements in image quality, detail rendering, and the ability to accurately generate readable text within images.

  💡 **Why is it useful?**

  Previous image generation models often struggled with two key challenges: editing existing images effectively and incorporating clear, readable text into generated visuals. GPT Image 2 addresses both of these limitations, opening up new possibilities for creating professional-quality images that include precise text elements, something that was previously difficult or impossible to achieve consistently.

  ⚙️ **How does it work?**

  GPT Image 2 is automatically used whenever you generate images through Dust agents or workflows. The model excels at understanding complex prompts, maintaining high fidelity to your specifications, and rendering fine details with unprecedented precision.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Marketing Materials**: Generate branded images with company names, slogans, or product descriptions clearly visible and professionally rendered, perfect for social media posts, presentations, or campaign materials.

  **Data Visualization Enhancement**: Create infographic-style images with charts, labels, and annotations that include actual readable data points and explanations, making complex information more accessible.

  **Image Editing & Iteration**: Take existing images and ask your agent to modify specific elements while preserving the overall composition, useful for refining visual assets or creating variations of existing designs.

  📈 **Benefits for you**

  You can now generate more professional, production-ready images directly within your Dust workflows. The ability to include clear text eliminates the need for post-processing in external design tools, saving time and cutting steps from your creative process. The improved editing capabilities also mean you can iterate on images more efficiently.

  🚀 **How to access it?**

  No action needed: GPT Image 2 is already the default image generation model on Dust. Continue using image generation in your agents as you normally would to automatically benefit from these improvements.
</Update>

<Update label="April 20th, 2026" tags={["Added"]}>
  ## Agents can now ask you questions to clarify their next steps

  🎯 **What is it?**

  Agents can now proactively pause and ask you structured questions mid-conversation when they need clarification. Instead of guessing or making assumptions, they'll present you with single or multi-select options to help guide their next actions.

  💡 **Why is it useful?**

  Until now, when an agent faced ambiguity, it would either guess (sometimes incorrectly), take a random path, or get stuck trying to interpret unclear instructions. Now, agents can ask you directly, turning uncertainty into a quick, interactive exchange. This prevents wasted time, reduces errors, and makes conversations feel more collaborative and intuitive.

  ⚙️ **How does it work?**

  When an agent needs input to proceed, it will pause and present you with a clear question and predefined answer options (single-choice or multiple-choice). You select your answer, and the agent continues with exactly the information it needs.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Research workflow**: You ask an agent to "analyze our competitors." Instead of picking arbitrary companies, it asks: "Which competitors should I focus on?" with options like \[Company A, Company B, Company C, All of the above].

  **Content formatting**: You request a report summary. The agent asks: "What format do you prefer?" with options like \[Bullet points, Paragraph form, Executive summary].

  **Data prioritization**: You ask for insights from multiple sources. The agent clarifies: "Which data sources should I prioritize?" offering \[Internal reports, Public data, Customer feedback, All sources].

  📈 **Benefits for you**

  * **More accurate outputs**: Agents work with your explicit input instead of assumptions
  * **Faster resolution**: No back-and-forth to correct misunderstandings
  * **Better control**: You guide the agent's direction at key decision points
  * **Richer interactions**: Conversations feel more natural and collaborative

  🚀 **How to access it?**

  This feature is available by default for all agents on Dust and Deep Dive, and works in Slack conversations as well. No configuration needed: your agents will automatically ask questions when they need clarification.
</Update>

<Update label="April 17th, 2026" tags={["Added"]}>
  ## 🔒 Private-by-default conversation URLs

  🎯 **What is it?**

  Workspace admins can now configure Dust conversations to be private by default. When this setting is enabled, conversation URLs are only accessible to participants: anyone else who tries to access the link will see a 404 error, ensuring the conversation's existence isn't even revealed to non-participants.

  💡 **Why is it useful?**

  This feature addresses the risk of accidentally sharing sensitive conversations through URLs. While Dust conversations are built for collaboration, sometimes conversation links get shared unintentionally (in Slack, email, or screenshots). With private-by-default URLs, you get an extra layer of protection against accidental leakage while maintaining flexibility when you explicitly need to share.

  ⚙️ **How does it work?**

  When a workspace admin enables this setting, all new conversations automatically become private: only people directly participating can access them via URL. Participants can still use @mentions to invite others to join conversations, and if needed, anyone in the conversation can flip it back to "accessible to workspace members" from the conversation menu.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **HR and sensitive discussions**: When discussing performance reviews, salary negotiations, or confidential employee matters, conversations stay strictly between participants even if someone accidentally copies the URL.

  **Strategic planning**: When working on confidential product launches, M\&A discussions, or competitive analysis with a small team, you can ensure the conversation doesn't leak to the broader workspace if a link is shared out of context.

  📈 **Benefits for you**

  * **Stronger security**: Reduce the risk of sensitive information leakage through shared URLs
  * **Peace of mind**: Know that conversations stay private unless you explicitly choose to share them
  * **Flexible control**: Keep the ability to make specific conversations workspace-accessible when collaboration requires it
  * **Maintain collaboration**: @mentions still work, so you can invite people without compromising privacy

  🚀 **How to access it?**

  Workspace admins can enable this feature by navigating to **Admin → Workspace Settings** and toggling the private-by-default conversation URLs setting. Once enabled, all new conversations will be private by default, while participants can override this on a per-conversation basis from the conversation menu.
</Update>

<Update label="April 17th, 2026" tags={["Added"]}>
  ## Import skills from GitHub or .zip file

  🎯 **What is it?**

  You can now import skills directly into Dust from a GitHub repository or by uploading a .zip file from your computer. This new capability gives you more flexibility in how you manage and deploy your skills across your workspace.

  💡 **Why is it useful?**

  If you're managing multiple skills or working with a team that maintains skills in a version control system, you previously had to manually copy and paste code into Dust. This new import feature allows you to centralize your skills in GitHub (or any other repository) and keep them in sync with your CI/CD pipeline, ensuring your Dust agents always use the latest versions.

  ⚙ **How does it work?**

  Provide a GitHub repository URL or upload a .zip file containing your skill files. Dust will import the skill structure and make it available in your workspace.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Development teams maintaining shared skills**: Your engineering team maintains a repository of company-specific skills (e.g., data formatting, internal API integrations). When you update the skill in GitHub, you can quickly re-import it to Dust to keep all agents synchronized.

  **Distributing skills across workspaces**: You've built a skill for market research and want to deploy it across multiple Dust workspaces (different departments or clients). Export it once as a .zip and import it wherever needed.

  📈 **Benefits for you**

  * **Version control**: Keep your skills in Git alongside your other code, with full history and collaboration features
  * **Automation**: Integrate skill updates into your existing CI/CD workflows
  * **Portability**: Easily share and duplicate skills across workspaces without manual copying
  * **Consistency**: Ensure all team members are using the same version of your custom skills

  🚀 **How to access it?**

  This feature is available to everyone. When creating or updating a skill, look for the new import options that allow you to specify a GitHub repository URL or upload a .zip file.
</Update>

<Update label="April 16th, 2026" tags={["Added"]}>
  ## Steering: Conversations That Keep Up With You

  🎯 **What is it?**

  Steering lets you send messages to Dust agents *while the agent is working*. You can now see every step of the agent's work in real-time (thinking, tool calls, searches) and redirect it on the fly without canceling or losing progress. Additionally, messages are now scoped to one agent at a time, displayed in the input bar, so you no longer need to use @mentions.

  💡 **Why is it useful?**

  Previously, conversations with agents were strictly turn-based: you'd send a message, wait for the complete response, and only then could you course-correct if needed. This made it difficult to guide the agent early when you saw it heading in the wrong direction, and you had no visibility into what was happening behind the scenes. Steering solves this by letting you shape the output as it's being built, not after it's done.

  ⚙ **How does it work?**

  As soon as an agent starts working, you'll see live updates of each step it takes. If you notice it's going off track or you want to add context, send a new message, and the agent will incorporate your input immediately without restarting from scratch.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Research and analysis**: You ask an agent to research a topic, but after seeing the first few searches, you realize you need a different angle. Instead of waiting for the full response, you immediately steer it: "Actually, focus on European regulations instead."

  **Data exploration**: An agent starts querying multiple data sources, and you see it's pulling from the wrong database. You send a quick message to redirect it before it completes unnecessary work, saving time and getting accurate results faster.

  📈 **Benefits for you**

  * **Save time**: Redirect agents early instead of waiting for full responses you'll need to regenerate
  * **Better control**: Guide the conversation dynamically based on what you see happening
  * **Full transparency**: Understand exactly what the agent is doing at each moment
  * **Smoother workflow**: No more @mentions needed when working with a single agent

  🚀 **How to access it?**

  Steering is now available to everyone automatically. Start a conversation with any agent and try sending a follow-up message while it's working. For complete details and examples, visit the [full documentation](/docs/user-documentation/agents/steering-conversations).

  <br />
</Update>

<Update label="April 14th, 2026" tags={["Added"]}>
  ## 🦊 Dust Browser Extension Now Available on Firefox

  🎯 **What is it?**

  The Dust browser extension is now officially available on Firefox! You can install it directly from the Firefox Add-ons store and enjoy the same Dust experience across all major browsers.

  💡 **Why is it useful?**

  Many of you use Firefox as your primary browser, and until now, the Dust extension was only available on Chromium-based browsers. We've expanded our support to ensure all teams can access Dust's capabilities directly from their preferred browser, regardless of which one they use.

  ⚙ **How does it work?**

  Visit the Firefox Add-ons store and install the Dust extension. Once installed, you'll have quick access to your agents and Dust features right from your browser toolbar, just like on Chrome or Edge.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **For Firefox users**: Finally get the same browser integration your Chrome-using colleagues have been enjoying: quick access to agents, easy content sharing, and uninterrupted workflows without switching browsers.

  **For mixed-browser teams**: Ensure everyone on your team can use Dust extension features regardless of their browser preference, making collaboration more consistent and inclusive.

  📈 **Benefits for you**

  * **Browser flexibility**: Use Dust on Firefox, Chrome, Edge, or any Chromium-based browser
  * **Consistent experience**: Same features and functionality across all supported browsers
  * **No workflow changes**: Firefox users can now integrate Dust into their daily browsing without switching browsers

  🚀 **How to access it?**

  Visit the Firefox Add-ons store: [https://addons.mozilla.org/en-US/firefox/addon/dust/](https://addons.mozilla.org/en-US/firefox/addon/dust/) and click "Add to Firefox". The extension will be ready to use immediately after installation.
</Update>

<Update label="April 14th, 2026" tags={["Added"]}>
  ## Microsoft Teams Meeting Transcripts Now Available in Dust

  🎯 **What is it?**

  We've expanded our Microsoft Teams integration with two new capabilities: agents can now list your Teams meetings and retrieve their transcripts directly within Dust. This means your meeting content is now accessible to your agents, just like your other connected data sources.

  💡 **Why is it useful?**

  Meeting discussions contain valuable information (decisions made, action items assigned, key insights shared), but this knowledge often stays locked in transcript files or requires manual review. By making transcripts accessible to your agents, you can automatically extract value from your meetings without manual work.

  ⚙️**How does it work?**

  Once your workspace admin reconnects the Microsoft Teams tool (to approve the new permissions), agents can access meeting transcripts using two new tools: one to list meetings, and another to retrieve transcript content when available.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Meeting Follow-up Agent**: Create an agent that reviews your leadership team's weekly sync, extracts action items, and sends a summary to relevant stakeholders automatically.

  **Cross-team Knowledge Capture**: Build an agent that monitors product planning meetings, identifies feature decisions and requirements, and updates your product documentation or project tracker.

  **Personal Meeting Assistant**: Set up an agent that summarizes all your meetings from the past week, highlighting decisions you participated in and tasks assigned to you.

  📈 **Benefits for you**

  * **Save time**: No more manual note-taking or transcript review
  * **Capture knowledge**: Turn meeting discussions into searchable, actionable insights
  * **Enable new workflows**: Automate meeting follow-ups, summaries, and action item tracking
  * **Connect the dots**: Let agents reference meeting decisions alongside your other company knowledge

  🚀 **How to access it?**

  **Action required**: A workspace admin must reconnect the Microsoft Teams tool in your Dust workspace to approve the new permissions (`OnlineMeetings.Read` and `OnlineMeetingTranscript.Read.All`). Once reconnected, the new meeting transcript tools will be available to all agents in workspaces using Microsoft Teams.
</Update>

<Update label="April 13th, 2026" tags={["Added"]}>
  ## 📧 Share MiniApps with specific people via email invite

  🎯 **What is it?**

  You can now invite specific people to view a MiniApp by sending them an email invitation. Recipients receive a direct link to access the MiniApp, even if they're not part of your Dust workspace.

  💡 **Why is it useful?**

  Previously, MiniApp sharing was all-or-nothing at the workspace level. This new capability gives you granular control over who can see your MiniApps, making it much easier to collaborate with specific stakeholders, partners, or team members. You can also track who has viewed your MiniApp.

  ⚙ **How does it work?**

  When sharing a MiniApp, you can now enter email addresses of people you want to invite. Each person receives an email with a secure link to access that specific MiniApp. This respects your workspace sharing policy settings.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Executive reporting**: Share a sales dashboard MiniApp with your CEO and CFO without giving them access to all workspace MiniApps.

  **Client presentations**: Send a project status MiniApp directly to external clients or partners for review, while keeping other internal MiniApps private.

  **Cross-team collaboration**: Share specific data visualizations with stakeholders from other departments who need visibility on just that information.

  📈 **Benefits for you**

  * **Precise control**: Share MiniApps on a need-to-know basis instead of workspace-wide
  * **Better collaboration**: Work directly with external partners and selective internal stakeholders
  * **Visibility tracking**: See who has actually viewed your MiniApp
  * **Time-saving**: No more screenshots or manual exports, just send a direct link

  🚀 **How to access it?**

  This feature is now available to everyone. When viewing any MiniApp, look for the sharing options and select "Invite by email" to start sharing with specific people.
</Update>

<Update label="April 9th, 2026" tags={["Added"]}>
  ## Amplitude MCP Integration: Query Your Product Data with Natural Language

  🎯 **What is it?**

  Dust now connects directly to Amplitude through their remote MCP (Model Context Protocol) server. Your agents can now access Amplitude's product analytics platform to query data, analyze experiments, manage dashboards, create cohorts, and more, all through natural language conversations.

  💡 **Why is it useful?**

  Amplitude is a leading product analytics platform that holds critical data about how users interact with your product. Until now, accessing this data required switching contexts, learning the Amplitude interface, or writing queries manually. With this integration, you can ask your Dust agents to retrieve and analyze Amplitude data conversationally, making product insights more accessible to your entire team.

  ⚙ **How does it work?**

  The integration uses Amplitude's official remote MCP server. Connect the appropriate server (US or EU, depending on your data residency requirements) to your Dust workspace's MCP catalog, and your agents can start querying Amplitude directly.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Product Manager reviewing experiment results**: "Show me the conversion rate for the checkout experiment we launched last week and compare it to the control group."

  **Customer Success analyzing user behavior**: "Create a cohort of users who completed onboarding in the last 30 days but haven't returned since."

  **Executive reviewing dashboard data**: "Pull the key metrics from our weekly product dashboard and summarize any significant changes from last week."

  📈 **Benefits for you**

  * **Democratize product data**: Make Amplitude insights accessible to anyone on your team through natural language, not just analytics experts
  * **Faster decision-making**: Get answers about product performance without leaving your workflow
  * **Automated reporting**: Build agents that regularly pull and synthesize Amplitude data for stakeholder updates

  🚀 **How to access it?**

  Connect Amplitude to your Dust workspace by adding the appropriate remote MCP server to your MCP catalog:

  * **US residency**: `https://mcp.amplitude.com/mcp`
  * **EU residency**: `https://mcp.eu.amplitude.com/mcp`

  Once connected, your agents will be able to interact with Amplitude's capabilities through conversation. You'll need your Amplitude credentials to complete the setup.
</Update>

<Update label="April 9th, 2026" tags={["Added"]}>
  ## Notion MCP Tools Now Use Official Notion Server

  ## 📌 Context

  When you create a new Notion MCP tool in Dust, it will now use Notion's official MCP server instead of our previous implementation. We've made this change to improve both the user experience and the reliability of Notion integrations.

  ## 🔄 Impact on Dust

  We've transitioned to Notion's official MCP server, which brings two significant improvements:

  **Better authentication model ("run as you"):**

  * The tool now has access to everything you can access in Notion, no need to manually select which pages to share
  * When you modify a document or add a comment through Dust, it appears as coming from you, not from the Dust integration

  **Improved reliability:**

  * Better handling of page relations and databases
  * Faster searches and fewer loops when finding related pages
  * Overall more stable performance

  Early feedback from users has been very positive, with reports of faster and more reliable operations.

  ## 👤 Impact for you

  **If you're creating new Notion MCP tools:**

  You'll automatically benefit from the improved official implementation. The authentication flow will be simpler, and you'll experience better performance.

  **If you already have Notion MCP tools:**

  Your existing tools will continue to work exactly as before using the previous implementation. There's no disruption to your current workflows.

  **Important clarification:**

  This change only affects Notion MCP tools (created under Spaces / Add Tools). Your Notion Connector remains completely unaffected and continues to work as usual.

  ## ✅ Actions required

  **No action required on your part** for existing tools: they'll keep working as-is.

  If you have agents that used Notion tools before, you can edit them and replace them with the new tools (once you have added them to your workspace).
</Update>

<Update label="April 8th, 2026" tags={["Added"]}>
  ## Interactive Workspace Analytics Dashboard & Public API

  🎯 **What is it?**

  Workspace admins now have access to a full analytics dashboard directly in Dust, plus a new public API endpoint to export all your workspace data. The dashboard gives you real-time visibility into how Dust is being used across your organization (from daily active users to agent performance), all with interactive charts and CSV export capabilities. The public API (`GET /api/v1/w/{wId}/analytics/export`) lets you programmatically pull 7 different data tables (usage metrics, active users, sources, agents, users, skill usage, and tool usage) to integrate with your own BI tools.

  💡 **Why is it useful?**

  As a workspace admin, you need clear visibility into adoption and ROI to justify investment and drive Dust usage across your organization. Until now, getting this data required manual CSV exports or reaching out to Customer Success for custom reports. This dashboard brings Dust in line with what you expect from enterprise tools: self-serve analytics that help you make data-driven decisions.

  ⚙ **How does it work?**

  The interactive dashboard is available directly in your Dust workspace. You can select flexible time ranges (7, 15, 30, or 90 days), view activity trends over time, monitor adoption metrics (DAU/WAU/MAU), see usage by source (web, Slack, extension, API), explore tool usage patterns, and identify your top-performing agents. Every chart can be exported to CSV for deeper analysis. The API endpoint works with simple GET requests and returns data in CSV format for easy integration.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Executive Reporting**: Pull monthly analytics showing DAU growth and top 10 agents by usage to demonstrate ROI to leadership and secure budget for broader rollout.

  **Adoption Campaigns**: Identify departments with low WAU rates and channels where engagement is highest, then target outreach through those preferred channels (Slack vs. web vs. extension).

  **Agent Optimization**: Track which agents are being used most frequently and by whom, then deprecate underused agents and promote high-value ones in your internal communications.

  **BI Integration**: Feed the API data into Tableau, Power BI, or your internal dashboards to combine Dust metrics with other productivity KPIs across your tech stack.

  📈 **Benefits for you**

  * **Save time**: No more manual exports or waiting for CS reports
  * **Make informed decisions**: Real-time data on what's working and where to focus your efforts
  * **Prove value**: Concrete metrics to demonstrate ROI to stakeholders
  * **Flexibility**: Use the dashboard for quick insights or the API for deep integrations

  🚀 **How to access it?**

  The analytics dashboard is available now to all workspace admins on all plans. Look for the Analytics section in your workspace settings. The API endpoint is live at `GET /api/v1/w/{wId}/analytics/export`. Check our API documentation for authentication details and available data tables.

  ***

  ## ⚠️ API Deprecation Notice

  📌 **Context**

  Two legacy API endpoints (`/api/v1/w/{wId}/usage` and `/api/v1/w/{wId}/workspace-usage`) are being deprecated and will be sunset on **June 1, 2026**. These are being replaced by the new `/api/v1/w/{wId}/analytics/export` endpoint, which provides all the same data plus additional metrics (skill usage, tool usage, per-agent and per-user breakdowns).

  🔄 **Impact on Dust**

  We're consolidating analytics endpoints to provide a single, more complete API that covers all workspace analytics needs while maintaining consistency with the new dashboard experience.

  👤 **Impact for you**

  **If you're using the old endpoints**: You need to migrate to the new endpoint before June 1, 2026. After that date, the legacy endpoints will stop working.

  **If you're not using the API**: No impact: the dashboard works out of the box with no changes needed.

  ✅ **Actions required**

  **Before June 1, 2026**:

  1. Audit any integrations, scripts, or BI tools currently calling `/api/v1/w/{wId}/usage` or `/api/v1/w/{wId}/workspace-usage`
  2. Update them to use `/api/v1/w/{wId}/analytics/export` with the appropriate data table parameter
  3. Test the new endpoint. The new API is a strict superset, so you'll get everything you had before plus more

  **Need help with migration?** Reach out to your Customer Success Manager or [support@dust.tt](mailto:support@dust.tt). We're here to help ensure a smooth transition.
</Update>

<Update label="April 8th, 2026" tags={["Added"]}>
  ## Workspace Analytics: Interactive Dashboard + Public API

  🎯 **What is it?**

  Workspace admins now have access to a full analytics dashboard directly within Dust, plus a new public API endpoint for programmatic data access. The dashboard provides real-time visibility into adoption metrics (DAU/WAU/MAU), activity trends (messages, conversations), usage breakdown by source (web, Slack, extension, API), tool usage patterns, and top-performing agents. Each chart supports CSV export and offers flexible time ranges (7, 15, 30, or 90 days).

  For teams that need to integrate Dust data into their own business intelligence tools, the new `GET /api/v1/w/{wId}/analytics/export` endpoint enables programmatic access to 7 data tables: usage metrics, active users, sources, agents, users, skill usage, and tool usage.

  💡 **Why is it useful?**

  Enterprise teams need self-service visibility into how Dust is being adopted across their organization to measure ROI and drive engagement. Until now, getting this data required manual CSV exports or reaching out to Customer Success for custom reports. This brings Dust's analytics capabilities in line with enterprise expectations for modern SaaS tools.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Executive reporting**: Export monthly adoption metrics to include in your quarterly AI transformation reports, showing DAU/MAU trends and demonstrating ROI to leadership.

  **Usage optimization**: Identify which agents are most popular and which sources drive the most engagement, then use those insights to optimize your Dust rollout strategy and training programs.

  **BI integration**: Pipe Dust analytics data into your existing Tableau, Looker, or PowerBI dashboards alongside other tools to create a unified view of productivity tool adoption.

  📈 **Benefits for you**

  * **Self-service insights**: No more waiting for manual reports. Get instant visibility into adoption patterns
  * **Data-driven decisions**: Use concrete metrics to guide your Dust rollout strategy
  * **Flexible export**: Download charts as CSV or pull data programmatically via API
  * **Executive-ready**: Generate adoption reports that demonstrate value to stakeholders

  🚀 **How to access it?**

  The analytics dashboard is available now to all workspace admins across all plans. Access it from your workspace admin panel. For API access, refer to the documentation for the new `/api/v1/w/{wId}/analytics/export` endpoint.

  ***

  ## ⚠️ API Deprecation Notice

  📌 **Context**

  The legacy analytics endpoints `/api/v1/w/{wId}/usage` and `/api/v1/w/{wId}/workspace-usage` are now deprecated and will be sunset on **June 1, 2026**.

  🔄 **Impact on Dust**

  We've built a new, more complete analytics API that supersedes these legacy endpoints, providing richer data and better functionality.

  👤 **Impact for you**

  **If you or your team are using the old endpoints**: You'll need to migrate to the new `/api/v1/w/{wId}/analytics/export` endpoint before June 1, 2026. The new endpoint is a strict superset: it covers everything the old endpoints provided plus adds skill usage, tool usage, and detailed per-agent and per-user breakdowns.

  **If you're not using these endpoints**: No impact, no action needed.

  ✅ **Actions required**

  * **Review your integrations**: Check if any of your systems or scripts are calling `/api/v1/w/{wId}/usage` or `/api/v1/w/{wId}/workspace-usage`
  * **Plan your migration**: Update those integrations to use the new `/api/v1/w/{wId}/analytics/export` endpoint before June 1, 2026
  * **Reach out if needed**: If you need assistance with migration, contact your Customer Success team
</Update>

<Update label="April 8th, 2026" tags={["Added"]}>
  ## Slack responses: streaming, live actions & rich formatting

  **Better Slack responses for Dust agents**

  Three improvements to how Dust agents respond in Slack, shipping together.

  🔄 **Smoother streaming**

  Agent responses now appear in real time as they're being generated, using Slack's native streaming. The experience feels faster and more alive, no more waiting for a full response to land before you can start reading !

  🔎 **See what your agent is doing**

  While an agent works, a live progress indicator shows which tools it's using and what it's doing with them. For web searches, you can see the query it ran. For browsing, you can see the sites it visited and the sources it pulled from. Once the agent is done, the indicator disappears cleanly.

  ✨ **Better formatted responses**

  Tables, dividers, and code blocks now render properly in Slack. Agents that output structured content like pipeline summaries, incident reports, or side-by-side comparisons will now display the way they were meant to, without workarounds.

  <Warning>
    Responses that include file uploads use the previous format for now.
  </Warning>

  <br />

  🔥 **Concrete Use Cases**

  All your current slack use cases, improved !

  🚀 **How to access it?**

  This feature is rolling out progressively to all Slack users this week. No action required on your part, you'll automatically see these improvements in your Slack workspace when they're available.
</Update>

<Update label="April 8th, 2026" tags={["Added"]}>
  ## GitOps sync for Skills & Agent configurations with GitHub Action

  🎯 **What is it?**

  We've released a new official GitHub Action called `dust-github-action` that lets you manage your Dust Skills and Agent configurations directly from your Git repository. You can now version-control your Dust setup, review changes through pull requests, and automatically sync your workspace from CI/CD pipelines.

  💡 **Why is it useful?**

  Managing Dust configurations through code gives you the same benefits you already get with your application code: change history, peer review, rollback capabilities, and automation. Instead of manually updating agents and skills in the Dust interface, you can define them in your repository and let your CI pipeline keep everything in sync. This is particularly valuable for teams that want to maintain consistency across workspaces, review configuration changes before deployment, or integrate Dust setup into their existing development workflows.

  ⚙ **How does it work?**

  The GitHub Action provides methods to "upsert" (create or update) Skills and Agent configurations from your repository into your Dust workspace. When you push changes to your repo or merge a PR, the action automatically applies those configuration changes to your workspace.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Development workflow**: Define your agents in YAML files in your repo, have teammates review changes in pull requests, then automatically deploy approved configurations to your production Dust workspace when merged to main.

  **Multi-workspace management**: Maintain a single source of truth for your agent configurations and sync them across development, staging, and production Dust workspaces using different GitHub Actions workflows.

  **Audit & rollback**: Track every change to your Dust setup in Git history, see who made what changes and why, and easily roll back to previous configurations if needed.

  📈 **Benefits for you**

  * **Better collaboration**: Review agent and skill changes through pull requests before they go live
  * **Version control**: Full history of all configuration changes with the ability to roll back
  * **Automation**: Reduce manual work by syncing configurations automatically from CI
  * **Consistency**: Keep multiple workspaces aligned using the same configuration source
  * **Integration**: Fits into your existing development workflows and tooling

  🚀 **How to access it?**

  The GitHub Action is available now for all workspace admins and developers using GitHub Actions. Check out the repository and documentation to get started: [https://github.com/dust-tt/dust-github-action](https://github.com/dust-tt/dust-github-action)

  The feature is in General Availability (GA) and ready for production use.
</Update>

<Update label="April 6th, 2026" tags={["Added"]}>
  ## Send Emails from Your Gmail Aliases

  🎯 **What is it?**

  You can now choose which email address to send from when using Dust agents with the Gmail tool. If you have aliases configured in your Gmail account (like [team@company.com](mailto:team@company.com) or [support@company.com](mailto:support@company.com)), agents can now send emails from these addresses instead of only your personal email.

  💡 **Why is it useful?**

  Many professionals use email aliases to represent teams, departments, or shared inboxes. Until now, when an agent sent an email on your behalf, it could only use your primary Gmail address. This created limitations when you needed to maintain a specific professional identity or represent a team.

  ⚙️ **How does it work?**

  When you ask an agent with the Gmail tool to send an email, you can now specify which of your configured Gmail aliases to use as the sender address. The agent will send the email from that alias, as long as it's properly set up in your Gmail account.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Customer Support**: Ask an agent to craft and send responses from your [support@company.com](mailto:support@company.com) alias, maintaining consistency in customer communications while saving time on routine replies.

  **Team Communications**: Have an agent send project updates or meeting summaries from your team's shared email address (like [marketing@company.com](mailto:marketing@company.com)), ensuring all correspondence appears to come from the team rather than an individual.

  📈 **Benefits for you**

  * **Professional consistency**: Maintain the right email identity for each context
  * **Team representation**: Send on behalf of groups or departments
  * **Time savings**: Automate email tasks without losing control over sender identity
  * **Better organization**: Keep communications aligned with your existing email structure

  🚀 **How to access it?**

  This feature is automatically available if you're using the Gmail tool. Ensure your aliases are configured in your Gmail account settings, then specify which address you'd like to use when asking an agent to send an email.
</Update>

<Update label="April 1st, 2026" tags={["Added"]}>
  ## Discover Skills - Find and leverage workspace capabilities directly in your agents

  🎯 **What is it?**

  Dust now includes a "Discover Skills" feature that allows agents to automatically find and use relevant skills from your workspace. Builders can flag specific skills as "discoverable," making them available to global agents like @dust and @deep-dive without manual configuration.

  💡 **Why is it useful?**

  Previously, if you wanted an agent to use a specific skill, you had to manually configure it for each agent. This created friction and meant many useful workspace skills went underutilized. With discoverable skills, your agents can now intelligently tap into your organization's collective capabilities, improving the baseline experience for everyone in your workspace.

  ⚙️**How does it work?**

  Builders can mark their skills as "discoverable" when creating or editing them. Once flagged, these skills become available to global agents, which can automatically detect when a skill is relevant to a user's request and activate it on the fly.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Sales team collaboration**: A sales ops builder creates a "CRM Integration" skill and marks it discoverable. Now when anyone asks @dust about customer data, the agent automatically uses that skill without individual setup.

  **Knowledge sharing**: Your engineering team builds a "Code Review Helper" skill. Mark it as discoverable, and @deep-dive can use it whenever someone asks technical questions, instantly improving responses across the workspace.

  📈 **Benefits for you**

  * **Zero configuration**: End users get access to these skills without any setup
  * **Better agent responses**: Global agents like @dust deliver more accurate, context-aware answers by tapping into workspace expertise
  * **Increased skill adoption**: Your team's best skills get used more widely, maximizing ROI on skill development
  * **Improved baseline experience**: Everyone in the workspace benefits from collective knowledge automatically

  🚀 **How to access it?**

  **For Builders**: When creating or editing a skill, look for the new "Make discoverable" option and enable it for skills you want to share workspace-wide.

  **For Users**: Use @dust or @deep-dive as usual - they'll automatically discover and use relevant skills when needed.
</Update>

<Update label="April 1st, 2026" tags={["Added"]}>
  ## Create Triggers on Any Agent You Can Talk To

  🎯 **What is it?**

  You can now create your own triggers on every agent you have access to, including default agents like `dust` and `deep-dive`. Triggers allow you to automate agent interactions based on specific events or conditions, extending automation beyond just the agents you've built yourself.

  💡 **Why is it useful?**

  Previously, trigger creation might have been limited to agents you owned or edited. We believe that if you can talk to an agent, you should be able to automate it. This opens up new automation possibilities across your entire workspace, letting you use any agent in your automated workflows.

  ⚙ **How does it work?**

  Create triggers directly from the Agent Details side panel of any agent you want to automate. Once created, all your triggers are centralized in your profile page where you can easily manage and monitor them.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Automated research digest**: Create a trigger on the `deep-dive` agent to automatically compile weekly competitive intelligence reports every Monday morning, even though you don't own that agent.

  **Team notification workflows**: Set up triggers on shared team agents to automatically notify specific channels when certain conditions are met, without needing editor permissions on those agents.

  **Cross-agent automation**: Build workflows that chain together multiple shared agents via triggers, creating sophisticated automation pipelines using agents created by different people across your organization.

  📈 **Benefits for you**

  * **Democratized automation**: Automate any agent you use, not just the ones you built
  * **Centralized management**: Find and control all your triggers in one place on your profile page
  * **Better collaboration**: Use agents built by colleagues in your automated workflows
  * **Transparency**: Agent editors can see and audit all triggers on their agents; admins maintain full oversight

  🚀 **How to access it?**

  1. Navigate to any agent you have access to
  2. Open the Agent Details side panel
  3. Create your trigger with your desired configuration
  4. Manage all your triggers from your profile page

  Agent editors can view and audit all triggers created on their agents directly in the builder. Workspace admins can delete any trigger if needed.
</Update>

<Update label="April 1st, 2026" tags={["Added"]}>
  ## API Keys Can Now Be Scoped to Multiple Spaces

  🎯 **What is it?**

  You can now configure a single API key to work across multiple spaces in your workspace, instead of being limited to one space at a time. This gives you more granular control over how integrations access your Dust environment.

  💡 **Why is it useful?**

  Previously, if you wanted an integration to access multiple spaces, you had two options: either give it workspace-wide access (too permissive) or create separate API keys for each space (too complex). This new capability follows the principle of least privilege: you can grant access to exactly the spaces an integration needs, nothing more and nothing less.

  ⚙️ **How does it work?**

  When creating or editing an API key in the admin UI, you can now select multiple spaces that the key should have access to. The permission resolution has been updated to handle this multi-space access smoothly.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Export shared agents**: You have an agent shared across 3 different team spaces (Sales, Marketing, Customer Success). You can now create one API key scoped to these 3 spaces to export or sync that agent's data, instead of managing 3 separate keys.

  **Controlled cross-team integration**: Your data pipeline needs to access specific spaces (Finance and Legal) but not others. You can create a single API key with access to only those two spaces, maintaining security while simplifying key management.

  📈 **Benefits for you**

  * **Better security**: Apply least-privilege principles without operational complexity
  * **Simpler management**: One key for multiple spaces instead of juggling multiple keys
  * **New workflows**: Run integrations across controlled sets of spaces that weren't practical before

  🚀 **How to access it?**

  This feature is already live for all workspace admins. When you create or manage API keys in your workspace admin panel, you'll see the option to select multiple spaces. All existing API keys have been automatically migrated, so nothing changes unless you want to adjust the configuration.
</Update>

<Update label="March 31st, 2026" tags={["Added"]}>
  ## Salesforce MCP Tool Can Now Create and Update Objects

  🎯 **What is it?**

  The Salesforce MCP tool has evolved beyond read access. It can now **create and update Salesforce objects** directly from within Dust. Any Salesforce object type that supports it (leads, opportunities, cases, contacts, custom objects, and more) is now writable by your agents.

  💡 **Why is it useful?**

  Until now, agents could query Salesforce data but any updates had to be made manually in Salesforce itself. This created a gap between insight and action: you'd get the answer from your agent, then switch tools to act on it. Write access closes that loop, letting agents complete tasks end to end, from retrieving data to updating records, without you leaving the conversation.

  ⚙️ **How does it work?**

  The Salesforce MCP tool now includes two new actions: **create object** and **update object**. Agents can call these during a conversation to write data back to your Salesforce org, using the same secure MCP connection already in place.

  ✨ **Concrete Use Cases**

  * **Meeting follow-ups**: After a call summary, have your agent create a new Salesforce task, log a call note, or update an opportunity stage in one step.
  * **Lead intake**: Process form responses or email content and have your agent create a lead record in Salesforce directly.
  * **Status updates**: Ask your agent to mark an opportunity as Closed Won and update the expected close date, without opening Salesforce.

  📈 **Benefits for you**

  Fewer manual data entry steps, faster CRM updates, and agents that can take meaningful action in Salesforce, not just report on it.

  🚀 **How to access it?**

  Write access is available to all users who already have the Salesforce MCP tool configured in their workspace. Use it in your existing agents. The new capabilities are available now.
</Update>

<Update label="March 30th, 2026" tags={["Added"]}>
  ## Email your agents directly at [agent-name@dust.team](mailto:agent-name@dust.team)

  🎯 What is it?

  You can now interact with your Dust agents directly via email. Send or forward an email to `agent-name@dust.team` and your agent will process it and reply back to you. This works just like talking to an agent in Slack or the web app, but right from your inbox.

  💡 Why is it useful?

  Many teams work primarily in email: customer support threads, vendor communications, contracts, bug reports. Until now, you had to switch to Dust's web app or Slack to get help from your agents. With email integration, agents meet you where you already work, making it faster to get answers, draft replies, or process information without context-switching.

  ⚙ How does it work?

  Once enabled in your workspace settings, you can send or forward emails to any agent using the format `agent-name@dust.team`. The agent processes your request and replies only to you (the sender). All conversations triggered by email are accessible in the Dust web app, just like agent conversations from Slack or Teams. If an agent needs authorization to use a specific tool, you'll receive a validation email with secure allow/decline links.

  ✨ Concrete Use Cases

  Here's how you could use it:

  **Customer Support**: Forward a customer complaint to your support agent and ask it to summarize the issue and suggest a reply draft.

  **Contract Review**: Send a vendor agreement to a specialized legal/compliance agent and get a quick analysis without leaving your email thread.

  **Internal Workflows**: CC an agent on an internal discussion thread and ask it to extract action items, create tickets, or draft follow-up communications.

  **Bug Triage**: Forward a bug report from a client to your technical agent for initial analysis and categorization.

  📈 Benefits for you

  * **Faster workflows**: No need to copy-paste email content into Dust, just forward and ask
  * **Stay in context**: Get agent help without leaving your inbox
  * **Flexible collaboration**: Use agents as you would a colleague: forward, CC, or send directly
  * **Consistent experience**: Same agent capabilities as Slack or web, accessible from email conversations in Dust

  🚀 How to access it?

  This feature is **opt-in**. To enable it:

  1. Go to **Workspace Settings → Capabilities → Email agents**
  2. Turn on the feature
  3. Start emailing your agents at `agent-name@dust.team`

  📖 Full documentation available here: [/docs/user-documentation/agents/integrations/send-and-forward-email-to-agents](/docs/user-documentation/agents/integrations/send-and-forward-email-to-agents)

  🔒 **Security note**: Just as you wouldn't click suspicious links in emails, avoid forwarding suspicious or untrusted emails to agents to minimize prompt injection risks.
</Update>

<Update label="March 30th, 2026" tags={["Added"]}>
  ## Configurable OAuth Scopes for Microsoft MCP Tools

  🎯 **What is it?**

  Admins can now customize which permissions (OAuth scopes) are requested when installing Microsoft MCP tools. When setting up tools like Outlook Mail, Outlook Calendar, Microsoft Drive, Excel, or Teams, you can uncheck optional permissions such as write access, shared mailboxes, or contacts access. Once configured, these restrictions apply automatically to all user connections in your workspace.

  💡 **Why is it useful?**

  Many enterprise organizations have strict Azure AD policies that require minimizing permission requests. Previously, MCP tools requested all possible scopes by default, which could trigger lengthy admin consent processes or even block installation entirely. This feature gives you granular control over the permission surface, making it easier to align Dust with your organization's security policies and get approvals faster.

  ⚙ **How does it work?**

  During the MCP tool installation flow, admins will see a list of available OAuth scopes with checkboxes. Uncheck any optional permissions your organization doesn't need. Dust will only request the scopes you've selected, and all users in your workspace will inherit these restrictions when they connect their personal Microsoft accounts to the agent.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Read-only access**: Your security team only wants agents to read emails and calendar events, not send or modify them. Uncheck write permissions during Outlook Mail and Calendar installation.

  **No shared mailbox access**: Your organization doesn't use shared mailboxes and your IT policy forbids requesting that permission. Uncheck the shared mailbox scope when installing Outlook Mail to avoid unnecessary admin consent blockers.

  📈 **Benefits for you**

  * **Faster deployment**: Reduce admin consent friction by requesting only the minimum required permissions
  * **Better security posture**: Minimize the permission surface and align with your zero-trust policies
  * **Greater control**: Tailor each tool's access level to match your organization's specific needs

  🚀 **How to access it?**

  This feature is automatically available when installing or reconfiguring Microsoft MCP tools (Outlook Mail, Outlook Calendar, Microsoft Drive, Excel, Teams). Workspace admins will see the configurable scopes during the installation flow. If you need this capability for other MCP tools, reach out to your Customer Success Manager.
</Update>

<Update label="March 20th, 2026" tags={["Added"]}>
  ## Google Drive Tool: Create Files in a Folder and Share Them Directly from Dust

  🎯 **What is it?**

  Dust agents can now create Google Docs, Sheets, and Slides directly in specific folders, and automatically manage file sharing permissions. Previously, agents could only create private Google Drive files in your root directory. Now they can share files on your behalf.

  💡 **Why is it useful?**

  This addresses a common workflow gap: agents could analyze data, draft content, compile reports and create the Google file, but you still had to manually place it in the right folder and share it with your team. Now, agents can complete the entire workflow autonomously, saving you several manual steps every time you need to create a shared document.

  ⚙ **How does it work?**

  When an agent creates a Google file, you can specify both the destination folder and who should have access. The agent handles file creation, placement, and permission settings in a single action.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Weekly Team Reports**: Ask an agent to compile your team's weekly metrics into a Google Sheet, place it in your "Weekly Reports" folder, and share it with your manager and teammates automatically.

  **Client Presentation Decks**: Have an agent draft a Google Slides presentation with project updates, save it to your "Client Materials" folder, and grant view access to specific client stakeholders.

  **Meeting Notes Distribution**: Create an agent that generates meeting summaries in Google Docs, stores them in your team's shared folder, and gives edit access to all attendees.

  **Collaborative Project Documents**: Ask an agent to create a project planning doc in Google Docs within your team's project folder and automatically share edit rights with all project members.

  📈 **Benefits for you**

  * **Time savings**: Eliminate 2-3 manual steps every time you create a shared document
  * **Fewer errors**: No more forgetting to share files or placing them in the wrong folder
  * **Complete workflows**: Agents can now fully automate document creation from start to finish
  * **Better collaboration**: Files are immediately accessible to the right people without follow-up

  🚀 **How to access it?**

  If you already have Google Drive connected to Dust, this capability is available immediately. When configuring an agent or using the Google Drive tool, specify the destination folder path and the sharing permissions you need. Your agent will handle the rest!
</Update>

<Update label="March 20th, 2026" tags={["Added"]}>
  ## Browser Extension Now Available on Arc & Edge

  🎯 **What is it?**

  The Dust browser extension is now compatible with Arc and Microsoft Edge browsers (and all Chromium-based browsers), in addition to Chrome. You can now use Dust's browser extension on the browser that fits your workflow best.

  💡 **Why is it useful?**

  Many teams use Arc for its innovative interface and productivity features, while Microsoft Edge is the standard browser in many enterprise environments. Until now, Dust extension users were limited to Chrome. This update ensures you can access Dust's capabilities directly in your browser of choice, wherever you work.

  ⚙ **How does it work?**

  The same Dust extension you know from Chrome now installs on Arc and Edge. All features work identically across browsers.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Arc users**: Integrate Dust into your split-view workflow and command bar for faster access to your agents while browsing research, documentation, or competitive analysis.

  **Edge users in enterprise environments**: Access Dust agents directly within your company's standard browser without needing to switch to Chrome for extension functionality.

  📈 **Benefits for you**

  Work with Dust where you're already working: no need to switch browsers or compromise on your preferred tools. This means faster access to your agents and a more integrated workflow.

  🚀 **How to access it?**

  If you use Arc or Edge: visit the Chrome Web Store and install the Dust extension as you would for Chrome. The extension works natively on all Chromium-based browsers.
</Update>

<Update label="March 20th, 2026" tags={["Added"]}>
  ## Dust Extension: Agents Now Understand Your Browser

  🎯 **What is it?**

  The Dust Chrome Extension now gives agents full browser awareness. Agents can automatically detect when they need content from your current page, work across multiple tabs simultaneously, and even interact with web pages directly through clicks and keystrokes. Plus, all your existing MCP tools (like Notion and Gmail) now work within the extension.

  💡 **Why is it useful?**

  Until now, working with browser content required manual steps: copying text, taking screenshots, or switching back to the web app. This update removes that friction entirely. Your agents can now understand and act on what you're looking at in real-time, making browser-based workflows dramatically faster and more intuitive.

  ⚙ **How does it work?**

  When an agent needs information from your browser, it automatically requests permission to access the relevant tab content or screenshots. Once granted, agents can read pages, navigate between tabs, and even perform actions like filling forms or clicking buttons, all while respecting your privacy with explicit permission prompts.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Research synthesis**: Ask an agent to "summarize the key points from these three open articles" and it will analyze all tabs at once, creating a unified summary without you switching windows.

  **Form automation**: Tell an agent to "fill out this application form with information from my resume" and it can read your resume from one tab while interacting with the form in another.

  **Competitive analysis**: With multiple competitor websites open, ask "compare pricing structures across these pages" and the agent will extract and analyze the information across all tabs.

  **Email drafting with context**: While reading a LinkedIn profile or company website, ask an agent to "draft an outreach email based on this page" using your Gmail MCP tool, all without leaving your browser.

  📈 **Benefits for you**

  * **Zero context switching**: Work directly where you are without copying content or moving to the web app
  * **Faster workflows**: Agents access what they need automatically with your permission
  * **New possibilities**: Browser interaction and multi-tab awareness open up entirely new use cases
  * **Unified experience**: All your existing MCP tools now work in the extension just like in the web app

  🚀 **How to access it?**

  Update your Chrome extension to the latest version. The new capabilities are available immediately: just start a conversation with an agent and it will automatically request browser access when needed.
</Update>

<Update label="March 20th, 2026" tags={["Added"]}>
  ## Chrome Extension: Major Update

  🎯 **What is it?**

  The Dust Chrome Extension has been completely redesigned to bring you the full web app experience, directly in your browser. You now get access to voice input, rich text formatting, message reactions, conversation management, and much more, all without leaving your current tab.

  💡 **Why is it useful?**

  Until now, the Chrome extension offered a simplified experience compared to the web app. Many recent features (like voice input, MiniApps display, or the ability to attach agents and data sources) were missing. This update closes that gap entirely, making the extension a complete, standalone way to work with Dust wherever you are on the web.

  ⚙ **How does it work?**

  Update your Chrome extension to the latest version. Once updated, you'll immediately see the new interface with all the features listed below.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Research & Writing**: Highlight text on any webpage, open the extension, and ask an agent to summarize, rephrase, or expand on it, using voice input if you prefer. Your draft is auto-saved, so you can close the extension and pick up where you left off.

  **Quick Access to Context**: Attach a specific data source or agent directly to your conversation in the extension, ask a question, and get an answer enriched with your company's knowledge, without opening the full web app.

  **Staying in the Flow**: Browse your conversation history, check your inbox for unread messages, and react to agent responses, all from the sidebar, while staying on your current page.

  📈 **Benefits for you**

  * **Time saved**: No need to switch between the web app and your browser: everything is accessible in one click
  * **Better efficiency**: Voice input, rich formatting, and draft auto-save make your interactions faster and smoother
  * **Full feature parity**: You no longer compromise on functionality when using the extension

  🚀 **How to access it?**

  Update your Dust Chrome Extension to the latest version. If auto-update is enabled, it should happen automatically. Otherwise, go to `chrome://extensions/`, find Dust, and click "Update." Once updated, open the extension to explore the new experience!

  **Key features included in this update:**

  * **Input bar**: voice input, human mentions, rich text formatting (bold, italic, lists), emoji support, and draft auto-save
  * **Sidebar**: conversation list, projects, and inbox with unread indicators
  * **Conversation layout**: updated message design, MiniApps display, message reactions, virtualized scrolling, and attached/generated files visible in the header
  * **Attach anything**: add agents, tools, skills, or data sources directly to your conversations
</Update>

<Update label="March 19th, 2026" tags={["Added"]}>
  ## Notion MCP now supports databases with multiple data sources

  ### 📌 Context

  Notion introduced support for databases with multiple data sources in late 2025. Until now, the Dust Notion MCP server was using an older Notion API version that couldn't access these databases, limiting functionality for users who had adopted this new Notion feature.

  ### 🔄 Impact on Dust

  We've updated the Notion MCP server to use the newest Notion API version and adapted it to support databases with multiple data sources. This update means your agents can now query and interact with these advanced Notion databases without restrictions.

  ### 👤 Impact for you

  **If you use the Notion MCP tool**: You can now access and work with Notion databases that use multiple data sources. No more errors or missing data when your agents query these databases.

  **If you use the Notion Connector**: This update does **not** apply to the Notion Connector, which still doesn't support databases with multiple data sources. There is currently no ETA for adding this capability to the Connector.

  ### ✅ Actions required

  **No action required on your part.** If you use the Notion MCP tool with databases containing multiple data sources, they will now work automatically. You can start using this capability immediately with your existing agents.
</Update>

<Update label="March 18th, 2026" tags={["Added"]}>
  ## Enhanced Speech Capabilities: Upgraded Audio Quality and 21 Languages Now Supported

  ## 📌 Context

  We've upgraded our ElevenLabs integration to provide you with significantly better speech-to-text (transcription) and text-to-speech (audio generation) capabilities. This upgrade brings more natural-sounding voices, improved transcription accuracy, and expanded language support.

  ## 🔄 Impact on Dust

  We've made several improvements to how agents handle audio:

  * **Transcription engine**: Upgraded to the latest model with better accuracy and additional metadata (like speaker identification and timestamps)
  * **Voice generation**: Switched to a more expressive audio engine that supports advanced audio formatting
  * **Language coverage**: Expanded from 9 to 21 supported languages
  * **Voice selection**: Improved the logic for matching voices to languages and contexts, so you get more appropriate and natural-sounding voices by default

  ## 👤 Impact for you

  **You'll notice immediate improvements:**

  * **Better transcription quality**: More accurate speech-to-text across all supported languages, with richer context
  * **More natural voices**: Audio generated by your agents will sound more expressive and human-like
  * **Broader language access**: You can now use speech features in 21 languages instead of 9
  * **Better default voices**: The system will automatically select more appropriate voices based on your language and use case, reducing instances of unexpected or mismatched voices

  These improvements apply automatically to all agents using speech capabilities.

  ## ✅ Actions required

  **No action required on your part.** All speech-enabled agents will automatically benefit from these improvements. The upgrade is transparent and backward-compatible with your existing agent configurations.

  If you'd like to explore the newly available languages or test the improved voice quality, use speech features in your agents as you normally would.
</Update>

<Update label="March 18th, 2026" tags={["Added"]}>
  ## Miro Integration Now Available in Dust

  🎯 **What is it?**

  The Miro MCP Server is now available across all Dust workspaces. This integration allows you to create diagrams, build tables, read and edit documents, and explore your entire Miro visual workspace directly from your Dust conversations, no need to switch between tools.

  💡 **Why is it useful?**

  Many of you have asked for a way to work with Miro boards without leaving Dust. Brainstorming ideas, documenting processes, collaborating on visual projects: this integration brings your Miro workspace into your agent conversations, reducing context switching and keeping your workflow fluid.

  ⚙ **How does it work?**

  Admins can set up the Miro integration in **Spaces > Tools** using OAuth authentication. Once configured, any team member can enable the Miro tool on their agents and start interacting with their Miro boards through natural conversation.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Strategic Planning**: Ask your agent to "Create a new mind map in Miro to brainstorm Q2 product features" and have it build the diagram while you discuss ideas.

  **Documentation**: Request "Read the onboarding process from our Miro board and summarize the key steps" to quickly extract information without manually navigating boards.

  **Collaborative Design**: Say "Add these three user feedback points to the UX review board" and let your agent update your shared workspace in real-time.

  📈 **Benefits for you**

  * **Uninterrupted workflow**: Access and modify Miro content without leaving your conversations
  * **Time savings**: Automate diagram creation and content updates through simple requests
  * **Better collaboration**: Keep visual work synchronized with your team's conversations

  🚀 **How to access it?**

  1. **Admins**: Go to **Spaces > Tools** in your Dust workspace
  2. Find the Miro MCP integration and connect via OAuth
  3. **All users**: Once set up, add the Miro tool to any agent you create
  4. Start creating, reading, and editing your Miro boards through conversation

  Learn more about Miro's MCP capabilities in their [official documentation](https://developers.miro.com/docs/miro-mcp?utm_campaign=glb-27q1-nsp-pn-c2_akc-miro-mcp-launch\&utm_source=miro\&utm_medium=redirect\&utm_content=website\&utm_term=landing-page\&src=-miro_glb|Doc).
</Update>

<Update label="March 17th, 2026" tags={["Added"]}>
  ## Fathom MCP Integration: Your Meeting Intelligence, Now in Dust

  🎯 **What is it?**

  Agents can now directly access your Fathom meeting recordings, summaries, and transcripts without leaving Dust. This new integration brings two tools to your agents: `list_meetings` to search and filter your call history with AI summaries and action items, and `get_transcript` to pull full conversation transcripts into your workflow.

  💡 **Why is it useful?**

  Meeting insights often get trapped in separate tools, requiring constant copy-pasting and context-switching between platforms. With Fathom MCP integrated directly into Dust, your agents can automatically search call history, extract action items, match meetings to CRM records, and reference full transcripts, all within the same conversation where you're working. No more toggling between tabs or manually transferring information.

  ⚙ **How does it work?**

  Once an admin sets up the OAuth connection (either shared across the workspace or per-user), you can add the Fathom MCP to any agent in any space. The agent then has native access to your Fathom data and can filter meetings by date, team member, recording owner, or domain, while optionally pulling AI summaries and CRM matches.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Pre-meeting prep**: Ask your agent "Pull up all meetings with Acme Corp from the last quarter and summarize key discussion points" to quickly get context before your next call.

  **Follow-up automation**: Have an agent scan this week's customer calls, extract action items, and create a prioritized task list with meeting context automatically attached.

  **Sales intelligence**: Query "Show me all discovery calls from February where pricing was discussed" and get transcripts with relevant CRM data matched automatically.

  **Team knowledge sharing**: Ask an agent to find and summarize calls about a specific feature or customer pain point, turning scattered meeting insights into actionable documentation.

  📈 **Benefits for you**

  * **Save time**: Eliminate manual note-taking and copy-pasting between tools
  * **Better context**: Keep meeting intelligence directly in your agent workflows
  * **Faster decisions**: Surface relevant call history and action items on demand
  * **Improved follow-through**: Never lose track of commitments made during meetings

  🚀 **How to access it?**

  Workspace admins can set up the Fathom MCP integration via OAuth in your workspace settings. Once configured, add the Fathom MCP to any agent's toolkit when building or editing an agent. Full setup instructions are available in our documentation: [/docs/user-documentation/agents/tools/fathom](/docs/user-documentation/agents/tools/fathom)
</Update>

<Update label="March 17th, 2026" tags={["Added"]}>
  ## One-Click Hex Integration via MCP Server

  🎯 **What is it?**

  Dust now supports Hex's remote MCP (Model Context Protocol) server with one-click setup. This means your agents can directly interact with Hex functionality (searching projects, creating conversation threads, and iterating on data work), all without leaving Dust.

  💡 **Why is it useful?**

  If your team uses Hex for data analytics and notebooks, you previously had to switch between platforms to find projects, ask questions, or collaborate on analysis. This integration eliminates that context-switching by bringing Hex's capabilities directly into your Dust workflows. Your agents can now autonomously search for the right Hex project, start analytical threads, and help you iterate faster.

  ⚙ **How does it work?**

  Once configured, Dust agents gain access to Hex tools like `search_projects`, `create_thread`, `get_thread`, and `continue_thread`. Agents can use these tools to find relevant Hex projects based on your query, initiate analytical conversations in Hex Threads, and continue iterating on analysis, all through natural language interaction.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Data Discovery**: Ask an agent "Find our customer churn analysis from last quarter" and it searches your Hex projects directly, returning the relevant notebook.

  **Analytical Assistance**: Request "Create a thread in Hex to explore why conversion dropped in EMEA" and the agent initiates a Hex Thread, bringing context from your Dust workspace.

  **Iterative Analysis**: Continue conversations with "What if we segment by enterprise vs. SMB?" and the agent updates the Hex Thread with your new question, maintaining analytical continuity.

  📈 **Benefits for you**

  * **Faster data discovery**: No more manual searching through Hex projects
  * **Smoother workflows**: Keep your analytical work connected to your broader team context in Dust
  * **Agent-powered iteration**: Let agents handle the mechanics of starting and continuing analytical threads while you focus on insights

  🚀 **How to access it?**

  This feature is available for **Hex Team and Enterprise plan customers**. To enable it, configure the Hex MCP server in your Dust workspace settings. Full setup instructions are available in the [Hex MCP documentation](https://learn.hex.tech/docs/administration/mcp-server).
</Update>

<Update label="March 17th, 2026" tags={["Added"]}>
  ## Semrush MCP Integration: SEO Insights Directly in Your Agents

  🎯 **What is it?**

  The Semrush MCP Server is now available across all Dust workspaces. This integration brings professional SEO tools (including keyword research, competitive analysis, and search insights) directly into your Dust conversations. You can now access Semrush's capabilities without switching contexts or leaving your workflow.

  💡 **Why is it useful?**

  Many teams need SEO data to inform their content strategy, competitive positioning, and marketing decisions. Previously, this meant jumping between Semrush and Dust. Now, your agents can pull real-time SEO intelligence on demand, making it faster and easier to create data-driven content, analyze competitors, or research keyword opportunities, all within your existing workflows.

  ⚙ **How does it work?**

  Workspace admins can connect Semrush via OAuth in **Spaces > Tools**. Once configured, any team member can enable Semrush capabilities in their agents, allowing those agents to query SEO data, analyze keywords, and retrieve competitor insights as part of their responses.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Content Strategy**: Ask an agent to analyze keyword difficulty and search volume for your target topics, then generate content briefs optimized for those keywords.

  **Competitive Intelligence**: Request competitor domain analysis to understand their top-performing pages, backlink profiles, and keyword rankings, then use those insights to inform your own strategy.

  **SEO Reporting**: Build agents that pull regular SEO metrics and package them into reports or summaries, keeping stakeholders informed without manual data gathering.

  📈 **Benefits for you**

  * **Faster insights**: Get SEO data instantly within your conversations
  * **Better decisions**: Ground content and marketing strategies in real search data
  * **Uninterrupted workflow**: No more context-switching between tools
  * **Team accessibility**: Anyone can use Semrush capabilities through agents once it's set up

  🚀 **How to access it?**

  **For admins**: Navigate to **Spaces > Tools** in your Dust workspace and connect Semrush using OAuth authentication. See the [Semrush documentation](https://www.semrush.com/kb/1618-mcp) for setup details.

  **For users**: Once your admin has enabled the integration, you can activate Semrush capabilities in any of your agents and start querying SEO data right away.
</Update>

<Update label="March 16th, 2026" tags={["Added"]}>
  ## Introducing Sidekick: Your AI Assistant for Building Better Agents

  🎯 **What is it?**

  Sidekick is a new AI assistant integrated directly into the Agent Builder. Instead of starting from a blank canvas, you can now describe what you want your agent to do in natural language, and Sidekick will draft the instructions, recommend the right tools and skills, and suggest improvements. All changes appear as reviewable inline diffs: you accept what works and reject what doesn't. You remain in complete control.

  💡 **Why is it useful?**

  Building effective agents often requires expertise in prompt engineering and deep knowledge of available tools. Sidekick removes this barrier by translating your intent into working agent configurations. It also helps you iterate faster by analyzing feedback, usage patterns, and suggesting concrete improvements to existing agents.

  ⚙ **How does it work?**

  Sidekick understands context. When you describe what you need, it may ask clarifying questions, then generates a complete agent configuration. For existing agents, it reads your current setup, reviews performance data, and proposes specific improvements as inline suggestions you can approve or dismiss with one click.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Creating a new agent**: Describe "I need an agent that monitors our #support channel and summarizes urgent tickets every morning" → Sidekick drafts the full configuration with appropriate data sources and scheduling.

  **Improving existing agents**: Open an underperforming sales research agent → Sidekick analyzes usage feedback and suggests "Add web search capability" and "Refine instructions to focus on competitor pricing" as reviewable changes.

  **Customizing templates**: Select the "Meeting Summarizer" template → Instead of generic instructions, Sidekick asks about your meeting format and adapts the template to your team's specific needs.

  **Converting conversations**: Had a productive back-and-forth with an agent? Use "Convert to agent" → Sidekick captures that conversation's tools, knowledge sources, and reasoning pattern into a reusable agent.

  📈 **Benefits for you**

  * **Faster agent creation**: Go from idea to working agent in minutes, not hours
  * **Better quality**: Benefit from best practices built into Sidekick's recommendations
  * **Continuous improvement**: Get data-driven suggestions to optimize existing agents
  * **Lower barrier to entry**: Build sophisticated agents without needing prompt engineering expertise

  🚀 **How to access it?**

  Sidekick is now available to all users directly in the Agent Builder. Open any agent or click "New Agent" to get started.

  📚 **Learn more**: [Agent Builder Sidekick documentation](/docs/user-documentation/agents/agent-builder-sidekick)

  🎥 **Live webinar**: Join us for a hands-on demo and Q\&A. [Register here](https://watch.getcontrast.io/register/dust-sidekick-hot-of-the-grill)
</Update>

<Update label="March 12th, 2026" tags={["Added"]}>
  ## Enhanced Attachments Management in Conversations

  🎯 **What is it?**

  The conversation Attachments popover has been completely redesigned to give you better visibility and control over all files in your conversations. You can now see both uploaded files and agent-generated content in one organized view, filter by content type, and get visual notifications when new content is added.

  💡 **Why is it useful?**

  During long conversations with agents, files and generated content can quickly pile up, making it hard to find that specific document or output you need. This improvement solves the common "where did that file go?" problem by centralizing all conversation content in an easy-to-browse interface with smart filtering options.

  ⚙ **How does it work?**

  When you click the Attachments button in any conversation, you'll now see a full table/preview of all content. New category filters let you narrow down by type (uploads vs. generated files), and the Attachments button will pulse whenever new content appears in the conversation, so you never miss important outputs.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Research & Analysis**: When working with an agent that generates multiple reports and charts, use the filters to quickly locate all generated visualizations versus your original source documents.

  **Document Management**: In conversations where you've uploaded several files and received edited versions back, easily distinguish between your uploads and agent outputs to grab the right version.

  📈 **Benefits for you**

  * **Save time**: No more scrolling through long conversations to find a specific file
  * **Better organization**: Clear separation between uploaded and generated content
  * **Never miss content**: Visual pulse notification alerts you to new files immediately
  * **Easier reuse**: Quick access to generated content for download or sharing

  🚀 **How to access it?**

  This feature is now live for all users, no action needed. Open any conversation and click the Attachments button to experience the improved interface.
</Update>

<Update label="March 12th, 2026" tags={["Added"]}>
  ## BigQuery connector: multi-project support

  🎯 **What is it?**

  The BigQuery connector now supports multiple GCP projects within a single connection. Instead of being limited to one project (the service account's default `project_id`), Dust now automatically discovers and lists all GCP projects accessible by your service account, letting you browse datasets and tables across all of them.

  💡 **Why is it useful?**

  Many organizations structure their BigQuery data across multiple GCP projects for governance, billing separation, or organizational reasons. Previously, the connector only accessed a single hardcoded project, forcing you to create multiple connections or miss out on data stored in other projects. This update removes that limitation entirely.

  ⚙ **How does it work?**

  When you connect BigQuery, Dust now queries all projects your service account can access and presents them in a unified view. You can browse and select datasets and tables from any accessible project without additional configuration.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Cross-project analytics**: Build agents that combine data from your production project, analytics project, and data warehouse project, all from a single BigQuery connection.

  **Multi-team access**: If your service account has access to projects owned by different teams (marketing, sales, engineering), your agents can now query data from all of them.

  📈 **Benefits for you**

  * Access all your BigQuery data through one connection instead of managing multiple connectors
  * Build agents that work with data across your entire GCP organization
  * Simpler setup and maintenance for multi-project BigQuery architectures

  🚀 **How to access it?**

  This improvement is available by default for all BigQuery connector users. If you're already using the BigQuery connector, you'll automatically see all accessible projects the next time you browse your data sources. No configuration changes needed.
</Update>

<Update label="March 11th, 2026" tags={["Improved"]}>
  ## Slack Tool Now Uses Official Dust Marketplace App

  Slack Tool Now Uses Official Dust Marketplace App

  **📌 Context**

  Previously, the Slack tool in Dust was using a non-approved Slack app. This caused a security warning to appear when connecting, and in some cases, it completely blocked the connection for companies with strict security policies that only allow approved Slack apps.

  We've now upgraded the Slack tool to use our official Dust app from the Slack Marketplace, the same trusted app that powers the Slack bot you may already be using.

  **🔄 Impact on Dust**

  Dust now provides a unified, approved Slack integration across all features. The Slack tool connection flow has been updated to use our official Marketplace app, ensuring a smooth and secure experience.

  **👤 Impact for you**

  **If you're already using the Slack tool:** No impact. Your existing connection will continue to work without any interruption.

  **If you're setting up a new Slack tool connection:** You'll now connect through our official Dust Marketplace app. This means:

  * No more security warnings during connection
  * Works even if your company policy restricts non-approved apps
  * Cleaner, more trustworthy connection experience

  **✅ Actions required**

  No action required on your part.

  If you previously couldn't connect the Slack tool due to company policy restrictions, you can now try again. The official app should be approved by your security settings.
</Update>

<Update label="March 5th, 2026" tags={["Added"]}>
  ## GPT 5.4 Now Available in Dust

  🎯 **What is it?**

  GPT 5.4, OpenAI's latest language model, is now available in Dust. You can use it when building custom agents in the Agent Builder, and it's already integrated into two of our global agents: `gpt5` and `gpt5-thinking`.

  💡 **Why is it useful?**

  GPT 5.4 represents OpenAI's latest advancement in language model capabilities, offering improved reasoning, better context understanding, and more accurate responses. Having access to the latest model ensures your agents benefit from the most up-to-date AI capabilities available.

  ⚙️ **How does it work?**

  When creating or editing an agent in the Builder, you can now select GPT 5.4 as the model. The two global agents (`gpt5` and `gpt5-thinking`) have been updated to use this model automatically.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Custom agents**: Build specialized agents using GPT 5.4 for tasks requiring advanced reasoning, such as complex data analysis, strategic planning support, or technical documentation review.

  **Quick access via global agents**: Use `@gpt5` for general-purpose tasks with the latest model, or `@gpt5-thinking` when you need extended reasoning capabilities for particularly complex problems.

  📈 **Benefits for you**

  * **Latest capabilities**: Access OpenAI's most advanced model directly in your workflows
  * **Better performance**: Benefit from improvements in reasoning, accuracy, and context handling
  * **Flexibility**: Choose GPT 5.4 for new agents or continue using existing models based on your needs

  🚀 **How to access it?**

  * **For custom agents**: Open the Agent Builder, create or edit an agent, and select GPT 5.4 from the model dropdown
  * **For quick tasks**: Mention `@gpt5` or `@gpt5-thinking` in any conversation to use the global agents powered by GPT 5.4
</Update>

<Update label="February 25th, 2026" tags={["Added"]}>
  ## Statuspage MCP Server - Now Available

  🎯 **What is it?**

  The Statuspage MCP Server is now generally available across all Dust workspaces. This integration allows your agents to interact directly with Statuspage to manage incident communications. Agents can list pages, components, and incidents, retrieve incident details, create new incidents (including affected components and impact levels), and update existing ones, all through natural conversation.

  💡 **Why is it useful?**

  When incidents occur, speed and clarity in communication are critical. Instead of manually switching between Dust and Statuspage to update your status page, you can now delegate this task to your agents. This integration addresses the need for faster incident response workflows and reduces the friction in keeping stakeholders informed during critical moments.

  ⚙️**How does it work?**

  Workspace admins can configure the Statuspage integration by adding an API Key in Spaces > Tools. Once set up, anyone in the workspace can enable the Statuspage tools on their agents, allowing them to execute Statuspage operations through conversation.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Incident Response Agent**: Create an agent that monitors your infrastructure alerts and automatically creates and updates Statuspage incidents when issues are detected, ensuring your customers are always informed in real-time.

  **Status Communication Assistant**: Build an agent that helps your support team quickly update incident status, affected components, and impact levels by describing the situation in natural language, eliminating the need to navigate the Statuspage interface during high-pressure moments.

  📈 **Benefits for you**

  * **Faster incident communication**: Reduce the time between detecting an issue and updating your status page
  * **Simpler workflows**: Keep all incident management within your Dust workspace
  * **Better coordination**: Enable your entire team to update status pages through agents, not just those familiar with Statuspage
  * **Reduced context switching**: Stay focused on resolving issues while agents handle status updates

  🚀 **How to access it?**

  1. If you're a workspace admin: Go to Spaces > Tools and add your Statuspage API Key
  2. Once configured, any team member can enable the Statuspage tools on their agents
  3. Your agents can now manage incidents, components, and status pages through conversation

  The Statuspage MCP Server has been thoroughly tested over the past few weeks and is now stable and ready for production use.
</Update>

<Update label="February 25th, 2026" tags={["Added"]}>
  ## Salesloft MCP Server Now Available

  🎯 **What is it?**

  The Salesloft MCP Server is now generally available in all Dust workspaces. Your agents can now directly retrieve your Salesloft actions, with the ability to filter for due or overdue tasks. This gives sales reps instant visibility into what requires their immediate attention, directly within Dust.

  💡 **Why is it useful?**

  Sales teams juggle multiple priorities and tools throughout their day. By connecting Salesloft directly to your Dust agents, you eliminate the need to constantly switch between platforms to check what's on your plate. Your agents can proactively surface what needs your attention, helping you stay on top of your sales activities without the manual overhead.

  ⚙ **How does it work?**

  Once configured by a workspace admin, any agent in your workspace can access the Salesloft integration. Agents can retrieve your current Salesloft actions and optionally filter to show only what's due or overdue, ensuring you focus on the most time-sensitive tasks first.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Daily Sales Assistant**: Create an agent that starts your day by pulling all overdue and due Salesloft actions, presenting them in a prioritized morning briefing alongside your calendar and recent emails.

  **Pipeline Management Agent**: Build an agent that monitors your Salesloft activities across all active deals, alerting you when follow-ups are due and suggesting next steps based on your sales playbook.

  📈 **Benefits for you**

  * **Time savings**: No more switching between tools to check your task list
  * **Better prioritization**: Instant visibility into what's overdue or due today
  * **Proactive workflows**: Let agents surface the right actions at the right time
  * **No tool-switching**: Your sales workflow stays within Dust

  🚀 **How to access it?**

  Workspace admins can set up the Salesloft integration by navigating to **Spaces > Tools** and adding the connection with a Salesloft API Key. Once configured, anyone in your workspace can add the Salesloft tools to their agents and start using them immediately.
</Update>

<Update label="February 25th, 2026" tags={["Added"]}>
  ## Front MCP Server: Now Generally Available

  🎯 **What is it?**

  The Front MCP Server is now available in all Dust workspaces. This integration allows your agents to interact directly with Front, your customer communication platform. Agents can search and read conversations, look up contact histories, manage inboxes and tags, create outbound messages, draft replies, send messages, add internal comments, and organize conversations.

  💡 **Why is it useful?**

  Managing customer communications often requires jumping between tools, searching through message histories, and manually drafting responses. The Front MCP Server brings Front's full capabilities directly into Dust, allowing your agents to access customer context, automate routine communication tasks, and maintain consistent follow-ups, all without leaving your workflow.

  ⚙ **How does it work?**

  Once your workspace admin sets up the Front MCP Server with an API key in the Spaces > Tools section, the tools become available to anyone in your workspace. You can then add these tools to your agents, giving them the ability to interact with Front on your behalf.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Customer Success Follow-up Agent**: Create an agent that monitors tagged conversations in Front, retrieves customer history, and automatically drafts personalized follow-up messages based on previous interactions and current context.

  **Support Triage Agent**: Build an agent that searches recent Front conversations by topic or contact, identifies patterns or urgent issues, adds internal comments with context for your team, and tags conversations appropriately for routing.

  **Outbound Campaign Agent**: Design an agent that creates outbound conversations in Front, personalizes messages based on contact information and history, and sends them at optimal times while maintaining a consistent brand voice.

  📈 **Benefits for you**

  * **Time saving**: Automate repetitive communication tasks and reduce context switching between tools
  * **Better efficiency**: Access full customer history and conversation context instantly within your agent workflows
  * **New possibilities**: Build intelligent communication workflows that combine Front's capabilities with other tools and data sources in Dust

  🚀 **How to access it?**

  1. **Admins**: Go to Spaces > Tools in your Dust workspace and set up the Front MCP Server using your Front API key
  2. **All users**: Once configured, add the Front tools to any agent you create or modify
  3. **Start automating**: Your agents can now interact with Front conversations, contacts, and messages directly

  The integration has been tested and stabilized over the past few weeks and is ready for production use across all workspaces.
</Update>

<Update label="February 25th, 2026" tags={["Added"]}>
  ## Ashby MCP Server Now Generally Available

  🎯 **What is it?**

  The Ashby MCP Server is now available to all Dust workspaces. This integration allows your agents to interact directly with your Ashby recruiting data: search for candidates, access interview feedback, manage notes on candidate profiles, and extract report data as CSV files using just a report URL.

  💡 **Why is it useful?**

  Recruiting teams often need to quickly access candidate information, review feedback across multiple interviews, or pull reports for analysis. Instead of switching between Dust and Ashby, your agents can now retrieve this information directly within your workflow, saving time and keeping your recruiting operations in one place.

  ⚙ **How does it work?**

  Workspace admins can configure the Ashby connection in Spaces > Tools using an Ashby API Key. Once set up, anyone in your workspace can enable these capabilities on their agents to start interacting with your Ashby data.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Candidate Research Agent**: Build an agent that searches for candidates by name or email and compiles all their interview feedback into a summary before your hiring committee meeting.

  **Recruiting Analytics Assistant**: Create an agent that pulls data from multiple Ashby reports and generates comparative analyses or weekly recruiting metrics dashboards.

  **Candidate Communication Helper**: Set up an agent that reads and adds notes to candidate profiles, helping recruiters maintain context and document important details throughout the hiring process.

  📈 **Benefits for you**

  * **Faster access to recruiting data**: No need to leave Dust to check candidate information
  * **Better context for decisions**: Agents can synthesize feedback and data from multiple sources
  * **Less manual work**: Automate repetitive tasks like pulling reports or updating candidate notes
  * **Improved collaboration**: Share agent-generated insights with your team directly in Dust

  🚀 **How to access it?**

  1. Navigate to **Spaces > Tools** in your Dust workspace
  2. Configure the Ashby MCP Server with your API Key (admins only)
  3. Enable the Ashby tools on any agent you want to use them with
  4. Start querying your recruiting data!

  This feature has been tested extensively over recent weeks, and we've refined the configuration process to make setup as smooth as possible.
</Update>

<Update label="February 25th, 2026" tags={["Added"]}>
  ## Slab MCP Server: Now Available

  🎯 **What is it?**

  The Slab MCP Server is now generally available across all Dust workspaces. Your agents can now directly interact with your Slab knowledge base: search for posts using keywords and filters, read full post content, browse topics, and access post metadata, all without leaving Dust.

  💡 **Why is it useful?**

  If your team uses Slab to centralize documentation, policies, or processes, this integration eliminates context switching. Instead of manually searching Slab and copying information into Dust, your agents can now retrieve and reference Slab content automatically, ensuring they always work with up-to-date information from your knowledge base.

  ⚙ **How does it work?**

  Once an admin connects Slab using an API key in the Tools section of a Space, any agent in that Space can search, filter, and read Slab posts directly. The server supports keyword search, filtering by topic or publication status, and full post retrieval.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Onboarding Agent**: Build an agent that answers new hire questions by searching your Slab onboarding documentation, delivering accurate answers with direct references to published posts.

  **Policy Assistant**: Create an agent that retrieves and explains company policies stored in Slab, filtering by specific topics (HR, Legal, IT) and ensuring only published, current versions are referenced.

  **Documentation Helper**: Deploy an agent that helps teams find technical documentation, API guides, or process workflows from Slab, reducing time spent searching and increasing consistency in how information is shared.

  📈 **Benefits for you**

  * **Time savings**: Agents retrieve Slab content instantly, eliminating manual lookups
  * **Better accuracy**: Agents reference the latest published information directly from your source of truth
  * **No tool switching**: Keep your team in Dust while accessing your full Slab knowledge base

  🚀 **How to access it?**

  Admins can set up the Slab MCP Server in **Spaces > Tools** using a Slab API Key. Once configured in a Space, any member can enable it on their agents and start searching Slab content immediately.
</Update>

<Update label="February 23rd, 2026" tags={["Added"]}>
  ## Better Support for Slideshow MiniApps

  🎯 **What is it?**

  Slideshow MiniApps now come with built-in navigation controls and can be exported as multi-page PDFs. Each slide is rendered as a full page with proper page breaks, making it easy to share and print your agent-generated presentations.

  💡 **Why is it useful?**

  When agents create slideshow presentations for you, you often need to share them with colleagues, present them in meetings, or print them for documentation. Until now, exporting these slideshows outside of Dust wasn't straightforward. This update makes it simple to take your agent-generated slide decks anywhere.

  ⚙️ **How does it work?**

  When you create a new slideshow MiniApp, it automatically includes navigation controls to move between slides. You can then export the entire presentation as a PDF, where each slide becomes its own properly formatted page.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Executive briefings**: Ask an agent to create a monthly performance dashboard as a slideshow, then export it as a PDF to email to leadership or print for board meetings.

  **Client presentations**: Generate a project status update slideshow from your latest data, export it as a PDF, and share it directly with clients who don't have access to Dust.

  📈 **Benefits for you**

  * **Better portability**: Share agent-generated presentations outside Dust in one step
  * **Print-ready**: Get properly formatted PDFs with each slide on its own page
  * **Professional output**: Navigation controls make it easy to review slides before exporting

  🚀 **How to access it?**

  This feature is available now for all new slideshow MiniApps you create. Ask an agent to generate a slideshow, and you'll automatically get the navigation controls and PDF export capability. Note that existing slideshows won't have this functionality. You'll need to regenerate them to use the new features.

  [Example slideshow MiniApp](https://app.dust.tt/share/frame/0b85cbbe-6f6d-42c2-b90a-d97837a128f3)
</Update>

<Update label="February 20th, 2026" tags={["Added"]}>
  ## Attio CRM Integration Now Available

  🎯 **What is it?**

  Dust now supports Attio's official MCP server, allowing you to connect your Attio CRM account directly to Dust. Once connected via OAuth, your Dust agents can access and interact with your Attio workspace directly.

  💡 **Why is it useful?**

  Managing your CRM often requires switching between multiple tools and manually updating information. With this integration, your Dust agents can handle CRM tasks directly, saving you time and keeping your customer data up-to-date without leaving your workflow.

  ⚙ **How does it work?**

  You connect your Attio account to Dust through a secure OAuth authentication. Once connected, your agents can read and write data across your Attio workspace, including contacts, companies, deals, tasks, notes, emails, and call recordings.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Sales workflow automation**: Ask an agent to "Find all companies in my pipeline that haven't been contacted in 30 days and draft personalized follow-up emails based on their latest notes."

  **Meeting preparation**: Before a client call, ask "Pull up all recent interactions, open deals, and tasks related to \[Company Name] and create a meeting brief."

  **Post-call documentation**: After a meeting, tell an agent to "Update the deal status for \[Company Name], log today's call recording, and create follow-up tasks based on our conversation."

  **Contact enrichment**: Request "Search for contacts without assigned owners and suggest assignments based on territory or relationship history."

  📈 **Benefits for you**

  * **Time saving**: Automate repetitive CRM updates and searches
  * **Better data quality**: Reduce manual entry errors with agent-assisted workflows
  * **More context**: Agents can cross-reference CRM data with other connected sources
  * **Unified workspace**: Manage CRM tasks without switching between platforms

  🚀 **How to access it?**

  This feature is available to all Dust users with an Attio account. To get started, connect your Attio workspace through Dust's connections settings using the OAuth authentication flow.
</Update>

<Update label="February 20th, 2026" tags={["Added"]}>
  ## Dust is now a Single Page Application

  ## 📌 Context

  We've migrated Dust's technical architecture from a server-side rendered Next.js application to a standalone React Single Page Application (SPA). Everyone now accesses Dust through a unified URL: **app.dust.tt**

  This change improves the underlying infrastructure that powers your experience with Dust, making the platform faster and more efficient.

  ## 🔄 Impact on Dust

  Behind the scenes, Dust now handles navigation and page rendering directly in your browser rather than on our servers. This architectural shift brings several technical improvements:

  * **Faster interactions**: The application responds more quickly to your actions
  * **Smoother navigation**: Moving between pages and features feels more fluid
  * **Better global performance**: Multi-region traffic is handled more transparently
  * **Reduced server load**: Lower memory footprint means better scalability

  ## 👤 Impact for you

  **No disruption to your workflow.** You'll continue using Dust exactly as before, but you should notice:

  * Snappier page transitions when navigating between assistants, conversations, and settings
  * More responsive interface interactions
  * A generally smoother experience throughout the platform

  The transition requires no changes on your side: most users won't notice anything beyond improved performance.

  ## ✅ Actions required

  **No action required on your part.** The change has been automatically deployed for all workspaces.

  If you experience any unexpected behavior, the SPA mode can be disabled for your specific workspace. Reach out to our support team, and we'll assist you.
</Update>

<Update label="February 18th, 2026" tags={["Added"]}>
  ## Intercom Official MCP Server Now Available in Dust

  🎯 **What is it?**

  Intercom's official MCP (Model Context Protocol) server is now integrated into Dust with native OAuth authentication. You can configure it directly in your workspace, giving your agents secure access to your Intercom data, support tickets, help center articles, and customer interaction history. Only available for US intercom workspace.

  💡 **Why is it useful?**

  Many of you asked for deeper Intercom integration to help your support and customer success teams work more efficiently. With this connection, your agents can now pull context from customer conversations, access knowledge base content, and even help manage support workflows, all without leaving Dust.

  ⚙️ **How does it work?**

  Once configured with OAuth authentication (a secure, one-click setup), your agents can query and interact with Intercom data as part of their workflow. The connection is authenticated through your Intercom account, ensuring secure access to your support data.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Customer Success Agent**: Build an agent that monitors open tickets, summarizes customer issues, and drafts personalized responses based on conversation history and help center articles.

  **Knowledge Base Assistant**: Create an agent that answers internal team questions by searching your Intercom help center, pulling the most relevant articles, and providing context-aware answers.

  **Support Triage Agent**: Design an agent that reviews incoming tickets, categorizes them by urgency and topic, and suggests appropriate responses or escalation paths based on similar past interactions.

  📈 **Benefits for you**

  * **Faster support response times** by giving agents instant access to customer context
  * **Better consistency** across support interactions with centralized knowledge access
  * **Reduced manual work** through automated ticket summaries and response suggestions
  * **Simpler setup** with secure, native OAuth authentication (no complex API key management)

  🚀 **How to access it?**

  1. Go to your Dust workspace settings
  2. Navigate to the "Connections" or "Integrations" section
  3. Select "Intercom" from the available MCP servers
  4. Click "Connect" and authenticate with OAuth
  5. Start building or updating agents to use your Intercom data

  This feature is available to all Dust users starting today. But only for US intercom workspace.
</Update>

<Update label="February 18th, 2026" tags={["Added"]}>
  ## Claude Sonnet 4.6 Now Available in Agent Builder

  🎯 **What is it?**

  Claude Sonnet 4.6, Anthropic's most capable mid-tier model, is now available in Dust's Agent Builder. You can select it when creating or editing a custom agent.

  💡 **Why is it useful?**

  Sonnet 4.6 brings better reasoning and stronger performance than previous Sonnet versions, while remaining a cost-effective choice for everyday agent workflows. Having it available in Dust means you can upgrade your most important custom agents to the latest model without switching tools.

  ⚙️ **How does it work?**

  Sonnet 4.6 appears in the model picker within the Agent Builder. You can select it when creating a new agent or switch an existing agent to it at any time.

  ✨ **Concrete Use Cases**

  * **Upgrade an existing agent**: Open a custom agent in the Agent Builder, select Claude Sonnet 4.6 in the model dropdown, and save. The agent will use the new model for all future conversations.
  * **Build a new agent with Sonnet 4.6**: Start from scratch and pick Claude Sonnet 4.6 as your model of choice from the beginning.

  📈 **Benefits for you**

  A stronger reasoning model with improved instruction-following, now accessible in Dust for anyone building custom agents.

  🚀 **How to access it?**

  Open the **Agent Builder**, create or edit an agent, and select **Claude Sonnet 4.6** in the model section. It's available now for all paid workspaces.
</Update>

<Update label="February 11th, 2026" tags={["Added"]}>
  ## 🆕 Dust Agents Can Now Create and Edit Google Drive Documents

  🎯 **What is it?**

  Dust agents can now create and modify Google Drive files directly. This means your agents can generate new Google Docs, Sheets, and Slides from scratch, edit existing documents, add comments, format content, and even insert tables, all without you having to do it manually.

  💡 **Why is it useful?**

  Until now, agents could only read your Google Drive files. This limitation meant that after analyzing data or processing information, you still had to manually create documents or update spreadsheets with the results. This new capability removes that friction entirely, allowing your agents to complete the full workflow: from analysis to documentation to sharing.

  ⚙ **How does it work?**

  When you connect your Google Drive to Dust using the updated OAuth permissions (`drive.file` scope), your agents gain the ability to perform write operations on Google Docs, Sheets, and Slides. They can create new files, clone templates, edit content, format text, and manage comments.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Weekly Report Generation**: Your agent analyzes your team's project management data, identifies key metrics and blockers, then automatically creates a formatted Google Doc with action items, ready to share with stakeholders.

  **Meeting Notes & Follow-ups**: After a meeting transcription is processed, your agent creates a Google Doc with structured notes, extracts action items into a tracking spreadsheet, and adds comments tagging relevant team members.

  **Data Pipeline to Spreadsheet**: Your agent pulls sales data from multiple sources, performs analysis, then updates a Google Sheet with the latest figures for your monthly review.

  **Project Status Updates**: Your agent monitors project channels, synthesizes updates, and automatically updates your project status document in Google Docs with formatted sections and tables.

  📈 **Benefits for you**

  * **Save hours of manual work**: Eliminate the copy-paste cycle between analysis and documentation
  * **Maintain consistency**: Agents follow your templates and formatting standards every time
  * **Enable end-to-end automation**: Complete workflows from data gathering to polished deliverables
  * **Improve collaboration**: Agents can comment and tag team members directly in documents

  🚀 **How to access it?**

  If you already have Google Drive connected to Dust, you'll be prompted to re-authenticate with the updated permissions the next time an agent attempts a write operation. If you're new to this integration, connect Google Drive from your Dust connections settings, and all write capabilities will be available immediately to your agents.
</Update>

<Update label="February 5th, 2026" tags={["Added"]}>
  ## 🔗✨ Message Reactions & Message Links in Conversations

  🎯 **What is it?**

  You can now react to messages with emojis and share direct links to specific messages within Dust conversations. This makes it easier to reference important points, navigate through discussions, and express quick feedback without writing a full response.

  💡 **Why is it useful?**

  As conversations grow longer and more collaborative, it becomes harder to track key decisions, highlight important information, or quickly acknowledge messages. Emoji reactions provide a lightweight way to respond, while message links allow you to jump directly to or reference specific points in a conversation. No more endless scrolling to find "that one message."

  ⚙ **How does it work?**

  Hover over any message in a conversation to reveal the reaction and link options. Click to add an emoji reaction, or copy the message link to share it with your team or bookmark it for later reference.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Team alignment**: React with a ✅ to show agreement on a decision without cluttering the conversation with "+1" messages, helping your team quickly see consensus.

  **Knowledge sharing**: Copy a direct link to a valuable assistant response (like a complex analysis or summary) and share it in your team channel or documentation, making it easy for colleagues to find exactly what they need.

  **Follow-up tracking**: Use 👀 reactions to show you've seen an important update, or react with ❓ to flag messages that need clarification, creating visual cues for what requires attention.

  📈 **Benefits for you**

  * **Save time**: No need to write short acknowledgment messages, a quick emoji does the job
  * **Better navigation**: Jump directly to key messages instead of searching through long conversations
  * **Clearer communication**: Visual reactions help the whole team understand what's important, what's been addressed, and what needs attention
  * **Better collaboration**: Make conversations more dynamic and easier to follow for everyone involved

  🚀 **How to access it?**

  This feature is now available to all Dust users in all conversations, no setup required! Just hover over any message to start using reactions and message links right away.
</Update>

<Update label="February 5th, 2026" tags={["Added"]}>
  ## Granola Official MCP Server Now Available in Dust

  🎯 **What is it?**

  Granola's official MCP (Model Context Protocol) server is now directly configurable within Dust. This native integration allows your Dust assistants to access and interact with your Granola meeting data directly.

  💡 **Why is it useful?**

  If you use Granola to record and manage your meetings, you can now use that meeting information directly within your Dust workflows. No more switching between tools or manually copying meeting notes: your assistants can automatically retrieve and work with your meeting data.

  ⚙️ **How does it work?**

  Once configured, the Granola MCP server connects your Granola account to Dust, enabling your assistants to query meetings, retrieve specific meeting details, and list your meeting history.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Meeting Follow-up Assistant**: Create an assistant that automatically pulls action items from recent Granola meetings and drafts follow-up emails to participants.

  **Weekly Meeting Digest**: Build a workflow that compiles summaries of all your team meetings from the past week, highlighting key decisions and next steps.

  **Meeting Prep Assistant**: Set up an assistant that retrieves notes from previous meetings with a specific client or on a particular topic to help you prepare for upcoming discussions.

  📈 **Benefits for you**

  * **Save time**: No more manual copying of meeting notes into other tools
  * **Better context**: Your assistants have full access to meeting history and insights
  * **Connected workflows**: Combine meeting data with other information sources in Dust to automate more of your work

  🚀 **How to access it?**

  If you're a Granola user, head to your Dust workspace settings, navigate to the MCP servers configuration section, and add the Granola official MCP server. Once connected, your assistants will be able to access your Granola meetings data.
</Update>

<Update label="February 5th, 2026" tags={["Added"]}>
  ## CSV Export for Programmatic Cost Chart

  🎯 **What is it?**

  You can now export your programmatic cost chart as a CSV file. This makes it easy to download your usage data and analyze it further outside of Dust.

  💡 **Why is it useful?**

  The in-app chart gives you a visual overview of your spending, but deeper analysis (filtering by team, building custom reports, or combining with other data) is easier when you have the raw data. CSV export gives you that without any additional setup.

  ⚙️ **How does it work?**

  From the programmatic cost chart view, you'll find an export button that downloads your current chart data as a CSV file. The data reflects whatever filters and time range you have applied.

  ✨ **Concrete Use Cases**

  * **Finance reporting**: Export monthly usage data and import it into your billing or finance tools for reconciliation.
  * **Team-level analysis**: Filter by workspace or use case, export, and share with relevant stakeholders.

  📈 **Benefits for you**

  A simple way to get your usage data out of Dust and into the tools where you do your financial analysis.

  🚀 **How to access it?**

  Open the **Programmatic Cost Chart** in your workspace and click the export button to download your data as a CSV.
</Update>

<Update label="February 5th, 2026" tags={["Added"]}>
  ## 🆕 Statuspage MCP Server Integration Now Available

  🎯 **What is it?**

  Dust now integrates with Atlassian Statuspage through a dedicated MCP (Model Context Protocol) server. Your agents can now directly interact with your Statuspage infrastructure to manage incidents, update component statuses, and monitor your system's health, all through natural conversation.

  💡 **Why is it useful?**

  When an incident occurs, speed and coordination are critical. This integration eliminates context-switching between tools and enables your DevOps teams and SREs to manage incident communication workflows without leaving Dust. Instead of manually logging into Statuspage to update statuses or create incident reports, your agents can handle these tasks instantly based on your instructions or automated triggers.

  ⚙️ **How does it work?**

  Admins configure the integration by adding their Statuspage API key to Dust. Once set up, agents can access Statuspage on-demand to perform key operations: listing pages and components, checking ongoing incidents, creating new incidents, updating incident details, and marking components as experiencing outages.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Automated Incident Response**: Ask an agent "Create a Statuspage incident for the API outage we're experiencing" and it instantly creates the incident, sets the appropriate component status, and can even draft customer-facing updates based on your internal incident notes.

  **Status Monitoring Dashboard**: Configure an agent to regularly check your Statuspage for ongoing incidents and provide morning briefings to your on-call team, summarizing what's currently under maintenance or experiencing issues.

  **Coordinated Communication**: During an incident, ask your agent to "Update the database incident with investigating status and ETA of 30 minutes" while you focus on actually resolving the technical issue.

  📈 **Benefits for you**

  * **Faster incident response**: Reduce the time between detection and public communication
  * **Reduced cognitive load**: Let agents handle status updates while your team focuses on resolution
  * **Consistent communication**: Ensure incident updates follow your established workflows and templates
  * **Centralized operations**: Manage incident communication alongside your other operational tasks in Dust

  🚀 **How to access it?**

  This integration is available on-demand for all Dust users with a Statuspage account. Workspace admins need to configure the Statuspage API key in your Dust workspace settings. Once configured, enable the Statuspage capability for any agent that needs incident management access.
</Update>

<Update label="February 3rd, 2026" tags={["Added"]}>
  ## 📊 Agent Builder Insights: Real-time Observability Dashboard

  🎯 **What is it?**

  The Agent Builder now features an observability dashboard that gives you real-time visibility into how your agents are performing. You can track usage trends, monitor which tools are being executed, analyze user feedback, measure response times, and understand how your retrieval systems are behaving, all linked to specific versions of your agents.

  💡 **Why is it useful?**

  AI agents often fail quietly in production. A prompt change might slow down responses, a tool update could break a workflow, or retrieval quality might degrade, and you won't know until frustrated users report it. This dashboard shifts you from reactive troubleshooting to proactive monitoring, letting you catch issues before they impact your team and understand the real-world impact of every change you make.

  ⚙ **How does it work?**

  The dashboard automatically collects performance data from your agents in real-time. Every conversation, tool execution, and retrieval query is tracked and visualized, with metrics tied to specific agent versions so you can compare performance before and after changes.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Validate prompt improvements**: You updated an agent's instructions to be more concise. Check the dashboard to see if average latency decreased and if user feedback scores improved compared to the previous version.

  **Debug tool execution issues**: Users mention an agent isn't providing complete answers. The dashboard reveals that a specific API tool is timing out 40% of the time, pointing you directly to the problem.

  **Optimize retrieval quality**: After adding new documents to your knowledge base, monitor RAG behavior metrics to ensure the agent is retrieving relevant information and not getting overwhelmed by irrelevant context.

  **Track adoption and impact**: See which agents are being used most frequently, during what times, and by which teams, helping you prioritize maintenance and development efforts.

  📈 **Benefits for you**

  * **Catch problems early**: Identify performance degradation or failures before they become widespread issues
  * **Make data-driven decisions**: Understand the real impact of configuration changes instead of guessing
  * **Save troubleshooting time**: Pinpoint the exact version and component causing issues
  * **Build confidence**: Deploy agent updates knowing you can monitor their real-world performance immediately

  🚀 **How to access it?**

  Open any agent in the Agent Builder. You'll find the new Insights tab alongside your existing configuration options. The dashboard is available immediately for all users, no setup or activation required.
</Update>

<Update label="February 3rd, 2026" tags={["Added"]}>
  ## Daily Spending Cap for API Usage

  📌 Context

  To help you maintain better control over your costs and protect against unexpected spending spikes, we've introduced a daily spending cap for all API (programmatic) usage on Dust.

  This safeguard automatically monitors your API consumption and prevents runaway costs from accidental loops, misconfigured scripts, or unexpected usage patterns.

  🔄 Impact on Dust

  We've implemented real-time tracking that:

  * Monitors your API spending throughout the day
  * Automatically resets at midnight UTC each day
  * Uses a fail-safe approach: if our tracking system encounters any issues, API calls are temporarily blocked to ensure you're never surprised by unexpected charges

  👤 Impact for you

  **Default limits:**

  * Standard workspaces: \$1,000 per day
  * Pay-as-you-go workspaces: The greater of \$1,000 or 20% of your monthly spending cap, per day

  **What this means:**

  * For most customers, daily API usage will continue without any interruption
  * If you approach your daily cap, API calls will be blocked until the next day (midnight UTC)
  * You'll have full visibility into your spending and won't encounter surprise bills from runaway usage

  **Need a different limit?**

  If your typical API usage requires a higher daily cap, you can request a custom limit between $100 and $10,000 through your account settings or by contacting your Customer Success Manager.

  ✅ Actions required

  **No immediate action required** for most customers. Your existing API integrations will continue to work within the default daily limits.

  **Optional:** If you regularly use the API extensively, we recommend:

  1. Reviewing your typical daily API spending patterns
  2. Contacting us if you need to adjust your daily cap to match your usage
  3. Implementing monitoring in your applications to track daily usage

  This change is live for all workspaces starting today.
</Update>

<Update label="January 30th, 2026" tags={["Added"]}>
  ## Export MiniApps as PDF

  🎯 What is it?

  You can now export any MiniApp as a PDF document directly from Dust. When exporting, you can choose between portrait or landscape orientation to best fit your content. Enterprise plans receive clean PDFs without any branding, while other plans include a discreet "Created with Dust" footer.

  💡 Why is it useful?

  MiniApps are visual tools for data analysis, reports, and presentations within Dust. However, many of you needed to share these insights outside the platform, whether for compliance documentation, distribution to external vendors, or integration into company repositories like SharePoint. This was one of your most requested features, and we're excited to make sharing your work easier.

  ⚙ How does it work?

  Open any MiniApp and select the export option. Choose your preferred orientation (portrait or landscape), and Dust will generate a PDF version of your MiniApp in seconds. The export handles most MiniApp layouts automatically.

  ✨ Concrete Use Cases

  Here's how you could use it:

  **Compliance & Documentation**: Export weekly analytics MiniApps as PDFs for compliance archives or audit trails in your document management system.

  **External Reporting**: Share performance dashboards or project status MiniApps with external partners, vendors, or clients who don't have Dust access.

  **Executive Presentations**: Convert data visualizations into PDFs for inclusion in board presentations, SharePoint libraries, or email distributions.

  **Offline Access**: Create PDF versions of critical MiniApps for offline reference during travel or in low-connectivity environments.

  📈 Benefits for you

  * **One-click sharing**: Transform interactive MiniApps into universally accessible PDF documents instantly
  * **Professional output**: Clean, presentation-ready documents suitable for any audience
  * **Flexibility**: Choose the orientation that best showcases your content
  * **Broader reach**: Share your Dust insights with anyone, regardless of their access to the platform

  🚀 How to access it?

  The feature is already live for all users! Navigate to any MiniApp you've created or have access to, and look for the export/PDF option. No setup or activation required: start exporting today.

  **Note**: While PDF export is designed to handle a wide variety of MiniApp layouts, from standard reports to advanced visualizations, we're continuously improving the feature to support even the most creative MiniApp designs. If you encounter any issues with specific layouts, please let us know so we can refine the experience.
</Update>

<Update label="January 29th, 2026" tags={["Added"]}>
  ## Per API-Key Usage Cap

  🎯 **What is it?**

  Admins can now set a spending limit on individual API keys. Each key can have its own maximum dollar amount for API usage, calculated on a 30-day rolling basis. This gives you precise control over how much each API integration or user can spend.

  💡 **Why is it useful?**

  As your team scales and more people use Dust programmatically, it becomes harder to track and control costs at a granular level. Until now, your only option was a workspace-wide limit. This new feature helps you prevent budget overruns, test new integrations safely, and allocate resources more strategically across different projects or teams.

  ⚙️ **How does it work?**

  Set a dollar cap when creating or editing an API key. Once the key reaches that spending limit within any 30-day period, it will stop working until the rolling window resets. Keys without a cap continue to use the workspace's overall limit.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Testing environment**: Set a \$50 cap on API keys used for development and testing to avoid unexpected costs from runaway scripts or experiments.

  **Team allocation**: Give your marketing team an API key with a $500 monthly cap and your engineering team a separate key with a $2,000 cap, matching each team's actual needs and budget.

  **Third-party integrations**: When connecting Dust to external tools or contractors, set conservative limits to control costs while you evaluate usage patterns.

  📈 **Benefits for you**

  * **Better budget control**: Prevent individual integrations or users from consuming your entire workspace credit unexpectedly
  * **Safe experimentation**: Test new use cases without risking your full budget
  * **Clearer accountability**: Track and manage costs at the team or project level
  * **Flexible scaling**: Adjust limits as needs change without affecting your entire workspace

  🚀 **How to access it?**

  Admins can access this feature in the Dust workspace settings, under the API Keys section. When creating a new API key or editing an existing one, you'll find the option to set a usage cap. No action is required if you prefer to keep your current setup: API keys without a cap will continue to work as before, limited only by your workspace's overall limit.
</Update>

<Update label="January 29th, 2026" tags={["Added"]}>
  ## 📬 Email Notifications Now Include Conversation Summaries

  🎯 **What is it?**

  Your Dust notification emails now include an AI-generated summary of unread messages. Instead of just being notified that you have new activity, you'll see a concise overview of what's been discussed directly in your inbox.

  💡 **Why is it useful?**

  We know your inbox is busy, and context switching takes time. With this update, you can quickly assess what's happening in your Dust conversations without needing to immediately open the app. This helps you prioritize which conversations need your immediate attention and which can wait.

  ⚙ **How does it work?**

  When you have unread messages in a Dust conversation, the notification email you receive will automatically include a brief summary of the key points discussed. This summary is generated to give you the essential context at a glance.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Prioritizing your morning**: Scan your email summaries over coffee to decide which conversations need your immediate input and which can be reviewed later in the day.

  **Staying informed on-the-go**: Quickly catch up on team discussions from your mobile email app while commuting, without needing to switch apps or log into Dust.

  📈 **Benefits for you**

  * **Save time**: Get context without opening multiple apps
  * **Stay informed**: Keep up with important conversations even when you're away from Dust
  * **Better prioritization**: Quickly identify which messages need your urgent attention

  🚀 **How to access it?**

  This feature is already active for all users. No setup required: your next notification email will automatically include summaries when you have unread messages.
</Update>

<Update label="January 28th, 2026" tags={["Added"]}>
  ## Discover Existing Skills Before You Build – Automatic Similar Skills Detection

  🎯 **What is it?**

  When you create a new skill in Dust, the platform now automatically scans your workspace to detect if similar skills already exist. As you write your skill description, AI analyzes it in real-time and alerts you if it finds potential matches, helping you discover skills you could reuse or build upon.

  💡 **Why is it useful?**

  Building skills takes time and effort. Without visibility into what already exists, teams often recreate the same automation multiple times, leading to fragmented knowledge, inconsistent results, and wasted time. This feature helps you maintain a clean, organized skill library by surfacing relevant existing work before you start from scratch.

  ⚙️ **How does it work?**

  As you type your skill description during creation, Dust's AI compares it against all custom skills in your workspace. If it detects similarities, you'll see a notification suggesting existing skills you might want to review or reuse instead.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Avoiding duplicates**: You're about to create a skill to "Create GitHub issues from meeting notes." Before you finish, Dust alerts you that "GitHub Issue Creator" already exists in your workspace, built by a colleague last month with the exact same purpose.

  **Building on existing work**: You start creating a skill for "Slack notifications on deal closures." Dust surfaces a similar skill called "CRM to Slack Updates" that you can either reuse directly or modify to fit your specific needs.

  📈 **Benefits for you**

  * **Save time**: Reuse existing skills instead of building from scratch
  * **Maintain consistency**: Reduce skill sprawl and duplicate automations across your workspace
  * **Discover team knowledge**: Find expertise and solutions your colleagues have already created
  * **Keep your workspace organized**: No more "Create Report v1, v2, v3" cluttering your skill library

  🚀 **How to access it?**

  This feature is automatically active for all builders. Start creating a new skill as usual. If similar skills exist, Dust will notify you while you're writing the description. No configuration needed.
</Update>

<Update label="January 28th, 2026" tags={["Added"]}>
  ## 📧 Gmail Integration: Send Emails Directly from Dust

  🎯 **What is it?**

  Your Gmail integration on Dust can now send emails directly. Previously, Dust could only read, search your Gmail messages and create drafts. Now your assistant can compose and send emails on your behalf through the Gmail tool.

  💡 **Why is it useful?**

  This feature addresses one of our most requested capabilities from customers. It enables your Dust assistants to take action on your behalf, not just retrieve information. You can now automate email workflows, draft responses, and send communications without leaving your conversation with Dust.

  ⚙ **How does it work?**

  Once enabled, your assistant can use the Gmail "send mail" tool to compose and send emails directly from your Gmail account. The assistant will handle the email composition based on your instructions.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Automated follow-ups**: Ask your assistant to "send a follow-up email to the prospects who haven't responded in the last 7 days" based on your CRM data and email history.

  **Quick responses**: "Draft and send a thank you email to John after our meeting, mentioning the key points we discussed about the Q1 roadmap."

  **Batch communications**: "Send a weekly summary email to my team with the top 5 updates from our project documentation."

  📈 **Benefits for you**

  * **Save time**: Automate routine email tasks and responses
  * **Stay in flow**: Send emails without switching between tools
  * **Increase efficiency**: Let your assistant handle email drafts and sends based on your knowledge and context

  🚀 **How to access it?**

  **For existing Gmail tool users**: This feature is disabled by default to ensure smooth operations. To enable it, go to **Spaces > Tools > Gmail > Send Mail** and toggle it on.

  **For new tool setup**: If you're installing a new instance of the Gmail tool now, the send mail feature will be enabled by default.
</Update>

<Update label="January 28th, 2026" tags={["Added"]}>
  ## ✨ More Powerful Image Generation with Gemini 3 Pro

  🎯 **What is it?**

  We've upgraded our image generation capabilities to Gemini 3 Pro Image (also known as Nano Banana 2), bringing you significantly higher quality outputs and more creative control. You can now generate images in resolutions up to 4K and include up to 14 reference images in a single composition.

  💡 **Why is it useful?**

  Creating high-quality visual content often requires combining multiple references, understanding nuanced creative direction, and producing outputs at professional resolutions. This upgrade addresses these needs by giving you more flexibility and better results when generating or editing images through Dust.

  ⚙ **How does it work?**

  The new engine processes more complex prompts with better accuracy and allows you to upload up to 14 reference images. These references can be used to edit existing assets or to compose entirely new images by combining multiple visual elements.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Marketing Materials**: Upload your brand guidelines, product photos, and mood board references (up to 14 images) to generate on-brand marketing visuals in 4K resolution for print and digital campaigns.

  **Design Iteration**: Provide multiple variations of a design concept and use detailed creative instructions to generate refined versions that blend the best elements of your references.

  **Product Visualization**: Combine lifestyle photos, product specifications, and environmental references to create high-resolution product mockups in various settings.

  📈 **Benefits for you**

  * **Higher quality outputs**: 1K to 4K resolution options for professional-grade results
  * **More creative flexibility**: Process complex, nuanced instructions more accurately
  * **Faster iteration**: Combine up to 14 references in one go instead of multiple attempts
  * **Better consistency**: Improved understanding of style and composition requests

  🚀 **How to access it?**

  The upgrade is already live in your Dust workspace. Use the image generation feature as usual: the new capabilities are automatically available. For inspiration and detailed examples, check out our documentation: [/docs/user-documentation/agents/tools/image-generation](/docs/user-documentation/agents/tools/image-generation)
</Update>

<Update label="January 27th, 2026" tags={["Added"]}>
  ## 🆕 Skills: Share Expertise Across All Your Agents

  🎯 **What is it?**

  Skills is a new capability that allows you to package instructions, knowledge, and tools into reusable modules. Once created, any agent in your workspace can access these Skills. When you update a Skill, all agents using it automatically benefit from the improvement, no need to manually update each agent.

  💡 **Why is it useful?**

  If you're building multiple agents for your team, you've probably noticed yourself copying and pasting the same instructions or configurations over and over. Skills solves this problem by letting you define something once and share it everywhere. It's designed to help builders spread their expertise efficiently and improve the agent-building experience for everyone in your workspace.

  ⚙ **How does it work?**

  You create a Skill by bundling together specific instructions, relevant knowledge sources, and tools. Once created, any agent can be equipped with that Skill. If you refine or update the Skill later, every agent using it instantly improves.

  ✨ **Concrete Use Cases**

  Here's how you could use it:

  **Standardized research methodology**: Create a "Market Research" Skill that includes your company's research framework, access to your research databases, and web search tools. Every agent tasked with research will follow the same rigorous process.

  **Consistent brand voice**: Build a "Brand Communication" Skill containing your tone of voice guidelines, brand vocabulary, and approved messaging. All customer-facing agents will automatically maintain your brand standards.

  **Domain expertise**: Package your team's specialized knowledge (like "Financial Analysis," "Legal Compliance," or "Technical Support") so any agent can use expert-level capabilities without you rebuilding the context each time.

  📈 **Benefits for you**

  * **Save time**: Build once, use everywhere, no more duplicating work across agents
  * **Maintain consistency**: Ensure all agents follow the same standards and best practices
  * **Scale expertise**: Share specialized knowledge across your entire workspace
  * **Easier updates**: Improve all your agents at once by updating a single Skill

  🚀 **How to access it?**

  Skills are now available to all builders in your workspace. Check out our documentation to learn how to create and manage Skills: [/docs/user-documentation/agents/skills/skill-examples](/docs/user-documentation/agents/skills/skill-examples)
</Update>

<Update label="January 27th, 2026" tags={["Added"]}>
  ## ✨ Customize global skills with your own branding and instructions

  * Take any Dust-managed skill (like Create MiniApps) and make it your own
  * Add your branding guidelines, attach specific assets, and include extra instructions
  * Access via Manage Skills → find the skill → click `...` → Customize skill
  * Each team can create their own independent extensions
</Update>

<Update label="January 27th, 2026" tags={["Added"]}>
  ## 🔍 Discover Tools - Global Skill for Agents

  Agents can now automatically discover and use any toolset available in the workspace without manual configuration in the Agent Builder.

  * Agents dynamically find the tools they need when they need them
  * Eliminates the need to pre-select specific tools during agent setup
  * Provides agents with access to the entire panel of available integrations in one click
</Update>

<Update label="January 27th, 2026" tags={["Added"]}>
  ## 🔍 Discover Knowledge global skill

  * New pre-packaged skill that enables agents to search and query company data sources
  * Supports warehouse connections including Snowflake and BigQuery
  * Searches across all accessible spaces
  * Available on @dust and @deep-dive agents
  * Can be added to custom agents from the Agent Builder
</Update>

<Update label="January 27th, 2026" tags={["Added"]}>
  ## ✨ Reference knowledge directly in skill instructions

  * Use `/` to search and tag specific folders or documents when building a skill
  * Agents now get automatic access to referenced content
  * Point directly to folders or documents instead of relying on ambiguous references
  * Enables specialized, knowledge-grounded skills with precise context
</Update>

<Update label="January 27th, 2026" tags={["Added"]}>
  ## ⚡ Just-in-time Skills

  * Add or remove skills from the input bar mid-conversation
  * Enable specific capabilities for individual questions without reconfiguring your agent
  * Compose capabilities on the fly to create complex custom agents
</Update>

<Update label="January 26th, 2026" tags={["Added"]}>
  ## ✈️ UKG Ready integration for PTO management

  * UKG Ready MCP integration now available
  * Request, view, and manage Paid Time Off (PTO) directly from Dust
  * Access PTO balances and submit time-off requests without leaving the platform
</Update>

<Update label="January 19th, 2026" tags={["Added"]}>
  ## ❄️ Snowflake MCP Tool with Personal Authentication

  * Added Snowflake as an MCP tool with OAuth-based personal authentication
  * Agents can access all data available to the user's configured Snowflake role
  * Supports Snowflake views
  * No manual table configuration required
</Update>

<Update label="January 19th, 2026" tags={["Improved"]}>
  ## ⚡ Parallelized Google Drive synchronization

  * Google Drive full and incremental syncs now run in parallel
  * Each drive is handled by a separate workflow
  * Significantly faster completion times for multi-drive synchronization
</Update>

<Update label="January 16th, 2026" tags={["Added"]}>
  ## 🔒 Static IP for custom MCP server calls

  You can now whitelist Dust's static IP addresses for secure communication with your custom MCP servers:

  * Verify your domain in Admin > People & Security > Verified domains
  * Once verified, all MCP server calls to that domain will use our static IPs
  * US region: 34.46.9.232
  * EU region: 35.195.191.222
</Update>

<Update label="January 16th, 2026" tags={["Added"]}>
  ## 🔧 Medium stake tools with per-agent approval history

  * Introduced a new medium stake level for tools that maintains approval history per agent rather than globally
  * Medium stake is now the default for Gmail drafting tools, Slack message posting, and Google Calendar event editing
  * Admins can configure the medium stake level for any tool
  * Users will be prompted to approve medium stake tools on a per-agent basis
</Update>

<Update label="January 13th, 2026" tags={["Added"]}>
  ## ⬅️➡️ Navigate between messages in conversation view

  * Added navigation arrows to jump to previous or next user message in conversations
  * Makes it easier to review and find specific messages in long conversations
</Update>

<Update label="January 12th, 2026" tags={["Added"]}>
  ## 🔌 Productboard integration

  * Connect your workspace to Productboard to capture feedback and manage product data
  * Create and update notes, features, and objectives directly from Dust agents
  * Support for both workspace and individual credentials
  * Sync product hierarchy and roadmap planning data
</Update>

<Update label="January 9th, 2026" tags={["Added"]}>
  ## 🛡️ Vanta Tools

  * Connect your workspace to Vanta directly from Dust
  * Access automated test status and vulnerability tracking
  * Review risk scenarios, frameworks, and control evidence
  * Monitor and audit compliance from the agent builder
</Update>

<Update label="January 8th, 2026" tags={["Added"]}>
  ## ✏️ Edit and Delete Messages & Conversations

  You can now edit or delete your messages and entire conversations directly in the interface. This feature is available to all users.
</Update>

<Update label="January 8th, 2026" tags={["Added"]}>
  ## 💬 Mention users in conversations

  * Use @mentions to directly notify and address specific users in conversations
  * Helps direct messages to the right people in multi-user discussions
</Update>

<Update label="January 8th, 2026" tags={["Added"]}>
  ## 🏷️ Mention users in the Agent Builder

  * You can now mention and tag real people directly while designing agents in the builder
  * Mentions work directly within the agent configuration interface
</Update>

<Update label="January 8th, 2026" tags={["Added"]}>
  ## ✨ Rich text formatting toolbar in conversations

  * New formatting toolbar available in the conversation interface
  * Support for text styling including bold, italics, and code formatting
  * Visual editing controls for composing messages
</Update>

<Update label="January 8th, 2026" tags={["Added"]}>
  ## 🔔 Mention and Agent Notifications

  Stay informed with new notification options:

  * Receive email notifications when you're mentioned in a conversation
  * Get browser push notifications when you're mentioned
  * Receive notifications when an agent completes its response
</Update>

<Update label="January 8th, 2026" tags={["Added"]}>
  ## 📬 New Inbox for Mentions and Notifications

  * A new 'Inbox' section is now available
  * All your mentions and notifications are gathered in one centralized place
  * Easily track conversations where you've been mentioned
</Update>

<Update label="December 23rd, 2025" tags={["Added"]}>
  ## 🧠 Guru Integration Now Available

  • Connect your Guru knowledge base to Dust

  • Search and reference Guru cards and collections directly within conversations

  • Access your trusted knowledge without switching platforms
</Update>

<Update label="December 23rd, 2025" tags={["Added"]}>
  ## 🆕 Freshservice MCP Tool Integration

  * New Freshservice MCP tool now available
  * Manage tickets directly through Dust
  * Submit service requests
  * Access knowledge base articles
  * Handle approvals
</Update>

<Update label="December 18th, 2025" tags={["Added"]}>
  ## ☁️ Dust n8n node now available on n8n Cloud

  The Dust n8n node is now available as a verified community node on n8n Cloud. Previously, the node was only accessible for self-hosted n8n instances.
</Update>

<Update label="December 17th, 2025" tags={["Added"]}>
  ## ⚡ Gemini 3 Flash model now available

  • New Gemini 3 Flash model added to the agent builder • Fast performance with strong benchmark results • Available for immediate use in agent configurations
</Update>

<Update label="December 16th, 2025" tags={["Added"]}>
  ## 💾 Draft Mode: Auto-save your messages

  • Messages are now automatically saved as drafts while you're composing them • Unsent messages persist across page reloads and browser sessions • Your drafts will be restored exactly where you left off
</Update>

<Update label="December 16th, 2025" tags={["Added"]}>
  ## 😊 Emoji shortcode support in messages

  You can now insert emojis in your messages using the `:emoji_name:` syntax. Type any supported emoji shortcode (like `:smile:` or `:rocket:`) and it will automatically convert to the corresponding emoji.
</Update>

<Update label="December 15th, 2025" tags={["Added"]}>
  ## 📎 Search and Attach Files from Tools

  You can now search and attach files directly from the attachment button in the input bar for: • Google Drive Tools • Microsoft Drive Tools • Notion Tools

  This feature is available on the web version when you have a Tool configured for these providers (and not the related Connection since we default to searching in the Connection it if is set).
</Update>

<Update label="December 11th, 2025" tags={["Added"]}>
  ## 🔍✨ Advanced Search & Pagination for GitHub MCP Issues & PRs

  • Added advanced search capabilities for GitHub MCP issues and pull requests • Implemented robust pagination to handle large repositories • Support for GitHub's advanced search syntax to filter and find specific items
</Update>

<Update label="December 11th, 2025" tags={["Added"]}>
  ## 💳 Programmatic Usage Tracking and Billing

  • Programmatic usage is now tracked and billed separately from regular usage • New dedicated 'API & Programmatic' section for admins to monitor usage and purchase credits • Programmatic usage is blocked when credits run out, while human usage continues uninterrupted • Free discovery credits provided monthly • Enterprise users can opt for Pay-as-you-go billing
</Update>

<Update label="December 11th, 2025" tags={["Improved"]}>
  ## ⚡ Search Latency Improvements

  • Optimized the search (retrieval) engine for faster performance • Search results now load significantly faster
</Update>

<Update label="November 28th, 2025" tags={["Added"]}>
  ## 🤖 Structured Response Format for Claude Sonnet 4.5

  • Claude Sonnet 4.5 now supports Structured Response Format with JSON schema • Define a JSON schema in the advanced menu of the Agent Builder to enforce model output format • Useful for workflows where agent output needs to be parsed and sent to other tools
</Update>

<Update label="November 28th, 2025" tags={["Improved"]}>
  ## 🔍 Better user search with accent support

  User search now supports diacritics (accents) and provides better ranking of results. • Search now works properly with accented characters in names • Email addresses are now searchable with smart handling of username and domain • Improved search available in Space user management and Agent editor management
</Update>

<Update label="November 25th, 2025" tags={["Added"]}>
  ## 🎛️ Customizable tool approval settings for MCP tools

  Admins can now define and adjust approval settings for MCP tools directly from the admin interface: • High stake: Agent always asks users to confirm before using the tool • Low stake: Agent asks users to confirm, with option to 'never ask again' • Never ask: Agent performs the action directly without confirmation
</Update>

<Update label="November 25th, 2025" tags={["Added"]}>
  ## 🎟️ Linear Built-in Webhook Provider

  • New webhook provider for Linear integration • Trigger agents automatically on Linear issues and project updates • Configure webhooks directly in Spaces settings
</Update>

<Update label="November 18th, 2025" tags={["Improved"]}>
  ## 🔐 Granular site access for Microsoft service principals

  • Service principals can now be restricted to specific sites only • No longer requires Sites.Read.All permission for limited access scenarios • Provides more fine-grained control over Microsoft connector permissions
</Update>

<Update label="November 17th, 2025" tags={["Improved"]}>
  ## 💬 Improved agent tagging in Slack

  • Agent mentions (+agent or \~agent) must now come immediately after @Dust • Previous behavior allowed agent mentions anywhere in the message
</Update>

<Update label="November 14th, 2025" tags={["Added"]}>
  ## 🖼️✨ Image Editing Tool

  You can now edit images directly within Dust: • Upload images to the platform • Adjust and modify images in-place • Annotate images with built-in tools • No need to switch to external image editing applications
</Update>

<Update label="November 14th, 2025" tags={["Added"]}>
  ## 🤖 GPT-5.1 now available in the builder

  • GPT-5.1 is now available as a model option in the agent builder • This is an alternative to GPT-5, which remains available • The new model offers improved performance characteristics
</Update>

<Update label="November 13th, 2025" tags={["Added"]}>
  ## 📊 Agent Builder Insights tab

  • Added a new 'Insights' tab in the Agent Builder • View usage metrics and tool execution data • Track feedback trends and latency performance • Correlate all metrics with specific agent versions for performance tracking
</Update>

<Update label="November 13th, 2025" tags={["Added"]}>
  ## 🎙️ Fathom webhook integration

  • New built-in webhook provider for Fathom • Automatically trigger agents when new Fathom transcripts are available • Configure webhooks directly from your Space settings
</Update>

<Update label="November 13th, 2025" tags={["Added"]}>
  ## 🎫 Zendesk built-in webhooks

  You can now trigger your agents automatically with Zendesk events: • New tickets • New comments • Status changes • Configure webhooks directly in your Spaces
</Update>

<Update label="November 13th, 2025" tags={["Added"]}>
  ## 🎫 Zendesk tools

  • Fetch tickets directly from Zendesk • Pull ticket metrics for analysis • Search across tickets • Draft replies to customer inquiries
</Update>

<Update label="November 12th, 2025" tags={["Added"]}>
  ## ✉️ Improved invitation flow and workspace selection

  • Predictable behavior when receiving multiple workspace invitations, no more random redirects • New selection page when you have multiple pending invitations, allowing you to choose which workspace to join • Invitation tokens are now always respected, ensuring you land in the correct workspace • Invitations now expire as expected • Pending invitations are now visible on your profile page with quick join buttons
</Update>

<Update label="November 10th, 2025" tags={["Added"]}>
  ## 🎫 Jira Built-in Webhook Provider

  • Added native Jira webhook integration to trigger agents automatically • Agents can now respond to Jira ticket updates in real-time • Webhooks can be configured directly in Spaces settings
</Update>

<Update label="November 10th, 2025" tags={["Added"]}>
  ## 🔗 GitHub Built-in Webhook

  • Trigger agents automatically on GitHub pull requests and issues updates • Configure webhooks directly in Spaces settings • Integrates with GitHub MCP Server for complete automation workflows
</Update>

<Update label="November 10th, 2025" tags={["Added"]}>
  ## 🌀 Webhooks as triggers

  • Agents can now be triggered by incoming webhooks • Admins can set up webhook sources directly in the Spaces UI • Webhook sources can be connected to any new or existing agent
</Update>

<Update label="November 7th, 2025" tags={["Added"]}>
  ## 🚀 Auto-create Spaces for provisioned groups

  • New option to automatically create empty Spaces when groups are provisioned • Spaces are created alongside their corresponding groups • Feature can be enabled on demand
</Update>

<Update label="November 6th, 2025" tags={["Improved"]}>
  ## ⚡ Lightning-Fast Photo-Realistic Image Generation

  • Upgraded to Nano Banana, Google's latest image generation model • 6x faster image generation • Photo-realistic image quality
</Update>

<Update label="November 5th, 2025" tags={["Improved"]}>
  ## 🤖 Dust is now your default agent

  • When you don't @ mention a specific agent, your message now automatically goes to @dust • If @dust is not activated in your workspace, we still recommend a list of suited agents
</Update>

<Update label="November 5th, 2025" tags={["Added"]}>
  ## 🔌 Global Agent Can Now Query Data Warehouses

  • The global agent can now execute SQL queries using the data warehouses tool • Supports Snowflake and BigQuery connections • Get instant answers to quantitative questions by querying structured data directly
</Update>

<Update label="November 5th, 2025" tags={["Added"]}>
  ## 🧠 Dust Global Agent Now Uses Memory

  • The Dust global agent can now store and recall information from your conversations • Memory tool enables learning from interactions to provide personalized responses • Preferences and context are remembered across conversations for more relevant assistance
</Update>

<Update label="November 5th, 2025" tags={["Added"]}>
  ## 🔍 Advanced Search now available on Dust global agent

  The Dust global agent can now access Advanced Search (Data Source File System) in addition to traditional semantic search. This enables the agent to: • Read documents in full • Navigate data source structures • Provide more precise answers with reduced hallucinations
</Update>

<Update label="November 3rd, 2025" tags={["Added"]}>
  ## 🎉 Dust Google Sheets Add-on now available on Google Workspace Marketplace

  • The Dust Google Sheets add-on is now officially published and available directly from the Google Workspace Marketplace • No more manual script installations required • Install and connect Dust to your spreadsheets in just a few clicks
</Update>

<Update label="October 31st, 2025" tags={["Improved"]}>
  ## 🔧 Slack MCP server improvements

  • Improved user permissions mapping for private channels and direct messages • Improved list channels functionality with reduced payload size to optimize LLM context usage • Added 'get channels details' function for more granular channel information • Added ability to schedule messages • Added ability to add and remove reactions to messages
</Update>

<Update label="October 31st, 2025" tags={["Added"]}>
  ## 📊 Excel MCP Server integration with SharePoint and OneDrive

  • Added tools to list, read, write, create, and clear data in Excel files • Direct integration with SharePoint and OneDrive storage • Simpler Excel workbook automation
</Update>

<Update label="October 31st, 2025" tags={["Added"]}>
  ## 🔗 Microsoft Teams MCP

  • Added new Microsoft Teams MCP server with a full set of tools • Search messages content across Teams • List teams, users, channels, and chats • View messages in channels • Post messages to teams and chats
</Update>

<Update label="October 31st, 2025" tags={["Added"]}>
  ## 📁 New SharePoint and OneDrive integration

  • Added search and retrieval capabilities for SharePoint and OneDrive files • Added file upload functionality to SharePoint and OneDrive • Added Word document editing capabilities • Agents can now perform end-to-end document workflows across Microsoft platforms
</Update>

<Update label="October 31st, 2025" tags={["Added"]}>
  ## 🤝 Microsoft Teams Dust Bot

  • Interact with Dust assistants directly from Microsoft Teams • Available in private chats with Dust or any Teams channel • Install via feature flag for Microsoft ecosystem users
</Update>

<Update label="October 27th, 2025" tags={["Added"]}>
  ## 🧠 Dynamic toolset discovery for Dust assistant

  • Dust assistant can now automatically discover and access available tools in the Company Data space • Tools are enabled dynamically on-demand during conversations • Expands what the assistant can do without manual tool setup
</Update>

<Update label="October 23rd, 2025" tags={["Added"]}>
  ## 🔊 Voice generation tools

  * Added 'Sound Studio' tool for generating sound effects
  * Added 'Speech Generator' tool to generate discussions, and speech
  * Enables podcast generation capabilities

  <br />
</Update>

<Update label="October 23rd, 2025" tags={["Added"]}>
  ## ✨ Data warehouse exploration for Deep Dive

  • Deep Dive can now explore and query entire data warehouses (Snowflake, BigQuery) without pre-configuration • Search for tables by name and examine schemas dynamically • Run SQL queries across multiple tables in a single research session • Support for large-scale data exploration (hundreds of tables, thousands of columns)
</Update>

<Update label="October 23rd, 2025" tags={["Improved"]}>
  ## 🌐⚡ Offloaded Browsing with AI Summaries

  • Deep Dive sub-agents now receive AI-generated summaries (200-500 tokens) instead of full page content when browsing web pages • Full page content is stored as accessible files for detailed analysis when needed • Enables browsing 20+ pages instead of 2-3 pages within context limits • Improves context efficiency by at least an order of magnitude for research tasks
</Update>

<Update label="October 23rd, 2025" tags={["Added"]}>
  ## 🔨 ✨ Dynamic Tool Discovery with Toolsets

  • @deep-dive can now discover and call MCP tools dynamically during research • Uses toolsets\_\_list to see available tool servers and selects relevant ones (GitHub, Salesforce, Monday, etc.) • Spawns sub-agents with specific tools for focused tasks • Extends capabilities on-demand based on task requirements
</Update>

<Update label="October 23rd, 2025" tags={["Improved"]}>
  ## 🧠 Better Context Management for All Agents

  • All agents now have improved context management that preserves conversations across more turns • When context window fills up, old tool outputs get pruned while keeping tool calls visible • Maintains reasoning chain so agents remember what they've done • Conversations stay coherent across more consecutive turns • Agents don't lose context even in extended back-and-forth sessions
</Update>

<Update label="October 23rd, 2025" tags={["Added"]}>
  ## 🧠 New Go Deep Tool for enhanced agent capabilities

  • Added a new Go Deep Tool that allows agents to hand off complex tasks for thorough analysis • Tool is available by default in @Dust agent • Can be added to any custom agent through the agent builder • Enables specialized agents to use deep-dive capabilities while maintaining awareness of main agent instructions
</Update>

<Update label="October 23rd, 2025" tags={["Added"]}>
  ## 🧠 New Deep Dive agent for comprehensive research

  • Added a new @deep-dive agent that conducts thorough research across company data, data warehouses, and the web • Uses sub-agents to perform parallel research tasks for extended periods (10+ minutes) • Explores topics iteratively before producing detailed answers • Available for complex tasks requiring in-depth analysis and synthesis
</Update>

<Update label="October 23rd, 2025" tags={["Added"]}>
  ## 🤖 Agent handover now supports direct conversation responses

  • Added option to select 'agent responds in conversation' when using Run Agent MCP tool • Agents can now post their answers directly in the conversation instead of running in background • Available across all workspaces for any user
</Update>

<Update label="October 23rd, 2025" tags={["Added"]}>
  ## 🧠 Advanced Search Mode for Agents

  • Added exploratory search mode with new tools for systematic data navigation • New `list` tool to browse folders and directory structures • New `find` tool to search for documents by filename • New `cat` tool to read complete documents instead of just chunks • New `locate_in_tree` tool to view document hierarchies • Updated `search` tool with folder-scoped searching capabilities • Toggle available in Agent Builder under 'Advanced settings'
</Update>

<Update label="October 22nd, 2025" tags={["Added"]}>
  ## 🚀 Val Town MCP Server Integration

  • Added tools to interact with Val Town's platform • Users can now write and scale serverless JavaScript directly from Dust • Build, deploy, and manage Val Town scripts • Enables automation and custom workflows through Val Town's serverless JS platform
</Update>

<Update label="October 21st, 2025" tags={["Added"]}>
  ## 🔗🦊 GitLab Official MCP Integration

  • Added support for the official GitLab Model Context Protocol (MCP) as a remote MCP • Automatic app creation on GitLab when registering the MCP from Dust • Available tools include: issue management, merge request operations, pipeline monitoring, and semantic code search • Integration is now live for all users
</Update>

<Update label="October 17th, 2025" tags={["Added"]}>
  ## 🛠️ New agent tools: time, wait, and random utilities

  • Agents can now get the current time • Added ability for agents to wait/pause execution • Agents can generate random numbers and dice rolls • These utilities are available to all agents immediately
</Update>

<Update label="October 16th, 2025" tags={["Deprecated"]}>
  ## 🕐 Dust Apps creation disabled for new workspaces

  • New workspaces can no longer create or use Dust Apps as tools • Existing workspaces with Dust Apps remain unaffected • Dust Apps will be replaced by various tools including fetch capabilities
</Update>

<Update label="October 15th, 2025" tags={["Added"]}>
  ## 🤖 Claude 4.5 Haiku model now available

  • Added support for Anthropic's new Claude 4.5 Haiku model • Available for selection when creating or editing agents under Advanced → From Anthropic → Claude 4.5 Haiku • Accessible to all users immediately
</Update>

<Update label="October 15th, 2025" tags={["Added"]}>
  ## 🖼️ MiniApps: Interactive responses for your agents

  • Agents can now create interactive components (MiniApps) instead of static text responses • Create live reports, dashboards, calculators, and data visualizations that users can explore in real time • Interactive features include hover, filter, click, and dive functionality • MiniApps update instantly when you ask your agent to make changes • Share MiniApps internally or externally as live, interactive files with secure, token-gated links • Available to all users with no feature flag required
</Update>

<Update label="October 13th, 2025" tags={["Improved"]}>
  ## 📱 Mobile and tablet experience improvements

  • Progressive loading of conversations and agents lists • Smooth conversation scrolling with virtualized message lists • Optimized performance for conversations with thousands of messages • Bigger touch targets for mobile-friendly interactions • Fixed mobile layouts for agent builder and conversation views • Smart keyboard handling that prevents unexpected pop-ups • Proper iOS status bar colors and theming • Touch-friendly interactions with disabled hover effects on mobile • Resizable panels that work correctly on mobile screens
</Update>

<Update label="October 10th, 2025" tags={["Added"]}>
  ## 📄 Document sharing in Slack channels

  • Agents can now share documents directly in Slack channels • Available for all agents with the Slack tool enabled • Enables automated document distribution and workflow integration
</Update>

<Update label="October 9th, 2025" tags={["Added"]}>
  ## 🎙️ Voice input and audio file support

  • Record audio directly in conversations or attach audio files (up to \~1 hour) • Automatic transcription with support for 29 spoken languages • Intent detection to automatically select relevant agents based on voice commands • Audio processing respects workspace region settings (EU/US models)
</Update>

<Update label="October 8th, 2025" tags={["Added"]}>
  ## 📝 (preview) Confluence Tool bring page creation and updates to Dust agents

  • Added OAuth authentication for personal or workspace credentials • Enabled agents to create new pages directly in Confluence spaces • Enabled agents to update existing pages in Confluence spaces • Added write actions alongside the existing semantic search capabilities

  To access the feature, contact [support@dust.tt](mailto:support@dust.tt)
</Update>

<Update label="October 7th, 2025" tags={["Added"]}>
  ## 📚 Select entire datasources from search

  • You can now select full datasources (not just individual files) directly from search results • Available in Agent Builder, Knowledge section, and the input bar • Enables adding all content from a datasource with a single click
</Update>

<Update label="September 29th, 2025" tags={["Added"]}>
  ## 📎 Auto-attachment for long pasted text

  • Long text content pasted into conversations is now automatically converted into file attachments • Keeps conversations visually clean and uncluttered • Handles lengthy content without disrupting message flow
</Update>

<Update label="September 19th, 2025" tags={["Added"]}>
  ## 🔑 GitHub Tool now supports personal credentials

  • Actions like creating issues and posting PR comments now appear as coming from you instead of the dust-agent bot • Personal attribution improves collaboration and makes audit trails clearer • Available to all users with no feature flag required
</Update>

<Update label="September 19th, 2025" tags={["Added"]}>
  ## 📁 Google Drive Tool for real-time document access

  • Agents can now access Google Drive documents in real-time using personal user credentials • Read-only access with role-based permissions - users only see files they have access to • No syncing or indexing required - documents are accessed on-demand • Available for all workspaces
</Update>

<Update label="September 18th, 2025" tags={["Added"]}>
  ## 🎉 Microsoft Excel Extension

  • Use Dust directly inside Microsoft Excel on both online and desktop versions • Access Dust functionality directly within your Excel workflows • Available at [office-addins.dust.tt](https://office-addins.dust.tt) with full documentation

  <br />

  [▶️ https://www.youtube.com/watch?v=42kGSigMEIk](https://www.youtube.com/watch?v=42kGSigMEIk)

  <br />
</Update>

<Update label="September 16th, 2025" tags={["Added"]}>
  ## 🎫 Jira integration now globally available

  • Create, read, update, and transition Jira issues directly from Dust • Advanced search capabilities with custom fields and JQL query support • Flexible authentication options with personal or workspace credentials • Comment on issues and manage workflows
</Update>

<Update label="September 16th, 2025" tags={["Added"]}>
  ## ⏰ Agent Scheduling

  • Users can now add schedules to their agents in the Agent Builder. More info here [schedules](/docs/user-documentation/agents/triggers/schedules)

  • Agents will run automatically on a regular basis following the configured schedule

  • Available for all users
</Update>

<Update label="September 15th, 2025" tags={["Added"]}>
  ## 👍 Agent feedback reactions in Slack

  • Added thumbs up, thumbs down, and arrow down reaction buttons to agent replies in Slack • Users can now provide direct feedback on agent responses without leaving Slack • Feedback reactions are consistent with the web application experience
</Update>

<Update label="September 8th, 2025" tags={["Added"]}>
  ## 🔧 Retry policies for Dust-provided tools

  • Dust-provided tools can now be configured with retry policies<br />• First available policy automatically retries tools if they are interrupted due to timeouts, deployments, or other issues<br />• Tool developers can flag each tool with specific retry policies<br />• Improves tool reliability and enables longer-running operations to resume after interruptions
</Update>

<Update label="September 5th, 2025" tags={["Added"]}>
  ## 👀 'Used by' columns for tools in Space admin

  • Added 'Used by' columns to the Space admin tools list<br />• Admins can now instantly see which assistants are using which tools<br />• Consistent 'Used by' UI across all admin interfaces
</Update>

<Update label="September 4th, 2025" tags={["Added"]}>
  ## 💬 Unread message indicators for conversations

  • Conversations now display clear indicators when you have unread messages<br />• Makes it easier to track new activity across ongoing conversations<br />• Helps prioritize which conversations need attention
</Update>

<Update label="September 2nd, 2025" tags={["Improved"]}>
  ## 🤖 Complete redesign of agent creation interface

  • New simplified interface for building custom agents<br />• Improved tool selection dialog with better discoverability<br />• XML block formatting for structured instructions<br />• Redesigned data source selection experience<br />• More intuitive knowledge configuration<br />• Better accessibility for new builders while maintaining advanced capabilities for power users
</Update>

<Update label="September 1st, 2025" tags={["Added"]}>
  ## ⚡ Zapier integration now supports non-blocking requests

  • Added 'blocking' parameter to Zapier integration<br />• Allows instant retrieval of conversation ID without waiting for agent response<br />• Enables separate polling for conversation results to avoid timeout issues
</Update>

<Update label="August 30th, 2025" tags={["Added"]}>
  ## 🔄 Asana available as tool

  * Asana is now available in the tools selection menu (Spaces > Tools > Add Tools)
  * No manual configuration required to connect Asana workspace
</Update>

<Update label="August 26th, 2025" tags={["Added"]}>
  ## 🪐 Cross-space tool and datasource access for Agents

  * Agents can now use tools and datasources from multiple spaces simultaneously
  * No restrictions on the number of spaces that can be accessed
  * Unified access to all available resources across spaces
</Update>

<Update label="August 25th, 2025" tags={["Added"]}>
  ## ⚡️ Long-Running Durable Agents

  * Improved time limitations on agent execution duration
  * Added resilience to system deploys and transient errors
  * Removed tool validation and authentication timing constraints
  * Increased maximum agent execution steps to 64
  * Added capability for granular message retry from point of failure in backend
</Update>

<Update label="August 22nd, 2025" tags={["Added"]}>
  ## 🔍 Channel selection for Slack tool

  * Added ability to select specific Slack channels when configuring the Slack tool in agents
  * Enables targeted channel access for both keyword and semantic search scenarios
</Update>

<Update label="August 14th, 2025" tags={["Improved"]}>
  ## 🔧 Multiple workspace selection in Agent Builder

  * Expanded tool and knowledge selection to support both company workspace and one additional workspace when configuring agents
  * Previously limited to a single workspace selection
</Update>

<Update label="August 13th, 2025" tags={["Added"]}>
  ## ✈️ Seamless cross-region workspace switching

  * Added ability to switch between US and EU workspaces directly from the user menu
  * Single sign-on functionality implemented across regions
  * Unified login system between dust.tt and eu.dust.tt domains
</Update>

<Update label="August 12th, 2025" tags={["Improved"]}>
  ## 🌐 Enhanced Web Search & Browse with HTML and Screenshot Support

  * Added ability to retrieve complete HTML source code of web pages
  * Added support for capturing viewport and full-page screenshots
</Update>

<Update label="August 11th, 2025" tags={["Added"]}>
  ## 🛠️ Tools Now Available in Conversations

  * Added the ability to use tools directly within conversations
  * Access the full suite of tools without creating an agent
</Update>

<Update label="August 11th, 2025" tags={["Added"]}>
  ## 🤖 Added GPT-5 model support

  * Added OpenAI's latest GPT-5 model
  * Available in 4 reasoning variants: none, light, medium, high
  * Includes dedicated global agent with medium reasoning settings
</Update>

<Update label="August 7th, 2025" tags={["Added"]}>
  ## 🔗 Personal Notion integration support

  * Added ability to connect personal Notion accounts to the Notion integration
  * Enable individual user authentication when the tool is configured as 'Personal'
</Update>

<Update label="August 7th, 2025" tags={["Added"]}>
  ## 📂 Added support for Confluence folder content synchronization

  * Content stored within Confluence folders is now synchronized and indexed
  * All folder content is searchable and retrievable alongside other Confluence content
</Update>

<Update label="August 1st, 2025" tags={["Added"]}>
  ## 🎛️ Filter Zendesk ticket syncing with tags

  * Added ticket tag filtering to control which Zendesk tickets sync to Dust
  * Added organization tag filtering to sync tickets based on organization tags
  * Both filters support inclusion and exclusion rules
  * Filters apply to new tickets only
</Update>

<Update label="August 1st, 2025" tags={["Added"]}>
  ## 🔄 Support for duplicate MCP server URLs

  * Multiple remote MCP servers can now be configured with identical URLs
  * Enables more flexible server configurations
</Update>

<Update label="August 1st, 2025" tags={["Added"]}>
  ## 🎛️ Selective MCP Tool Enablement

  * Individual tools from MCP servers can now be enabled/disabled when configuring a remote MCP server
  * Granular control over which tools are available to agents
</Update>

<Update label="July 30th, 2025" tags={["Added"]}>
  ## 🗓️ New Outlook Calendar integration

  * List and manage calendar events directly from Dust
  * Create new calendar events
  * Send event invitations to other participants
</Update>

<Update label="July 30th, 2025" tags={["Added"]}>
  ## 📧 Connect and manage Outlook emails in Dust

  * Connect Outlook email accounts to Dust
  * List and read emails directly from the platform
  * Create and manage email drafts
  * Delete draft emails
  * Early access: Contact [support@dust.tt](mailto:support@dust.tt) for activation
</Update>

<Update label="July 29th, 2025" tags={["Added"]}>
  ## 🗄️ Improved table storage infrastructure

  • Migrated table data storage from SQL to individual GCS files<br />• Significantly improved data upsert performance<br />• Reduced storage footprint by over 80%
</Update>

<Update label="July 29th, 2025" tags={["Added"]}>
  ## 🔐 Personal authentication mode for HubSpot integration

  * Added personal connection mode to HubSpot integration
  * Users can now access their own HubSpot data and permissions
  * Scope of accessible objects is tied to individual user accounts
</Update>

<Update label="July 25th, 2025" tags={["Added"]}>
  ## 🧠 Agent Memory - Store and recall information across conversations

  * New memory capabilities for agents to store and recall information
  * Memories are scoped per user and accessible in the agent details drawer
  * Can be added to any agent without configuration
</Update>

<Update label="July 21st, 2025" tags={["Removed"]}>
  ## 🔒 Standardized agent step limit to 128

  * Removed configurable step limit for agents (previously 1-24 steps)
  * All agents now have a fixed limit of 128 steps
</Update>

<Update label="July 18th, 2025" tags={["Improved"]}>
  ## 🎨 Enhanced error message visualization

  * Redesigned error display with improved visual hierarchy
  * Added clearer error titles
  * Implemented expanded message layout for better readability
</Update>

<Update label="July 17th, 2025" tags={["Added"]}>
  ## 🤖 New Kimi K2 Instruct model available

  * Added Kimi K2 Instruct model from Fireworks AI
  * Available for selection in the agent builder
</Update>

<Update label="July 11th, 2025" tags={["Added"]}>
  ## 📧 Gmail Tool now reads and replies to email threads

  * Added ability to read email message content directly within the tool
  * Enabled drafting replies within existing email threads
  * Integrated thread context handling for easier email management
</Update>

<Update label="July 10th, 2025" tags={["Added"]}>
  ## 📄 Self-serve PDF scanning controls and workspace storage limits

  * Added storage quota indicators showing when workspace document limits are reached
  * Introduced self-serve PDF scanning toggle in Google Drive and Microsoft connectors settings
</Update>

<Update label="July 9th, 2025" tags={["Added"]}>
  ## 💳 SEPA Direct Debit Support

  * Added SEPA direct debit as a payment method
  * Available for organizations based in France and the United Kingdom
</Update>

<Update label="July 8th, 2025" tags={["Added"]}>
  ## 📊 Google Sheets integration with read and write capabilities

  * Read data from Google Sheets directly in workflows
  * Write and update data to Google Sheets automatically
  * Direct integration with spreadsheet data
</Update>

<Update label="July 7th, 2025" tags={["Improved"]}>
  ## 🔄 Enhanced HubSpot integration capabilities

  * Increased API results limit from 50 to 200 records
  * Added pagination support for datasets exceeding 10,000 records
  * Improved object counting and searching reliability
  * Added user activity tracking functionality
  * Added owner filtering to search capabilities
  * Added association management features
</Update>

<Update label="July 7th, 2025" tags={["Added"]}>
  ## 🔧 Linear Integration Available as a Tool

  * Linear tool integration now available for configuration in all workspaces
  * Enables agents to manage Linear issues and projects
  * Supports automated project management workflows
</Update>

<Update label="July 7th, 2025" tags={["Added"]}>
  ## 🧠 New Reasoning Effort Controls for Language Models

  * Introduced configurable reasoning effort levels for language models in the agent builder
  * Added 'medium' and 'high' reasoning options for OpenAI o-series models, defaulting to medium (o1, o3, o4-mini)
  * Implemented 'light' and 'none' reasoning options for Claude and Gemini 2.5 pro models (light is default)
</Update>

<Update label="July 3rd, 2025" tags={["Added"]}>
  ## ✈️ Import Front Conversations Feature

  * New open-source script available to import Front conversations into Dust
  * Conversations can be used as a data source for Dust workflows
</Update>

<Update label="July 3rd, 2025" tags={["Improved"]}>
  ## 🧠 Enhanced OpenAI Model Reasoning

  * Added native reasoning capabilities for OpenAI o-series models
  * Improved tool usage behavior to match ChatGPT experience
  * Added visibility into model's thought process through summary display
</Update>

<Update label="July 3rd, 2025" tags={["Added"]}>
  ## 💳 Stripe integration now available as a tool

  * Added official Stripe integration as a configurable tool
  * Enables payment and billing operations through Stripe's API
  * Available as a standard tool for all workspaces
</Update>

<Update label="July 2nd, 2025" tags={["Added"]}>
  ## 🔍 New Slack Tool: Search and Post Messages

  * Search messages across Slack channels directly from Dust
  * Post messages to Slack channels through Dust
  * Interact with Slack workspace content
</Update>

<Update label="July 2nd, 2025" tags={["Added"]}>
  ## 🔄 SCIM User and Group Provisioning Support

  * Enable user provisioning through SCIM-compatible identity providers
  * Synchronize user groups from enterprise directories
  * Automate user access management across spaces
</Update>

<Update label="June 30th, 2025" tags={["Added"]}>
  ## 🤖 Non-Interactive Chat Support in CLI

  * Added new CLI flags for non-interactive chat mode:
    * `--agent` (`-a`) to select agents by name
    * `--message` (`-m`) to send messages and get JSON responses
    * `--conversationId` (`-c`) to continue existing conversations
</Update>

<Update label="June 27th, 2025" tags={["Added"]}>
  ## 🔌 New Salesforce Integration

  * Query Salesforce data directly from the platform
  * Support for workspace-level shared credentials
  * Support for individual user authentication
</Update>

<Update label="June 25th, 2025" tags={["Improved"]}>
  ## 🔌 Gmail & Google Calendar tools now available with simple authentication

  * Gmail and Google Calendar tools can now be used with standard Google account login
  * No custom OAuth credentials required anymore
  * Direct connection through Google account authentication
</Update>

<Update label="June 24th, 2025" tags={["Improved"]}>
  ## 🔄 Authentication System Upgrade

  * Transitioned to a new authentication platform
  * Implemented improved user authentication and management system
  * Maintained backward compatibility for existing enterprise SSO users
</Update>

<Update label="June 24th, 2025" tags={["Added"]}>
  ## 🛠️ Enhanced CLI with new flags, commands and caching

  • Added `--agent` flag for specifying agent name at launch<br />• New `/attach` and `/clear-files` commands for native file management<br />• Implemented caching system for faster CLI startup<br />• Added `dust cache:clear` command for cache management
</Update>

<Update label="June 24th, 2025" tags={["Added"]}>
  ## 🔍 Improved BigQuery views support

  • Automatic handling of access to underlying tables when a view is selected<br />• Support for authorized views
</Update>

<Update label="June 24th, 2025" tags={["Added"]}>
  ## 🕷️ Enhanced Web Crawler with Advanced Features

  • Added support for client-side rendered pages and JavaScript execution<br />• Integrated PDF and Google Docs parsing capabilities<br />• Improved content extraction from modern websites<br />• Implemented residential proxy rotation for better reliability
</Update>

<Update label="June 20th, 2025" tags={["Added"]}>
  ## 🔍 Notion Page Visibility Checker

  * Added a diagnostic tool to verify Notion page visibility and indexing status
  * Enables checking whether specific Notion pages are accessible and indexed
</Update>

<Update label="June 19th, 2025" tags={["Added"]}>
  ## 🔑 Support for Snowflake key pair authentication

  • Added support for key pair authentication in the Snowflake connector<br />• Alternative to password-based authentication
</Update>

<Update label="June 18th, 2025" tags={["Added"]}>
  ## 🔍 Search for documents by URL

  * Added URL-based search functionality in Knowledge base and Assistant Builder
  * Search documents by pasting their source URL
  * Automatically detect and retrieve matching documents from sources
</Update>

<Update label="June 16th, 2025" tags={["Added"]}>
  ## 🔄 New script for importing Planhat data

  * Added script to import data from Planhat into Dust
  * Available in dust-labs repository: [https://github.com/dust-tt/dust-labs/tree/main/planhat](https://github.com/dust-tt/dust-labs/tree/main/planhat)
</Update>

<Update label="June 16th, 2025" tags={["Improved"]}>
  ## 🔄 Enhanced Zendesk App with Extended Response Time

  * Increased maximum wait time for agent responses to 3 minutes
  * Implemented non-blocking calls with status polling
  * Refreshed UI design to align with Dust's visual identity
</Update>

<Update label="June 11th, 2025" tags={["Added"]}>
  ## 🤖 New Run Agent Tool

  * Added ability to execute agents as tools within other agents
  * Sub-agents run in separate conversations that can be inspected
  * New tool enables modular agent capabilities and longer execution chains
</Update>

<Update label="June 11th, 2025" tags={["Added"]}>
  ## 🔐 Added OAuth credential options for remote MCP servers

  * Added support for both workspace-level and personal credentials when authenticating to remote MCP servers
  * Administrators can now choose between shared workspace credentials or individual user credentials for OAuth authentication
</Update>

<Update label="June 11th, 2025" tags={["Added"]}>
  ## 🔐 Flexible authentication options for Salesforce integration

  * Added support for both workspace-level and personal Salesforce credentials
  * Users can now authenticate using either shared workspace credentials or individual accounts
</Update>

<Update label="June 10th, 2025" tags={["Added"]}>
  ## 🔄 Salesforce SOQL Query Sync Support

  • Added ability to sync custom SOQL queries as data source documents<br />• Documents from SOQL queries are now available through the Search tool
</Update>

<Update label="June 6th, 2025" tags={["Added"]}>
  ## 🔐 OAuth Authentication Support for Remote MCP Servers

  * Added automatic OAuth authentication flow when connecting to remote MCP servers
  * Implemented support for the latest MCP protocol revision
</Update>

<Update label="June 4th, 2025" tags={["Added"]}>
  ## 📝 New Notion Agent Tool

  * New MCP-powered tool for agents to:
    * Read Notion documents and pages
    * Search across Notion workspace content
    * Create and write new Notion content
</Update>

<Update label="June 4th, 2025" tags={["Added"]}>
  ## 📂 Dropbox Files Import Integration

  * New integration to import files directly from Dropbox into Dust
  * Available in beta version
  * Supports importing Dropbox content as a data source
</Update>

<Update label="June 4th, 2025" tags={["Added"]}>
  ## 🔌 New Hubspot Integration Tool

  * Added Hubspot CRM tool for agents
  * Enables reading, updating, and creating CRM records
  * Supports interactions with contacts, deals, and other Hubspot objects
</Update>

<Update label="June 2nd, 2025" tags={["Added"]}>
  ## 🤖 New xAI Grok Models Available

  * Added Grok 3 model to the agent builder
  * Added Grok 3 Mini model to the agent builder
  * To use these models, make sure the xAI provider is enabled in your Workspace Settings.
</Update>

<Update label="May 30th, 2025" tags={["Improved"]}>
  ## 📊 Enhanced Google Sheets data selection capabilities

  * Added support for multiple-column selection in Google Sheets
  * Included column headers in data context for more accurate responses
</Update>

<Update label="May 27th, 2025" tags={["Added"]}>
  ## 🔐 Personal Tools Support

  * New support for tools requiring personal authentication
  * Tools can now be configured to use individual user credentials
  * Personal tools are activated by workspace admins
  * Tools are attached to agents like regular tools
  * User authentication happens on first tool execution
</Update>

<Update label="May 26th, 2025" tags={["Improved"]}>
  ## 🚀 System-wide performance optimizations

  * Optimized expensive database queries
  * Fixed memory-intensive loop causing high resource usage
  * Resolved streaming chunk errors caused by resource constraints
</Update>

<Update label="May 24th, 2025" tags={["Improved"]}>
  ## 🔌 Remote MCP Server Connection Enhancements

  * Added support for StreamableHTTP transport protocol
  * Added ability to set bearer token when adding a remote MCP server
</Update>

<Update label="May 15th, 2025" tags={["Added"]}>
  ## 🏷️ Improved Assistant Discovery and Organization

  * Added tags and categories for assistants
  * Implemented advanced search functionality
  * Improved sharing controls and permissions
  * Added assistant routing capabilities
</Update>

<Update label="May 15th, 2025" tags={["Added"]}>
  ## 🛠️ New GitHub Tools

  Agents can now:

  * Create and manage GitHub issues
  * Retrieve pull request information
  * Generate code reviews
</Update>

<Update label="May 15th, 2025" tags={["Improved"]}>
  ## 🔄 Simplified Assistant Builder Interface

  * Merged Tools & Capabilities sections into a cleaner interface
  * Added two main dropdown categories: Knowledge and Tools
  * Implemented search functionality for tools
</Update>

<Update label="May 14th, 2025" tags={["Added"]}>
  ## 🎉 MCP Support Now Available for All Workspaces

  * Remote MCP server connections available
  * File generation and conversion tools enabled
  * GitHub integration tools accessible
  * Feature available in all regions
</Update>

<Update label="May 12th, 2025" tags={["Added"]}>
  ## 🖥️ Chat with Dust Agents via CLI

  * New CLI tool to interact with Dust agents from the terminal
  * Install globally via npm: `@dust-tt/dust-cli`
  * Start chatting by running the `dust` command
</Update>

<Update label="May 2nd, 2025" tags={["Added"]}>
  ## 📊 BigQuery table descriptions available to Agents

  • Table and column descriptions from BigQuery schemas are now accessible to Agents<br />• Can be enabled in BigQuery connection settings
</Update>

<Update label="April 30th, 2025" tags={["Added"]}>
  ## 🤖 Smarter Agent Recommendations

  • Added automatic agent suggestions when posting messages without @mentions<br />• Suggestions are based on message content and agent capabilities
</Update>

<Update label="April 24th, 2025" tags={["Added"]}>
  ## 🎨 GPT Image Model Integration for Enhanced Image Generation

  • Added gpt-image-1 model for image generation in agents<br />• Available through 'Image Generation' capability in agent builder<br />• Includes tiered usage limits per workspace
</Update>

<Update label="April 23rd, 2025" tags={["Improved"]}>
  ## 🔄 Enhanced Extract Data Tool Capabilities

  • Added dynamic timeframe support for data extraction<br />• Introduced dynamic schema support<br />• Implemented JSON schema formatting<br />• Added ability to store extraction results in downloadable files<br />• Enabled direct extraction from files shared in conversations
</Update>

<Update label="April 17th, 2025" tags={["Added"]}>
  ## 🛠️ Preview: New Tools and External MCP Server Support in Agents

  * We're adding new tools: image generation, file conversion, improved web browsing, GitHub issues and pull request, etc...
  * Agents can use external MCP servers
  * Doc is available [here](/docs/user-documentation/admins/tools-management/adding-an-mcp-server)

  [Contact us](mailto:support@dust.tt) if you'd like early access to the preview!
</Update>

<Update label="April 17th, 2025" tags={["Added"]}>
  ## 🤖 New OpenAI o4-mini Model Available

  • Added o4-mini model<br />• Added o4-mini (High Reasoning) model<br />• Both models can now be used in the agent builder
</Update>

<Update label="April 16th, 2025" tags={["Added"]}>
  ## 🤖 GPT-4.1 Model Now Available

  * New GPT-4.1 model is now accessible across all agents
  * Default @gpt4 agent has been upgraded to use GPT-4.1
</Update>

<Update label="April 15th, 2025" tags={["Added"]}>
  ## 🔧 Structured JSON Output Support for OpenAI Models

  • Added ability to enforce JSON-schema formatted responses from OpenAI models<br />• Available in both agent configurations (via advanced builder settings) and app chat blocks<br />• Ensures consistent output formatting for reliable downstream processing
</Update>

<Update label="April 11th, 2025" tags={["Added"]}>
  ## 🔌 Personal connections support for Salesforce connector

  * Added the ability to use personal Salesforce credentials instead of a shared service account when connecting to Salesforce
  * Users can now access data based on their individual Salesforce permissions
</Update>

<Update label="April 8th, 2025" tags={["Added"]}>
  ## 🧪 Import Linear Issues Feature

  • New script to import issues from Linear into Dust<br />• Available in dust-labs repository
</Update>

<Update label="April 8th, 2025" tags={["Improved"]}>
  ## 🔗 Smoother account linking experience

  • Added a new notice screen explaining the account merge process when signing in with different authentication methods<br />• Automatic redirection to merge flow when duplicate email accounts are detected<br />• Accounts are now consolidated based on the oldest identity
</Update>

<Update label="April 8th, 2025" tags={["Added"]}>
  ## 🤖 Gemini 2.5 Pro available in Custom Agents

  * Added Gemini 2.5 Pro as a model option for Custom Agents
  * Can be selected from the model dropdown menu
</Update>

<Update label="April 4th, 2025" tags={["Added"]}>
  ## 🌗 Chrome extension now supports Dark mode

  * Added Dark mode support to the Chrome extension
  * Refreshed extension design to match current website styling
</Update>

<Update label="April 3rd, 2025" tags={["Added"]}>
  ## 🖥️ New Dust CLI Tool

  * Introduced a Command Line Interface (CLI) tool for Dust
  * Run a local MCP server with your selected Dust agents
  * Enables interaction between Cursor/Windsurf/Claude and Dust agents
  * Install via npm: `@dust-tt/dust-cli`
</Update>

<Update label="April 2nd, 2025" tags={["Added"]}>
  ## 📎 Attach Knowledge Items Directly in Input Bar

  • Added ability to search and attach documents, tables, and folders from Knowledge directly in the input bar<br />• Added support for pasting document URLs in the input bar to attach them

  [▶️ Attach datasources to your conversations dynamically](https://www.youtube.com/watch?v=ZCtwc-j7i90)
</Update>

<Update label="April 2nd, 2025" tags={["Added"]}>
  ## 🔑 Service Principal authentication for Microsoft connector

  • Added Service Principal (service account) authentication method as an alternative to OAuth<br />• Enables automated, non-interactive authentication with Microsoft services
</Update>

<Update label="March 7th, 2025" tags={["Improved"]}>
  ## 🔍 Smarter label filtering with dynamic search

  * Added dynamic label search capability before filtering
  * Models now identify existing valid labels first
  * Improved accuracy of label-based filtering

  <br />

  [▶️ Introducing labels as a filter for data sources](https://www.youtube.com/watch?v=QwHyMpVJva4)
</Update>

<Update label="March 6th, 2025" tags={["Added"]}>
  ## 🔌 Native Gong Integration Released

  * Direct connection to sync Gong call transcripts
  * Filter and search conversations by participants
  * AI-powered analysis of sales calls and meetings
  * Automatic transcript syncing capabilities

  [Read more](/docs/user-documentation/admins/connections-management/gong)
</Update>

<Update label="March 4th, 2025" tags={["Added"]}>
  ## 🔍 Added keyword search in Builder and Knowledge

  * Search and add documents by keywords when configuring data sources in Assistant Builder
  * Search functionality added for documents in Knowledge management
</Update>

<Update label="February 28th, 2025" tags={["Improved"]}>
  ## 🎯 Solutions Pages Revamp with Enhanced Use Cases

  * Added solutions pages featuring 10 core functions
  * Included detailed explanations for top 4 use cases per function
  * Added custom illustrations for better visual understanding
  * Integrated demo videos showcasing product functionality
  * Added customer success stories for real-world applications
</Update>

<Update label="February 28th, 2025" tags={["Improved"]}>
  ## ✨ Enhanced markdown support in chat

  * Added proper markdown handling in the chat input bar
  * Pasted formatted text now maintains its original formatting
</Update>

<Update label="February 26th, 2025" tags={["Added"]}>
  ## 🌙 Dark mode support

  * Added dark mode theme option to Dust's interface
  * Toggle between light/dark via Preferences menu in sidebar
  * Respects system color scheme preferences
</Update>

<Update label="February 24th, 2025" tags={["Added"]}>
  ## 🤖 Claude 3.7 Sonnet Model Now Available

  * Added Claude 3.7 Sonnet to the list of available models in the assistant builder
  * Accessible when creating or editing assistants
</Update>

<Update label="February 24th, 2025" tags={["Added"]}>
  ## 🔄 Optional sync of unresolved Zendesk tickets

  * Added ability to sync unresolved tickets (new, open, pending, on-hold) from Zendesk
  * Previously only resolved tickets were synced
  * Both resolved and unresolved tickets can now be synced based on configuration
</Update>

<Update label="February 19th, 2025" tags={["Added"]}>
  ## 🏷️ Enhanced data filtering with labels

  • Added label-based filtering capabilities to Search, Include, and Extract data source tools<br />• New documents in Connections now automatically capture labels
</Update>

<Update label="February 14th, 2025" tags={["Added"]}>
  ## Notion management: Admins can force sync pages/dbs

  * In connection admin / notion, Admins can provide a list of URLs for databases or pages they want to sync immediately
  * Feature is available on demand only (feature flag)
</Update>

<Update label="February 14th, 2025" tags={["Added"]}>
  ## 🔌 BigQuery Connector Now Available

  * Connect and query BigQuery datasets directly from Dust
  * Import data from your BigQuery tables into your workspaces

  [Read more](/docs/user-documentation/admins/connections-management/bigquery)
</Update>

<Update label="February 14th, 2025" tags={["Improved"]}>
  ## 🧩 Browser Extension Updates

  * Improved assistant autocomplete and search functionality
  * Improved UI styling elements

  [Read more](/docs/user-documentation/agents/integrations/browser-extension)
</Update>

<Update label="February 13th, 2025" tags={["Added"]}>
  ## 📊 Support for Excel file uploads in conversations

  * Added support for uploading .xls and .xlsx files directly in conversations
  * Excel sheets are automatically converted to CSV format
  * Converted sheets can be queried using table operations
</Update>

<Update label="February 11th, 2025" tags={["Added"]}>
  ## 🏢 New About Us page

  * Added a dedicated About Us page showcasing company information
  * Includes sections about mission and operating principles
  * Features team structure and investor information
  * Accessible at /home/about
</Update>

<Update label="February 11th, 2025" tags={["Added"]}>
  ## 🔌 Released Dust Node for n8n Integration

  * New n8n community node available for installation
  * Enables interaction with Dust assistants directly from n8n workflows
  * Supports document upload functionality
  * Documentation: [/docs/user-documentation/agents/integrations/n8n](/docs/user-documentation/agents/integrations/n8n)
</Update>

<Update label="February 7th, 2025" tags={["Added"]}>
  ## 🇪🇺 EU Data Hosting Option Available

  * New data hosting option in European servers
  * Available **exclusively** for enterprise customers
  * Covers storage of databases, files, and vectors
  * Language models accessed through provider APIs
</Update>

<Update label="February 6th, 2025" tags={["Added"]}>
  ## 🔌 BigQuery Connector Beta Release

  * New data connector for BigQuery databases
  * Enables live data querying capabilities
  * Supports data visualization and interpretation features
  * Provides similar functionality to the Snowflake connector
</Update>

<Update label="February 3rd, 2025" tags={["Added"]}>
  ## 🤖 OpenAI O3-mini model now available

  • Added O3-mini model with two modes: normal and high-reasoning<br />• Available in the builder as main assistant and reasoning model<br />• New 'O3 Mini' global agent using O3-mini high-reasoning mode
</Update>

<Update label="January 29th, 2025" tags={["Added"]}>
  ## 🐳 New DeepSeek R1 Global Agent

  * Added DeepSeek R1 model as a global agent for direct interactions
  * Available for users with appropriate feature flags enabled
  * Served through fireworks.ai, US based servers
</Update>

<Update label="January 29th, 2025" tags={["Added"]}>
  ## 🧠 New Reasoning Tool for Assistants

  • Added a new tool for Assistants to invoke reasoning models (R1 or O1)<br />• Enables better handling of complex problems while maintaining fast responses for simpler queries<br />• Integrates with existing Assistant tools and instructions<br />• Supports both DeepSeek R and OpenAI O1 models
</Update>

<Update label="January 29th, 2025" tags={["Added"]}>
  ## 🏥 HIPAA Compliance Certification

  • Dust is now HIPAA compliant<br />• Documentation can be found on the security page and on Dusts' trust center
</Update>

<Update label="January 28th, 2025" tags={["Added"]}>
  ## 👥 Batch member addition in Space settings

  * Added a new feature to add multiple members to a Space at once
  * Support for adding up to 100 members simultaneously via email addresses
</Update>

<Update label="January 25th, 2025" tags={["Added"]}>
  ## 🔗 Slack bot now includes thread files in conversations

  * Files shared in Slack threads are now automatically included when invoking @dust or custom assistants
  * Supports various file formats (images, PDF, DOC, PPT, CSV)
  * File size limit: 10MB

  ⚠️ **Existing workspaces must re-authorize the Slack connexion to enable this feature.**
</Update>

<Update label="January 24th, 2025" tags={["Added"]}>
  ## 🎙️ Added Modjo as a transcripts processing provider

  * Support for Modjo transcripts integration
  * Ability to sync personal transcripts or company-wide transcripts
</Update>

<Update label="January 24th, 2025" tags={["Added"]}>
  ## 🔍 OCR Support for uploaded PDF Files

  Automatically run OCR (Optical Character Recognition) on PDF files uploaded to conversations when text cannot be directly extracted, enabling text extraction from PDFs containing images of text
</Update>

<Update label="January 24th, 2025" tags={["Improved"]}>
  ## 🧩 Browser Extension Updates

  • Added feedback functionality in conversations<br />• Added support for EU region<br />• Added URL blacklisting with path-level control<br />• Improved SSO workspace integration<br />• Refreshed various UI elements
</Update>

<Update label="January 23rd, 2025" tags={["Improved"]}>
  ## 🔒 Completed Annual Security Certification

  Successfully renewed security certifications and compliance requirements for platform infrastructure and data handling capabilities
</Update>

<Update label="January 21st, 2025" tags={["Added"]}>
  ## 📦 Extended File Format Support for Attachments

  Added support for multiple new file formats:<br />• Programming languages: Python, C/C++, C#, Java, PHP, Ruby, SQL, Swift, Rust, Go, Kotlin, Scala, Groovy, Perl<br />• Presentations: PowerPoint<br />• Configuration: YAML
</Update>

<Update label="January 17th, 2025" tags={["Improved"]}>
  ## 📂 More granular file selection in assistant tools

  * Added ability to select individual files from a folder when configuring assistant tools (search, include, etc.)
  * No longer required to select an entire folder when using folder content in tools
</Update>

<Update label="January 17th, 2025" tags={["Improved"]}>
  ## 🔄 Increased default and maximum steps for assistant runs

  * Default number of steps per assistant run increased from 3 to 8
  * Maximum allowed steps increased from 8 to 12
</Update>

<Update label="January 16th, 2025" tags={["Improved"]}>
  ## 📱 Improved conversation layout responsiveness

  * Messages now adapt their width based on content length
  * Better readability across all screen sizes
  * Optimized layout for both mobile and desktop views
</Update>

<Update label="January 14th, 2025" tags={["Improved"]}>
  ## 🔒 Reduced Google Meet permissions scope

  * Now using a more restrictive permission scope (`drive.meet.readonly`) to access Google Meet transcripts
  * Dust only requests access to Google Meet-generated files instead of all Google Drive files
</Update>

<Update label="January 9th, 2025" tags={["Added"]}>
  ## 👍 Assistant feedback system launch

  * Added feedback functionality for custom assistant responses
  * Users can now rate assistant responses and optionally share conversations
  * Introduced feedback statistics dashboard in the assistant manager
  * Feedback metrics now available through workspace usage API

  <br />

  [▶️ Agents Feedback loop](https://www.youtube.com/watch?v=KYihEH1Z-bQ)
</Update>

<Update label="January 8th, 2025" tags={["Added"]}>
  ## ⏱️ Conversations now sorted by last activity

  Conversations are now automatically sorted by most recent activity:<br />• When posting a message in a conversation, it moves to the top of the list<br />• Most recently used conversations appear first
</Update>

<Update label="January 6th, 2025" tags={["Added"]}>
  ## 🤖 DeepSeek V3 Model Now Available

  • Added DeepSeek V3, a new large language model, to the platform<br />• Model can be used in Dust Apps, as a global agent, and in custom assistants<br />• Known for high performance on benchmarks, fast response times, and efficient processing<br />• Enabling DeepSeek on a Workspace requires reaching out to Dust
</Update>

<Update label="December 30th, 2024" tags={["Added"]}>
  ## 🚫 New option to skip storage of Dust app execution logs

  * Added ability to disable storage of execution logs for custom Dust apps
  * When enabled, the app will not store inputs and outputs of blocks in the database
  * Only affects custom Dust apps (conversation agents are not impacted)
</Update>

<Update label="December 19th, 2024" tags={["Added"]}>
  ## ⚡️ Faster conversation page loading

  • Improved assistant loading time for quicker auto-complete availability<br />• Simplified input bar animation for smoother transitions
</Update>

<Update label="December 19th, 2024" tags={["Added"]}>
  ## 📚 New Dust Enterprise Rollout Guide

  • Added detailed documentation to help deploy Dust within organizations<br />• Introduced resources including webinar registration and community access<br />• Created step-by-step guidelines for successful enterprise implementation

  [Read more](/docs/user-documentation/getting-started/dust-rollout-guide/index)
</Update>

<Update label="December 18th, 2024" tags={["Added"]}>
  ## 🎙️ Added support for Modjo transcripts processing

  * Process and store transcripts from Modjo conversations
  * Support for both individual and company-wide transcript processing
</Update>

<Update label="December 16th, 2024" tags={["Added"]}>
  ## 🎯 Zendesk integration now available publicly

  * Sync your Zendesk Help Center articles and tickets histories directly into Dust
  * Search across past support conversations and Help Center articles to find relevant solutions
  * Manage your Zendesk connection with granularity in Connection Admin
  * Check out the docs at [/docs/user-documentation/admins/connections-management/zendesk](/docs/user-documentation/admins/connections-management/zendesk)
</Update>

<Update label="December 5th, 2024" tags={["Added"]}>
  ## 💾 Prompt version history

  • Added ability to recover previous assistant instructions<br />• Each version of a prompt is now saved and accessible
</Update>

<Update label="December 3rd, 2024" tags={["Added"]}>
  ## 🧩 Chrome Extension Now Available on Chrome Web Store

  • Official Dust Chrome extension released on Chrome Web Store<br />• Share webpage content directly in Dust conversations<br />• Access Dust features while browsing

  <br />

  [▶️ Integrating Dust into your Customer Support flow](https://www.youtube.com/watch?v=UC9B4l8FMTc)
</Update>

<Update label="December 3rd, 2024" tags={["Added"]}>
  ## 🔐 SAML SSO Authentication Support

  * Added SAML SSO authentication method
  * Compatible with most Identity Providers (IdPs)
</Update>

<Update label="November 28th, 2024" tags={["Added"]}>
  ## 🎫 New Zendesk connection

  * Sync your Zendesk Help Center articles and tickets histories directly into Dust
  * Search across past support conversations and Help Center articles to find relevant solutions
  * Manage your Zendesk connection with granularity in Connection Admin
  * Check out the docs at [/docs/user-documentation/admins/connections-management/zendesk](/docs/user-documentation/admins/connections-management/zendesk)
</Update>

<Update label="November 27th, 2024" tags={["Improved"]}>
  ## 📄 Enhanced document upload capabilities

  * Added support for more file extensions, including .docx files
  * Improved error handling during file upload
  * Refreshed upload interface design
</Update>

<Update label="November 27th, 2024" tags={["Added"]}>
  ## 👍 New feedback system with thumbs up/down reactions

  * Introduced a new feedback system allowing users to rate assistant responses
  * Added thumbs up/down reactions to replace previous emoji reactions
  * Implemented a dialog box for providing additional context when giving feedback
  * Feedback data available through the workspace-usage API
</Update>

<Update label="November 27th, 2024" tags={["Added"]}>
  ## 🔄 New PagerDuty Schedule Import Script

  * Added a new script to import PagerDuty schedules into Dust
  * Available in dust-labs repository
</Update>

<Update label="November 20th, 2024" tags={["Added"]}>
  ## 🔍 Code inspection for visualizations

  * Added a new button to visualizations allowing users to view the underlying code
  * Enables direct access to visualization implementation details
</Update>

<Update label="November 15th, 2024" tags={["Improved"]}>
  ## 🚀 Enhanced Raycast Extension with New Features

  * Added sign-in functionality with Dust account credentials
  * Removed workspace key requirement
  * Added ability to list all assistants
  * Introduced favorites management (add/remove assistants)
  * Updated to latest API implementation

  [Read more](/docs/user-documentation/agents/integrations/raycast-extension)
</Update>

<Update label="November 13th, 2024" tags={["Added"]}>
  ## 🎨 Visualization and web search features enabled in assistants

  • Visualization feature automatically enabled for new assistants<br />• Web search capability added to raw model assistants (except anthropic models)<br />• Visualization support added to raw model assistants
</Update>

<Update label="November 13th, 2024" tags={["Improved"]}>
  ## 🔄 Enhanced Zendesk Integration

  * Added assistant descriptions for better context
  * Introduced ability to restrict available assistants
  * Added option to hide sensitive information
</Update>

<Update label="November 13th, 2024" tags={["Added"]}>
  ## 📊 Added CSV support and export in Visualization

  * Support for parsing and loading CSV files in Visualization
  * Added ability to download processed data as CSV files
  * Full data transformation capabilities including merging, computed columns and transformations
</Update>

<Update label="November 12th, 2024" tags={["Added"]}>
  ## 🔒 Private Slack channels indexing (available on request)

  * On request to the Dust team, private Slack channels can now be indexed when the Dust bot is invited
  * Admins can see and select private channels in the sync interface
  * Clear labeling of private channels in the admin interface
  * Safety confirmations when adding private channels to spaces
</Update>

<Update label="November 12th, 2024" tags={["Improved"]}>
  ## 🔄 'Most Recent Data' Tool Renamed to 'Include Data'

  * Tool renamed to 'Include Data' for better clarity
  * Timeframe configuration is now optional and disabled by default
  * Documents can be included in their entirety when they fit within context window
</Update>

<Update label="November 10th, 2024" tags={["Improved"]}>
  ## 🎨 Enhanced UI Design System

  * Upgraded core UI components for better accessibility
  * Improved visual consistency across the platform
  * Implemented more sophisticated document-centric interface elements
</Update>

<Update label="November 7th, 2024" tags={["Improved"]}>
  ## 🔍 Enhanced Extract Tool with Improved Context Awareness

  * Completely revamped extraction pipeline for better data analysis
  * Added conversation context awareness for more precise extractions
  * Expanded capability to identify and extract more data points
  * Increased overall accuracy of extraction results
</Update>

<Update label="November 5th, 2024" tags={["Improved"]}>
  ## 🤖 Claude 3.5 Haiku Integration

  * Added support for Claude 3.5 Haiku model
  * Upgraded all existing Claude Haiku assistants to version 3.5
</Update>

<Update label="October 29th, 2024" tags={["Added"]}>
  ## 💾 Store Google Meet and Gong Meeting Transcripts

  * Meeting transcripts from Google Meet and Gong can now be stored in Dust Folders
  * Transcript storage can be enabled independently from transcript processing
  * Stored transcripts can be accessed and used within Dust workspaces
</Update>

<Update label="October 28th, 2024" tags={["Improved"]}>
  ## 🔄 New Google Sheets Integration with Sidebar

  * Completely redesigned Google Sheets integration now appears in a sidebar
  * Improved performance and reliability of the `DUST()` function
</Update>

<Update label="October 25th, 2024" tags={["Improved"]}>
  ## 🤖 Updated Claude 3.5 Sonnet model version

  Upgraded all assistants using Claude 3.5 Sonnet to the latest model version (20241022)
</Update>

<Update label="October 23rd, 2024" tags={["Added"]}>
  ## 🚀 Spaces: Enhanced Data Management

  * Introduced Spaces to organize and share data within workspaces
  * Spaces can be open (accessible to all) or restricted (limited access)
  * Pro plans get one additional space beyond the default 'Company Data' space
  * [Documentation](/docs/user-documentation/admins/spaces-management)
</Update>

<Update label="October 21st, 2024" tags={["Added"]}>
  ## 🌨️ Snowflake Integration: Connect and Query Your Data

  • Add Snowflake data warehouses as connections in Dust<br />• Add Snowflake tables to vaults<br />• Query Snowflake tables using Tables Query feature in assistants and Dust apps
</Update>

<Update label="October 18th, 2024" tags={["Added"]}>
  ## 🚨 Dust Incidents Now Visible in UI

  * Dust-specific incidents are now displayed directly in the user interface
  * Incidents are shown in the same manner as provider incidents
</Update>

<Update label="October 17th, 2024" tags={["Added"]}>
  ## ⭐️ Add Assistant to Favorites

  * Add ability to mark assistants as favorites
  * New tab to view favorite assistants
  * Favorite assistants appear first in sort order
  * New button bar in assistant details modal for quick actions
</Update>

<Update label="October 10th, 2024" tags={["Improved"]}>
  ## 📊 Tables Query outputs now available as file attachments

  • Query results are accessible by the model as a file<br />• Supports larger datasets without manual data input<br />• Allows retrieval of more than 128 rows from tables<br />• Enables generation of charts with numerous data points directly from database
</Update>

<Update label="October 10th, 2024" tags={["Improved"]}>
  ## 🚀 Slack Integration Enhancements

  * Shorter, clearer responses
  * Added links to relevant documentation
  * Introduced ability to choose from the 10 most popular assistants directly in Slack
</Update>

<Update label="October 10th, 2024" tags={["Improved"]}>
  ## 📚 Updated Documentation and Video Guides for Data Management

  ➡️ Connect Data to Dust: [/docs/user-documentation/data-sources/connections](/docs/user-documentation/data-sources/connections)<br />➡️ Manage Data on Dust (Company Data vs Vaults): [/docs/user-documentation/admins/spaces-management](/docs/user-documentation/admins/spaces-management)<br />➡️ Adding data to a vault as an admin: [/docs/user-documentation/admins/spaces-management#how-to-add-data-to-a-vault](/docs/user-documentation/admins/spaces-management#how-to-add-data-to-a-vault)
</Update>

<Update label="October 8th, 2024" tags={["Added"]}>
  ## 📘 OpenAPI definition and Postman collection now available

  * Added OpenAPI definition for easy integration with developer tools
  * Released public Postman collection for quick API exploration
  * Accessible here: [OpenAPI and Postman](https://docs.dust.tt/reference/openapi)
</Update>

<Update label="October 4th, 2024" tags={["Improved"]}>
  ## 📁 Enhanced Folder Naming Flexibility

  • Expanded character support for folder names<br />• Now accepts any valid UTF-8 character<br />• Improved user experience in folder creation and management
</Update>

<Update label="September 26th, 2024" tags={["Added"]}>
  ## 📸 Download Visualizations

  * Added a download button that appears when hovering over visualizations
  * Allows users to save visualization outputs for use elsewhere
</Update>

<Update label="September 24th, 2024" tags={["Improved"]}>
  ## 🔍 Improved Data Source Exploration

  * Added a file explorer interface in the 'Data Sources' tab
  * All users can now browse company data sources
  * Simplified connection management
</Update>

<Update label="September 18th, 2024" tags={["Added"]}>
  ## 🗑️ Multi-select and bulk delete conversations

  * Added 'edit mode' accessible via new '...' button next to 'New Conversation' in sidebar
  * Ability to select multiple conversations simultaneously
  * Option to delete selected conversations in bulk
  * New feature to delete entire conversation history with one click
</Update>

<Update label="September 12th, 2024" tags={["Added"]}>
  ## 🧪 Zendesk Knowledge Base Import Tool

  * New script available to import articles from a Zendesk knowledge base into a Dust datasource
  * Easily transfer all articles from Zendesk to Dust
  * Script can be run using `npm run articles` in the Dust-labs repository here: [https://github.com/dust-tt/dust-labs/tree/main/zendesk](https://github.com/dust-tt/dust-labs/tree/main/zendesk)
</Update>

<Update label="September 10th, 2024" tags={["Removed"]}>
  ## 🔒 Removal of public Dust apps

  * Removed the concept of public Dust apps
  * All apps are now private by default and only usable within a workspace
  * Improved safety and standardized workspace segregation checks for all endpoints
  * Removed clone operations for apps
</Update>

<Update label="September 6th, 2024" tags={["Added"]}>
  ## 🔗 Make.com Integration Added

  • Dust is now available as an integration on Make.com<br />• Users can incorporate Dust functionalities into their Make.com scenarios<br />• Enables creation of automated workflows using Dust capabilities<br />• Documentation available here: [Make.com: Trigger Dust assistants from any scenario](/docs/user-documentation/agents/integrations/make-com)
</Update>

<Update label="September 4th, 2024" tags={["Added"]}>
  ## 🧪 \[Dust Labs] Hubspot Companies to Dust Datasource Exporter

  * New script available in dust-labs repository: [https://github.com/dust-tt/dust-labs/tree/main/hubspot](https://github.com/dust-tt/dust-labs/tree/main/hubspot)
  * Allows exporting Hubspot company data
  * Enables importing exported data into a Dust Datasource
</Update>

<Update label="September 4th, 2024" tags={["Improved"]}>
  ## 🔍 Improved search accuracy for specific data sources

  * Improved precision when searching within individual data sources (e.g., Notion, Slack)
  * Users can now get more relevant results when querying information from a particular source
</Update>

<Update label="August 30th, 2024" tags={["Added"]}>
  ## 🎙️ New Gong Transcripts Exporter for Dust

  * Added a script to export Gong transcripts
  * Enables importing Gong transcripts into a Dust Datasource
  * Script available in the dust-labs GitHub repository: [https://github.com/dust-tt/dust-labs/tree/main/gong](https://github.com/dust-tt/dust-labs/tree/main/gong)
</Update>

<Update label="August 29th, 2024" tags={["Added"]}>
  ## 🔗 New Microsoft SharePoint Connector

  • Added a new datasource connector for Microsoft SharePoint<br />• Enables indexing of various document types including docs, spreadsheets, PowerPoint presentations, and PDFs from Microsoft drives<br />• Now available for all users
</Update>

<Update label="August 27th, 2024" tags={["Added"]}>
  ## 🤖 New Zapier action to interact with Dust assistants

  * Added a new Zapier action that allows users to communicate with Dust assistants
  * Enables integration of Dust assistants with other Zapier-supported tools and workflows
</Update>

<Update label="August 27th, 2024" tags={["Added"]}>
  ## 🚀 Dust for Google Spreadsheets (Beta)

  * Introduced a beta integration of Dust with Google Spreadsheets
  * Users can now interact with Dust assistants directly from spreadsheet cells
  * Installation guide available for easy setup
  * Adds AI support to your spreadsheets
  * Particularly useful for tasks requiring an assistant run per row
  * Exclusively available to Enterprise customers
</Update>

<Update label="August 21st, 2024">
  ## 🧪 \[Dust Labs] Jira Issues To Dust Import Script

  * Added a pre-made script to import updated issues from Jira to Dust
  * Script available in the dust-labs GitHub repository
  * Allows for regular updates of Jira data in Dust
  * Available here: [https://github.com/dust-tt/dust-labs/tree/main/jira](https://github.com/dust-tt/dust-labs/tree/main/jira)
</Update>

<Update label="August 19th, 2024">
  ## 🧪 \[Dust Labs] Salesforce Accounts To Dust Import Script

  * Added a pre-made script for importing updated account summaries from Salesforce to Dust
  * Supports both OAuth and username/password/security-key authentication methods
  * Enables regular and automated data imports from Salesforce
  * Available here: [https://github.com/dust-tt/dust-labs/tree/main/salesforce](https://github.com/dust-tt/dust-labs/tree/main/salesforce)
</Update>

<Update label="August 13th, 2024" tags={["Added"]}>
  ## 🚀 Provider Status Page Updates

  * Added ability to display incident banners in the app for provider disruptions
  * Status page can now be updated to show real-time information about provider issues
</Update>

<Update label="August 2nd, 2024" tags={["Added"]}>
  ## 🎨 Data Visualization with React Components

  * Assistants can now generate visual elements using code
  * These visualizations are rendered directly in the conversation UI
  * Enables the creation of graphs and charts for data analysis
  * Feature can be toggled for any assistant via the assistant builder tools screen
</Update>

<Update label="July 26th, 2024" tags={["Added"]}>
  ## 🔐 Microsoft Entra ID SSO now available

  • Implemented Single Sign-On (SSO) support for Microsoft Entra ID<br />• Enabled upon request for Enterprise customers
</Update>

<Update label="July 26th, 2024" tags={["Added"]}>
  ## 🔌 Microsoft SharePoint Connector (Beta)

  * Added a new datasource connector for Microsoft SharePoint
  * Enables indexing of various file types including documents, spreadsheets, presentations, and PDFs from Microsoft drives
  * Currently available as a beta feature
</Update>

<Update label="July 23rd, 2024" tags={["Added"]}>
  ## 🚀 GPT4o mini model now available in assistant builder

  • Added support for the new GPT4o mini model<br />• Users can now select and utilize this model when creating assistants
</Update>

<Update label="July 22nd, 2024" tags={["Removed"]}>
  ## 🔥 Nango dependency removed from connectors

  * Completely eliminated Nango as a dependency from the connectors codebase
  * Implemented a new OAuth service to handle authentication
  * Migrated all connector code to be Nango-free
</Update>

<Update label="July 18th, 2024" tags={["Added"]}>
  ## 🖼️ Vision Capabilities Added to Anthropic Models

  • Integrated support for Anthropic's vision models<br />• All three Anthropic models now support vision capabilities<br />• This feature is accessible to all users
</Update>

<Update label="July 8th, 2024" tags={["Improved"]}>
  ## 🚀 Drag-and-Drop File Support in Conversations

  • Added drag-and-drop functionality for files in the conversation view<br />• Supported file formats include JPEG, PNG, and PDF<br />• Simplifies sharing files within conversations
</Update>

<Update label="July 4th, 2024" tags={["Added"]}>
  ## 🖼️ Vision Support Added to the App

  • Integrated Vision capability for OpenAI's gpt-4 and gpt-4-turbo models/assistants<br />• Supports JPEG and PNG image formats<br />• Available for all users to explore and use
</Update>

<Update label="July 3rd, 2024" tags={["Improved"]}>
  ## 📊 Workspace Metrics: Monthly Reports Now Available

  • Introduced downloadable monthly reports as a zip file<br />• Reports include four CSV files:

  * Messages: List of user and agent messages
  * Users: User activity levels
  * Builders: Individuals editing assistants
  * Assistants: List and usage statistics
</Update>

<Update label="July 2nd, 2024" tags={["Improved"]}>
  ## 🎨 Emoji Suggestions for New Assistants

  * Automatically suggest an appropriate emoji based on the assistant's instructions when creating a new assistant
  * Suggested emoji serves as the assistant's icon
  * Replaces previous default of assigning a random avatar from the Droids & Spirits library
  * Users can still edit and choose any other avatar
</Update>

<Update label="July 1st, 2024" tags={["Fixed"]}>
  ## 🔢 LaTeX Equations Now Supported in Agent Messages

  • Added support for LaTeX equations in agent messages<br />• Useful for mathematical and scientific communication
</Update>

<Update label="July 1st, 2024" tags={["Deprecated"]}>
  ## Removal of @github, @notion and @slack global assistants

  We have removed the generic assistants @slack and @notion because of their lack of usage on the platform.

  If you were using them, you can use the **@dust** general assistant in the exact same way by asking it to search in slack, notion or github
</Update>

<Update label="June 26th, 2024" tags={["Added"]}>
  ## Product Update 4

  * Multi-Tool assistants
  * Enhanced Model Capabilities
  * Dust Tool: Extract Data
  * Dust Tool: Web Navigation
  * Support for Microsoft Office Files
  * Zapier Integration (Beta)
  * Multi-File Uploads in Chat
  * Customizable Model Provider Settings
  * Enhanced Login Options
  * Improved Member Management
  * And more

  Full updates descriptions: [https://blog.dust.tt/dust-product-update-4/](https://blog.dust.tt/dust-product-update-4/)
</Update>

<Update label="June 24th, 2024" tags={["Improved"]}>
  ## New documentation & developer platform

  The documentation was fully refreshed and merged with our developer platform

  * API reference
  * User guides
  * Changelog
  * Discussions
</Update>

<Update label="May 21st, 2024" tags={["Added"]}>
  ## Product update 3

  * Updated GPT-4 Model to GPT4o
  * Assistant Templates Gallery
  * Suggested Instructions when Building Assistants
  * Multi-File Uploads in the Input Bar
  * Developer secrets
  * Add Dust Assistants to Your Slack Workflow
  * More Flexibility for Intercom Connection
  * Dust Website Refresh
  * \[BETA] Create An Assistant to Process Large Amounts of Data
  * \[BETA] Google Meet Transcripts Summarization
  * And more

  Full updates descriptions: [https://blog.dust.tt/dust-product-update-3-gemini-gpt4o-templates/](https://blog.dust.tt/dust-product-update-3-gemini-gpt4o-templates/)
</Update>

<Update label="April 18th, 2024" tags={["Added"]}>
  ## Product update 2

  * Gemini 1.5 pro
  * SOC2 Type II Compliance Achieved
  * Multi-File Upload for Folders
  * Simplified Data Source Selection
  * Dust can be used in Slack workflows
  * Mermaid Diagrams Support
  * And more

  Full updates at: [https://blog.dust.tt/dust-product-update-2/](https://blog.dust.tt/dust-product-update-2/)
</Update>

<Update label="March 21st, 2024" tags={["Added"]}>
  ## Product update 1

  * Mistral Large Now Available
  * New Cutting-Edge Models from Anthropic
  * Introducing Table Queries
  * Confluence Connection
  * Intercom Connection
  * Summon Assistants in Slack
  * Quick Start Guide
  * Dust Builders Sessions #1
  * And more
  * Full updates: [https://blog.dust.tt/dust-product-update-1/](https://blog.dust.tt/dust-product-update-1/)
</Update>
