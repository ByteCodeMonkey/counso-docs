# Upload documents with Zapier

A Zap can turn a source event into a document in Counso. For example, a new support ticket can be formatted into text and added to a folder used by an Agent.

## Prepare the destination

Choose the Counso Space and folder that should contain the imported material. Check who can read that location before connecting customer records. Use the Counso Zapier integration and credentials supplied for the workspace.

## Create the Zap

1. Select the source application and trigger, then test the source event.
2. Add the integration's document-upload action and choose the Counso connection.
3. Select the destination folder. Map a stable document identifier, a readable title, and the content needed by the Agent.
4. Test with one record and open the resulting document in Counso.
5. Confirm the content and destination, then enable the Zap.

Check how the action handles an existing identifier before relying on repeat runs. An upload trigger does not automatically synchronize later edits or deletions in the source application; those require their own supported workflow.
