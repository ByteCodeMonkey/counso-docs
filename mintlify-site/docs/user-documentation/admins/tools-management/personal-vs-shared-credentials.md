---
title: "Personal and shared credentials for tools"
---
A tool's credential model determines which provider identity performs an operation and whose permissions apply. Providers may support personal credentials, a shared workspace credential, or only one of these options. Use the choices shown in the tool's current setup form.

**Personal credentials** let each user authorize their own account. The provider can attribute actions to that user, and results follow their provider access. An administrator may still need to complete initial app setup or consent before users can connect individually.

**Shared credentials** use one administrator-configured account for everyone allowed to use the tool. This simplifies setup, but the shared account may see more data than any individual user. Restrict the tool to the smallest Space and Agent group, and decide who owns credential rotation and revocation.

Choose the model by asking who should be accountable, whether access should vary by user, what provider scope is needed, and how access will be removed. Both models still require Space and Agent access controls. If the connected account or membership changes, revoke or reconnect it and recheck one known object. Users can usually disconnect their personal grant from their profile's connected tools area.
