> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Google Sheets Add-on

<Tip>
  **The Dust Google Sheets Add-on is officially available on Google Workspace
  Marketplace.** Connect Dust to your spreadsheets in just a few clicks:
  [Install from
  Marketplace](https://workspace.google.com/marketplace/app/dust/444426060155)
</Tip>

## About the Add-on

The Dust Google Sheets Add-on lets you call your Dust agents directly from your spreadsheets. Process data, analyze information, and automate tasks, all without leaving Google Sheets.

## Getting Started

### Step 1: Install the Add-on

From any spreadsheet, visit the Google Workspace Marketplace by navigating to **Extensions > Add-ons > Get add-ons**.

* Click **Install**
* Follow the authorization prompts
* Done! The add-on is now available in all your spreadsheets

### Step 2: Set up the connection

Navigate to **Extensions > Dust > Setup**.

When prompted, fill in this information to connect the Add-on to your Dust workspace:

**Workspace ID**

This information is found in your Dust URL. Example: `https://dust.tt/w/your-workspace-id/agent/new`. Copy the part after `/w/`.

**API Key**

In Dust, navigate to **Admin > API Keys**:

* Click **Create an API Key**
* Copy and paste the generated key

<Info>API Keys must be created by a workspace admin.</Info>

**Region**

Region is optional: leave empty for US, or enter `eu` if you usually use Dust on eu.dust.tt.

## Using the Add-on

Select the cells you want to process, then click **Dust > Call an Agent**.

Use the sidepanel to:

* Choose the agent that should answer the question
* Verify input range (or use "Use Selection")
* Specify target column (e.g., 'B')
* Add optional instructions
* Click **Run**

## Best Practices

**Do:**

* Start with small test batches
* Use clear, specific instructions
* Save templates for repeated tasks

**Avoid:**

* Processing thousands of rows before testing small batches
* Vague or overly complex prompts

### Performance & Limits

Agents must respond within 30 seconds. Keep queries concise and specific to avoid timeouts.
