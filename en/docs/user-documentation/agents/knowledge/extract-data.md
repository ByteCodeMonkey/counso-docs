# Extract Data

If available in your workspace, the **Extract Data** action lets an Agent extract structured information from a large selection of data sources over a time frame. It returns a list of objects following a schema, which the Agent can use to prepare an answer. The action can process up to 500,000 tokens of source data; the available limit may depend on workspace configuration.

This action is useful for recurring summaries from mailing lists or for extracting structured fields from a stream of support interactions. It complements search, which retrieves relevant passages without guaranteeing that the entire source set was processed, and **Include Data**, which is limited by its own context capacity and is intended for recent material.

## Configure Extract Data

1. In Agent Builder, add the **Extract Data** action if it is available.
2. Select the data sources to process, as you would for a search action. Common sources include a Slack channel, a folder populated by an integration, or a support-ticket source. Use only sources connected to your workspace and accessible to the Agent's audience.
3. Open **Advanced Settings** if you need additional controls.
4. Choose a time frame. By default, the action can use the period implied by the conversation. Enable manual selection when the task requires a specific range.
5. Define the extraction schema when the output needs stable fields. Enter a JSON Schema directly, or use **Generate** to draft one from your instructions and then edit it. If you omit a schema, the action derives a structure from the conversation context.
6. Save the Agent and test a small period with known records. Check the returned objects against their source before expanding the date range.

## Write useful extraction instructions

Tell the Agent what to extract, how to handle repeated items, and what to do when a field is missing. For example, a weekly support summary might group interactions by company, merge multiple contacts for the same company, and return a concise highlight, open issues, and stated requirements. Do not fill gaps from similar records; leave absent values empty or use the convention defined by the schema.

The output can be inspected before the Agent synthesizes its final answer. Ask it to preserve source identifiers and distinguish extracted facts from its summary. Extract Data can take longer than an ordinary search because it processes a larger source window. A configured schema controls the output shape; it does not guarantee that every extracted value is correct or complete.
