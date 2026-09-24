# 文档发布范围与准备稿

当前提供 263 篇中英文正文、2 份接口规范和 Postman 导入文件，另有 28 篇中英文准备稿。是否进入用户目录，按教程依赖的内容和当前发布策略判断；工作区尚未完成配置，本身不是隐藏配置教程的理由。

## 发布建议

| 内容范围 | 建议 | 交接时需要明确的事项 |
| --- | --- | --- |
| 已纳入目录的 263 篇中英文正文、2 份接口规范及 Postman 文件 | 直接纳入文档目录 | 教程依赖的常规部署、应用注册与授权按正文配置；这项建议针对文档内容，不代表生产功能已逐项验收。 |
| 下表 28 篇中英文准备稿 | 确认对应条件后发布 | 每篇列明需要确认的内容和未确认时可能出现的问题。已完成配置或已有交付物的，核对后即可转为正文，无需重新立项。 |
| 末表 9 项历史资料 | 不纳入用户目录 | 原产品更新历史、实验仓库导航和已弃用框架不作为 Counso 当前使用说明；原文仍保留在来源资料中。 |

## 配置与使用说明

以下 5 篇配置与使用说明列入正常目录。使用前需完成相应的部署配置和工作区授权。应用注册、凭据、回调、事件接收、后台服务及功能开关，由部署管理员完成；普通用户按正文执行授权、选择范围和使用步骤。

| 主题 | 类型 | 部署前提 | 文章 |
| --- | --- | --- | --- |
| GitHub 工具 | 应用配置 | 注册并配置相应用途的 GitHub App、凭据与回调，再授权仓库。 | [EN](en/docs/user-documentation/agents/tools/github.md) · [中文](zh-cn/docs/user-documentation/agents/tools/github.md) |
| Monday 工具 | OAuth 配置 | 注册自己的 Monday OAuth 应用，填写部署回调和凭据；从 Counso 发起授权，不沿用原教程的固定应用 ID。 | [EN](en/docs/user-documentation/agents/tools/monday-com.md) · [中文](zh-cn/docs/user-documentation/agents/tools/monday-com.md) |
| 外部客户端连接 Counso MCP | 服务与 OAuth 配置 | 配置 MCP 服务与 OAuth 授权，客户端按文档连接实际端点。 | [EN](en/docs/user-documentation/agents/integrations/counso-mcp-server.md) · [中文](zh-cn/docs/user-documentation/agents/integrations/counso-mcp-server.md) |
| 会议转录 | 使用与自动化配置 | 普通使用说明保留；自动处理另外要求转录来源、后台处理服务和工作区设置。 | [EN](en/docs/user-documentation/agents/integrations/meeting-transcripts.md) · [中文](zh-cn/docs/user-documentation/agents/integrations/meeting-transcripts.md) |
| GitHub 数据同步 | 应用配置 | 注册并配置相应用途的 GitHub App、凭据与回调，再授权仓库。 | [EN](en/docs/user-documentation/admins/connections-management/github.md) · [中文](zh-cn/docs/user-documentation/admins/connections-management/github.md) |

GitHub 和 Monday 的源码提供配置自有应用的入口。原教程中的固定域名和应用 ID 是托管环境的值，不能直接用作 Counso 配置。注册并配置自己的应用后，可沿用已有集成实现。Slack 相关页面按当前发布策略统一隐藏。

## 已准备、暂不进入用户目录的文章

以下文章的双语品牌化稿件保存在 `prepared/`。正文保留用途、配置前提和使用流程；安装包、分发地址、脚本命令或服务地址须与实际交付对应。

这 28 篇是当前文档的发布状态，不等于 Counso 缺少 28 项功能。原文及下列引用的上游实现已核对，但尚未逐项核对 Counso 当前部署的代码、配置和分发包。表中的条件用于核对发布依据，不能据此断言 Counso 尚未实现。

产品帮助 Skill 适合纳入 Counso 使用文档。上游已有内置 Skill，主要需要替换其产品名称、适用范围、检索来源和支持入口，无需另建一套客服系统。不过，原指令明确使用原产品文档与社区，并限制适用产品；只改文章名称，不能让实际回答自动改用 Counso 资料。当前保留准备稿，待确认部署中的 Skill 与文章描述一致后即可发布。

邮件联系智能体也有现成实现。它按发件人的成员身份定位工作区，再按收件地址的名称匹配智能体；并非为每个智能体逐个创建独立邮箱账号。收件域名、SendGrid 入站解析与校验、回复发信配置和工作区开关仍需在 Counso 环境接通，因此不能仅凭主服务已经 fork 就认定邮件入口可用。

其余文章介绍的是具体应用、客户端或脚本。暂缓的是依赖这些交付物的安装与运行步骤，不是排除对应平台或数据源。Zapier、Make 等原文要求选择原产品应用或模块；尚未核实这些应用能否配置自定义服务地址，不能直接断言必须重新开发，也不能把原应用当作 Counso 版本发布。

`translations.json` 的 `prepared` 字段关联这些稿件；当前站点只使用 `notice` 显示简短的“文档更新中”。确认现有实现已满足条件，或补齐对应交付物并核对具体步骤后，可将准备稿移入正常正文并开放入口。Slack 相关稿件还需要发布策略明确解除隐藏后才能恢复。

| 主题 | 类别 | 原始 URL | 发布建议 | 需要确认 | 未确认时可能出现的问题 | 中英文稿 |
| --- | --- | --- | --- | --- | --- | --- |
| Slack 消息链接定位问题 | Slack FAQ | [https://docs.dust.tt/docs/user-documentation/getting-started/faq/troubleshooting-and-limitations/when-asking-a-question-about-data-within-slack-the-link-to-the-thread-isnt-always-the-right-one](https://docs.dust.tt/docs/user-documentation/getting-started/faq/troubleshooting-and-limitations/when-asking-a-question-about-data-within-slack-the-link-to-the-thread-isnt-always-the-right-one) | 当前隐藏 | Slack 相关文档恢复公开。 | 用户看到当前未开放的 Slack 使用说明。 | [EN](prepared/en/docs/user-documentation/getting-started/faq/troubleshooting-and-limitations/when-asking-a-question-about-data-within-slack-the-link-to-the-thread-isnt-always-the-right-one.md) · [中文](prepared/zh-cn/docs/user-documentation/getting-started/faq/troubleshooting-and-limitations/when-asking-a-question-about-data-within-slack-the-link-to-the-thread-isnt-always-the-right-one.md) |
| Slack 工具 | Agent Tool | [https://docs.dust.tt/docs/user-documentation/agents/tools/slack-tools](https://docs.dust.tt/docs/user-documentation/agents/tools/slack-tools) | 当前隐藏 | Slack 相关文档恢复公开。 | 用户看到当前未开放的 Slack 工具说明。 | [EN](prepared/en/docs/user-documentation/agents/tools/slack-tools.md) · [中文](prepared/zh-cn/docs/user-documentation/agents/tools/slack-tools.md) |
| Slack 自动回复 | Slack 集成 | [https://docs.dust.tt/docs/user-documentation/agents/integrations/dust-in-slack/slack-auto-reply](https://docs.dust.tt/docs/user-documentation/agents/integrations/dust-in-slack/slack-auto-reply) | 当前隐藏 | Slack 相关文档恢复公开。 | 用户尝试配置当前未开放的自动回复能力。 | [EN](prepared/en/docs/user-documentation/agents/integrations/counso-in-slack/slack-auto-reply.md) · [中文](prepared/zh-cn/docs/user-documentation/agents/integrations/counso-in-slack/slack-auto-reply.md) |
| Slack Workflow | Slack 集成 | [https://docs.dust.tt/docs/user-documentation/agents/integrations/dust-in-slack/slack-workflows](https://docs.dust.tt/docs/user-documentation/agents/integrations/dust-in-slack/slack-workflows) | 当前隐藏 | Slack 相关文档恢复公开。 | 用户尝试配置当前未开放的 Workflow 能力。 | [EN](prepared/en/docs/user-documentation/agents/integrations/counso-in-slack/slack-workflows.md) · [中文](prepared/zh-cn/docs/user-documentation/agents/integrations/counso-in-slack/slack-workflows.md) |
| Slack 自动加入频道 | Slack 集成 | [https://docs.dust.tt/docs/user-documentation/agents/integrations/dust-in-slack/slack-auto-join](https://docs.dust.tt/docs/user-documentation/agents/integrations/dust-in-slack/slack-auto-join) | 当前隐藏 | Slack 相关文档恢复公开。 | 用户尝试启用当前未开放的自动加入频道能力。 | [EN](prepared/en/docs/user-documentation/agents/integrations/counso-in-slack/slack-auto-join.md) · [中文](prepared/zh-cn/docs/user-documentation/agents/integrations/counso-in-slack/slack-auto-join.md) |
| Slack 数据同步 | 数据连接 | [https://docs.dust.tt/docs/user-documentation/admins/connections-management/slack](https://docs.dust.tt/docs/user-documentation/admins/connections-management/slack) | 当前隐藏 | Slack 相关文档恢复公开。 | 管理员尝试配置当前未开放的 Slack 连接。 | [EN](prepared/en/docs/user-documentation/admins/connections-management/slack.md) · [中文](prepared/zh-cn/docs/user-documentation/admins/connections-management/slack.md) |
| Slack 排障 | 管理员说明 | [https://docs.dust.tt/docs/user-documentation/admins/admin-troubleshooting/slack-troubleshooting](https://docs.dust.tt/docs/user-documentation/admins/admin-troubleshooting/slack-troubleshooting) | 当前隐藏 | Slack 相关文档恢复公开。 | 用户看到与当前发布能力不一致的排障步骤。 | [EN](prepared/en/docs/user-documentation/admins/admin-troubleshooting/slack-troubleshooting.md) · [中文](prepared/zh-cn/docs/user-documentation/admins/admin-troubleshooting/slack-troubleshooting.md) |
| 产品支持指引 | 产品帮助 Skill | [https://docs.dust.tt/docs/user-documentation/agents/dust-support](https://docs.dust.tt/docs/user-documentation/agents/dust-support) | 建议纳入，确认后发布 | 内置 Skill 的名称、适用产品、文档检索来源和支持入口已改为 Counso；在工作区能找到并使用它。 | 仅改文章名称，实际帮助仍可能检索原产品资料，或不适用于 Counso 问题。 | [EN](prepared/en/docs/user-documentation/agents/counso-support.md) · [中文](prepared/zh-cn/docs/user-documentation/agents/counso-support.md) |
| 通过邮件联系智能体 | 邮件服务 | [https://docs.dust.tt/docs/user-documentation/agents/integrations/send-and-forward-email-to-agents](https://docs.dust.tt/docs/user-documentation/agents/integrations/send-and-forward-email-to-agents) | 邮件服务确认后发布 | Counso 收件域名、入站解析与签名校验、回复发信配置、工作区开关及实际智能体地址已接通。 | 照着教程发送却无人处理，地址仍指向原产品，或只能收信不能回复。 | [EN](prepared/en/docs/user-documentation/agents/integrations/send-and-forward-email-to-agents.md) · [中文](prepared/zh-cn/docs/user-documentation/agents/integrations/send-and-forward-email-to-agents.md) |
| 通过 Zapier 运行智能体 | 专用应用 | [https://docs.dust.tt/docs/user-documentation/agents/integrations/zapier](https://docs.dust.tt/docs/user-documentation/agents/integrations/zapier) | 应用连接确认后发布 | 原教程使用专用应用及 Talk to an Agent 动作。确认实际提供的应用、Counso 目标地址、凭据和动作名称；若可用自定义连接，无需假定必须新开发。 | 搜索不到文档所写应用，或动作仍请求原平台，Counso 凭据无法使用。 | [EN](prepared/en/docs/user-documentation/agents/integrations/zapier.md) · [中文](prepared/zh-cn/docs/user-documentation/agents/integrations/zapier.md) |
| 通过 Make 运行智能体 | 专用应用 | [https://docs.dust.tt/docs/user-documentation/agents/integrations/make-com](https://docs.dust.tt/docs/user-documentation/agents/integrations/make-com) | 模块连接确认后发布 | 确认提供给用户的模块及连接方式可访问 Counso；原模块能否指定自定义服务地址尚未核实。 | 原模块名称、连接字段与教程不符，或请求仍发往原平台。 | [EN](prepared/en/docs/user-documentation/agents/integrations/make-com.md) · [中文](prepared/zh-cn/docs/user-documentation/agents/integrations/make-com.md) |
| 在 n8n 中使用 Counso | 节点包 | [https://docs.dust.tt/docs/user-documentation/agents/integrations/n8n](https://docs.dust.tt/docs/user-documentation/agents/integrations/n8n) | 节点包确认后发布 | 确认节点的安装名称、版本、凭据字段和 API 地址。已检查的上游节点只在原站 US/EU 地址间选择。 | 安装原节点后仍连接原平台，填写 Counso 工作区和密钥也不能自动切换目标。 | [EN](prepared/en/docs/user-documentation/agents/integrations/n8n.md) · [中文](prepared/zh-cn/docs/user-documentation/agents/integrations/n8n.md) |
| 在 Power Automate 中使用 Counso | 连接器安装包 | [https://docs.dust.tt/docs/user-documentation/agents/integrations/power-automate](https://docs.dust.tt/docs/user-documentation/agents/integrations/power-automate) | 安装包确认后发布 | 提供实际 Solution 下载入口，并核对包内服务地址、认证与两个动作的配置；原文下载地址属于原产品。 | 安装链接不可用，或导入的连接器仍引用原平台。尚未核对 Counso 的实际包。 | [EN](prepared/en/docs/user-documentation/agents/integrations/power-automate.md) · [中文](prepared/zh-cn/docs/user-documentation/agents/integrations/power-automate.md) |
| 在 Google Sheets 中使用 Counso | 表格插件 | [https://docs.dust.tt/docs/user-documentation/agents/integrations/google-sheets-add-on](https://docs.dust.tt/docs/user-documentation/agents/integrations/google-sheets-add-on) | 插件确认后发布 | 确认实际插件的安装入口、授权、服务地址与界面步骤；这篇讲的是表格插件，不是 Google Drive 数据连接。 | 原 Marketplace 插件仍显示原品牌或连接原服务；已有 Drive 连接不能替代插件。 | [EN](prepared/en/docs/user-documentation/agents/integrations/google-sheets-add-on.md) · [中文](prepared/zh-cn/docs/user-documentation/agents/integrations/google-sheets-add-on.md) |
| 在 Zendesk 中使用 Counso | Zendesk 应用 | [https://docs.dust.tt/docs/user-documentation/agents/integrations/dust-in-zendesk](https://docs.dust.tt/docs/user-documentation/agents/integrations/dust-in-zendesk) | 应用包确认后发布 | 确认 Counso 侧边栏应用的安装方式、服务地址、登录与账号匹配。它与 Zendesk 数据连接和工具不同。 | 安装了原品牌应用，或登录与会话仍进入原平台。 | [EN](prepared/en/docs/user-documentation/agents/integrations/counso-in-zendesk.md) · [中文](prepared/zh-cn/docs/user-documentation/agents/integrations/counso-in-zendesk.md) |
| 在浏览器中使用智能体 | 浏览器扩展 | [https://docs.dust.tt/docs/user-documentation/agents/integrations/browser-extension](https://docs.dust.tt/docs/user-documentation/agents/integrations/browser-extension) | 扩展确认后发布 | 确认 Counso 扩展的构建与实际分发入口，核对登录地址、站点权限和文档中的安装步骤。 | 商店链接安装的是原品牌扩展，无法登录 Counso，或扩展没有所需站点权限。 | [EN](prepared/en/docs/user-documentation/agents/integrations/browser-extension.md) · [中文](prepared/zh-cn/docs/user-documentation/agents/integrations/browser-extension.md) |
| 通过 Raycast 使用 Counso | Raycast 扩展 | [https://docs.dust.tt/docs/user-documentation/agents/integrations/raycast-extension](https://docs.dust.tt/docs/user-documentation/agents/integrations/raycast-extension) | 扩展确认后发布 | 确认实际安装来源、Counso 服务地址与 OAuth 客户端；已检查的上游扩展仍使用原站地址和登录配置。 | 扩展打开原产品登录页，或授权成功后请求的仍是原平台。 | [EN](prepared/en/docs/user-documentation/agents/integrations/raycast-extension.md) · [中文](prepared/zh-cn/docs/user-documentation/agents/integrations/raycast-extension.md) |
| ServiceNow | Agent Tool | [https://docs.dust.tt/docs/user-documentation/agents/tools/servicenow](https://docs.dust.tt/docs/user-documentation/agents/tools/servicenow) | 工具与 OAuth 流程确认后发布 | 确认 Counso 已提供 ServiceNow 工具、实际 OAuth 回调地址、Table API 方法和集成账号权限。 | 按文档配置后找不到工具、OAuth 回调不匹配，或只能读取而不能创建和更新记录。 | [EN](prepared/en/docs/user-documentation/agents/tools/servicenow.md) · [中文](prepared/zh-cn/docs/user-documentation/agents/tools/servicenow.md) |
| 在 Microsoft Teams 中使用智能体 | Teams 应用包 | [https://docs.dust.tt/docs/user-documentation/agents/integrations/dust-in-teams](https://docs.dust.tt/docs/user-documentation/agents/integrations/dust-in-teams) | 应用包与机器人确认后发布 | 确认 Teams 应用包、机器人注册、消息服务、授权和安装步骤一致；原文给的是原产品应用包。 | 可以安装图标但机器人不响应，或消息和授权仍进入原平台。 | [EN](prepared/en/docs/user-documentation/agents/integrations/counso-in-teams.md) · [中文](prepared/zh-cn/docs/user-documentation/agents/integrations/counso-in-teams.md) |
| 将 Dropbox 文件导入 Counso | 导入脚本 | [https://docs.dust.tt/docs/user-documentation/data-sources/custom-connections/beta-import-dropbox-files](https://docs.dust.tt/docs/user-documentation/data-sources/custom-connections/beta-import-dropbox-files) | 脚本确认后发布 | 确认实际脚本与运行命令，Counso 上传目标、Dropbox 授权、选定目录及重复导入行为。 | 原脚本仍向原平台上传，或导入范围与教程不同；不能把脚本教程当作内置 Connection。 | [EN](prepared/en/docs/user-documentation/data-sources/custom-connections/beta-import-dropbox-files.md) · [中文](prepared/zh-cn/docs/user-documentation/data-sources/custom-connections/beta-import-dropbox-files.md) |
| 将 Front 会话导入 Counso | 导入脚本 | [https://docs.dust.tt/docs/user-documentation/data-sources/custom-connections/beta-import-front-conversations](https://docs.dust.tt/docs/user-documentation/data-sources/custom-connections/beta-import-front-conversations) | 脚本确认后发布 | 确认脚本、Counso 上传目标、Front 权限、会话筛选与时间窗口；窗口以交付脚本为准。 | 目标仍为原平台，或时间窗口不同造成遗漏、重复导入。 | [EN](prepared/en/docs/user-documentation/data-sources/custom-connections/beta-import-front-conversations.md) · [中文](prepared/zh-cn/docs/user-documentation/data-sources/custom-connections/beta-import-front-conversations.md) |
| 将 Guru 卡片导入 Counso | 导入脚本 | [https://docs.dust.tt/docs/user-documentation/data-sources/custom-connections/beta-import-guru-cards](https://docs.dust.tt/docs/user-documentation/data-sources/custom-connections/beta-import-guru-cards) | 脚本确认后发布 | 确认脚本、Counso 上传目标、Guru 凭据、集合范围和再次运行时的更新方式。 | 目标或集合选错，已有文档更新方式与教程不符。 | [EN](prepared/en/docs/user-documentation/data-sources/custom-connections/beta-import-guru-cards.md) · [中文](prepared/zh-cn/docs/user-documentation/data-sources/custom-connections/beta-import-guru-cards.md) |
| 将 HubSpot 公司摘要导入 Counso | 导入脚本 | [https://docs.dust.tt/docs/user-documentation/data-sources/custom-connections/beta-import-hubspot-data](https://docs.dust.tt/docs/user-documentation/data-sources/custom-connections/beta-import-hubspot-data) | 脚本确认后发布 | 确认脚本、Counso 上传目标、HubSpot 授权、公司摘要字段和增量时间窗口。 | 把公司摘要误当作全部 CRM 数据同步，或时间窗口不同造成遗漏。 | [EN](prepared/en/docs/user-documentation/data-sources/custom-connections/beta-import-hubspot-data.md) · [中文](prepared/zh-cn/docs/user-documentation/data-sources/custom-connections/beta-import-hubspot-data.md) |
| 将 Jira Issue 导入 Counso | 导入脚本 | [https://docs.dust.tt/docs/user-documentation/data-sources/custom-connections/beta-import-jira-issues](https://docs.dust.tt/docs/user-documentation/data-sources/custom-connections/beta-import-jira-issues) | 脚本确认后发布 | 确认脚本、Counso 上传目标、Jira 站点与授权、项目筛选和增量更新方式。 | 脚本请求或上传目标仍为原环境，或导入项目范围不符。 | [EN](prepared/en/docs/user-documentation/data-sources/custom-connections/beta-import-jira-issues.md) · [中文](prepared/zh-cn/docs/user-documentation/data-sources/custom-connections/beta-import-jira-issues.md) |
| 将 Linear Issue 导入 Counso | 导入脚本 | [https://docs.dust.tt/docs/user-documentation/data-sources/custom-connections/beta-import-linear-issues](https://docs.dust.tt/docs/user-documentation/data-sources/custom-connections/beta-import-linear-issues) | 脚本确认后发布 | 确认脚本、Counso 上传目标、Linear 凭据、团队范围和重复运行行为。 | 目标仍为原平台，或筛选范围和更新方式与教程不同。 | [EN](prepared/en/docs/user-documentation/data-sources/custom-connections/beta-import-linear-issues.md) · [中文](prepared/zh-cn/docs/user-documentation/data-sources/custom-connections/beta-import-linear-issues.md) |
| 将 Salesforce 客户摘要导入 Counso | 导入脚本 | [https://docs.dust.tt/docs/user-documentation/data-sources/custom-connections/beta-import-salesforce-data](https://docs.dust.tt/docs/user-documentation/data-sources/custom-connections/beta-import-salesforce-data) | 脚本确认后发布 | 确认脚本、Counso 上传目标、Salesforce 登录与组织、客户摘要字段及更新方式。 | 把客户摘要误当作全部 Salesforce 同步，或连错组织和上传目标。 | [EN](prepared/en/docs/user-documentation/data-sources/custom-connections/beta-import-salesforce-data.md) · [中文](prepared/zh-cn/docs/user-documentation/data-sources/custom-connections/beta-import-salesforce-data.md) |
| 通过 Zapier 上传文档 | 专用应用 | [https://docs.dust.tt/docs/user-documentation/data-sources/custom-connections/zapier-automatically-add-datasource](https://docs.dust.tt/docs/user-documentation/data-sources/custom-connections/zapier-automatically-add-datasource) | 上传动作确认后发布 | 确认实际 Zapier 应用、上传动作、Counso 连接和目标资料库。原文模板依赖原产品的 Upload Document 动作。 | 原模板找不到对应动作，或文档上传到错误的平台、工作区或资料库。 | [EN](prepared/en/docs/user-documentation/data-sources/custom-connections/zapier-automatically-add-datasource.md) · [中文](prepared/zh-cn/docs/user-documentation/data-sources/custom-connections/zapier-automatically-add-datasource.md) |
| Counso CLI | 命令行客户端 | [https://docs.dust.tt/docs/developer-platform/dust-cli/dust-cli](https://docs.dust.tt/docs/developer-platform/dust-cli/dust-cli) | CLI 构建确认后发布 | 提供实际安装包、命令名称、版本和 Counso 登录配置。已检查的 @dust-tt/dust-cli@0.4.6 将服务配置编译进包内，不能仅靠运行时环境变量切换。 | 安装后仍调用原站 API 或登录原账号；文档中的 Counso 地址不会改变二进制配置。 | [EN](prepared/en/docs/developer-platform/counso-cli/counso-cli.md) · [中文](prepared/zh-cn/docs/developer-platform/counso-cli/counso-cli.md) |

导入概念、资料整理和核对方法可以介绍；当前保留为准备稿的是具体脚本教程。仅将源平台凭据填入原脚本，不会自动把原站上传目标改成 Counso。数据导入可使用已提供的 API 说明；这里列的是具体导入脚本及其使用稿。

实现依据：[内置帮助 Skill](https://github.com/dust-tt/dust/blob/c0dd3d79f264963ad5df5b768450e3735245bf66/front/lib/resources/skill/code_defined/global/support.ts)、[邮件地址与工作区匹配、回复](https://github.com/dust-tt/dust/blob/c0dd3d79f264963ad5df5b768450e3735245bf66/front/lib/api/assistant/email/email_trigger.ts)、[邮件收件域名](https://github.com/dust-tt/dust/blob/c0dd3d79f264963ad5df5b768450e3735245bf66/front/lib/api/assistant/email/constants.ts)、[邮件入站处理](https://github.com/dust-tt/dust/blob/c0dd3d79f264963ad5df5b768450e3735245bf66/front-api/routes/email/webhook.ts)。这些引用固定在已核对的上游提交，不代表 Counso 当前部署版本。

## API 与开发资料

68 篇接口参考、8 篇开发指南和 2 份接口规范已纳入中英文文档。原始 URL、原文文件与改写正文仍逐篇对应；CLI 使用稿另列在准备稿中。普通配置尚未完成，不再作为排除 API 或连接器说明的理由。

| 材料 | 内容 |
| --- | --- |
| API 参考 | 工作区 API、用户会话接口、客户端 MCP、登录流程与 Webhook；按各接口的认证方式使用。 |
| OpenAPI / Swagger | 两个文件均为 OpenAPI 3.0 格式，统一包含最新公开 sitemap 对应的 68 个操作，默认服务地址为 `https://app.counso.ai`。 |
| Postman | 集合与环境文件包含完整请求，分别使用工作区 API key、用户 token 或接口自身的认证参数；凭据值留空。 |
| JavaScript SDK | 使用已发布的客户端包，并在初始化时明确指定 Counso 地址。包名、类名和 API 字段保留可执行的技术标识。 |

[英文 API 入口](en/docs/developer-platform/counso-api-documentation/openapi-and-postman.md) · [中文 API 入口](zh-cn/docs/developer-platform/counso-api-documentation/openapi-and-postman.md)

接口资产现在以最新公开 `swagger.json` 为技术来源，保留 API path、字段、枚举和 `frames` 等技术标识；品牌化仅调整说明文字、服务地址和认证说明。旧版公开的 59 个 `private-*` 页面已随最新 sitemap 移出，新增消费分析导出接口，并按最新规范将 Webhook 路径保留为 `/api/v1/w/{wId}/triggers/hooks/{webhookSourceId}`。

部署时，API 服务和身份服务须使用同一 Counso 环境的配置；这里的文档与格式校验不代表生产接口已逐项调用验收。

Postman 页面提供文件和 URL 导入方式，不再引用原产品的公共集合 ID。若需要一键 Fork 的 Run in Postman 按钮，应从 Counso 管理的公开 Postman 集合生成真实链接；现有集合文件可直接导入使用。

## 不纳入 Counso 的历史内容（9 项）

这些内容属于原产品更新历史、实验仓库导航或已弃用框架，不作为 Counso 使用文档。原文继续保留。

| 原文标题 | 原始 URL | 原因 |
| --- | --- | --- |
| Changelog | [https://docs.dust.tt/docs/changelog](https://docs.dust.tt/docs/changelog) | 原产品的更新历史，不属于 Counso 更新记录。 |
| Dust-Labs repository | [https://docs.dust.tt/docs/developer-platform/dust-labs/dust-labs-repository](https://docs.dust.tt/docs/developer-platform/dust-labs/dust-labs-repository) | 原产品实验仓库的导航说明，不作为 Counso 使用文档。 |
| Creating Google Calendar events from a Dust agent | [https://docs.dust.tt/docs/user-documentation/deprecated/legacy-dust-apps/creating-google-calendar-events-from-a-dust-agent](https://docs.dust.tt/docs/user-documentation/deprecated/legacy-dust-apps/creating-google-calendar-events-from-a-dust-agent) | 已弃用的旧应用框架或其示例，不纳入 Counso 文档。 |
| Allowing an agent to send an email | [https://docs.dust.tt/docs/user-documentation/deprecated/legacy-dust-apps/allowing-an-agent-to-send-an-email](https://docs.dust.tt/docs/user-documentation/deprecated/legacy-dust-apps/allowing-an-agent-to-send-an-email) | 已弃用的旧应用框架或其示例，不纳入 Counso 文档。 |
| Dev : pre-configuring a custom MCP server | [https://docs.dust.tt/docs/user-documentation/deprecated/dev-pre-configuring-a-custom-mcp-server](https://docs.dust.tt/docs/user-documentation/deprecated/dev-pre-configuring-a-custom-mcp-server) | 已弃用的开发端 MCP 预配置方式；现行 MCP 接入说明已保留。 |
| What is a Dust App? | [https://docs.dust.tt/docs/developer-platform/legacy-dust-apps/what-is-a-dust-app](https://docs.dust.tt/docs/developer-platform/legacy-dust-apps/what-is-a-dust-app) | 已弃用的旧应用框架或其示例，不纳入 Counso 文档。 |
| Dust Apps: Core Concepts | [https://docs.dust.tt/docs/developer-platform/legacy-dust-apps/dust-apps-core-concepts](https://docs.dust.tt/docs/developer-platform/legacy-dust-apps/dust-apps-core-concepts) | 已弃用的旧应用框架或其示例，不纳入 Counso 文档。 |
| Build your first Dust App | [https://docs.dust.tt/docs/developer-platform/legacy-dust-apps/build-your-first-dust-app](https://docs.dust.tt/docs/developer-platform/legacy-dust-apps/build-your-first-dust-app) | 已弃用的旧应用框架或其示例，不纳入 Counso 文档。 |
| Core Blocks | [https://docs.dust.tt/docs/developer-platform/legacy-dust-apps/blocks/core-blocks](https://docs.dust.tt/docs/developer-platform/legacy-dust-apps/blocks/core-blocks) | 已弃用的旧应用框架或其示例，不纳入 Counso 文档。 |
