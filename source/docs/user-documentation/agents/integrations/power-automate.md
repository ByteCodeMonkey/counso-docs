> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Power Automate

Install the Dust custom connector in your Power Automate environment.

## Prerequisites

Before installing the Dust Assistant Solution, ensure you have:

* **Power Platform Access**: get the *Power Automate Premium* [license](https://www.microsoft.com/power-platform/products/power-automate/pricing)
* **Environment Permissions**: Environment Maker role or higher
  1. Go to [admin.powerplatform.microsoft.com](https://admin.powerplatform.microsoft.com)
  2. Select **Environments**  Your environment
  3. Verify you have **Environment Maker** or **System Administrator** role
* **Dust Account**: Active Dust workspace with API access
* **API Credentials**: Create a Dust API key from your workspace settings
  1. **Log into Dust**
     * Go to [dust.tt](https://dust.tt)
     * Navigate to your workspace

  2. **Generate API Key**
     * As a workspace admin, go to **Admin** > **API & Programmatic** > **API Keys**
     * Click **"Create API Key"**
     * Copy the generated key
     * **Store securely** - you won't see it again

## Installation Guide

### Step 1: Download the Connector

Download the latest version: [DustAssistantSolution.zip](https://office-addins.dust.tt/power-automate/PowerAutomate_DustAssistantSolution.zip)

### Step 2: Import the Solution

1. **Navigate to Power Automate**
   * Go to [make.powerautomate.com](https://make.powerapps.com)
   * Select your target environment (top-right dropdown)

2. **Import Solution**
   * Click **"Solutions"** in the left navigation
   * Click **"Import solution"**
   * Click **"Browse"** and select the downloaded `.zip` file
   * Click **"Next"**

3. **Review Import Settings**
   * Review the solution details
   * Click **"Import"**
   * Wait for import completion (2-5 minutes)

### Step 3: Test connection

1. **Open the Custom Connector**
   * Go to **"Solutions"**  **"Dust Assistant Solution"**
   * Click on the Custom Connector you want to test

2. **Test connection**
   * Click **"Edit"** (pencil icon)
   * Go to **"Test"** tab
   * **Create a new connection**: Enter your **Dust API Key** in the authentication field ( :warning:You must add "Bearer " before your API token)
   * Test with a sample body (select the connector you want to test below and copy the corresponding sample body)

```json Talk to an Agent theme={null}
{
  "message": {
    "context": {
      "timezone": "Europe/Paris",
      "username": "xxx"
    },
    "content": "hello",
    "mentions": [
      {
        "configurationId": "gpt-5"
      }
    ]
  },
  "blocking": true
}
```

```json Upload document theme={null}
{
  "text": "This is my doc content",
  "title": "Doc title",
  "tags": ["tag1", "tag2"]
}
```

* Wait for the response: the HTTP status should be 200.

### Step 4: Share the connector

* Go to **"Solutions"**  **"Dust Assistant Solution"**
* Click on the Custom Connector you want to share
* Go to the "Share" tab
* You can now decide either to share the connector with your whole organization, or select specific users to share with.

## Updates and Maintenance

### Updating the Connector

1. **Download** the latest version
2. **Import** the new solution (it will update the existing one)
3. **Test** your existing flows/apps

Add a Dust connector to your flows.

## Prerequisites

* **Power Platform Access**: get the *Power Automate Premium* [license](https://www.microsoft.com/power-platform/products/power-automate/pricing). Ask your admin to grant you a licence.
* **Dust Account**: Active Dust workspace with API access
* **API Credentials**: Create a Dust API key from your workspace settings
  1. *Log into Dust*\*
     * Go to [dust.tt](https://dust.tt)
     * Navigate to your workspace

  2. **Generate API Key**
     * As a workspace admin, go to **Admin** > **API & Programmatic** > **API Keys**
     * Click **"Create API Key"**
     * Copy the generated key
     * **Store securely** - you won't see it again

## User guide

### Step 1: Use the Dust connector in your flow

1. In Power Automate, create a new flow or use an existing one

2. Add a new action

3. Search for "Dust" in the search bar (you can click on the "Custom" filter to see only custom connectors)

4. Select the Dust connector you want to use (either *Talk to an Agent* or *Upload document*)

5. Enter your **Dust API Key** in the authentication field ( :warning: You must add "Bearer " before your API key)

### Step 2: Enter the required Parameters

You may need to click on the "Display all" button.

<Tabs>
  <Tab title="'Talk to an Agent' Connector" />

  <Tab title="'Upload Document' Connector" />
</Tabs>
