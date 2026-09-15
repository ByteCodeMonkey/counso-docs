# UKG Ready

UKG Ready 工具支持读取和 PTO 流程，不提供 UKG Ready 全部功能，也不支持 UKG Pro。可用操作包括 **Get My Info**、**View PTO Requests**、**Create PTO Request**、**Delete PTO Request**、**View PTO Request Notes**、**Get Accrual Balances**、**Get Schedules** 和 **Get Employees**。

## 创建并连接 OAuth 应用

在 UKG Ready 中打开 **Settings → Global Setup → Company Setup → OAuth Applications**，创建 **Interactive** 类型应用。UKG 会生成客户端 ID。回调地址填写 Counso 工具设置表单显示的值。在 **Spaces → Tools** 中添加 UKG Ready，并填写实例网址、Company ID 和生成的客户端 ID。Company ID 可从租户网址中识别。将工具分享给获准的 Space，再加入 Agent。

可以新建或取消 PTO 申请；应将这些操作限制在获批的人力资源流程中。员工、额度和排班详情仍受连接的 UKG 用户权限限制。
