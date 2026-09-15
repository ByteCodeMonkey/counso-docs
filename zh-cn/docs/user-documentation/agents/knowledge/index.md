# 智能体的 Knowledge（知识）

Knowledge 设置决定智能体可以使用哪些资料，以及如何检索这些资料。根据问题选择合适方式；可用能力和来源类型取决于工作区配置。

| 方法 | 适用问题 | 工作方式 |
|---|---|---|
| **Search（搜索）** | 在连接来源中查找相关段落 | 按含义搜索选定内容，并为回答返回相关片段。通常适合政策、主题或背景问题。 |
| **Include Data（纳入数据）** | 每次运行都提供近期来源资料 | 从最新文件开始纳入，直到达到上下文上限；不会按当前问题的相关性排序。 |
| **Query Tables（查询表格）** | 计数、汇总、筛选、比较等结构化分析 | 在可用时先查询已选的结构化表格，再由智能体解释结果。 |
| **Extract Data（提取数据）** | 从多个文档中收集指定字段 | 搜索已选来源，并按定义或生成的 Schema 提取信息。 |

在 Agent Builder 中选择需要的数据源，并说明其中的内容，帮助智能体选择合适操作。Search 和 Include Data 针对选定文档；Query Tables 面向结构化行数据；Extract Data 用于跨来源一致地收集字段。

具体操作见[搜索数据源](search-data-sources.md)、[Include Data](include-data.md)、[表格查询](table-queries.md)和[提取数据](extract-data.md)。
