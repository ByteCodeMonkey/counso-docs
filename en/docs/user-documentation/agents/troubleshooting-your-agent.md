# Troubleshoot an Agent

When an Agent behaves unexpectedly, identify the symptom first and change the smallest relevant part of its setup. Use Preview to compare results after each change.

| Symptom | What to check | What to try |
|---|---|---|
| The Agent cannot find the right source | Confirm the intended source, folder, channel, or Space is selected and that the user and Agent can access it. Check whether a label filter excludes the document. | Narrow the source list to relevant material. In the prompt, name the document or topic to search for. Improve source organization where needed. |
| The Agent makes up details | Check whether the answer is supported by retrieved material, whether the source set is too broad, and whether the conversation is very long. | Ask it to cite the source and state when evidence is missing. Add an example or a constraint such as “do not assume missing values.” Start a fresh conversation for a new task. For complex work, test a more capable available model or reasoning setting. |
| The answer format changes between runs | Check whether the requested format and required fields are explicit. | Specify the output structure, for example a table with named columns, and include a good example. Test more than one input. |

## Use the builder to iterate

Sidekick can help refine instructions with targeted suggestions. You can also start from a template. Apply suggestions selectively, then test them in Preview with the same representative request. If a setting or source is unavailable, ask a workspace administrator to check the Agent's permissions and configuration.
