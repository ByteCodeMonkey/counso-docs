---
title: "GitHub"
---
GitHub 工具可让 Agent 搜索代码仓库、Issue 和 Pull Request；获得授权后，也可创建或更新 Issue、评论和 PR。用于同步代码搜索的 GitHub Connection 与实时 GitHub Tool 是两种不同配置。

自托管部署需先由部署管理员注册 GitHub Tool 使用的 GitHub App 和一个或多个 OAuth 应用，并配置相应回调地址。随后，工作区管理员授权已配置的应用、选择其可访问的仓库，并将工具分享给目标 Space。工作区凭据和个人凭据流程可能使用不同的应用。工作区凭据使用为工作区配置的应用身份；个人凭据使用调用者自己的 GitHub 身份，并受其成员权限限制。将 GitHub 加入 Agent，并在指令中明确它可处理的仓库范围。

先读取一份已知仓库文件或 Issue，并核对仓库所有者和名称。创建 Issue 或 PR 前，请 Agent 先概述拟执行的改动和目标仓库。仓库缺失时，检查应用安装范围和实际操作用户的成员身份；完成认证并不等于获得仓库访问权。
