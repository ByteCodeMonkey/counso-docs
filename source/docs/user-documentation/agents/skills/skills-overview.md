> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

> Reusable packages of instructions, knowledge, and tools you can share across multiple agents.

## What are Skills

Skills are reusable packages of instructions, knowledge and tools that you can share across multiple agents. Think of them as specialized toolboxes that contain the knowledge and capabilities needed for specific tasks or domains.

Dust comes with default skills, but you can also create your own. Check out our [examples](/docs/user-documentation/agents/skills/skill-examples).

| Skill name                                         | What the agent will be able to do                                                                                                                                                                            |
| :------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Discover Knowledge                                 | Search across all your company documents and data warehouses to surface the information you need without manual configuration.                                                                               |
| Discover Tools                                     | Automatically discover and use specialized tools as needed. Extend your agent's capabilities on-demand without manual configuration.                                                                         |
| [Go Deep](/docs/user-documentation/agents/go-deep) | Hand off complex tasks to the @deep-dive agent for comprehensive analysis. With one click, you enable your agent to delegate deep research questions while preserving your agent's context and instructions. |
| MiniApp sharing                                      | Turn insights into interactive dashboards and presentations your team can explore, customize, and share. Living documents that adapt to different stakeholders.                                              |
| Your own custom skill                              | Your own company-specific custom reusable set of instructions and tools.                                                                                                                                     |

## When to create a skill

* Create a skill to share instructions and tools across multiple agents.
* Create a skill when your agent instructions are getting overly long and/or you want to move specialized knowledge into a reusable package to share with your team.
* Create a skill to define standard ways of doing things in your organization.

Skills are shareable: when you update a skill's instructions, every agent using that skill automatically gets the improvement. It's a way to create a single source of truth for how certain things should be done.

## Creating a skill

<Note>
  Skill creation and editing is reserved to Builders and Admins. Any user can leverage existing skills. Builders are therefore responsible for making great skills to share with the company!
</Note>

**Name and description:** A clear name and description that helps users understand what the skill does and what it can be used for.

**What will this skill be used for:** Indications that will be used by the agent to determine when to enable the skill.

**What guidelines should it provide:** Actual content of the skill — instructions that explain how to perform specific tasks, which tools or skills to use and how to use them, and document any company-specific processes or conventions.

<Tip>
  You can reference MCP tools directly inside a skill's instructions. This gives the agent access to specific tools when the skill is active, and allows you to give context on how and when to use them.

  **How to add a tool inline:**

  Type `/` anywhere in the instructions editor. A dropdown will appear letting you search for a tool by name. Select the one you want to reference, and it will be inserted as a chip at the cursor position. Alternatively, click the **Add capabilities** button to open the same dropdown.

  A summary of all referenced items is displayed in a read-only section at the bottom of the skill editor.
</Tip>

<Tip>
  Skills can reference other skills inside their instructions. This lets you build modular workflows: a high-level skill delegates specific steps to lower-level ones, and the agent knows when to activate each of them.

  **How to add a skill inline:**

  Type `/` or click **Add capabilities**, then select an existing skill from the dropdown. It will appear as a chip in the instructions.

  **How it works at runtime:**

  When a skill references sub-skills, those sub-skills are automatically surfaced to the agent as available capabilities. The agent then decides when to enable them based on context and your instructions. Be explicit in your instructions about when the sub-skill should be invoked. For example:

  > "Before generating the account brief, use the \[Sales Validation] skill to confirm the deal context."

  **Why this is useful:**

  * Break complex skills into smaller, reusable units instead of one long monolithic instruction set.
  * Avoid duplicating instructions across skills: define a primitive once and reference it from multiple parent skills.
  * Keep each skill focused and easier to maintain.
  * Allow for progressive discovery: break a large skill into coherent units so each situation only loads what it needs.
</Tip>

<Note>
  You can reference knowledge such as Notion pages, Google Drive documents, or Confluence pages naturally in your instructions by pressing `/` or clicking the **Attach knowledge** button. This opens a search bar where you can search content by title, or paste a URL directly.

  When you add knowledge to a skill, agents using that skill automatically get the ability to search and browse that knowledge.
</Note>

### Creating a customized version of a global skill

Global skills are pre-built skills provided by Dust that cover common use cases. You can customize a global skill to adapt it to your organization's specific needs while keeping its core functionality.

For instance, you can customize the MiniApp sharing skill to add your own branding guidelines, reference specific assets, or define preferred layout types.

To extend a global skill, go to **Manage Skills**, find the global skill you want to customize, click the **...** menu, and select **Customize skill**. This creates a new skill based on the global one, where you can add your own instructions, attach specific knowledge, or include additional tools. The customized skill will be labeled as "Based on \[original skill name]". Any updates you make to your extended skill won't affect the original global skill, and other teams can create their own extensions independently.

<Note>
  To share a direct link to a skill, open **Manage Skills**, select the skill, and click **Copy link**. The link opens the **Manage Skills** page, focused on that skill.
</Note>

## How agents use skills

You can add skills to your agents in the Agent Builder. Select specific skills to add to your agent. The agent will rely on those skills to perform complex tasks and achieve the goal defined in the agent's instructions or in your questions.

<Note>
  The agent will decide to enable a skill by analyzing the current situation. Skills that are not relevant will not be loaded, optimizing the context exposed to the agent at a given time.
</Note>

## Managing access to skills

Both data access (what data the skill can use) and user access (who can use the skill) are handled through [Spaces](/docs/user-documentation/admins/spaces-management).

When you create a skill, the skill may rely on resources from specific spaces — e.g. a Notion page in the Product space, Zendesk tickets in the Customer Success space. To ensure data is only accessible to those who have access to the same spaces, the skill is scoped to a set of spaces required to use it. An agent can only use a skill if it has access to every space required by that skill.

This relationship is live: any update to a skill's space requirements is immediately reflected in the agents that use it.

**Editors:** You designate who can edit the skill. Editors can modify the skill's instructions, tools, and settings.

Workspace admins can open any skill in the Skill Builder even if they are not editors — the builder opens in view-only mode. To make changes, admins can click **Become an editor** to add themselves to the editors list.

## Keeping track of a skill's evolution

Skills are versioned. In the Skill Builder, the **history** button in the Guidelines section lets you list all past versions with their date and author. Clicking on a version shows the changes made since then, making it easy to track additions and deletions.

## Getting started

Identify a few processes that could be turned into Skills. Good candidates are recurring processes that need to be documented, or sets of guidelines often required for agents to work well. Turn them into a skill, add the skill to your agents, and tweak it as needed — you only need to change it once to keep all linked agents up-to-date.

Over time, you'll build a library of skills that will make creating new agents faster and more consistent.

***

## FAQ

**Who can create and edit skills?**

Builders can create and edit skills. Ask an admin to bump your role if you want to get creative and unlock value for your co-workers.

**Who can view and use skills?**

Anyone in your workspace can view and use skills, provided they have access to every underlying resource (tools and knowledge).

**How do I add knowledge to a skill?**

In the Skill Builder, add knowledge references inline in the guidelines. Start typing, then press `/` or click the **Attach knowledge** button to search for content by title. Pasting a URL is also supported.

**What does this change for MiniApp sharing and Go deep?**

MiniApp sharing and Go deep are now available as skills instead of tools. This change is retro-compatible for existing agents. The main benefit is that you can now customize them — for instance, add your own branding guidelines to the MiniApp sharing skill.

A more subtle change: the skill loads dynamically, keeping the context lighter for the agent when not needed, making it more focused and less prone to hallucinations.

<Warning>
  This change will cause existing agents to be less prone to create MiniApps. Agents used to have a strong tendency to create MiniApps as long as the tool was added, even when it was not called for. You may need to update agent instructions accordingly.
</Warning>

**Do I need to rewrite all my agent instructions?**

No. Existing agents will continue to work exactly as before. Build Skills and replace redundant agent instructions gradually, as you iterate and standardize your agent library.

**What is the relationship between Dust Skills and Anthropic/Claude Skills?**

They are a similar concept applied in different products: both represent a reusable bundle of instructions and best practices to perform a task. We recommend checking out [Anthropic skills](https://github.com/anthropics/skills) for inspiration.

**When should I use a Skill or a sub-agent?**

Use Skills to share reusable expertise (instructions + tools) across multiple agents — they compose seamlessly and update everywhere when changed. Use sub-agents only when you need true context isolation (e.g. heavy independent research). Skills is the default choice for sharing sets of guidelines across multiple agents, as sub-agents introduce prompting coordination overhead.

**How do I know whether a skill was used for a message?**

In your conversation, click the "Completed in N sec" message to open the details panel. At the bottom you will find a summary and a list of the skills that were loaded and exposed to the agent for that message.
