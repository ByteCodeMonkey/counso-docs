> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshooting your agent

Think of your agent as an intern who improves as you provide more specific and clear instructions. Here’s a guide on how to diagnose issues and adjust settings to improve your agent's performance.

## Common Issues

Below are some key types of issues you may encounter with your Dust agent.

### "It is not finding the right source"

* **Focus on Specific Sources**: Limit the agent's access to the most relevant sources. For example, if you have a ProcessSupport agent, ensure it only has access to the “Process” pages.
* **Prompting**: Provide hints in your prompts, such as “look for documents titled X or that refer to Y.”
* **Knowledge Base Hygiene**: You may sometimes decide to organize your documents or create dedicated channels for specific topics to make information easier to find.

### "It's making things up" ("hallucinating)

* **Select the Right Model**: If your tasks involve complex information, choose a model that is better suited for intricate queries. Check our [blog post on this](https://blog.dust.tt/comparing-ai-models-claude-gpt4-gemini-mistral/)!
* **Adjust Reasoning Effort**: In Advanced settings, set Reasoning effort to Medium or High to encourage more deliberate reasoning. High is slower; Light is faster but can be more superficial.
* **Long Conversations**: Long conversations tend to overflow the model. When you see your agent hallucinating a bit too much, start a new conversation.
* **Use ‘Chain of Thought’ Prompting**: Direct the agent to approach tasks step-by-step (“first do this, then do that”) to ensure clarity in reasoning.
* **Specific Prompting**:
  * Include instructions on what to avoid, such as “do not speculate” or “steer clear of assumptions.”
  * Tell the model it’s okay not to know: models are designed to try and provide an answer even if they don’t have it. Adding, “if you don’t have the answer, just say “I don’t know””

### It's not getting consistent output formats

* **Prompt the Format**: Clearly state how you want the information presented, e.g., “present the data in a table with columns A, B, C.”
* **Provide Examples**: Share examples of the desired outputs to guide the agent's responses.

## How Dust can help you

Make sure you check what we have built for you!

* Use Sidekick to iterate on instructions and troubleshoot behavior with targeted suggestions
* Start from a template to quickly explore a use case; Sidekick will tailor it to your needs
* Test changes in the preview area and iterate until outputs are consistent
