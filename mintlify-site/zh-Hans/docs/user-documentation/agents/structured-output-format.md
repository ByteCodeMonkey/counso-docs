---
title: "要求结构化响应"
---
## 前提

先定义字段。结构化格式约束形状，不保证事实；重要动作保留人工复核。

## 步骤

### Schema 外层格式

如果编辑器要求完整 JSON Schema 对象，可使用下面的外层格式；其中的 schema 是回答值的实际契约。

```json
{
  "type": "json_schema",
  "json_schema": {
    "name": "invoice_check",
    "strict": true,
    "schema": {
      "type": "object",
      "properties": {
        "status": { "type": "string", "enum": ["clear", "review"] },
        "amount": { "type": ["number", "null"] },
        "reason": { "type": "string" }
      },
      "required": ["status", "amount", "reason"],
      "additionalProperties": false
    }
  }
}

```

1. 确定列表、对象或单值，并定义字段名称、类型和含义。
2. 如果所选模型支持，在智能体的 **Advanced > Structured Response Format** 控件中选择 Schema。不支持的模型不会显示该控件；如果没有控件，就在指令中写格式并由应用校验。
3. 统一未知值表达，加入正常和边界样例。
4. 用完整、缺失和多记录输入测试类型和含义后保存。

上例的有效结果可以是 `{"status":"review","amount":1250.5,"reason":"来源显示仍有未付余额。"}`。金额缺失用 `null`，但 reason 是必填字段，缺失时应判为无效。

## 结果

当前支持的配置会返回可重复结构，复核者知道哪些字段仍需确认。

## 常见问题

**Schema 能防止幻觉吗？** 不能，重要字段仍需来源或审批。

**未知值怎么写？** 统一使用 null 或明确未知状态。

**为什么校验失败？** 检查必填字段、类型、多余属性和未知值处理。
