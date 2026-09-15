# 筛选 Webhook 负载

筛选条件决定收到的 Webhook 事件是否启动智能体运行。对于受支持的集成，构建器可以根据自然语言描述帮助生成筛选条件。自定义 Webhook 则要使用来源实际发送的负载字段编写表达式。

## 表达式格式

筛选条件使用 Lisp 风格的 S-expression：`(操作符 参数 ...)`。表达式返回 true（处理事件）或 false（忽略事件）。字符串使用双引号；数字和布尔值不加引号；列表用括号括起。

使用以点分隔的路径引用字段，例如 `"action"`、`"issue.state"` 或 `"pull_request.head.ref"`。引用数组对象中的字段时使用 `*`，例如 `"tags.*.name"`。字段路径区分大小写，且必须与 JSON 负载一致。

## 操作符

| 操作符 | 用途 | 示例 |
|---|---|---|
| `and` | 所有子表达式都为真。 | `(and (eq "action" "opened") (eq "issue.state" "open"))` |
| `or` | 至少一个子表达式为真。 | `(or (eq "action" "opened") (eq "action" "edited"))` |
| `not` | 对一个表达式取反。 | `(not (eq "issue.state" "closed"))` |
| `eq` | 精确比较字符串、数字或布尔值。 | `(eq "issue.number" 42)` |
| `starts-with` | 检查字符串是否以指定前缀开头。 | `(starts-with "pull_request.head.ref" "feature/")` |
| `has` | 检查数组是否包含指定值。 | `(has "issue.labels" "bug")` |
| `has-all` | 检查数组是否包含列出的全部值。 | `(has-all "issue.labels" ("bug" "critical"))` |
| `has-any` | 检查数组是否至少包含一个指定值。 | `(has-any "issue.labels" ("bug" "enhancement"))` |
| `gt`, `gte`, `lt`, `lte` | 比较数值。 | `(gte "pull_request.changed_files" 5)` |
| `exists` | 检查字段是否存在且不为 null 或 undefined。 | `(exists "issue.milestone")` |

“不等于”可写作 `(not (eq "field" value))`。starts-with 用于字符串；数值操作符需要数值参数。

## 测试筛选条件

使用应该命中和应该被拒绝的样例负载进行测试，并核对字段名称、类型、大小写、嵌套路径和数组内容。比较是类型安全的：不兼容的类型结果为 false。字段缺失或为 null 时，所有操作都返回 false；唯一例外是 `(not (exists "field"))`，它会返回 true。has-all 或 has-any 使用空列表时返回 false。表达式中的空格和换行不会影响结果。
