# What Agents can do in a Pod

Agents use the **Pods skill** to work with Pods, conversations, knowledge, tasks, and Pod settings. This skill is available to all Agents by default; there is nothing to enable separately. The available tools are shown in an Agent's tool execution details.

## Pod tools

| Work area | Tool | What it does |
|---|---|---|
| Pods | `list_pods` | Lists Pods the Agent can access: the user's Pods by default, or all Open Pods in the workspace. |
| Pods | `create_pod` | Creates a Pod, Restricted by default, optionally with initial members and starter tasks. |
| Pod details | `get_information` | Reads the Pod URL, title, description, visibility, pinned Frame, and linked Company Data. |
| Pod details | `edit_information` | Updates the Pod title, description, or visibility. |
| Members | `list_members` | Lists Pod members and their Member or Editor role. |
| Members | `update_members` | Invites, adds, removes, promotes, or demotes Pod members and Editors. |
| Conversations | `create_conversation` | Starts a conversation in the Pod, optionally triggering an Agent for a task. |
| Conversations | `add_message_to_conversation` | Adds a message to an existing Pod conversation. |
| Conversations | `list_conversations` | Lists recent conversations, optionally unread-only or with full transcripts. |
| Conversations | `move_conversation` | Moves a conversation into a Pod or back to personal conversations. |
| Knowledge | `semantic_search` | Searches Pod files, linked Company Data, and Pod conversation transcripts by meaning. |
| Knowledge | `retrieve_recent_documents` | Retrieves the most recently added or updated documents in Pod knowledge. |
| Knowledge | `add_content_node` | Links a document or folder from Company Data to Pod knowledge. |
| Knowledge | `remove_content_node` | Removes a Company Data reference from the Pod. |
| Pod settings | `set_pinned_frame` | Pins a Frame as the Pod banner or unpins the current Frame. |
| Pod settings | `set_default_agent` | Sets or resets the Agent used for new Pod conversations. |
| Tasks | `list_tasks` | Lists tasks by assignee (mine or all) and status (open, done, or all). |
| Tasks | `create_tasks` | Creates up to 30 tasks, assigned to a Pod member or left unassigned. |
| Tasks | `update_tasks` | Updates task descriptions, assignees, and states, including marking tasks done. |
| Tasks | `start_task_agent` | Starts an Agent on an open task, creates its linked conversation, and moves the task to **In progress**. |

Agents use shared file-system tools for Pod files rather than Pod-specific file tools. They can browse and read files, create files such as Frames, edit, copy, move, or delete files, and import a file from a URL. Files created or updated by an Agent appear in Files and are available to Pod members and other Agents.

## Permission boundaries

An Agent acts on behalf of a user and can do only what that user could do. It cannot access a Restricted Pod unless the user is a member. Managing membership, Pod settings, visibility, and the pinned Frame requires the user to be a Pod Editor. A tool appearing in the list does not override these access rules.
