# Salesloft

The Salesloft tool lets an Agent retrieve cadence actions and related sales context, such as tasks and people. Available operations depend on the connected account, key scopes, and current tool configuration.

In Salesloft administration, create or select an API key for the intended account owner and enable only the cadence, task, people, and activity scopes needed. In **Spaces → Tools**, add Salesloft, enter the key, choose the credential ownership mode shown by the form, and share it with the relevant Space. Add the tool to the Agent.

Start with a read of one cadence and one task. Before changing an activity or task, confirm the account identity, record ID, and intended change. Read the record back after the update. A key can authenticate successfully while lacking access to a cadence or task; check the specific API key scopes and account ownership when data is missing.

## Available operations

Available tools include `List Actions` and `Get Action`. The API key requires `cadences:read`, `people:read`, `team:read`, and `calls:read` for the documented retrievals. Connect the account that owns the required cadence data and start by listing actions within the intended account scope.
