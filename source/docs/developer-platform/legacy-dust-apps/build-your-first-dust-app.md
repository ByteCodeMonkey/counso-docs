> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Build your first Dust App

<Warning>
  **Dust Apps are deprecated.** Only Dust Apps created before October 2025 are accessible. The creation of new Dust Apps is deactivated. For building on top of Dust, see the [Developer Platform](/docs/developer-platform/overview/developer-platform).
</Warning>

## Prerequisites

You need a Dust workspace and at least one model provider configured. Go to **Providers** from your main account page and set up OpenAI (or another supported provider) with a valid API key.

## Step 1: Create a new app

Go to a Space, click **Company Data** (or another Space), then **Apps**, then **New App**. Give your app a short, memorable name (lowercase, no spaces).

## Step 2: Add an input block

Click **+ Block** and add an `input` block. The `input` block is the entry point to your app. Attach it to a dataset by clicking **Create Dataset**.

In the dataset editor, define a schema matching the inputs your app expects (for example, `currentCompany` and `currentCity` as strings), then add a few example entries. These are used to test your app during design.

## Step 3: Add an LLM block

Click **+ Block** and add an `llm` block. Select your model provider and model. Write a prompt that references your `input` block using Tera templating:

```
Company: {{INPUT.currentCompany}}
City: {{INPUT.currentCity}}

Suggest three alternative companies to work at in the same city:
```

## Step 4: Run your app

Click **Run**. The app executes once per dataset entry. Inspect each block's outputs by clicking on them.

## Step 5: Deploy by API

Once satisfied with your app, retrieve its API endpoint from the **API** panel. Pass inputs as JSON arguments. See the [Developer Platform](/docs/developer-platform/overview/developer-platform) for authentication and API reference.

## Related

* [What is a Dust App?](/docs/developer-platform/legacy-dust-apps/what-is-a-dust-app)
* [Core Blocks](/docs/developer-platform/legacy-dust-apps/blocks/core-blocks)
* [Dust Apps: Core Concepts](/docs/developer-platform/legacy-dust-apps/dust-apps-core-concepts)
