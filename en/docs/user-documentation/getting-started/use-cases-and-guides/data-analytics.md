# Data analytics use cases

An Agent can help analysts clarify a question, locate schema documentation, draft a query, or explain a result. A live data query is possible only when the workspace provides an appropriate connection and tool with the required permissions.

## Prepare a query

State the business question, date range, entity, metric definition, filters, and expected grain. Provide the relevant schema or data dictionary. Ask the Agent to explain joins and assumptions before running anything.

## Explore a result

Where a read-only query tool is available, begin with a small sample or aggregate. Check the generated query, filters, join keys, null handling, and time zone. Compare important totals with a known report or source system before sharing conclusions.

## Make analysis accessible

For a non-technical audience, ask for a summary that explains the metric, period, exclusions, and limitations in plain language. Keep the query or source reference with the result so another analyst can reproduce it.

## Suggested request

```text
Using the attached schema, draft a read-only query for monthly invoice totals by entity for the last complete quarter. State assumptions about date field, status, currency, and duplicates. Do not run or alter data until I review the query.
```

An Agent’s explanation does not validate a business definition. The data owner or analyst must confirm the metric and query before decisions are made.
