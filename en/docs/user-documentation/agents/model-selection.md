# Choose a model for an Agent or conversation

A model supplies the language and reasoning capability behind an Agent. Choose a model in Agent Builder for a saved default, or in the composer when only the next message needs a different model. The options depend on workspace settings and provider availability.

## Choose in a conversation

1. Open a conversation and select the model control beside the message box.
2. Choose an automatic level, or open **More models** to select an individual model. In some workspaces you can type **/** and choose **Pick model**.
3. Send the message. The composer choice applies to that message only; it does not edit the Agent or affect other members. If you do not choose a model for the message, the Agent uses its configured default.

## Set an Agent's default

Open the Agent in Builder. In **Instructions**, select the model control showing the current choice, choose an available automatic level or a specific model, then save. A specific model remains selected until changed. An automatic level follows its maintained, ordered list of model and reasoning combinations. If one candidate is unavailable for the workspace, the next available candidate in that list may be used. Automatic levels do not inspect each question and select a different level based on its difficulty.

## Automatic levels and access tiers

If offered, **Basic**, **Standard**, and **Premium** are curated automatic choices for different cost and capability needs. These picker levels are not the same as an administrator's model access tiers. Access tiers may control individual models, reasoning efforts, and automatic choices. See [Model access tiers](../admins/usage-seats-and-credits/model-access-tiers.md).

## Reasoning effort and availability

When selecting an individual model, the picker may offer **None**, **Light**, **Medium**, or **High** reasoning effort. Higher effort can take longer and may use more credits. Only options supported by the model and allowed for the workspace appear. If a model is missing, check administrator access, provider or regional availability, and the current workspace plan.
