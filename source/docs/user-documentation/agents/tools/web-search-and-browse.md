> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Web Search & Browse

With Dust, you can ask your agents to search through your entire selected Data Sources and pick the most relevant documents to tap into to answer. This is the **“Search”** tool (cf. [Understanding Retrieval Augmented Generation (RAG) in Dust](/docs/user-documentation/agents/llm-best-practices/understanding-rag))

But sometimes, the context you need for your agent to answer your query using outside data found online. Enter the **Web Search & Browse** capability, powering up your agent with capabilities to search and browse on the web to answer with the freshest information.

To enable it, just tick the corresponding box in the "Tools & Data sources" tab.

## Web navigation, how exactly?

When this method is activated, **the agent will search online for the right information by inferring the Google query that it should run, and browse the first few results to answer you with that context.**

Let’s take an example:

Imagine you are creating an agent whose goal is to write cold outreach emails using the latest news of a prospect. This is how the agent will gather information to generate answers to your questions:

1. It will run a Google query with the context of your question
2. Then it will pick the first few websites (up to 10) and browse their content
3. It will then feed this content to the model in the same way we do with datasources.
4. Finally, it will generate a response to the question you asked, taking into account the results from the web search.

## Enhanced Browsing Capability

The Web Search & Browse tool offers multiple format options when retrieving web content. The format is determined  based on the agent message:

* **Markdown format (default):** Clean, readable text content extracted from web pages
* **Raw HTML format:** Access to the complete HTML source code of web pages for detailed analysis
* **Screenshot capability:** Visual capture of web pages (viewport or full page) for visual content analysis. These enhanced capabilities allow your agents to:
  * Analyze website layouts and visual elements through screenshots
  * Parse complex HTML structures and extract specific data elements
  * Capture visual information that text extraction might miss

## When should I use the ‘web search’ option?

This method is particularly useful in scenarios where the data might be coming from several websites and updated regularly: basically, if you believe a Google search is the way to go to get the information needed.

Another again:

You are a VC analyst that wants to keep tracks of fundraises to be able to place your bets on their next rounds. You can create an agent that will search for the last fundraises and categorize them by size.

## **Limitations**

* Because this method is running a web-search, results can sometimes really depend on the current context and your agent can feel like it behaves differently with the same query at different times
* Raw HTML and screenshot features may increase processing time
* Some websites may block automated screenshot capture

## Target specific sites

* If you want to limit the agent to a certain site (news or else) you can tell it to use the `site:{YOUR_SITE_HERE.com}` command specifically

For example : `Use only results from the command site:docs.dust.tt `

And remember when creating an agent, **try different options to check which one suits you best**!
