# Run an Agent from Make

Use a Make scenario to send information from another application to a Counso Agent. The reply can become input for the following module, such as a draft summary or a classification field.

## Build a scenario

Start with the Counso module and account connection supplied for your workspace. Choose an Agent that is shared with the account used by the scenario.

1. Create a scenario and select the event or schedule that will start it.
2. Add the Counso Agent module and select the correct workspace connection.
3. Choose an Agent and map the incoming fields into its message.
4. Include the relevant timezone and a recognizable conversation name.
5. Run the scenario once with a sample record. Open the module output and check the reply before passing its content to another module.

Review the schedule, error handling, and retry behavior before turning the scenario on. A successful Agent response does not by itself confirm that a later module has saved a record or delivered a message; check that step separately.
