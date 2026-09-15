---
title: "Request a structured response"
---
## Before you begin

Define the required fields. A schema constrains shape, not truth; keep human review for decisions and external actions.

## Steps

### Schema envelope

Use the response-schema envelope below when the editor requests the full JSON Schema object. The inner schema is the contract for the returned value.

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

1. Choose list, object, or value and define each field's name, type, and meaning.
2. In the Agent's **Advanced > Structured Response Format** control, choose the schema when the selected model supports it. The control is hidden for unsupported models; if it is absent, describe the format in instructions and validate in your app.
3. Define the unknown convention, add normal and edge examples, and test complete, missing, and multiple-record inputs.
4. Save only after checking types and business meaning.

For this example, a valid response is `{"status":"review","amount":1250.5,"reason":"The source shows an unpaid balance."}`. A missing amount is `null`; a missing reason is invalid because it is required.

## Result

The Agent returns a repeatable shape for the supported configuration, with fields needing confirmation clearly identified.

## Common questions

**Does a schema prevent hallucinations?** No. Require sources or approval for important fields.

**How should unknown values appear?** Use one convention, such as null or an explicit unknown status.

**Why did validation fail?** Check required fields, types, extra properties, and unknown-value handling.
