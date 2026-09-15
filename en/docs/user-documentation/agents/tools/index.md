# Agent tools

Tools give an Agent access to built-in capabilities or operations in connected services. The selected tool list is part of the Agent configuration; availability alone does not mean that an Agent can use it. A workspace administrator may need to enable and share a provider tool with the relevant Space first.

## Choose only what the task needs

Built-in options can include knowledge search, web search and browsing, data visualisation, file and image creation, memory, and delegation to another Agent. Provider tools can search or act on services such as mail, calendars, project trackers, CRMs, storage, and support systems. The current builder shows the tools available in this workspace.

For each capability, decide: which requests should use it, what data it may access, whether it can change or send anything, and how a person will check the result. Write those expectations into the Agent instructions. Prefer a read-only permission set when the Agent only needs answers. For write-capable tools, identify the responsible account, limit Space access, and require a person to review an important action.

## Configure and check

1. In the Agent builder, open **Tools** and add the capabilities needed for the role.
2. Under the data/knowledge settings, select only the sources the Agent needs and describe their purpose.
3. Ask a representative question and check whether the expected tool was used and whether its source or provider record is correct.
4. If the Agent has a write tool, test only a safe, bounded action and verify the resulting object in the provider.

A tool call can return partial results because of provider permissions, account ownership, or source scope. Adding more tools does not fix those limits and may make it harder to understand where an answer came from. For a one-off request, use a conversation-scoped tool option when available instead of changing a shared Agent.
