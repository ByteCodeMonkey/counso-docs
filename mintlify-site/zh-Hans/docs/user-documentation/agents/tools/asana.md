---
title: "Asana"
---
Asana 工具让 Agent 使用获授权的 Asana 身份搜索和处理任务、项目。根据授予的权限，可读取项目和任务，也可新建或更新任务。

## 管理员配置

在工作区的 **Spaces → Tools** 中添加 Asana，并选择当前表单支持的凭据模式：**Workspace credentials** 使用一套共享账号；**Personal credentials** 则要求每位用户连接自己的账号。完成第三方 OAuth 授权。如果使用自建 Asana OAuth 应用，请采用 Counso 配置表单显示的回调地址，不要复制其他部署环境的地址。

Asana 管理员还需要打开 **My Apps → Manage distribution**，选择允许此应用使用的 Asana 工作区并保存。若漏掉这一步，授权看似成功，Agent 仍可能查不到工作区数据。

将 Asana 加入目标 Agent 后，先读取一个项目和一条任务。开启新建或更新任务前，确认实际操作身份及其项目权限。工具已连接但无数据时，检查应用分发设置、工作区成员身份和用户对该项目的访问权限。
