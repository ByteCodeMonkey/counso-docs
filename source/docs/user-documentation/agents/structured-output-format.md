> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Structured output format

## How to configure

* Open the agent builder
* Click Advanced > Structured Response Format
* Paste a valid JSON schema
* Click Save

## Schema format

The schema must follow this structure:

```json JSON format theme={null}
{
  "type": "json_schema",
  "json_schema": {
    "name": "your_schema_name",
    "strict": true,
    "schema": {
      "type": "object",
      "properties": {
        "property1": { "type": "string" },
        "property2": { "type": "number" }
      },
      "required": ["property1", "property2"],
      "additionalProperties": false
    }
  }
}
```

## Example

A schema to extract city information:

```json structured output format example theme={null}

{
  "type": "json_schema",
  "json_schema": {
    "name": "city_info",
    "strict": true,
    "schema": {
      "type": "object",
      "properties": {
        "country": { "type": "string" },
        "state": { "type": ["string", "null"] },
        "city": { "type": "string" },
        "zipcode": { "type": "string" }
      },
      "required": ["country", "state", "city", "zipcode"],
      "additionalProperties": false
    }
  }
}
```

## Supported models

Not all models support structured output. The option only appears in the Advanced menu when the selected model supports it.

Model supporting it:

* Chat GPT 5 and following versions
* Sonnet and Haiku starting with version 4.5
* Gemini 3.0 and following versions
