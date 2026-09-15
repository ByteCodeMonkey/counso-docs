---
title: "Engineering use cases"
---
Engineering teams can use Agents to search technical documentation, explain code or schemas, analyse incident notes, and prepare reviewable drafts. The result depends on which repositories, tools, and environments the workspace has connected.

## Code and system questions

Provide the relevant repository or documentation scope, version, and error context. Ask the Agent to cite files or sections and distinguish what it observed from what it inferred. Treat generated code or commands as suggestions: review and test them in the appropriate environment before use.

## Incident summaries

Give the Agent an approved incident timeline, logs or notes, and the intended audience. Ask it to separate impact, confirmed timeline, contributing factors, unresolved questions, and follow-up actions. Do not let it invent root causes or include credentials and personal data in a report.

## Technical documentation assistant

An Agent can answer repeated questions from an approved set of runbooks, API references, and internal guides. Name the version or service involved and ask for links to the source documents. Assign an owner to maintain the underlying docs when a procedure changes.

## Suggested request

```text
Review these incident notes for service X. Separate confirmed events from hypotheses, cite each item, and propose follow-up checks. Do not conclude root cause or modify code, alerts, or production systems.
```

Repository writes, issue updates, deployments, and incident communications require separately enabled tools and normal engineering review.
