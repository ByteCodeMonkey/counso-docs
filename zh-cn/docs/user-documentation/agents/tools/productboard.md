# Productboard

Productboard 工具可让 Agent 记录产品反馈并处理备注、功能和相关产品实体，可用于反馈分流、待办事项梳理、路线图规划、研究摘要和依赖关系检查。具体操作受连接账号及 Productboard 字段权限约束。

管理员从 **Spaces → Tools → Add Tools** 添加 Productboard 并完成 OAuth。工具可能支持工作区级或个人用户凭据；请根据当前表单选择。将其分享给目标 Space，再加入 Agent。

## 可用操作

- **Get Configuration**：查看备注和实体类型、必填字段、支持的值和允许的操作。
- **Create Note**、**Update Note**、**Get Note** 和 **Query Notes**：创建、更新、读取或搜索备注，可按来源、负责人、状态、标签和日期筛选。
- **Query Entity**、**Create Entity** 和 **Update Entity**：处理产品、组件、功能、子功能、计划、目标、关键结果、发布、发布组、公司和用户。字段及关系因实体类型而异。
- **Get Relationships**：读取父子、链接、阻塞或被阻塞等关系。

写入前先读取配置，因为不同类型的创建字段和更新操作各不相同。确认目标备注或实体及其关系，改动后回到 Productboard 检查记录。
