> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Branch a Conversation

Branching lets you spin off a new conversation from any point in an existing one. The branched conversation starts with a summary of what happened so far, plus copies of any files and tool outputs, so you can keep working without losing context.

## Example use cases

* **Split into work streams**: A conversation produces a plan with three parts, each requiring a technical design. Branch once per part; each child conversation has the full context it needs to go deep.
* **Hand off a result**: You built something with an agent (a report, a frame, a draft) and want a teammate to iterate on the output, without them needing to scroll through all the back-and-forth that produced it.
* **Try a different approach**: You're mid-conversation and want to explore an alternative direction without dirtying the original thread.
* **Delegate cleanly**: Branch at the point where work is ready to hand off, so the recipient's conversation starts exactly there.

## How it works

### Branching

You can branch a conversation from the conversation menu on the top right corner of your conversation (3-dots menu).

### What the branched conversation receives

When you branch, Dust creates a brand-new standalone conversation. It:

1. **Generates a summary** of the parent conversation up to the branch point (using compaction). This becomes the first message in the child, giving the agent full context.
2. **Copies all files and tool outputs** from the parent so the child has its own isolated working set. Edits in the child do not affect the parent, and vice versa.
3. **Inherits the same space / project**, enabled tools, and MCP servers that you have access to.

**Note:** Branching takes 10–20 seconds, the summary is generated during this time.

### Lineage

The branched conversation displays a **"Branched from …"** link so you can always trace it back to its origin. The parent conversation also shows a note when one of its messages was used as a branch point.

### Permissions

The child conversation inherits access rights from its parent at time of branching. The user who branched becomes the initial participant. Access rights may diverge later if restricted content is added to either conversation.

## FAQ

### How long does branching take?

Typically 10–20 seconds. During this time, Dust generates the summary that seeds the child conversation. You can send messages during this time; they will be enqueued and processed once the branched conversation is ready.

### Does branching affect the parent conversation?

No. The parent conversation is left completely unchanged. Branching is a read-only operation on the parent.

### Can I branch from the middle of a conversation?

Yes. Use the per-message menu on any agent message to branch from that exact point. Branching from the conversation menu always uses the latest agent message.

### Are my files and attachments available in the branched conversation?

Yes, as new copies. Files and tool outputs from the parent are deep-copied into the child, so they're fully available and independent. Changes you make to files in the child do not affect the parent, and vice versa.

### Is the branched conversation independent?

Fully. It's a standalone conversation with its own history, files, and participants. Future messages, files, and agent actions in the child are isolated from the parent.

### Can I branch a branched conversation?

Yes. You can branch any conversation, including one that was itself branched. Each branch is an independent conversation with its own lineage link.

### Can my teammates see the branched conversation?

Access follows standard conversation permissions: the child conversation is created in the same space/project as the parent. The person who branched is the initial participant. Workspace access rules apply as normal from there.

### What if I want the agent to go in a different direction after branching?

Just send a message in the branched conversation. The agent has full context from the summary and can continue from there in any direction you choose.
