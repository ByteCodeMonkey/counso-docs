# Use Counso in n8n

An n8n workflow can ask a Counso Agent to process a message or upload a document for later use. Start with the node package and connection settings provided for your Counso deployment.

## Configure the workflow

An n8n administrator installs the node package using the installation method supported by your n8n environment. Create credentials for the intended Counso workspace and restrict access to the workflows that need them.

1. Add a trigger, such as a schedule or a new source record.
2. Add the Counso node and choose the Agent or document-upload operation.
3. For an Agent request, select the shared Agent and map the message and relevant context.
4. For a document upload, select the destination and map the document identifier, title, and content required by the node.
5. Execute a single test and inspect both the n8n output and the result in Counso.

Confirm the node's destination before enabling the workflow. Review retries and record identifiers so a temporary failure does not create duplicate conversations or documents.
