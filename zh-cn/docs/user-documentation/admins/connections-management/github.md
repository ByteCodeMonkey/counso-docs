# 连接 GitHub

GitHub 连接让助手能够检索仓库的 Issue、Discussion 和 Pull Request 对话。代码同步可单独开启，读取仓库默认分支中的源文件。

## 安装与配置

部署管理员需要先注册并配置当前 Counso 部署使用的 GitHub App，包括对应的回调和 Webhook 地址。GitHub 组织所有者或管理员需有权将该应用安装到要连接的仓库。

1. 使用 Counso 管理员账号打开 **Spaces > Connections > GitHub**，点击 **Configure**。
2. 完成 GitHub 授权，并安装当前部署配置的应用。
3. 在 **Repository access** 中选择需要连接的仓库。
4. 如需索引代码，为相应仓库开启 **Code synchronization**，然后保存。

连接请求读取仓库内容、Issue、Discussion、Pages、项目和 Pull Request 的权限。请确保安装的应用及连接账号持续有权访问所选仓库。

## 索引范围

| 内容 | 包含范围 |
| --- | --- |
| Issue | 标题、描述、评论和标签。 |
| Discussion | 标题、首帖和评论。 |
| Pull Request | 标题、描述和顶层评论，不包含代码行内的评审评论。 |
| 已开启同步的代码 | 默认分支中的文件，超过 4 MiB 的文件会跳过。 |

连接不提供完整的提交历史归档。如果助手需要实时操作仓库，请另外配置合适的 GitHub 工具。

## 调整连接范围

在 Connections 中找到 GitHub，点击 **Manage**，通过数据或权限设置调整所选仓库；如有提示，重新授权并保存。即使仓库仍显示在 Counso 设置中，在 GitHub 撤销应用访问也会阻止后续同步。

Issue、Discussion 和 Pull Request 会持续同步。代码约每八小时刷新一次，因此刚提交的修改可能尚未出现在搜索结果中。

## 按标签检索

Issue 和 Pull Request 的标签会一起同步，还会补充标题、是否为 Pull Request 和作者等标签，例如 `title:Fix search`、`isPullRequest:true`、`author:@alex`。可在[知识搜索](../../agents/knowledge/search-data-sources.md)中用它们缩小范围。
