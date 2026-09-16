> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Agent tools

> The full list of tools agents get through the Pods skill to work with Pods, conversations, tasks, files, and settings.

A core principle of Pods: **everything a human can do, an agent can do**. This is made possible by the **Pods skill**, which is available to all agents by default, including the global Dust agent, agents invoked inside a Pod, and triggered agents. The Pods skill provides a set of **tools**: the individual actions listed on this page.

<Info>
  **A note on naming.** You may hear these referred to as "Pod tools". The precise naming: agents have one **Pods skill**, and that skill provides the **tools** below. Each individual action, such as `create_tasks`, is a tool.
</Info>

There is nothing to enable or configure: when an agent works in or around a Pod, it picks the right tool on its own. The tool names below are the ones shown in the agent's tool execution details during a run, so you can also use this page to follow what an agent did.

## Pod management

### Finding and creating Pods

| Tool               | What it does                                                                                         |
| ------------------ | ---------------------------------------------------------------------------------------------------- |
| `list_pods`        | List the Pods the agent can access: the user's Pods by default, or all Open Pods in the workspace    |
| `create_pod`       | Create a new Pod (Restricted by default), optionally with initial members and a set of starter tasks |
| `get_information`  | Read a Pod's metadata: URL, title, description, visibility, pinned MiniApp, and linked Company Data    |
| `edit_information` | Update a Pod's title, description, or visibility (Open or Restricted)                                |

### Members

| Tool             | What it does                                                    |
| ---------------- | --------------------------------------------------------------- |
| `list_members`   | List everyone in the Pod with their role (Member or Editor)     |
| `update_members` | Invite, add, remove, promote, or demote Pod members and Editors |

### Conversations

| Tool                          | What it does                                                                        |
| ----------------------------- | ----------------------------------------------------------------------------------- |
| `create_conversation`         | Start a new conversation in the Pod, optionally triggering another agent on a task  |
| `add_message_to_conversation` | Post a follow-up message to an existing Pod conversation                            |
| `list_conversations`          | List recent Pod conversations, optionally unread ones only or with full transcripts |
| `move_conversation`           | Move a conversation into a Pod, or out of a Pod back to personal conversations      |

### Knowledge

| Tool                        | What it does                                                                       |
| --------------------------- | ---------------------------------------------------------------------------------- |
| `semantic_search`           | Search Pod files, linked Company Data, and Pod conversation transcripts by meaning |
| `retrieve_recent_documents` | Fetch the most recently added or updated documents in the Pod's knowledge          |
| `add_content_node`          | Link a document or folder from Company Data to the Pod's knowledge                 |
| `remove_content_node`       | Unlink a Company Data reference from the Pod                                       |

### Pod settings

| Tool                | What it does                                                                                    |
| ------------------- | ----------------------------------------------------------------------------------------------- |
| `set_pinned_frame`  | Pin a [MiniApp](/docs/user-documentation/pods/frames) as the Pod banner, or unpin the current one |
| `set_default_agent` | Set or reset the agent that handles new conversations started in the Pod                        |

## Tasks

| Tool               | What it does                                                                                          |
| ------------------ | ----------------------------------------------------------------------------------------------------- |
| `list_tasks`       | List the Pod's tasks, filtered by assignee (mine or all) and status (open, done, or all)              |
| `create_tasks`     | Create up to 30 tasks at once, assigned to a Pod member or left unassigned                            |
| `update_tasks`     | Update task descriptions, assignees, and states, including marking tasks done                         |
| `start_task_agent` | Start an agent on an open task: creates the linked conversation and moves the task to **In progress** |

See [Tasks](/docs/user-documentation/pods/tasks) for how these show up in the Tasks tab, including syncing with external tools like Jira, Asana, or Linear.

## Files

Agents work with Pod files through Dust's shared file system tools rather than Pod-specific tools. Inside a Pod, these let an agent:

* List and browse the Pod's files and folders
* Read file contents
* Create new files, including agent-generated artifacts such as [MiniApps](/docs/user-documentation/pods/frames)
* Edit, copy, move, and delete existing files
* Import a file into the Pod from a URL

Files created or updated by agents appear in the [Files tab](/docs/user-documentation/pods/files) and are immediately available to all Pod members and other agents.

## Permissions

Agent tools follow the same permission model as the Dust interface: an agent acting on behalf of a user can only do what that user could do themselves.

* A Restricted Pod the user is not a member of is not accessible to their agents
* Managing membership, settings, visibility, and the pinned MiniApp requires the user to be a Pod **Editor**

See [Members and roles](/docs/user-documentation/pods/members-and-roles) for the full role breakdown, and [Admin controls](/docs/user-documentation/pods/admin-controls) for workspace-level policies.

## See it in action

These tools are what make Pods a natural target for automations: a triggered agent can post a daily brief into a Pod, open a conversation when a ticket arrives, or keep Pod tasks in sync with an external tool.

* [Conversations](/docs/user-documentation/pods/conversations) and [Tasks](/docs/user-documentation/pods/tasks): concrete patterns
* Examples: [Ticket handling and support knowledge](/docs/user-documentation/pods/examples/ticket-handling-and-support-knowledge), [One Pod per customer](/docs/user-documentation/pods/examples/one-pod-per-customer), [Competitive intelligence](/docs/user-documentation/pods/examples/competitive-intelligence)
