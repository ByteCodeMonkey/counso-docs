---
title: "智能体在 Pod 中可以做什么"
---
智能体通过 **Pods skill** 管理 Pod、对话、知识、任务和 Pod 设置。所有智能体默认都可以使用这项 skill，无需单独启用。实际执行过的工具可在智能体的工具执行详情中查看。

## Pod 工具

| 工作区域 | 工具 | 作用 |
|---|---|---|
| Pod | `list_pods` | 列出智能体可访问的 Pod：默认是用户自己的 Pod；也可列出工作区中的所有开放 Pod。 |
| Pod | `create_pod` | 创建 Pod，默认设为 Restricted；可同时指定初始成员和待办任务。 |
| Pod 信息 | `get_information` | 读取 Pod 的 URL、标题、说明、可见性、置顶 MiniApp 和关联的 Company Data。 |
| Pod 信息 | `edit_information` | 更新 Pod 标题、说明或可见性。 |
| 成员 | `list_members` | 列出 Pod 成员及其 Member 或 Editor 角色。 |
| 成员 | `update_members` | 邀请、添加、移除成员，或提升、降低成员与 Editor 角色。 |
| 对话 | `create_conversation` | 在 Pod 中新建对话；也可指定任务并触发智能体。 |
| 对话 | `add_message_to_conversation` | 向现有 Pod 对话追加消息。 |
| 对话 | `list_conversations` | 列出近期对话，可筛选未读对话或读取完整记录。 |
| 对话 | `move_conversation` | 将对话移入 Pod，或移回个人对话。 |
| 知识 | `semantic_search` | 按含义搜索 Pod 文件、关联的 Company Data 和 Pod 对话记录。 |
| 知识 | `retrieve_recent_documents` | 获取最近添加或更新的 Pod 知识文档。 |
| 知识 | `add_content_node` | 将 Company Data 中的文档或文件夹关联到 Pod 知识。 |
| 知识 | `remove_content_node` | 移除 Pod 中的 Company Data 引用。 |
| Pod 设置 | `set_pinned_frame` | 将 MiniApp 置顶为 Pod 横幅，或取消当前置顶。 |
| Pod 设置 | `set_default_agent` | 设置或重置处理 Pod 新对话的默认智能体。 |
| 任务 | `list_tasks` | 按指派人（自己或全部）和状态（未完成、已完成或全部）列出任务。 |
| 任务 | `create_tasks` | 一次创建最多 30 项任务，可指派给 Pod 成员或暂不指派。 |
| 任务 | `update_tasks` | 更新任务说明、负责人和状态，也可将任务标记为完成。 |
| 任务 | `start_task_agent` | 让智能体开始处理未完成任务，同时创建关联对话并将任务设为 **In progress**。 |

智能体通过共享文件系统工具处理 Pod 文件，而不是使用专属的 Pod 文件工具。它可以浏览和读取文件，创建 MiniApps 等文件，编辑、复制、移动或删除文件，也可以从 URL 导入文件。智能体创建或更新的文件会出现在 Files 中，Pod 成员和其他智能体都可以访问。

## 权限边界

智能体代表当前用户操作，只能执行该用户本人有权执行的操作。用户不是 Restricted Pod 成员时，智能体也不能访问该 Pod。管理成员、Pod 设置、可见性和置顶 MiniApp 需要用户具有 Pod Editor 角色。工具出现在列表中并不会绕过这些访问规则。
