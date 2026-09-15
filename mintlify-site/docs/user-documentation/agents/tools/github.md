---
title: "GitHub"
---
GitHub tools let an Agent search repositories, issues, and pull requests and, where authorized, create or update issues, comments, and pull requests. A GitHub Connection for synchronized code search is a separate setup from the live GitHub Tool.

For a self-hosted deployment, the deployment administrator registers the GitHub App and OAuth application or applications used by the GitHub Tool and configures their callback addresses. The workspace administrator then authorizes the configured app, selects the repositories it may access, and shares the tool with the intended Space. The workspace-credential and personal-credential flows may use different registered apps. Workspace credentials act as the app identity configured for the workspace; personal credentials act as the user who invoked the Agent and remain limited by that user's GitHub membership. Add GitHub to the Agent and specify the repositories it should use in the Agent instructions.

Start with one known repository file or issue and verify its owner/repository. Before creating an issue or pull request, ask the Agent to summarize the proposed change and target repository. If a repository is missing, check app installation scope and the acting user's membership; authentication alone does not grant repository access.
