# Use Counso from Google Sheets

The spreadsheet add-on sends a selected range to a Counso Agent and writes the result to a chosen output column. It is useful for short summaries, classifications, and other tasks that can be checked row by row.

## Connect the add-on

Install the Counso add-on provided for your workspace, then open its setup panel from the spreadsheet's **Extensions** menu. Connect the intended workspace using the credentials and connection options supplied by your administrator.

## Process a range

1. Select a small input range.
2. Open the add-on's Agent panel and choose the shared Agent for the task.
3. Confirm the input range and select an output column that does not contain information you need to keep.
4. Add specific instructions and run the request.
5. Compare the returned values with the source rows before processing a larger batch.

Keep requests focused and avoid starting with thousands of rows. Check that the destination column is correct whenever you reuse a sheet. Formula calculations and ordinary spreadsheet edits remain separate from Agent-generated answers.
