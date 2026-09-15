---
title: "Monday.com"
---
Monday 工具可让 Agent 查看和管理看板、分组、项目、列、子项目、更新及相关工作区资料。具体操作取决于 Monday 授权身份和看板权限。

在 **Spaces → Tools** 中添加 Monday，并从 Counso 工具表单发起授权。自托管部署需由部署管理员先注册 Monday OAuth 应用并配置回调地址。按提示登录 Monday；如果需要安装或审批应用，请将其授权给目标工作区。如果界面允许，可选择个人或工作区凭据：个人凭据保留各用户自己的看板权限；共享凭据则使用已配置的账号。确认凭据所有者有权访问目标看板，包括私有看板。将工具分享给目标 Space，并加入 Agent。

先读取一个看板和一条项目。修改前检查列 ID 和类型、所属分组，以及需要保留的子项目或更新。明确指定要改的项目和字段，之后回到 Monday 按同一项目回读。看板或列缺失通常与账号成员权限、私有看板访问权或字段可见性有关。

## 可用操作

Monday 工具提供以下类别；名称对应工具列表中的操作：

- 看板：`get_boards`、`get_board_values`、`create_board`、`get_board_analytics`。
- 项目：`get_board_items`、`get_item_details`、`search_items`、`create_item`、`create_multiple_items`、`update_item`、`update_item_name`、`delete_item`、`move_item_to_board`、`get_items_by_column_value`。
- 分组和列：`create_group`、`get_group_details`、`delete_group`、`duplicate_group`、`create_column`、`get_column_values`、`get_file_column_values`、`upload_file_to_column`。
- 子项目和更新：`create_subitem`、`update_subitem`、`get_subitem_values`、`create_update`。
- 用户和活动：`find_user_by_name`、`get_user_details`、`get_activity_logs`。

Monday 管理员必须先批准应用访问目标 Monday 工作区，再完成 OAuth。操作应遵循各用户权限时，优先采用个人凭据；工作区共享凭据则始终使用配置的账号。工具列表中看板和项目查询每次最多返回 100 条；更大数据集应使用筛选条件或继续查询。更新前先读取列 ID；批量创建或删除前尤其要检查目标范围。

## 凭据设置

从 **Spaces → Tools → Monday** 发起授权。如果 Monday 要求审批或安装应用，请由管理员批准该应用访问目标工作区。以当前工具表单显示的凭据选项为准。不要使用从其他部署复制的授权链接。
