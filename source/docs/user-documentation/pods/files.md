> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Files

The **Files tab** is the shared knowledge library of the Pod. It holds uploaded files, folders, and data linked from Company Data. Agents automatically use everything in it when working inside the Pod.

## How to add a file

**As a human:**

1. Open the Pod and click the **Files** tab
2. Click **Add** and select **Upload file**
3. Choose one or more files from your computer, or drag and drop them directly onto the tab

**As an agent:**

Agents can upload files to the Pod directly, for example to save a report, store a generated document, or persist output from a workflow. Files created by agents appear in the same list and are immediately available to all members and other agents. This is made possible by the **Pods skill**, which is available to all agents by default. See [Agent tools](/docs/user-documentation/pods/agent-tools) for the full list of tools the skill provides.

## How to organise files into folders

Files can be organised into folders to keep the Files tab structured as it grows.

**How to create a folder:**

1. Open the Pod and click the **Files** tab
2. Click **Add** and select **New folder**
3. Enter a folder name and confirm

Folders can be nested inside other folders. Navigate into a folder by clicking on it.

**How to move a file into a folder:**

* **Drag and drop**: drag any file or folder onto a destination folder to move it
* **Via the menu**: open the `...` menu on a file  **Move**, then select the destination folder

## How to link data from Company Data

1. Open the Pod and click the **Files** tab
2. Click **Add** and select **Add from Company Data**
3. Browse and select the pages, documents, or folders you want to link
4. Click **Save**

<Info>
  **Why only Company Data?** Only data from the Company Data section can be linked. It is the only data guaranteed to be accessible to every Pod member. Other data can be restricted or made private at any time, which would break that guarantee and create inconsistent access within the Pod.

  Linked data appears in the same list as uploaded files and is marked with a sync icon. It is retrieved via search by agents and is not directly editable.
</Info>

## Importing files from external sources

Beyond Company Data, an agent can fetch content from external sources and save it directly into the Pod's Files tab, making it available to all members and searchable by other agents.

This is useful when the source is not connected to Company Data, when you need a snapshot rather than a live link, or when you want to transform the content before saving it (e.g. summarise a long document, translate it, or reformat it).

**How it works:**

1. Start a conversation in the Pod
2. Mention an agent that has the relevant external tool (Google Drive, Notion, SharePoint, a web browser, etc.)
3. Ask it to fetch and save the content: *"Read the Q2 roadmap doc from Google Drive and save it as a file in this Pod's Files tab"*
4. The agent fetches the content, converts it to a compatible format, and saves it to the Pod

**Keeping imported files up to date with the wake-up tool:**

For files that change regularly (a living roadmap, a weekly report, a shared spec), use the **wake-up tool** to schedule an agent that re-fetches and overwrites the file on a set cadence:

Example prompt: *"Every Friday at 5pm, fetch the latest version of the Q2 roadmap from Google Drive and overwrite the existing roadmap file in this Pod. Use the wake-up tool to schedule this automatically."*

Since the agent overwrites the same file, the Pod banner, agent context, and member access all update automatically without any manual action.

<Info>
  **The agent can use the Pods skill by default to write to the Files tab. The appropriate external tool (Google Drive, Notion, Microsoft Drive, etc.) must be available to the agent so it can read the source.**

  **Managing files**
</Info>

| Action                    | How                                                                                                       |
| ------------------------- | --------------------------------------------------------------------------------------------------------- |
| Preview a file            | Click on it in the list                                                                                   |
| Rename                    | Open the `...` menu  **Rename**                                                                           |
| Move                      | Drag to a folder, or open the `...` menu  **Move**                                                        |
| Delete an uploaded file   | Open the `...` menu  **Delete**                                                                           |
| Remove a linked data node | Open the `...` menu  **Remove**                                                                           |
| Pin a MiniApp as Pod banner | Open the `...` menu on a MiniApp  **Pin as Pod banner**; see [MiniApps](/docs/user-documentation/pods/frames) |

***

<Info>
  **Everything in the Files tab (uploaded files, linked data, and Pod conversations) is indexed* and searchable by agents. There is nothing to configure: agents use it automatically.*\*

  \*Most common file formats are automatically indexed for semantic search. Some formats are not indexed: agents can still use them directly when referenced in a conversation, but they will not be surfaced automatically via search. If you need a specific file format to be indexed, [contact us](mailto:support@dust.tt).
</Info>

<Info>
  **Pods scale to thousands of files.** Semantic search by agents is unaffected by file count: agents retrieve the right content reliably even in large knowledge bases. The only behaviour that changes at scale is UI file listing: browsing the Files tab may become slower when a Pod contains thousands of files. If you are building a large agent-first knowledge base, prefer navigating via search rather than scrolling the list.
</Info>
