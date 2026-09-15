> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Dust Apps: Core Concepts

<Warning>
  **Dust Apps are deprecated.** Only Dust Apps created before October 2025 are accessible. The creation of new Dust Apps is deactivated. For building on top of Dust, see the [Developer Platform](/docs/developer-platform/overview/developer-platform).
</Warning>

## Blocks

Dust Apps are composed of Blocks executed sequentially. Each block has a name, a type, a specification, and a configuration. Blocks can reference the outputs of previously executed blocks using their name.

See [Core Blocks](/docs/developer-platform/legacy-dust-apps/blocks/core-blocks) for the full block reference.

## Datasets

Datasets are collections of JSON objects used to:

* Provide few-shot examples to `llm` blocks via prompts
* Supply test inputs to `input` blocks during app design

## Inputs and outputs

The `input` block is the entry point to a Dust App. It forks execution on each element of its associated dataset during design, and accepts API arguments at runtime.

Every block produces an output accessible to subsequent blocks as `env.state.<BLOCK_NAME>`.

## Running apps

Apps can be run:

* **In the Dust UI** against a dataset for iterative design
* **By API** by passing arguments to the `input` block (see the [Developer Platform](/docs/developer-platform/overview/developer-platform))

## Execution model

Blocks execute sequentially. The `map`/`reduce` blocks enable parallel execution over arrays. The `while`/`end` blocks enable loops with a termination condition.

## Related

* [What is a Dust App?](/docs/developer-platform/legacy-dust-apps/what-is-a-dust-app)
* [Core Blocks](/docs/developer-platform/legacy-dust-apps/blocks/core-blocks)
* [Build your first Dust App](/docs/developer-platform/legacy-dust-apps/build-your-first-dust-app)
