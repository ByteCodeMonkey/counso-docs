# Run another Agent

The `run_agent` capability lets an Agent call a specialised Agent as a tool. Use it when a task benefits from a separate role or a bounded subtask, such as asking a research Agent to find evidence before a writing Agent prepares a response.

In the Agent builder, enable the capability and select which Agents may be called. Keep the delegated Agent's instructions and data access appropriate to the task. The parent Agent should pass only the context the subtask needs and say what format it expects back.

The default mode runs the called Agent in a separate conversation and returns its result when complete; this suits longer or independent work. A response-in-conversation mode, when available, keeps the call within the current interaction. Neither mode guarantees that the delegated answer is correct. The calling Agent should review the returned result, sources, and any side effects before using it. Avoid recursive or overly broad delegation that makes ownership difficult to trace.
