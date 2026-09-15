# Why is a table analysis incomplete or incorrect?

First check that the Agent has access to every table or file involved. For CSV or spreadsheet input, confirm the first row contains column names and that introductory notes are not mixed into the data rows.

If tables are related, explain their keys and relationships explicitly, such as “match invoice rows to suppliers using supplier_id.” Ask the Agent to show the rows and assumptions it used, then verify a small sample before relying on totals.

For Notion databases, a table view does not automatically include its related databases. Make sure every related database used by a Relation or Rollup property is also within the Agent's available data scope.
