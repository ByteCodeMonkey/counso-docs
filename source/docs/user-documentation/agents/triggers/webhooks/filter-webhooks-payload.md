> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Filter webhooks payload

Dust can generate a filter with a Large Language Model to help you determine precisely which events should be triggering your agent, and create new conversation.

Just describe when you want your agent to act, and Dust takes it from here.

For custom webhooks, Dust cannot generate a filter automatically for triggers based on your natural language description. To filter the incoming calls, you'll need to write a filter using a custom syntax.

## Webhook Filter Expression Language

This syntax is described below. To use it and write your filters, you'll need to know the payload that the webhook source will send.

## Overview

The Webhook Filter Expression is a declarative language for filtering webhook payloads based on their JSON content. Filter expressions evaluate to either `true` (the webhook should be processed) or `false` (the webhook should be ignored).

The language uses **Lisp-style S-expression syntax**, where expressions are written as parenthesized prefix notation: `(operator arguments...)`.

## Syntax Basics

### S-Expression Format

All expressions follow the pattern: `(operator argument1 argument2 ...)`

* **Parentheses**: Every expression is wrapped in parentheses
* **Prefix notation**: The operator comes first, followed by its arguments
* **Whitespace**: Arguments are separated by whitespace (spaces, tabs, newlines are all valid)

### Data Types

* **Strings**: Must be enclosed in double quotes: `"value"`
* **Numbers**: Written without quotes: `42`, `3.14`
* **Booleans**: `true` or `false` (no quotes)
* **Lists**: Space-separated values in parentheses: `("option1" "option2" "option3")`

### Field Access

Fields are referenced using **dot notation** to traverse the JSON payload structure:

* Top-level field: `"action"`
* Nested field: `"issue.state"`
* Deeply nested: `"pull_request.head.ref"`
* **Array wildcards**: `"tags.*.name"` extracts the `name` property from each object in the `tags` array

**Example payload:**

```json theme={null}
{
  "action": "opened",
  "issue": {
    "number": 42,
    "state": "open",
    "labels": ["bug", "critical"]
  },
  "tags": [
    {"name": "bug", "id": 1},
    {"name": "feature", "id": 2}
  ]
}
```

Field references:

* `"action"`  `"opened"`
* `"issue.number"`  `42`
* `"issue.labels"`  `["bug", "critical"]`
* `"tags.*.name"`  `["bug", "feature"]`

## Operators

### Logical Operators

#### `and`

Returns `true` if **all** sub-expressions evaluate to `true`.

**Syntax:** `(and expr1 expr2 ... exprN)`

**Example:**

```
(and
  (eq "action" "opened")
  (eq "issue.state" "open"))
```

Returns `true` only if action is "opened" AND issue state is "open".

***

#### `or`

Returns `true` if **any** sub-expression evaluates to `true`.

**Syntax:** `(or expr1 expr2 ... exprN)`

**Example:**

```
(or
  (eq "action" "opened")
  (eq "action" "edited"))
```

Returns `true` if action is either "opened" OR "edited".

***

#### `not`

Returns the **negation** of its single sub-expression.

**Syntax:** `(not expr)`

**Example:**

```
(not (eq "issue.state" "closed"))
```

Returns `true` if issue state is NOT "closed".

### Equality Operator

#### `eq`

Checks for **exact equality** between a field and a value.

**Syntax:** `(eq "field.path" value)`

**Examples:**

```
(eq "action" "opened")           ; String comparison
(eq "issue.number" 42)           ; Numeric comparison
(eq "issue.locked" true)         ; Boolean comparison
```

### String Operators

#### `starts-with`

Checks if a string field starts with a given prefix.

**Syntax:** `(starts-with "field.path" "prefix")`

**Example:**

```
(starts-with "pull_request.head.ref" "feature/")
```

Returns `true` if the branch name starts with "feature/".

**Note:** Only works on string fields.

### Array Operators

#### `has`

Checks if an array contains a specific value.

**Syntax:** `(has "field.path" value)`

**Examples:**

```
(has "issue.labels" "bug")
```

Returns `true` if the labels array contains "bug".

**For arrays of objects, use wildcard paths:**

```
(has "tags.*.name" "important")
```

Returns `true` if any tag object has `name` equal to "important".

***

#### `has-all`

Checks if an array contains **all** specified values.

**Syntax:** `(has-all "field.path" (value1 value2 ... valueN))`

**Examples:**

```
(has-all "issue.labels" ("bug" "critical"))
```

Returns `true` only if the labels array contains both "bug" AND "critical".

**For arrays of objects:**

```
(has-all "tags.*.name" ("bug" "feature"))
```

Returns `true` if tags include objects with both names.

***

#### `has-any`

Checks if an array contains **at least one** of the specified values.

**Syntax:** `(has-any "field.path" (value1 value2 ... valueN))`

**Examples:**

```
(has-any "issue.labels" ("bug" "enhancement"))
```

Returns `true` if the labels array contains either "bug" OR "enhancement" (or both).

**For arrays of objects:**

```
(has-any "tags.*.id" (1 2 3))
```

Returns `true` if any tag has id 1, 2, or 3.

### Numeric Operators

#### `gt` (Greater Than)

Checks if a numeric field is greater than a value.

**Syntax:** `(gt "field.path" number)`

**Example:**

```
(gt "issue.comments" 10)
```

Returns `true` if the issue has more than 10 comments.

***

#### `gte` (Greater Than or Equal)

Checks if a numeric field is greater than or equal to a value.

**Syntax:** `(gte "field.path" number)`

**Example:**

```
(gte "pull_request.changed_files" 5)
```

Returns `true` if the PR changed 5 or more files.

***

#### `lt` (Less Than)

Checks if a numeric field is less than a value.

**Syntax:** `(lt "field.path" number)`

**Example:**

```
(lt "issue.comments" 3)
```

Returns `true` if the issue has fewer than 3 comments.

***

#### `lte` (Less Than or Equal)

Checks if a numeric field is less than or equal to a value.

**Syntax:** `(lte "field.path" number)`

**Example:**

```
(lte "pull_request.additions" 100)
```

Returns `true` if the PR added 100 lines or fewer.

### Existence Operator

#### `exists`

Checks if a field exists and is not null or undefined.

**Syntax:** `(exists "field.path")`

**Example:**

```
(exists "issue.milestone")
```

Returns `true` if the issue has a milestone assigned.

## Common Patterns

### Not Equal

To express "not equal", combine `not` and `eq`:

```
(not (eq "issue.state" "closed"))
```

### Has None

To check that an array contains none of the specified values:

```
(not (has-any "issue.labels" ("wontfix" "duplicate")))
```

### Multiple Conditions

Combine conditions with `and`:

```
(and
  (eq "action" "opened")
  (eq "sender.login" "alice")
  (has "issue.labels" "urgent"))
```

### Any of Multiple Conditions

Use `or` for alternatives:

```
(or
  (eq "sender.login" "alice")
  (eq "sender.login" "bob")
  (eq "sender.login" "charlie"))
```

## Complete Examples

### Example 1: Simple Filter

**Requirement:** Only process when action is "opened"

```
(eq "action" "opened")
```

### Example 2: Multiple Conditions

**Requirement:** Process opened tickets from a specific user

```
(and
  (eq "action" "opened")
  (eq "sender.login" "alice"))
```

### Example 3: Label-Based Routing

**Requirement:** Process issues that have either "bug" or "enhancement" label

```
(has-any "issue.labels" ("bug" "enhancement"))
```

### Example 4: Complex Criteria

**Requirement:** Process opened PRs with more than 20 changed files

```
(and
  (eq "action" "opened")
  (gt "pull_request.changed_files" 20))
```

### Example 5: Advanced Multi-Condition

**Requirement:** Process if:

* Action is "opened" by alice or bob with a critical/urgent label, OR
* Action is "labeled" with both "needs-review" and "backend" labels and more than 5 comments

```
(or
  (and
    (eq "action" "opened")
    (or
      (eq "sender.login" "alice")
      (eq "sender.login" "bob"))
    (has-any "issue.labels" ("critical" "urgent")))
  (and
    (eq "action" "labeled")
    (has-all "issue.labels" ("needs-review" "backend"))
    (gt "issue.comments" 5)))
```

## Important Notes

### Type Safety

* All operators perform type-safe comparisons
* Comparing incompatible types returns `false`
* Example: `(gt "issue.title" 5)` returns `false` because title is a string, not a number

### Non-Existent Fields

* Non-existent or null fields return `false` for all operations
* Exception: `(not (exists "field"))` returns `true` for non-existent fields

### Empty Lists

* Empty lists in `has-all` and `has-any` return `false`
* Example: `(has-any "labels" ())` always returns `false`

### Case Sensitivity

* Field paths are **case-sensitive**
* `"issue.State"` and `"issue.state"` are different fields

### Formatting

* Whitespace and newlines are ignored
* Use indentation for readability in complex expressions

## Best Practices

1. **Keep it simple**: Use the simplest expression that meets your requirements
2. **Be specific**: Reference the most specific fields available to avoid false positives
3. **Test thoroughly**: Verify your filter against sample payloads before deployment
4. **Use wildcards**: Use `.*` notation for arrays of objects instead of complex nested logic
5. **Document complex filters**: Add comments (outside the expression) explaining the logic for complex filters
6. **Prefer `has-any` over multiple `or` statements**: `(has-any "labels" ("a" "b" "c"))` is cleaner than `(or (has "labels" "a") (has "labels" "b") (has "labels" "c"))`

## Testing Your Filters

When writing filters:

1. Start with your JSON payload structure
2. Identify the fields you need to check
3. Write a simple expression and verify it works
4. Incrementally add conditions
5. Test edge cases (missing fields, empty arrays, etc.)

**Example workflow:**

```
Payload: {"action": "opened", "issue": {"labels": ["bug"]}}

Step 1: (eq "action" "opened")
Step 2: (has "issue.labels" "bug")
Step 3: (and (eq "action" "opened") (has "issue.labels" "bug"))
```
