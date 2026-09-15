# 让智能体发现 Skills

**Discover Skills（发现 Skills）** 允许智能体在对话中查找可被发现的 Skill，并在其说明与当前请求匹配时启用。这样不必在智能体初始配置中加载全部专业指令和能力。部分工作区默认智能体可能已包含 Discover Skills。

## 添加到自定义智能体

在 Agent Builder 中打开智能体，在 **Capabilities（能力）** 中选择 **Discover Skills** 并保存。要让工作区 Skill 出现在发现结果中，它的可用性设置必须允许智能体发现；未标记为可发现的 Skill 不会显示。

## 对话中的工作方式

智能体会检查标记为可发现的工作区 Skill，以及开放给它的全局 Skill。它根据 Skill 的名称和说明判断是否适合当前请求，然后可以在本次对话中启用相关 Skill。被选中的 Skill 的指令、工具和知识将对智能体可用，并可在同一对话后续消息中继续使用。

Discover Skills 不会预先加载全部 Skill，也不会绕过工作区或 Space 权限。智能体只能看到处于启用状态且对它开放的 Skill。

## 适用场景

通用智能体需要处理多种请求，或工作区持续为不同团队增加可复用 Skill 时，可以启用 Discover Skills。它能保持智能体初始配置聚焦，同时让新发布的可发现流程无需逐个修改智能体就可使用。可见性设置见[Skill 可用性](skill-availability.md)。
