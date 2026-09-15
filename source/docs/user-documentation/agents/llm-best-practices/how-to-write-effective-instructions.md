> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# How to write effective instructions

To really make the most of your Dust agents, you need to learn how to instruct them and communicate with them effectively. And that's where the art of crafting effective prompts comes in.

Instructions are like the secret handshake between you and your AI agents. They set the stage for the entire conversation and can make a huge difference in the kind of responses you get back. Basically, if you want your agent to give you high-quality, relevant, and useful information, you've got to do the work.

In this tutorial, we'll explore:

1. What prompts are
2. How to write great prompts
3. A framework to structure your instructions

**Prompts** are the instructions and context you provide to a Large Language Model (LLM) to guide its responses and outputs. Think of prompts as your way of communicating your intent to the AI. The better you are at expressing what you want, the more likely the AI will be able to deliver it.

**Agent's instructions** are structured prompts you give your agents to answer to a recurring use case or need - like writing an email, a blog post or a documentation.

Tip: You can use Sidekick to help structure and refine these instructions from a blank page or a template.

Those instructions are the constitution or **the soul of your agent.** You can update those instructions, and the agent will have those instructions in memory whenever you use it.

The key thing to understand is that working with AI doesn't require deep technical skills. You don't need to be an engineer - you just need practice communicating with AI like you would another person.

* **Be specific:** Clearly articulate your intent. Don’t write prompts like you would write a Google query with keywords. The more precise your ask, the better the AI can address it. Vague, open-ended or too complex prompts lead to unfocused responses.
* **Provide context:** Give the AI relevant background information to work with. This could include details about the topic, audience, desired format, etc. More context allows the AI to tailor its response.
* **Use examples:** Showing is often better than telling. Provide examples of what you're looking for to give the AI a template to work from.
* **Adopt a persona:** Assigning the AI a specific role or persona in your instructions can yield outputs better fit for purpose. An AI acting as a "teacher of engineering students" will respond differently than one acting as a "sales representative."
* **Break it down:** For complex tasks, guide the AI step-by-step with what is called "chain-of-thought" instructions. This makes the AI's reasoning more transparent and debuggable.
* **Read your instructions:** as if you were a contractor tasked for this project. If you understand it, the model will understand as well. If not, the model won’t either.
* **Iterate:** If the output isn't quite right, tweak your prompt or instructions and try again. View prompting as a conversation.

When you give instructions to an agent, you should **be concise and use simple and direct language, avoiding ambiguous words.** AI lacks built-in context, so guiding it with detailed prompts is crucial.

This not only improves immediate results but also helps in developing smarter AI systems over time.

**Designing an agent is like crafting a new product.**
Start by understanding your users and their questions. This insight will guide how you set up and instruct your agent.

If you want to share knowledge with your agent and connect some data sources or connections, remember: The more data you give access to an agent, the lower the chance of retrieving the correct information at the right time.

## Framework to write good Instructions

*Follow this framework to structure the instructions of your agents.*

* **Role and goal:** role and goal-based constraints limit the AI to a narrower, more appropriate range of responses
* **\[optional]** **Step-by-step instructions:** if relevant, explain the steps your agent will have to follow to walk users through the process - i.e., “When the user asks you a question, start by asking them if they want A or B.” If instructions are easy for someone else to understand (who is unfamiliar with your specific request or domain), then the AI is more likely to understand your instructions.
* **Expertise:** this is the most important part; your knowledge and viewpoint are key to helping the AI action. Figure out what you want the agent to do and how it differs from its default behavior, which is generating text.
* **Constraints:** they are rules or conditions that guide the behavior of the agent in its interactions with the user - i.e., “only ask one question at a time”, “reply in bullet points”, “reply in French only,”….
* **Specific output.** there are many outputs that you can request: an explanation, a table, or an SQL query. Experiment with different approaches, and you might be surprised.
