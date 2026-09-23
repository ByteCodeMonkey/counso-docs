# 通过 Raycast 使用 Counso

Raycast 扩展可以让 Counso 智能体处理 macOS 中任意应用里选中的文字。对于受支持的命令，智能体回答会直接替换原选区，无需切换应用或手动复制粘贴。

## 安装与登录

安装为当前 Counso 部署提供的扩展，打开登录命令，核对 Counso 工作区地址，并使用 Counso 账号完成授权。除非已经配置为使用 Counso 服务地址和 OAuth 客户端，否则不要安装上游品牌的扩展。

## 智能体快捷键

通过 **Agent Quicklink** 命令可以把快捷键绑定到指定智能体：

1. 在 Raycast 中打开 **Agent Quicklink**。
2. 选择 Counso 智能体。
3. 创建 Quicklink 并分配快捷键。

可以为不同智能体设置不同快捷键。在任意 macOS 应用中选中文字后按下快捷键，并检查智能体生成的替换内容。Raycast 会通过通知显示进度或错误。

如果只需要打开普通对话而不替换选中文字，可以为 Counso 通用命令或具体智能体命令设置 Raycast alias 或 hotkey。

## 发布条件

只有在 Counso 环境中验证扩展安装包、服务地址、OAuth 配置、工作区选择和原位文本替换后，才应发布本页。
