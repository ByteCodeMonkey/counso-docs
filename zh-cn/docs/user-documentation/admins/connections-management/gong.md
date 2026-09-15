# 连接 Gong

Gong 连接索引通话转写文本，范围覆盖所连接的 Gong 工作区，但不包含标记为 **Private** 的通话。授权前，请先核对这一工作区范围是否合适。

## 连接工作区

1. 使用具有 Counso 管理权限和 Gong **Technical administrator** 权限的账号。可在 Gong 的 **My Profile > Workspaces and permissions** 中确认角色。
2. 打开 **Spaces > Connections**，选择 Gong 并登录。
3. 核对 Gong 授权页面，完成授权。
4. 同步后，将数据分配到合适的 [Space](../spaces-management.md)，供助手使用。

连接建立后开始首次导入，耗时取决于转写数量。后续新增转写最多可能需要约一小时才能出现。

## 同步的转写内容

每份索引内容包含转写文本、可用的发言人邮箱、原始 Gong 通话链接和通话时长。同步的知识来源是文字转写，不是音视频录制文件。

标签记录标题、日期、语言、媒体类型、内部或外部通话、呼叫方向、参与者以及触发的 tracker。语言采用 ISO-639-2B 编码，例如 `eng`、`fre`；tracker 标签使用 `tracker:{name}` 格式。

可以在[知识搜索工具](../../agents/knowledge/search-data-sources.md)中按这些标签筛选，例如只查找某种语言的外部通话。参与者信息仅在 Gong 提供时才会包含。
