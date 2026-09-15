> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Tasks

The **Tasks tab** is where work gets defined, assigned, and executed. Tasks are lightweight items that describe something that needs to happen. Any Pod member can create them, assign them, and start an agent on them. Agents can do the same: create tasks, start working on them, and mark them done, all without a human in the loop.

This reflects a core principle of Pods: **everything a human can do, an agent can do**. Agents interact with Tasks through the **Pods skill**, which is available to all agents by default. See [Agent tools](/docs/user-documentation/pods/agent-tools) for the full list of tools the skill provides.

## How to create a task

**As a human:**

1. Open the Pod and click the **Tasks** tab
2. Click **Add a task** and type a description
3. Optionally assign it to a Pod member using the assignee picker
4. Press **Enter** to save

**As an agent:**

Agents can create tasks directly in a Pod, for example after analysing a conversation, processing an incoming request, or as part of a larger workflow. Tasks created by agents appear in the same list and are treated identically to tasks created by humans.

Tasks are grouped by assignee. Unassigned tasks appear in their own section.

<Info>
  **Write task descriptions as clear, self-contained instructions: the agent will read the task text as its starting brief when it begins working.**

  **Task states**
</Info>

| State           | What it means                                                          |
| --------------- | ---------------------------------------------------------------------- |
| **Open**        | Task has been created but no one has started working on it yet         |
| **In progress** | An agent has been started on the task and a linked conversation exists |
| **Done**        | The task has been completed, by a human or an agent                    |

## How to start an agent on a task

**As a human:**

1. Hover over a task and click the \*\*\*\* (play) button
2. Optionally add a custom message or select a specific agent
3. Click **Start**. A conversation linked to the task is created and the task moves to **In progress**

**As an agent:**

Agents can start working on a task directly: picking it up, opening a linked conversation, and progressing it to **In progress** without any human trigger.

The linked conversation is visible in the Conversations tab. You can follow the agent's progress, step in, and redirect at any time.

## How to mark a task done

* **By a human:** click the checkbox next to the task; it moves to **Done** immediately
* **By an agent:** the agent can mark its own task done at the end of a conversation, with a short rationale explaining what was accomplished

Completed tasks remain visible with a strikethrough. They can be unchecked to reopen if needed.

## How to edit or delete a task

* **Edit text:** click directly on the task description to edit it inline, then press **Enter** to save
* **Reassign:** click the assignee avatar to change who the task is assigned to
* **Delete:** open the `...` menu on the task  **Delete task**; a confirmation is required

## Filtering and searching tasks

| Filter   | Shows                 |
| -------- | --------------------- |
| **Mine** | Tasks assigned to you |
| **All**  | Every task in the Pod |

The search bar filters tasks by description text in real time.

## Syncing tasks with an external tool

Tasks in a Pod can be kept in sync with external project management tools such as Jira, Asana, or Linear. This is done by setting up an agent with the relevant external tool (Jira, Asana, or Linear). The Pods skill is available by default.

**One-time import:**

Ask an agent to read your open issues or tasks from the external tool and create the corresponding tasks in the Pod:

1. Start a conversation in the Pod
2. Mention an agent that has the Jira / Asana / Linear tool enabled
3. Ask it to import your open items: *"Read all open Jira tickets assigned to this team and create a matching task in this Pod for each one"*
4. The agent creates the tasks, preserving the title, description, and assignee where possible

**Keeping tasks in sync with the wake-up tool:**

For ongoing sync, use the **wake-up tool** to schedule a recurring agent that runs at a set interval and reconciles the two systems:

* New items in the external tool  created as tasks in the Pod
* Tasks marked done in the Pod  closed or updated in the external tool
* Changes to titles or assignees in either direction can be propagated

Example prompt: *"Every weekday morning, check for new open Jira tickets in project XYZ and create a task in this Pod for any that don't already exist. Also check for tasks in this Pod that are marked done and close the corresponding Jira ticket. Use the wake-up tool to schedule this automatically."*

<Info>
  The sync agent can use the Pods skill by default to read and write Pod tasks. The relevant external tool (**Jira**, **Asana**, or **Linear**) must be available to the agent so it can read and write external issues.
</Info>

<Warning>
  Two-way sync requires careful instructions to avoid loops. Specify clearly which system is the source of truth for each type of change, or instruct the agent to only sync in one direction per run.
</Warning>
