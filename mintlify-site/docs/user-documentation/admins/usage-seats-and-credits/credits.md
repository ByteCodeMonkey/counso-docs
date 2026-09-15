---
title: "Credits"
---
Credits measure usage of AI features in a Counso workspace. A message may consume credits for model processing and for actions such as retrieval, file generation, or connected tools. The exact charge depends on the work performed and the current workspace configuration.

## What contributes to usage

A useful way to understand an interaction is:

`interaction usage = model processing + applicable action charges`

Model usage changes with the amount of text and data the model processes, the model selected, and its reasoning setting. An action charge may apply when an agent uses a tool or another metered capability; the amount depends on the capability and the current configuration. Background agents or other agent runs triggered by a request may contribute to the total as well.

The product displays the cost of a completed interaction in the conversation when usage details are available. Check the displayed breakdown to understand whether a request used model processing, tools, or additional agent runs. Use the usage details shown in Counso as the current reference; rates and allocations can differ between workspaces.

## Credit allocation and reset

Credit allocation, seat names, reset dates, and any carry-over rules depend on the active Counso subscription. Members can check their current usage in **Admin > Usage** or in the usage details shown for their account. Workspace administrators should use the active subscription and the values shown there when explaining a member's available balance.

Credits assigned to an individual are not the same as a shared workspace pool. Whether a member can use both, and the order in which usage draws from them, depends on the workspace configuration. See [Credit management](/docs/user-documentation/admins/usage-seats-and-credits/credit-management) and [Seat management](/docs/user-documentation/admins/usage-seats-and-credits/seat-management).

## Use credits well

Credit usage should be judged alongside the work completed. A well-scoped request can reduce retries and irrelevant searches; a stronger model or deeper investigation may be appropriate when the work calls for it. See [Optimize credit consumption](/docs/user-documentation/admins/usage-seats-and-credits/optimize-credit-consumption) for practical guidance.
