# Gong

Gong 工具可实时读取通话信息和转录文本。它可以按日期范围列出通话，通过 `callId` 获取详情，并返回按说话人整理的转录。这与用于搜索同步资料的 Gong Connection 不同。

管理员从 **Spaces → Tools → Add Tools** 添加 Gong 并完成 OAuth，再将工具分享给目标 Space。向更多成员开放前要注意，第三方工具可能返回整个 Gong 工作区的通话，而不只是授权用户本人参与的通话。通过 Space 成员范围控制使用者，并确认该 Space 内所有成员都获准查看这些通话。

先用 `fromDateTime` 和 `toDateTime` 调用 `list_calls` 限定范围，再用返回的 `callId` 调用 `get_call` 或 `get_call_transcript`。结果可能分页，需要使用返回的游标继续读取。系统处理完成前，转录可能尚未生成。如果只需要搜索同步资料，应配置 Connection，而非实时 Tool。
