# Use Counso in Power Automate

A Counso custom connector can be used in Power Automate flows to request an Agent response or upload a document. Your administrator provides the solution package and the connection details for the intended workspace.

## Install and connect

The person importing the solution needs permission to create resources in the selected Power Platform environment. Confirm the licensing requirements for custom connectors with your Power Platform administrator.

1. Open the target environment and import the supplied solution from **Solutions**.
2. Open its custom connector and create a connection using the authentication settings documented with the package.
3. Test the operation with a short message or a small document.
4. Check the actual conversation or document in Counso, then share the connector with the people who need it.

## Add it to a flow

Select the connector action, choose the workspace connection, and map the required fields. Test the complete flow before enabling it. When importing an updated solution, check existing connections and flows again; a successful import alone does not verify their results.
