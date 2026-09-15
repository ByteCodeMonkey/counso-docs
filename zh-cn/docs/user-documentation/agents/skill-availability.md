# 管理 Skill 的发现和使用范围

Skill 的可用性设置决定谁能从对话输入框或 Agent Builder 中找到它。这与 Skill 引用的数据和工具权限是分开的。分享 Skill 时，两者都要检查。

## 可用性选项

- **Editors only（仅编辑者）：** 只有 Skill 编辑者能在对话输入框和 Agent Builder 中找到它。适合开发期间或个人使用。非编辑者仍可能通过自己能访问的智能体或其他 Skill 使用它。
- **All members（所有成员）：** 全体工作区成员都能从对话输入框和 Agent Builder 中找到并使用。更改为此选项需要 **Manage skill availability（管理 Skill 可用性）** 权限。
- **Members and agents（成员和智能体）：** 成员以及启用了 **Discover Skills（发现 Skills）** 的智能体可以找到和使用它；智能体可在认为适用时自动启用。此选项需要同时具备 **Manage skill availability** 和 **Make skills discoverable to agents（允许智能体发现 Skills）** 权限。

## 限制 Skill 访问

Skill 默认不是私有的。若要限制访问，可将 Skill 关联到受限 Pod。只有能访问该 Pod 的人员和智能体才能使用这个 Skill。编辑者也需要拥有该受限 Pod 的访问权限，才能找到和使用它。

调整可用性前，检查 Skill 附加的 Knowledge、Tools 和必需 Space。让 Skill 可被发现不会自动授予用户或智能体访问这些资源的权限。自动发现方式见[发现 Skills](discover-skills.md)。
