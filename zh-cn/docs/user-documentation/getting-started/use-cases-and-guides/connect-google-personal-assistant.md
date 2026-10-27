# 连接 Google 并使用个人 Google 助手

import { TutorialVideo } from "/snippets/tutorial-video.jsx";

连接自己的 Google 账号，即可使用智能体已配置的 Google 工具。本指南讲解管理员完成工具配置后的个人授权和日常助手使用。

<TutorialVideo videoId="etv-cr1-8vI" title="如何连接个人 Google 账号" language="zh-cn" />

## 连接前

请工作区管理员提供需要的 Google 工具，再使用有权调用这些工具的智能体。管理员的 Google 账号仅用于首次配置，不会因此向其他成员开放该账号的文件、邮件或日历。管理员的应用设置及必要客户端凭据应填写在工具配置中。

管理员配置与支持的操作分别见 [Google Drive](../../agents/tools/google-drive.md)、[Gmail](../../agents/tools/gmail.md) 和 [Google Calendar](../../agents/tools/google-calendar.md)。

## 授权个人 Google 账号

1. 打开与有权使用所需 Google 工具的智能体的对话，让它查找一个已知文件、邮件或日历事件。
2. 智能体首次使用需要你授权的工具时，可能出现连接提示或身份验证错误。点击 **Connect（连接）**。
3. 选择你要使用的 Google 账号，检查请求的权限后完成授权。各工具使用实际连接用户的身份，访问范围取决于该账号的权限；Drive、Gmail 或 Calendar 如分别提示连接，应按各自提示完成。
4. 返回对话。如果智能体没有自动继续，点击 **Retry（重试）** 重新执行刚才的请求。
5. 回到 Google 应用核对原始资料，确认结果来自预期账号。

个人授权用于工具实时操作；同步文件供搜索的 Drive Connection 需要单独配置，见[连接](../../data-sources/connections.md)。

## 使用个人助手

向智能体说明具体任务和范围，例如：

- 在 Google Drive 中查找指定文档，总结重点并给出来源链接。
- 在 Gmail 中查找一封已知邮件，准备回复草稿供你检查。
- 按你的时区总结明天的日历安排。

发送邮件、更改日程或编辑文件前，先检查拟执行的操作、账号和收件人。完成后回到对应 Google 应用核验结果。

## 找不到资料时

检查智能体是否具备对应工具、连接的是否为正确 Google 账号，以及该账号在 Google 应用中是否能访问目标资料。如果缺少写入权限，重新连接相应工具并检查授权请求。若工作区未提供工具，请联系管理员。
