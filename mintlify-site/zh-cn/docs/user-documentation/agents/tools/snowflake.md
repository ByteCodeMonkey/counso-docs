---
title: "Snowflake"
---
Snowflake Tool 可浏览数据库、Schema、表和视图，并使用选定的 Snowflake 角色执行只读 SQL。可用操作包括 **List Databases**、**List Schemas**、**List Tables**、**Describe Table** 和 **Query**。Query 只接受一个只读 `SELECT` 语句，不接受分号分隔的多语句或写入操作；每次最多返回 1,000 行。

## 创建 OAuth 集成

Account Administrator 在 Snowflake 中创建 confidential custom OAuth Security Integration。使用 Counso 连接表单显示的回调 URI，启用刷新令牌，并通过 Snowflake 支持的密钥查看函数获取客户端 ID 和密钥。必要时，将集成使用权授予目标角色。不要把密钥粘贴到 Agent 提示词中。

## 配置工具

在 **Spaces → Tools → Add Tools** 中选择 Snowflake，填写账户标识、客户端 ID、客户端密钥、Warehouse 和 Role。选择 **Personal** 凭据时，每位用户的角色决定可访问数据；选择 **Workspace** 凭据时，所有使用者共用已配置的服务账号、角色和 Warehouse。个人凭据用户可在 OAuth 时选择获准角色；共享凭据下这些值固定。

先列出数据库并描述目标表结构，再执行查询。当前 Role 控制可访问对象。个人凭据可查询视图并按用户权限隔离；Snowflake Connection 则独立配置，由管理员指定同步表集合，可能适用于更大范围的检索。需要实时查询并遵循角色权限时用 Tool；需要固定同步集合时用 Connection。通过筛选条件控制结果量。
