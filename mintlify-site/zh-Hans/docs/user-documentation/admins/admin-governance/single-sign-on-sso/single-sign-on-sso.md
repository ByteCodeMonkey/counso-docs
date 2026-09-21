---
title: "配置单点登录"
---
单点登录（SSO）让成员通过组织现有的身份提供商（IdP）进行身份验证。应由同时有权访问工作区管理区域和 IdP 控制台的管理员配置连接。

## 配置 SSO

1. 在工作区管理区域打开 **People & Security（人员与安全）**，进入 **Domain and Members（域和成员）**，再选择 **Single Sign-On（单点登录）**。
2. 选择 **Activate SSO（启用 SSO）**，并在设置流程中选择身份提供商。
3. 保持设置页打开，按照页面说明在 IdP 中创建 SAML 应用，并填入工作区显示的参数。
4. 完成 IdP 字段配置后，回到工作区保存设置。
5. 使用身份属性与工作区成员信息相匹配的账号测试登录。

SAML 属性和应用配置的详细说明见[SAML 单点登录](/zh-Hans/docs/user-documentation/admins/admin-governance/single-sign-on-sso/saml-sso)。

## 测试后再强制使用 SSO

配置 SSO 后，管理员可以对整个工作区强制启用。这会阻止成员继续使用其他登录方式。强制启用可能会让尚未使用 SAML 的成员退出，因此请先确认测试成员和管理员都能通过 IdP 登录，并为管理员保留恢复方式。
