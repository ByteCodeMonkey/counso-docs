# Counso CLI

请使用为你的 Counso 工作区提供的 CLI 构建版本，并按照随版本提供的安装说明完成安装。然后在终端确认命令可用：

```bash
dust --version
```

交互使用时，请登录 Counso 部署所配置的账号和工作区：

```bash
dust login
dust status
```

登录流程使用 Counso 部署配置的 OAuth 提供方。管理员配置 CLI 时，应确保 WorkOS 域名、Client ID 和 Claim Namespace 与该部署一致。

启动交互会话并选择 Agent，也可以直接指定 Agent 名称：

```bash
dust chat
dust chat --agent "My Agent"
```

不带子命令运行 `dust` 时，默认也会启动聊天。聊天会话可以访问终端中的本地文件；使用 `/attach` 选择文件，使用 `/clear-files` 移除附件，使用 `/switch` 切换 Agent，使用 `/resume` 继续已有会话，使用 `/exit` 退出。`/auto` 可以切换本地文件编辑的自动批准，`Shift+Tab` 也可完成相同操作。

需要发送单条非交互消息时，使用 `--message`（`-m`），命令会将 JSON 响应写入标准输出。添加 `--conversationId`（`-c`）可继续已有会话；使用 `--agent`（`-a`）或 `--sId`（`-s`）选择 Agent。

```bash
dust chat --agent "My Agent" --message "Summarize the latest invoices"
dust chat -a "My Agent" -m "Add a note about the next steps" -c <conversationId>
```

脚本、CI 任务或无法交互登录的终端，可以通过环境配置提供工作区 API key 和 ID。请将密钥保存在密钥管理服务或其他受保护的配置中，不要放在命令行参数或提交到代码仓库。

```bash
export DUST_API_KEY="<workspace-api-key>"
export DUST_WORKSPACE_ID="<workspace-id>"
dust chat --agent "My Agent" --message "Summarize the latest invoices"
```

CLI 还提供 `dust skill:init`，可在本地创建一个帮助编程助手通过 CLI 调用 Agent 的 Skill；`dust cache:clear` 可清理本地启动缓存。相关概念见[Skills](../../../../../zh-cn/docs/user-documentation/agents/skills/skill-examples.md)。使用 `dust help` 或 `dust --help` 查看命令选项，使用 `dust --version` 查看 CLI 版本。在 Linux 上，凭据存储可能需要 `libsecret`：Debian/Ubuntu 安装 `libsecret-1-dev`，Red Hat 系统安装 `libsecret-devel`，Arch 安装 `libsecret`。
