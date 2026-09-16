# Skill examples

A Skill packages a repeatable procedure so several Agents can follow the same rules. These examples show how to describe when a Skill applies, write its guidelines, and add capabilities when the workflow needs them. Adapt the fields and rules to your own systems.

## Example 1: Enter a CRM deal

A sales team can use one shared Skill to keep deal entries consistent across Agents.

**Description**

> This Skill describes how to add a deal to our CRM, including our company's field conventions.

**Guidelines**

```text
Purpose: Format deal details consistently before creating a CRM entry.

Required fields:
- amount_usd: number only, without currency symbols (example: 15000)
- size_bucket: small when below $2,000; big when $2,000 or more
- spqr_stage: suspect | prospect | qualified | ready_to_close
  SPQR is the legacy name for our Sales Pipeline Qualification Rating.
- close_date: YYYY-MM-DD

Example:
Deal name: Acme Corp - Enterprise
Amount: 15000
Size: big
Stage: qualified
Close date: 2026-03-15

Check the threshold: a $1,800 deal is small, not big.
```

If the Skill creates or updates CRM records, add the CRM tool only when it is available and approved for the Agent's users. The Skill supplies procedure; it does not grant account access by itself.

## Example 2: Create branded MiniApps

A team can keep chart and presentation styling consistent with a shared Skill. The example assumes the team already has a MiniApp template saved in an accessible folder.

**Description**

> Use this Skill when creating a MiniApp that should follow our visual identity.

**Guidelines**

Include the team's colors, fonts, layout principles, and what each color means. To refer to a saved template, type **/** in the guidelines editor, search for the template by title, and select it from the picker. Then add any natural-language rules that are not already in the template, such as preferred chart types or how to arrange summary figures.

Add a MiniApp-creation capability only if it is available to the Agent. Test a sample MiniApp and check that it uses the intended template and visual rules.

## Example 3: Keep a consistent company voice

A shared tone Skill can help customer-facing, internal communications, and content Agents use consistent language.

**Description**

> Use this Skill for messages to customers, prospects, or partners. Keep the tone professional and approachable, and reflect our company's values.

**Guidelines**

```text
Purpose: Keep external communications clear and consistent.

Voice principles:
- Clear, not corporate: use simple language and avoid unnecessary jargon.
- Helpful, not robotic: be warm and focus on solving the reader's problem.
- Confident, not arrogant: be direct without talking down to the reader.
- Professional, not stiff: stay approachable.

Prefer: help, use, simple, fix, show, explain, we recommend.
Avoid: leverage, utilize, remediate, and inflated phrases such as
"we would suggest that you might consider."

Keep sentences short, use active voice, put the main point first, and use
sections or bullets for long messages.

For customer support, acknowledge the problem and state specific next steps.
For product updates, lead with the user's benefit.
For sales, explain outcomes and ask questions before recommending a solution.

Bad: "We are pleased to inform you that the requested functionality has been
implemented pursuant to your feedback."
Better: "Good news: the feature you asked for is ready. Here's how to use it."
```

This Skill is about communication guidance, so it may not need a Tool. If the Agent needs examples from past email or support messages, add an approved mail or customer-support Tool and confirm its access separately.
