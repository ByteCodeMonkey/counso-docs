---
title: "连接 BigQuery"
---
BigQuery 连接让助手对指定数仓表执行[表格查询](/zh-Hans/docs/user-documentation/agents/knowledge/table-queries)。连接索引数据集和表名等元数据，不会把整个数仓复制到 Counso；查询结果会返回给助手，用于回答问题或生成图表。

## 准备 Google Cloud 权限

建议使用专门的服务账号。在 **IAM & Admin > Service Accounts** 中创建账号，并授予运行查询及读取目标数据所需的权限。连接配置使用 `roles/bigquery.user` 和 `roles/bigquery.dataViewer`。部分外部存储格式还需要对应底层存储的权限。

在账号的 **Keys** 标签下，选择 **Add Key > Create new key > JSON**。妥善保存下载的密钥，它能用于访问该账号有权读取的 BigQuery 资源。

项目中包含数据集，数据集中包含表。每个数据集有自己的区域或多区域位置；同一查询不能混用不同位置的数据集，例如 US 和 EU。

## 配置 Counso

1. 打开 **Spaces > Connections**，添加 BigQuery，在凭据字段中填入服务账号 JSON 密钥。
2. 选择连接使用的 BigQuery 位置。如果表单还在处理密钥，请稍等片刻。
3. 选择该位置中的数据集和表。
4. 如需让助手理解字段含义，开启 **Use BigQuery descriptions**，使用表和列的描述。
5. 将表分配到相应 Space，再为助手的表格查询能力选择这些表。

一个工作区使用一条 BigQuery 连接和一个服务账号授权。连接凭据能够访问 Google Cloud IAM 授予该账号的全部资源；Space 再按表限定助手可用范围。服务账号权限也应与计划开放的数据集保持一致。

## 检查查询

提问时说明指标和日期范围。通过 **Tools inspection** 查看生成的 SQL 和查询结果，再使用汇总值或图表。查询失败或字段选错时，检查数据集位置、服务账号角色、所选表以及字段描述。
