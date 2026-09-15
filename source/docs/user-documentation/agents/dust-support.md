> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Dust Support

> Get help with Dust using public docs, open-source issues, and community knowledge.

Dust Support is a Dust-provided skill that turns your agent into a first line of support for Dust itself. When enabled, the agent answers questions about how to use Dust, its capabilities and limits, or unexpected behavior, and grounds every answer in public Dust sources rather than answering from memory.

<Info>
  The `@dust` agent includes Dust Support by default. When you ask `@dust` a clear support question about the Dust platform, it enables the skill automatically before answering.
</Info>

## How to add it

Dust Support is already available on `@dust`: simply mention `@dust` and ask your support question.

To add it to a custom agent, select the `Dust Support` skill from the **Capabilities** section in the Agent Builder. Agents with [Discover Skills](/docs/user-documentation/agents/discover-skills) can also find and enable it on their own when a support question comes up.

## What it does

When the Dust Support skill is enabled, your agent:

| Capability               | Description                                                                                                                                                                                                                                                                                                         |
| :----------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Grounded answers         | Searches and browses public Dust sources before answering: the [documentation](https://docs.dust.tt), the [open-source code and public issues](https://github.com/dust-tt/dust), and the [Dust community](https://community.dust.tt).                                                                               |
| Request classification   | Distinguishes how-to questions, suspected product bugs, and private matters (billing, security, account recovery), and handles each appropriately.                                                                                                                                                                  |
| Bug report qualification | Checks public GitHub issues for an existing match, then helps you structure a report: reproduction steps, expected vs. actual behavior, visible errors, and environment details.                                                                                                                                    |
| Escalation guidance      | Points you to the right channel: documentation and [Community support on Slack](https://dust-community.tightknit.community/join) for how-to questions, the [public issue tracker](https://github.com/dust-tt/dust/issues) for bugs, and your official Dust support or customer-success channel for private matters. |

The skill uses the Web Search & Browse tool to verify answers against these sources at response time.

## What it doesn't do

Dust Support is deliberately conservative:

* It only relies on public information. It does not inspect your workspace, account, billing state, logs, or any internal Dust system.
* It never invents features, limits, policies, or timelines, and never promises fixes, SLAs, credits, or refunds.
* It does not file GitHub issues on your behalf. Instead, it prepares a report outline you can review and submit yourself.
* If public sources do not answer the question, it says so and tells you which surfaces it checked.

## When to use it

Ask your agent Dust Support questions like:

* "How do I connect Snowflake as a data source?"
* "What is the file size limit for uploads?"
* "Why is my agent not picking up the latest documents from my connected data source?"
* "Is there a reported problem with PDF parsing right now?"
* "Help me prepare a bug report for this error."

For billing, security, or account-specific issues, the skill will direct you to your official Dust support or customer-success channel, since those require access to private account state.
