# Skills

A Skill is a reusable set of instructions, knowledge references, and capabilities for a recurring kind of work. Add a Skill to an Agent when you want the same procedure to be available to several Agents or when the main instructions have become too long. Workspace members can use available Skills; creating and editing them requires the appropriate Builder or administrator access.

## What a Skill contains

When creating a Skill, provide a **name and description**, explain **when the Agent should use it**, and write the **guidelines** it should follow. The guidelines can describe a process, company conventions, and which capabilities to use. Built-in Skills may cover document discovery, tool discovery, deeper research, or Frame creation; a custom Skill can capture a team-specific procedure. See [Skill examples](skill-examples.md) for patterns.

## Add tools or other Skills inline

In the instructions editor, type **/** to search for a Tool or Skill and insert it at the cursor. You can also choose **Add capabilities** to open the same picker. The inserted item appears as a chip, and the editor shows the referenced capabilities in a read-only list below the instructions.

A Skill can refer to smaller Skills to keep a larger workflow modular. Be explicit in the parent Skill about when the Agent should use each one. At run time, referenced Skills become available to the Agent; the Agent chooses whether to activate them based on the task and the guidance you wrote.

## Attach Knowledge

To give a Skill reference material, type **/** or choose **Attach knowledge** in the guidelines editor. Search by title or paste a supported content URL. Once attached, Agents using the Skill can search or browse that material, subject to the source's access rules.

## Customize a shared Skill

You can make an organization-specific version of an available global Skill without changing the original. In **Manage Skills**, open the Skill's **...** menu and choose **Customize skill**. In the new Skill, add your instructions, Knowledge, or capabilities. Its details identify the global Skill it was based on; your changes do not alter that original. Use **Copy link** from a Skill's page to share a link to it.

## Add a Skill to an Agent

In Agent Builder, select the Skills the Agent should use. The Agent considers the task and its instructions before enabling a Skill, so explain the situations in which it should be used. Adding a Skill does not bypass the Agent's access to its underlying Tools or Knowledge.

## Space access and editors

A Skill that depends on resources in particular Spaces is available only to Agents that can access every required Space. This keeps a Skill's data dependencies aligned with the Agent's access. If the Skill's required Spaces change, check the Agents that use it.

Choose the Skill's **Editors** to control who can change its instructions, capabilities, and settings. Workspace administrators can open a Skill in view-only mode; if they need to edit it, they can use **Become an editor** where that option is available.

## Review changes and usage

Skills keep a version history. In Skill Builder, open **history** in the Guidelines section to see earlier versions, dates, authors, and the changes in a selected version. Review this history when a shared procedure changes.

You can also review a Skill's usage record where the workspace provides it, to see how it is being used and help decide whether its guidance should be improved or retired.

## Getting started

Pick one recurring process, describe when it applies, and write the steps the Agent should follow. Attach only the Knowledge and capabilities needed for those steps. Try it with an Agent on a representative task, review the answer, then refine the Skill once for all linked Agents.

For access and discoverability, read [Skill availability](../skill-availability.md) and [Discover Skills](../discover-skills.md).
