---
title: "Control who can discover and use a Skill"
---
A Skill's availability setting controls who can find it from the composer or Agent Builder. It is separate from access to the data and tools that the Skill references. Check both when sharing a Skill.

## Availability choices

- **Editors only:** only Skill editors can find it in the composer and Agent Builder. This is useful while developing a Skill or keeping it for personal use. A non-editor may still use it when it is included in an Agent or another accessible Skill.
- **All members:** all workspace members can find and use it from the composer and Agent Builder. Changing to this setting requires **Manage skill availability** permission.
- **Members and agents:** members and Agents with **Discover Skills** can find and use it; Agents may activate it when it fits a request. This requires both **Manage skill availability** and **Make skills discoverable to agents** permissions.

## Restrict a Skill

Skills are not private by default. To limit access, associate the Skill with a restricted Pod. Only people and Agents who can access that Pod can use the Skill. Editors also need access to the restricted Pod to find and use it.

Before changing availability, review the Skill's attached Knowledge, Tools, and required Spaces. Making a Skill discoverable does not grant a person or Agent access to those resources. For automatic discovery, see [Discover Skills](/docs/user-documentation/agents/discover-skills).
