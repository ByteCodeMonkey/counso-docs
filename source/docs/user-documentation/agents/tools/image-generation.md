> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Image Generation

## Overview

Dust agents can generate images from text prompts using the Image Generation capability. This feature allows your agents to create custom visuals based on natural language descriptions, enabling a wide range of creative and practical applications.

What sets Dust's image generation apart is the ability to use **reference images** and run **parallel generations**. Agents can use previously generated images (or uploaded images) as references for subsequent generations, maintaining visual consistency across a series of assets. Combined with parallel execution, this enables complex asset creation pipelines where multiple variations are generated simultaneously.

Your agents can create product photography pipelines, brand asset variations, multi-format marketing campaigns, and visual style transfers on demand.

## How to Enable Image Generation

When creating or editing an agent:

1. In the Agent Builder, click on **Add Tools**
2. Select the **Image Generation** capability
3. Save your agent

That's it! Your agent can now generate images when needed.

## Tool Capabilities

The Image Generation tool provides several configurable options displayed in the UI:

### Quality Settings

Choose between quality levels based on your needs. Higher quality produces more detailed images but takes longer to generate.

| Tool | Description |
| ---- | ----------- |
| `1K` | 1024px      |
| `2K` | 2048px      |
| `4K` | 4096px      |

<Note>
  **Full quality downloads:** For performance reasons, image previews in the
  conversation are compressed. Click the download button to get the generated
  image at maximum quality.
</Note>

### Aspect Ratio Options

Select from multiple aspect ratios to fit your use case:

| Tool          | Description                                                       |
| ------------- | ----------------------------------------------------------------- |
| `1:1`         | Square format for social media profile images and Instagram posts |
| `3:2 / 2:3`   | Classic photography ratio for prints and traditional displays     |
| `4:3 / 3:4`   | Standard format for presentations and product showcases           |
| `4:5 / 5:4`   | Instagram portrait/landscape posts                                |
| `16:9 / 9:16` | Widescreen for YouTube thumbnails and Instagram Stories           |
| `21:9`        | Ultra-wide cinematic format for banners                           |

### Reference Images

Use images from previous tool calls or uploaded images as references for new generations. This maintains visual consistency across multiple outputs, essential for creating cohesive brand assets, product variations, or campaign materials.

<Info>Currently up to 14 references per image generation.</Info>

### Parallel Execution

Agents can run multiple image generations simultaneously. This enables efficient asset pipelines where several variations are created at once, dramatically speeding up workflows that require multiple related images.

<Tip>
  **Power feature:** Combine reference images with parallel execution to create
  entire asset suites in a single conversation. Generate a hero image, then
  request multiple variations simultaneously. The agent handles the pipeline
  automatically.
</Tip>

## How to Use Image Generation

### As a tool in an agent

When the Image Generation capability is enabled, your agent can autonomously decide to generate images when it determines they would be helpful for the task at hand. The agent evaluates your request and uses image generation when it's appropriate to create visual content.

For example, if you ask an agent with Image Generation enabled to "help me design a logo concept," the agent will automatically use the image generation tool to create visual proposals.

### In conversations

You can directly ask any agent with Image Generation enabled to create images in your conversations. Describe what you want to see, and the agent will generate the image for you.

## Safety features

* All generated images are [watermarked with SynthID](https://ai.google.dev/gemini-api/docs/image-generation)
* NSFW and images including celebrities won't be accepted

<Warning>
  **Content policies:** Generated images are automatically filtered for safety.
  Requests for inappropriate content, celebrity likenesses, or NSFW material
  will be declined.
</Warning>

## Advanced Usage

Agents can run multiple image generations **in parallel** and use **reference images** from previous outputs. This lets you build creative pipelines that maintain consistency while producing multiple assets.

<Tip>
  **How it works:** Describe your complete asset needs in a single prompt. The agent automatically identifies what to generate first, what to use as references, and what can be parallelized.

  **Pro tip:** The more specific you are about what should stay consistent (character design, room architecture, product appearance) and what should vary (pose, context, format), the better results you'll get.
</Tip>

### E-commerce: Product Photography Pipeline

```text theme={null}
Create a complete e-commerce photography suite for a premium leather handbag:
1. Female model in a city shot
2. Close-up detail showing leather texture and stitching
3. Lifestyle context shot on a marble surface with sunglasses and coffee
4. Scale reference next to a smartphone
5. Square format version for Instagram feed
Maintain consistent product appearance across all images.
```

### Real Estate: Property Staging

```text theme={null}
Generate a property staging showcase:
1. Base room: modern minimalist living room with large windows, hardwood floors, neutral colors, architectural visualization style
2. Three alternative furniture styles: mid-century modern, Scandinavian minimalist with light wood, and industrial with metal accents
Maintain the exact same room architecture across all variations.
```

## Best Practices

* Be descriptive: Provide clear, detailed descriptions of what you want to see
* Specify style: Mention artistic styles, color schemes, or reference styles when relevant
* Iterate: Don't hesitate to ask for modifications if the first result isn't quite right
* Context matters: Explain the purpose of the image to help the agent make better creative decisions
* Use references strategically: When maintaining consistency matters, explicitly tell the agent which previous image to use as reference
* Use parallel generation: For pipelines requiring multiple assets, describe all variations in a single request to enable parallel execution

<Tip>
  Iteration is key: If the first result isn't quite right, ask the agent to
  refine specific aspects. You can also use the generated image as a reference
  for the next iteration to build on what worked.
</Tip>

For any questions about using Image Generation or Image Editing with your Dust
agents, please contact us at [support@dust.tt](mailto:support@dust.tt)
