# Run an Agent from Zapier

A Zap can pass an event from another application to a Counso Agent, then use the response in a later step. For example, a new spreadsheet row can become the input for a short customer summary.

## Set up the Zap

Use the Counso integration supplied by your workspace administrator. You need access to its account connection and an Agent shared with the workspace.

1. Create a Zap and choose the event that should start it.
2. Add the integration's Agent action and connect the intended Counso workspace.
3. Select the Agent. Map the source fields into a clear message, including the task and any context the Agent needs.
4. Set the timezone and the name used for the automated conversation.
5. Test with one source record. Check the response before mapping it into the next action.

Publish the Zap after checking its trigger frequency and destination. Avoid sending the same record through an unfinished test and a live Zap. Agent responses should be reviewed before they are used for consequential updates or customer messages.
