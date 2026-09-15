> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Read images

Dust has introduced a new feature called Vision, enabling users to send images to Dust agents for analysis using company data. You can use it for tasks like visual content analysis and brand compliance checking.

You can find it in the attachment icon which used to only accept text files (pdfs, etc) but now accepts images as well.

## How Vision Works

With Vision, you can now:

* Send images to your Dust agents
* Analyze images in the context of your company's data
* Get detailed feedback on visual elements

## Example Use Case: Brand Compliance Checking

Let's explore a practical example of how Vision can be used for brand compliance checking.

### Setting Up

1. Have your brand guidelines document available in your Dust datasources.
2. Create a specialized agent (like "BrandGuard") trained on your brand guidelines.
3. Configure the agent to analyze images against these guidelines.

### Using the BrandGuard Agent

1. Capture a screenshot of the website or visual asset you want to analyze.
2. Open Dust and select your BrandGuard agent.
3. Upload the screenshot to the chat.
4. Send the message to initiate the analysis.

### Analysis Process

The agent will:

1. Examine the uploaded image
2. Compare it to the brand guidelines in its knowledge base
3. Provide a detailed analysis of compliance and discrepancies

### Example Output

The agent might provide feedback on:

* Color usage and differences from brand guidelines
* Typography inconsistencies
* Layout elements that don't adhere to standards
* Recommendations for improvements

## Potential Use Cases

Vision in Dust opens up numerous possibilities:

* Brand consistency checks across digital assets
* Product image analysis for e-commerce
* Visual content moderation
* Design feedback and iteration

## Getting Started

To start using Vision with your Dust agents:

1. Ensure the model you use has vision capabilities: Only GPT4o and Claude currently have it.
2. Prepare relevant visual guidelines or datasets
3. Create or modify an agent to handle image analysis tasks
4. Test with sample images to refine the agent's performance

Remember, the effectiveness of your Vision-enabled agent depends on the quality and specificity of the data it's trained on. Don't hesitate to iterate and improve your agent's knowledge base for better results.

For any issues or questions while building your Vision-enabled agents, please reach out to the Dust support team.
