---
title: "Counso 开发者平台"
---
Counso 开发者平台帮助团队将 Agent 接入自己的应用和工作流程。你可以通过 API 以编程方式创建会话并使用工作区数据。[API 参考](/zh-cn/docs/developer-platform/counso-api-documentation/openapi-and-postman)列出了可用请求。在相应开发环境中，也可以使用 JavaScript SDK。

Agent 由模型、指令、工具和公司知识组成。成员可以使用默认 Agent，也可以为具体任务创建自定义 Agent；多个 Agent 可以参与同一会话。模型选择器会显示工作区提供的模型，管理员可以限制成员可选的模型。Conversation 是用户与 Agent 交流请求和结果的地方。Workspace 包含成员和配置；Space 用于组织会话、工具和数据的访问范围。

Counso 通过多种数据源提供信息：会同步第三方内容的托管连接器、供搜索的公开网站、用于上传文档和表格的 Folder，以及通过 API 或导入脚本建立的自定义数据源。连接器按已配置的来源设置同步；在连接器支持的情况下，管理员可以缩小范围，仅纳入特定频道、文件夹或页面。工具则允许 Agent 在连接身份的权限范围内对外部系统执行操作。数据源用于索引内容，供 Agent 搜索或纳入上下文；工具用于执行操作。文件被索引不代表 Agent 获得了修改来源系统的权限，添加工具也不代表该系统中的所有内容都会变得可搜索。

根据配置，Agent 可以搜索资料、按时间倒序纳入最新文档，直到达到模型上下文上限，也可以查询表格或提取结构化数据。例如，可以通过 `POST https://app.counso.ai/api/v1/w/{wId}/assistant/conversations` 创建会话，再向 `/api/v1/w/{wId}/assistant/conversations/{cId}/messages` 发送消息。应用连接到其他 Counso 环境时，请替换基础地址。可用模型、集成和管理能力取决于工作区。开发工具说明见 [JavaScript SDK](/zh-cn/docs/developer-platform/overview/javascript-sdk) 和 [API 参考](/zh-cn/docs/developer-platform/counso-api-documentation/openapi-and-postman)。
