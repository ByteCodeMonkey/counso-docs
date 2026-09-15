> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Core Blocks

<Warning>
  **Dust Apps are being deprecated.** Only Dust Apps that were created before October 2025 are accessible to users. The creation of new Dust Apps is now deactivated.
</Warning>

Dust apps are composed of [Blocks](/docs/developer-platform/overview/developer-platform) which are executed sequentially. Each block produces outputs and can refer to the outputs of previously executed blocks.

For each block we describe its *specification* parameters and *configuration* parameters.

## Input block

The `input` block is the entry point to a Dust app and receives the arguments on which the app is executed, in the form of JSON objects. During the design phase of the app it is associated to a dataset of examples used to iterate on the app. When deployed by API, the `input` block receives the arguments passed to the app by API. When run by API, the dataset to which the `input` block is associated is ignored and replaced by the arguments passed by API.

### Specification

* **dataset**: The dataset of examples to be executed by the app during the design phase. Ignored and replaced by the arguments passed when run by API.

## Data block

The `data` block outputs the dataset it is associated with. Unlike the `input` block it does not fork the execution of the app and simply returns the entire dataset as an array of JSON objects. The `data` block is generally used in conjunction with an `llm` block to output a dataset of few-shot examples to prompt models.

### Specification

* **dataset**: The dataset of examples to be returned by the block as array.

## Code block

The `code` block executes the Javascript code provided by the user. The code must define a function `_fun` which takes as input an `env` variable. `_fun` is executed as the block is run by the app. `code` blocks are generally used to glue other blocks together by postprocessing previous blocks outputs.

### Specification

* **code**: The code to be executed. Exposed as a function named `_fun` taking an `env` variable as argument.

### Properties of the `env` variable

* **state**: An object whose fields are the name of previously executed blocks and values are the output of the associated blocks. The output of a previously executed `EXAMPLE` block can be accessed as `env.state.EXAMPLE`.
* **input**: An object with fields `input` and `index`. `input` is the input object of the current execution stream, *null* if there is no `input` block executed yet. `index` is the index of the current input object in the dataset associated with the `input` block.
* **map**: An optional object set only in the context of a block being executed as part of a `map` `reduce` pair. If set, contains a field `name` set to the name of the current `map` block and a field `iteration` which is the index of the element being executed as part of the `map` `reduce`.
* **config**: The configuration with which the app is currently run. An object whose keys are block names and values are the associated configuration values.

## Chat block (LLM)

The `chat` block provides a standardized interface to chat-based Large Language Models such as OpenAI's `gpt-4o` ([Chat API](https://platform.openai.com/docs/guides/chat)) or Anthropic's `claude-3.5-sonnet`. It has templated instructions that serve as initial prompt and exposes a `messages` code block to output previous messages (generally passed to the app as input). It is used to build chat-based experiences where the model is exposed with previous interactions and generates a new message in response.

### Prompt templating

The `instructions` field of the `chat` block can be templated using the [Tera](https://keats.github.io/tera/docs/#templates) language. This is particularly useful to construct few-shot prompts for models from datasets or previous blocks' outputs. Here's an example of a templated model prompt:

```
{% for e in EXAMPLES %}
EN: {{e.english}}
FR: {{e.french}}
{% endfor %}
EN: {{INPUT.english}}
FR:
```

In this example, for each object in the output of the `EXAMPLES` block (which is an array of JSON objects), create a line with the English sentence and French translation. Then, add a final line with the English sentence from the `INPUT` block output `english` field.

The [Tera](https://keats.github.io/tera/docs) templating language supports a variety of constructs including loops and variable replacement. Please refer to the [Tera Documentation](https://keats.github.io/tera/docs/#templates) for more details.

### Specification

* **instructions**: The instructions are passed to the model as initial *system* role message (see OpenAI's [Chat guide](https://platform.openai.com/docs/guides/chat)). The instructions can be templated using the [Tera](https://keats.github.io/tera/docs/#templates) templating language (see above for more details on templating).
* **messages\_code**: A Javascript function `_fun` which takes a single argument `env` (see the [Code block](#code-block) documentation for details) and returns an array (possibly empty) of messages (but you generally want at least one *user* role message). Messages should be objects with two fields: *role* and *content*. Values should be string. Possible values for `role` are *user*, *agent* and *system*.
* **temperature**: The temperature to use when sampling from the model. A higher *temperature* (e.g. *1.0*) results in more diverse completions, while a lower *temperature* (e.g. *0.0*) results in more conservative completions.
* **stop**: An array of strings that should interrupt completion when sampled from the model.
* **max\_tokens**: The maximum number of tokens to generate from the model for the next message. It can be very broadly seen as a word worth of content. The model may decide to stop generation before reaching `max_tokens`.
* **frequency\_penalty**: Number between *-2.0* and *2.0*. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.
* **presence\_penalty**: Number between *-2.0* and *2.0*. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.
* **top\_p**: An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with `top_p` probability mass. So *0.1* means only the tokens comprising the top 10% probability mass are considered.
* **functions\_code**: A Javascript function `_fun` which takes a single argument `env` (see the [Code block](#code-block) documentation for details) and returns an array (possibly empty) of functions specification objects. Only available for selected OpenAI's models. See the [OpenAI function calling guide](https://platform.openai.com/docs/guides/gpt/function-calling) for more details.

### Configuration

* **provider\_id**: The model provider to use. One of *openai*, *anthropic*, *mistral* or *google\_ai\_studio*.
* **model\_id**: The model to use from the provider specified by `provider_id`.
* **temperature**: An override for the temperature to use when sampling from the model. See the specification section for more details.
* **use\_cache**: Whether to rely on the automated caching mechanism of the `llm` block. If set to *true* and a previous request was made with the same specification and configuration parameters, then the cached response is returned.
* **use\_stream**: In the context of running an app by API. Whether to stream each token as they are emitted by the model. Currently only supported for `provider_id` set to `openai`.
* **function\_call**: If `functions_code` returns a list of functions specifications, `function_call` lets you influence how the model will decide whether to use a function or not. Possible values are `auto`, `none`, `any` or one of your functions' name (forcing the call of that function).

## Map Reduce blocks

The `map` and `reduce` blocks are used to execute the set of blocks in between them on each element of an array, in parallel. The `map` block takes a block name as `from` specification argument. If the output of the block referred to is an array, the execution stream will fork on each element of the array. If the output is an object you can use the `repeat` specification argument to map on the same element `repeat` times.

The `reduce` block does not take any argument and has the same name as its associated `map` block. After executing a `reduce` block, each output of the blocks in between the `map` and `reduce` blocks will be collected in an array accessible from any subsequent block.

Assume we have a **MAPREDUCE** `map` block whose `from` specification argument points to a block whose output is an array of length 4. Assume it is followed by a **DUMMY** `code` block and an associated **MAPREDUCE** `reduce` block, and finally a **FINAL** code block. Also assume that the output of the **DUMMY** block is a simple `{ "foo": "bar" }` object. The **DUMMY** code block will be executed 4 times in parallel, and as we execute the **FINAL** block, `env.state.DUMMY` will contain an array of 4 `{ "foo": "bar" }` objects.

### Configuration

* **from**: The name of the block's output to map on. If the output is an array, the execution stream will fork on each element of the array. If the output is an object the `repeat` specification argument must be specified.
* **repeat**: Only valid if the output of the `from` block is an object. The number of times to repeat the execution of the blocks in between the `map` and `reduce` blocks on the same object.

## While End blocks

The `while` and `end` blocks are used to execute the set of blocks in between them sequentially until a termination condition is met. The `while` block takes a `condition` argument expecting code to be executed at each iteration of the loop. The code must return a boolean value. If the value is `true` the loop continues, otherwise it stops.

The `end` block does not take any argument and has the same name as its associated `while` block. After executing the `end` block, each output of the blocks in between the `while` and `end` blocks will be collected in an array accessible from any subsequent block (see the [Map Reduce blocks](#map-reduce-blocks) documentation for more details on this behavior).

### Configuration

* **condition**: A Javascript function `_fun` which takes a single argument `env` (see the [Code block](#code-block) documentation for details) and returns a boolean value. If the value is `true` the loop continues, otherwise it stops.
* **max\_iterations**: The maximum number of iterations to execute the blocks in between the `while` and `end` blocks. Must be set and has a maximum value of **32**.

## DataSource block

The `data_source` block provides an interface to query a [Datasource](/docs/developer-platform/core-concepts/datasources) and return chunks that are semantically similar to the query provided. When executed, the query is embedded using the embedding model set on the Data Source and the resulting embedding vector is used to perform semantic search on the Data Source's chunks.

The output of the `data_source` block is a list of document objects. Each document may include one or more chunks (only those that were returned from the search). The documents are sorted by decreasing order of the max of their retrieved chunks score. Please refer to the [Datasources overview](/docs/developer-platform/core-concepts/datasources) for more details about how documents are chunked to enable semantic search.

### Specification

* **query**: The query to embed and use to perform semantic search against the data source. The query can be templated using the [Tera](https://keats.github.io/tera/docs/#templates) templating language (see the [Chat block](#chat-block-llm) documentation for more details on templating).
* **full\_text**: Whether to return the full text of the retrieved documents (in addition to each chunk text). If true, each returned document object will have a `text` property containing the full text of the document.

### Configuration

* **top\_k**: The number of chunks to return. The resulting number of document objects may be smaller if multiple chunks from the same document are among the `top_k` retrieved chunks.
* **data\_sources**: An array of objects representing the Data Sources to query. Note that the Dust interface currently only supports adding one Data Source to a block, but you can pass many by API. The objects must have the following properties: `workspace_id`, the id of the workspace who owns the Data Source, and `data_source_id`, the name of the Data Source.
* **filter**: An object representing the filters to apply to the query. The `tags` field is an object with properties `in` and `not`, both arrays of strings (the tags to filter on). The documents' tags must match at least one of the tags specified in `in` and none of the ones specified in `not`. The `timestamp` field is an object with properties `gt` and `lt`. The query will only return chunks from documents whose timestamp is greater than `gt` and lower than `lt`. The timestamp values are represented as epoch in ms. The filter configuration is optional, and each of the fields in `tags` or `timestamp` are also optional.

  Example filter:

  ```json theme={null}
  {
    "tags": {"in": ["tag1", "tag2"], "not": null},
    "timestamp": {"gt": 1675215950729, "lt": 1680012404017}
  }
  ```

  The `tags.in` and `tags.not` values can be templated using the [Tera](https://keats.github.io/tera/docs/#templates) templating language (see the [Chat block](#chat-block-llm) documentation for more details on templating).
