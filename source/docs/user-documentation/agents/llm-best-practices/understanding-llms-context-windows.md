> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Understanding LLMs Context Windows

At Dust, we're passionate about making work work better. As we dive into the world of AI agents, it's crucial to understand the concept of context windows and how they impact the performance of large language models (LLMs). Let's explore this topic together, focusing on how it relates to creating effective AI agents with Dust.

## What's a Context Window?

A context window is the maximum number of tokens an LLM can process at once. Think of it as the AI's short-term memory capacity. When you create a conversation with your agent, it means both the input (your questions, instructions, and retrieved data sources) and the output (the agent's response) will be included in the context window of the model you choose to set for your agent.

Here's how it works in practice:

1. Text is broken down into tokens (roughly 4 characters each; see the picture below).
2. The LLM processes these tokens, considering the input and any relevant training data.
3. It then generates an output based on what it deems the most likely continuation.

## Why Context Windows Matter When You Use Dust

When you're creating custom agents with Dust, understanding context windows helps you design more effective tools. Here's why:

1. **In-conversation information retention**: With a bigger context window, your agent can recall more details from earlier in the conversation, leading to more consistent and relevant responses.

2. **Data processing**: When using the `Use most recent` tool, a larger context window enables agents to process and analyze more extensive documents or datasets, expanding their capabilities.

3. **Conversation management**: We recommend starting new conversations for distinct topics or tasks. This practice helps avoid extended conversations that can overflow the context window of the models, ensuring optimal performance and preventing potential errors or inconsistencies in responses.

## Context Windows in Popular LLMs

Dust gives you access to various LLMs, each with different context window sizes. Among the popular ones, here are the ones with the largest context windows:

* Claude 4 Sonnet and 3.7 Sonnet: 200,000 tokens
* GPT-4.1: 1,000,000 tokens
* Gemini 2.5 Pro and 1.5 Pro: Up to 1 million tokens

## Balancing Act: Pros and Cons of Large Context Windows

While larger context windows offer benefits, they're not always the best choice. Here's what to consider:

### Advantages:

* More detailed conversations
* Reduced likelihood of AI "hallucinations" or made-up information
* Ability to process larger documents or datasets

### Challenges:

* Increased processing time and costs
* Potential for information overload
* Risk of conflicting information leading to inconsistent responses

## Optimizing Your Dust Agents

When designing custom agents in Dust, keep these tips in mind:

1. **Quality over quantity**: Focus on providing relevant, high-quality information rather than overwhelming the agent with unnecessary data.

2. **Clear instructions**: Spend time designing your instructions and giving your agents precise guidelines and objectives.

3. **Appropriate model selection**: Choose the LLM that best fits your specific use case, way of prompting, and consideration of context window size and other factors.

4. **Manage conversations wisely**: Remember to encourage your users to start new conversations for different topics or tasks to prevent context window overflow. This approach ensures your agent maintains accuracy and relevance throughout interactions.
