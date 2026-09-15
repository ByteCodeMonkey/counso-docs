> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# The agent is producing links that don't work and falsely claiming something untrue, what's going on?

* Agents are limited to text responses and can't browse the internet or use unapproved tools. They rely on approved data sources and Admin permissions.

* GPT4 and Claude are transformer-based models. They're trained to predict the next word in a sentence using probability, not grammar. For example, if you input 'chair', it predicts the next word based on patterns. But it doesn't really "understand" what a chair is. That's why the agent might sometimes make mistakes or "hallucinate".

* **About links in particular**, we recommend NOT to ask for links in your prompts. Models tend to make them up. Use the citation numbers instead (purple numbers)

* Learn more about how to optimize your prompts in [How to optimize your agents](/docs/user-documentation/agents/troubleshooting-your-agent)
