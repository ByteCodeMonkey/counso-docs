---
title: "Ashby"
---
Ashby 可将招聘资料接入 Agent。根据 API 密钥权限，Agent 可搜索候选人和申请、读取职位与报告、查询用户和推荐表单，以及创建候选人备注或推荐记录。

## 配置访问

管理员从 **Spaces → Tools → Add Tools** 添加 Ashby 并输入 API 密钥。在 Ashby Admin 中，为目标招聘工作区创建密钥。原始设置要求：Candidates 读写权限用于候选人搜索、申请详情、反馈、备注和推荐；Jobs 读取用于职位列表；Reports 读取用于报告数据；Organization 读取用于内部用户查询；Hiring Process 读取用于推荐表单。只有确实需要访问时，才授予机密职位或私有字段权限。

配置完成后，将工具加入对应 Agent，并确认密钥属于正确的 Ashby 组织。先进行候选人搜索或读取职位列表。密钥本身有效，不代表它具备所请求对象的权限；结果缺失时检查对应权限类别。创建候选人备注或推荐前，应先核对内容。

## 可用操作

工具集包括候选人搜索、候选人备注、申请详情和面试反馈、推荐表单读取、提交推荐、职位列表、同步报告及用户搜索：`Search Candidates`、`List Candidate Notes`、`Create Candidate Note`、`Get Application Details`、`Get Application Feedback`、`Get Referral Form`、`Create Referral`、`List Jobs`、`Run Synchronous Report` 和 `Search Users`。仅在创建备注或推荐时授予候选人写入权限；Jobs、Reports、Organization 和 Hiring Process 的读取权限分别用于对应查询。
