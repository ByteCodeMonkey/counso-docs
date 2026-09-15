# Include data

Use **Include Data** when an Agent needs a selected set of documents to be part of the context for every question. This differs from search: search tries to find the most relevant material for the current question, while Include Data adds the selected source material without ranking it by that question.

## How it selects material

When this action is enabled, the Agent takes documents from its selected data source in reverse chronological order, starting with the most recently updated. It keeps adding the preceding documents until the Include Data context limit is reached. It does not filter documents for relevance to the question.

The Include Data action has its own context limit. It does not exactly match the full context window of the model selected for the Agent. Material beyond that limit is not included in the current run, even if it remains visible in the source.

## When to use it

Include Data can suit a small, focused source where recent items should consistently be considered, such as a stream of product updates or weekly project notes. For example, an Agent could use recent entries from a release-updates source to prepare a weekly summary.

For a large source, or when the question should determine which documents matter, use search instead. Search ranks material for relevance; Include Data prioritizes recency and keeps taking documents until its context limit is reached.

## Important limitations

- The action takes the newest documents first; it does not select the most relevant documents for the question.
- It includes recent source content without a relevance filter. An older document that directly answers the question may be left out when newer material fills the context limit.
- The amount included depends on document size and the action's context limit. A larger source does not mean every document is available in each run.

If your workspace exposes the **Include Data** action, add it to the Agent and select the intended source there. Confirm the source scope and test with a known recent item and an older relevant item, so you can see which material is actually considered.
