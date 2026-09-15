---
title: "Filter webhook payloads"
---
A filter decides whether an incoming webhook event starts an Agent run. For a supported integration, the builder can help generate a filter from a plain-language description. For a custom webhook, write an expression using fields in the payload sent by that source.

## Expression format

Filters use Lisp-style S-expressions: `(operator argument ...)`. An expression evaluates to true (process the event) or false (ignore it). Put strings in double quotes; write numbers and booleans without quotes. Lists use parentheses.

Refer to fields by dot-separated paths, such as `"action"`, `"issue.state"`, or `"pull_request.head.ref"`. Use `*` for fields inside objects in an array, for example `"tags.*.name"`. Field paths are case-sensitive and must match the JSON payload.

## Operators

| Operator | Purpose | Example |
|---|---|---|
| `and` | All nested expressions must be true. | `(and (eq "action" "opened") (eq "issue.state" "open"))` |
| `or` | At least one nested expression must be true. | `(or (eq "action" "opened") (eq "action" "edited"))` |
| `not` | Negates one expression. | `(not (eq "issue.state" "closed"))` |
| `eq` | Tests exact equality for strings, numbers, or booleans. | `(eq "issue.number" 42)` |
| `starts-with` | Tests whether a string begins with a prefix. | `(starts-with "pull_request.head.ref" "feature/")` |
| `has` | Tests whether an array contains a value. | `(has "issue.labels" "bug")` |
| `has-all` | Tests whether an array contains every listed value. | `(has-all "issue.labels" ("bug" "critical"))` |
| `has-any` | Tests whether an array contains at least one listed value. | `(has-any "issue.labels" ("bug" "enhancement"))` |
| `gt`, `gte`, `lt`, `lte` | Compare numeric values. | `(gte "pull_request.changed_files" 5)` |
| `exists` | Tests whether a field exists and is not null or undefined. | `(exists "issue.milestone")` |

To test “not equal,” use `(not (eq "field" value))`. starts-with applies to strings; numeric operators require numeric values.

## Test a filter

Test with sample payloads that should match and should be rejected. Check field names, types, capitalization, nested paths, and array contents. Comparisons are type-safe: incompatible types evaluate to false. Missing or null fields evaluate to false for every operation except `(not (exists "field"))`, which evaluates to true. Empty lists passed to has-all or has-any evaluate to false. Whitespace and line breaks do not affect an expression.
