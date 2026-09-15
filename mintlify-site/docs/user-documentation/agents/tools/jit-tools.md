---
title: "Just-in-time tools"
---
Just-in-time (JIT) tools let a user enable an available capability from the conversation composer for one task, rather than changing the saved Agent configuration. The choice is temporary and conversation-scoped; it does not permanently add a tool for other users.

Use JIT when a one-off request needs a capability that should not always be available, or when you want to apply least privilege. From the composer, open the tool/capability picker, select what the request needs, and continue with the task. Available options depend on workspace configuration and the selected Agent.

JIT does not override provider authentication, data access, or Space sharing. The user still needs permission to invoke the provider tool, and the Agent can only reach records available to the authorized identity. Before a write, confirm the target and content. If the same capability is needed regularly, ask an administrator to review the shared Agent configuration rather than relying on repeated one-off activation.
