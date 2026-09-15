> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# What is a Dust App?

<Warning>
  **Dust Apps are deprecated.** Only Dust Apps created before October 2025 are accessible. The creation of new Dust Apps is deactivated. For building on top of Dust, see the [Developer Platform](/docs/developer-platform/overview/developer-platform).
</Warning>

A Dust App is a chain of one or more prompted calls to models or external services (such as APIs or Data Sources) designed to perform a particular task. A Dust App is an orchestration layer that sits on top of a model to specialize its behavior for a specific task.

## Core idea

The design of a Dust App is the process of defining prompts and chains of large language model calls or external service calls to expose a structured API with predictable behavior. Dust Apps are composed of [Blocks](/docs/developer-platform/legacy-dust-apps/blocks/core-blocks) executed sequentially. Each block produces outputs and can reference the outputs of previously executed blocks.

## Example apps

### Translation (Easy)

Translation can be encoded using a few-shot prompt. A Dust App for translation consists of:

* An `input` block to receive the text to translate
* A `data` block that returns few-shot examples from a dataset
* An `llm` block that parametrizes the call to the model
* A `code` block to process the model output

### Recursive Summarization (Medium)

Recursive summarization handles text that is too long for a single model context. The technique splits the text into chunks, summarizes each separately, then concatenates and produces a final summary.

### Multi-step Research (Advanced)

Multi-step apps chain several model calls, data source queries, and code blocks together to perform complex research or reasoning tasks.

## Related

* [Core Blocks](/docs/developer-platform/legacy-dust-apps/blocks/core-blocks)
* [Dust Apps: Core Concepts](/docs/developer-platform/legacy-dust-apps/dust-apps-core-concepts)
* [Build your first Dust App](/docs/developer-platform/legacy-dust-apps/build-your-first-dust-app)
