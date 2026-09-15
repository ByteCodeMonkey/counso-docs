# The Agent Builder assistant

If your Counso workspace provides an assistant in Agent Builder, it can help draft and refine an Agent. Its suggestions are a starting point: review them before applying changes.

## Create an Agent from scratch

1. Open **New Agent** in Agent Builder and describe the task in plain language. Include who will use the Agent, what sources it may use, and the result it should produce.
2. Answer any clarifying questions. The assistant can draft instructions as inline suggestions and recommend Tools, Skills, and a model.
3. If it offers to inspect workspace knowledge to understand your process, review the requested scope before allowing that search.
4. Review each proposed instruction change. Use **Accept** to apply a suggestion or **Reject** to dismiss it. You can edit the instructions yourself at any time; the form remains available while suggestions are pending.
5. Review capability and model recommendations separately. Add a data source to the Agent only when you intend it to use that source and the relevant audience is allowed to access it.
6. Switch to **Preview** and test a representative request. Continue editing and testing until the output follows the intended process.

## Start from a template

Choosing a template in the gallery opens Agent Builder with the template's context loaded. The assistant can help adapt the initial instructions and suggest relevant Tools or Knowledge. Replace sample assumptions with your actual workflow, review every suggestion, then test in Preview before publishing.

## Improve an existing Agent

Open the Agent in Builder. Where available, the assistant can review its current configuration, feedback, and usage signals, then suggest instruction changes, missing capabilities, or useful Knowledge sources. Suggestions appear for review; they do not change the Agent until an editor applies them. Confirm that a proposed source or capability fits the Agent's intended audience and access before adding it.

## Turn a conversation into an Agent

If a conversation shows **Convert to agent**, you can use it to start an Agent from that conversation. The builder assistant receives the available conversation context and can draft instructions and configuration suggestions from the workflow. Review the result; do not assume every prior tool or source is appropriate for the new Agent.

## What the assistant can and cannot do

When these functions are enabled, the builder assistant can draft or revise instructions, recommend available Tools and Skills, suggest a model, identify Knowledge sources, and help outline a workflow. Some workspaces also let it produce a simple workflow diagram.

The assistant does not replace the Agent editor or Preview. In the documented builder flow, trigger setup remains manual, the assistant can recommend existing Skills but does not create or edit them, and testing still happens in Preview. It evaluates the Agent being edited; it does not design or run a multi-Agent workflow for you.

The assistant can use workspace information for recommendations only within the access available to it. Restricted sources remain out of scope, and a recommended source is not automatically added to the Agent. Check the source list and access settings before saving.

Assistant conversations may be temporary even when proposed edits remain available in the builder. Check the state shown in your workspace before leaving the page, and make sure any change you want to keep has been applied and saved.
