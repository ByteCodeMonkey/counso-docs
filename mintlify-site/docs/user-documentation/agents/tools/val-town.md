---
title: "Val Town"
---
The Val Town tool connects an Agent to Vals and files available in the authorized Val Town account. Depending on the enabled operations, it can list and search Vals, read files, create or update code, delete files, and call HTTP endpoints.

Add Val Town from **Spaces → Tools**, complete OAuth with the intended account, share it with the relevant Space, and add it to an Agent. Check the connected account before using the tool. Start with `list vals`, `get val`, or `list val files` to identify the target and inspect existing code.

Operations such as running a Val, writing files, deleting content, or calling an HTTP endpoint can have effects outside the conversation. Review the code and endpoint before running it, specify the exact Val/file, and confirm the expected result. If a Val appears but its files or endpoint are missing, check ownership and account permissions. Do not treat successful authentication as approval to run arbitrary code.

## Available operations

The tool supports creating a Val, retrieving/listing/searching Vals, listing files, reading file content, creating or writing files, updating or deleting files, and calling an HTTP endpoint. Serverless functions may be deployed and executed as a result. Configure the provider token with read and write access to Vals using the workspace's protected secret mechanism; do not paste it into the conversation.
