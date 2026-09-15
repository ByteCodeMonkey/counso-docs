> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Skill Availability

### Controlling skill availability

Skills have three availability settings:

**Editors only**

Only editors can find the skill via the composer and agent builder. Use this setting while developing a skill or when it is intended for personal use. A skill set to **Editors only** can still be used by non-editors if it has been added to an agent or a skill they can access.

**All members**

Everyone in your workspace can find and use the skill via the composer and agent builder. Use this setting when the skill is ready to share broadly with workspace members.

To use this setting, you need the **Manage skill availability** permission.

**Members and agents**

The skill is available to all workspace members and to agents that have [Discover Skills](/docs/user-documentation/agents/discover-skills) enabled (including @Dust). These agents can automatically enable the skill when they determine that it is relevant to a task.

Use this setting carefully. The skill may be enabled automatically by many agents, which can affect other workspace members' experience without their explicit action.

To use this setting, you need both the **Manage skill availability** permission and the **Make skills discoverable to agents** permission.

### How can I create a private skill?

Skills are not private by default. To restrict access, add a restricted Pod to the skill. Only people and agents with access to that Pod can view or use the skill. Note that editors also need access to the restricted Pod to find and use the skill.
