---
title: "连接 Snowflake"
---
连接 Snowflake 后，助手可直接查询指定表，无需把数仓导入为文档集合。连接保存结构元数据，查询结果会返回给助手。该连接提供表，不提供视图或物化视图。

## 准备只读权限

建议使用独立的角色、服务用户和计算仓库。如果 Snowflake 设置了网络策略，请允许当前 Counso 部署提供的出口地址，不要沿用其他服务的地址白名单。

Warehouse 提供查询计算资源，数据库包含 Schema，Schema 包含表。角色需要 Warehouse、数据库和 Schema 的 `USAGE` 权限，以及目标表的 `SELECT` 权限。例如，按实际资源名称调整以下配置：

```sql
CREATE ROLE counso_reader;
CREATE USER counso_service TYPE = SERVICE DEFAULT_ROLE = counso_reader;
CREATE WAREHOUSE counso_queries
  WAREHOUSE_SIZE = 'XSMALL' AUTO_SUSPEND = 300 AUTO_RESUME = TRUE;
GRANT USAGE ON WAREHOUSE counso_queries TO ROLE counso_reader;
GRANT USAGE ON DATABASE BUSINESS TO ROLE counso_reader;
GRANT USAGE ON SCHEMA BUSINESS.REPORTING TO ROLE counso_reader;
GRANT SELECT ON TABLE BUSINESS.REPORTING.MONTHLY_SALES TO ROLE counso_reader;
GRANT ROLE counso_reader TO USER counso_service;
```

`USAGE` 只允许角色访问容器，并不等于有权读取其中的表。如果要开放整个 Schema，可改为 `SELECT ON ALL TABLES IN SCHEMA`；只有新建表也应开放时，才另加 `SELECT ON FUTURE TABLES IN SCHEMA`。请保持角色只读，写入权限可能导致连接的权限检查失败。

## 配置密钥对认证

按照 Snowflake 的[密钥对配置说明](https://docs.snowflake.com/en/user-guide/key-pair-auth)，生成至少 2048 位的 RSA 密钥对。以下命令生成加密的 PKCS#8 私钥及对应公钥：

```sh
openssl genrsa 2048 | openssl pkcs8 -topk8 -inform PEM -out rsa_key.p8
openssl rsa -in rsa_key.p8 -pubout -out rsa_key.pub
```

将公钥内容去掉 PEM 首尾标记和换行后，设置到服务用户的 `RSA_PUBLIC_KEY`。私钥仅用于连接凭据字段，不应写进文档或仓库。

只有 Snowflake 账号认证策略仍允许时，才可使用密码认证。服务连接优先选择密钥对。

## 建立连接并选择表

在 **Spaces > Connections** 中添加 Snowflake，选择支持的认证方式，填写账号标识、角色、Warehouse 和用户名。使用密钥对时，粘贴包含首尾标记的完整私钥 PEM；私钥已加密时，还需填写口令。连接接受 PKCS#8、加密 PKCS#8 和 PKCS#1 RSA 私钥。使用密码认证时，则填写被账号策略允许的服务用户密码。

点击 **Connect and select tables**，再选择供助手使用的表。表缺失时，检查该表的 `SELECT` 权限，以及上级 Schema 和数据库的 `USAGE` 权限。即使角色可以读取视图，视图也不会出现在此连接中。

提出一个有已知结果的[表格查询](/zh-Hans/docs/user-documentation/agents/knowledge/table-queries)问题。通过 **Tools inspection** 查看 SQL 和结果，也有助于发现连接条件或筛选条件错误。
