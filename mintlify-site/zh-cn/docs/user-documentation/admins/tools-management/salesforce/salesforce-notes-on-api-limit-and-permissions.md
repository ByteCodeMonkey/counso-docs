---
title: "Salesforce 查询限额与访问权限"
---
Agent 请求 Salesforce 信息时，Salesforce 工具会发起第三方查询。它不需要将所有 Salesforce 记录导入工作区，但每次查询和元数据刷新都可能消耗 Salesforce API 额度。可用额度受 Salesforce 版本、许可证、额外购买的额度和组织设置影响；请在 Salesforce Setup 查看当前 24 小时用量和限额，不要依赖通用数字。

## 控制资料边界

查询使用已连接 Salesforce 身份的权限。使用共享凭据时，应采用专用服务账号，并只授予所需对象、字段和记录访问权。使用个人凭据时，则由 Salesforce 按各用户权限控制。还应限制每个 Space 可查询的 Salesforce 对象，让 Space 成员范围和第三方权限共同构成访问边界。

并非所有对象和字段都能自动查询。Salesforce 可能要求配置对象权限、字段级安全、自定义权限或其他设置。自定义字段 API 名通常以 `__c` 结尾；应在 Agent 指令中说明业务特有的字段关系和映射。

## 提高查询可靠性

明确对象、日期范围和返回记录上限。多个 Account 同名时，使用 Account Number 或外部 ID，或请 Agent 先确认目标记录。数据量较大时缩小筛选范围，减少延迟和 API 用量。可在 Salesforce Setup 监控用量，并按需设置阈值提醒。

依赖结果前，检查记录 ID、筛选条件、字段访问和操作身份。登录成功不代表用户能看到所有对象或字段。
