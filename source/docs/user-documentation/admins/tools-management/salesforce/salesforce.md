> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Salesforce

<Info>Available on Business and Enterprise plans.</Info>

## Admin: Setup in Salesforce

### Create an External Client App in Salesforce

Go to Salesforce Setup (gear icon in the top right corner). In the search bar on the left sidebar, search for "External Client App Manager" and click **New External Client App**.

**Fill in basic information**

* External Client App Name: "Dust Integration".
* API Name: will auto-populate.
* Contact Email: your email.
* Distribution State: keep default value "Local".

**API (Enable OAuth Settings)**

* Check the "Enable OAuth" box.

**Set the callback URLs**

```
https://dust.tt/oauth/salesforce/finalize
https://eu.dust.tt/oauth/salesforce/finalize
https://app.dust.tt/oauth/salesforce/finalize
```

**Select the OAuth scopes**

* Access the identity URL service (id, profile, email, address, phone)
* Manage user data via APIs (api)
* Perform requests at any time (refresh\_token, offline\_access)
* Access custom permissions (custom\_permissions)

**Set up Flow Enablement & Security**

Tick these options:

* Enable Client Credentials Flow
* Enable Authorization Code and Credentials Flow
* Require secret for Web Server Flow
* Require secret for Refresh Token Flow
* Require Proof Key for Code Exchange (PKCE) extension for Supported Authorization Flows

Click on **Create**.

### Get your credentials

* Click on the **Settings** tab and then the **Edit** button.
* Open the **OAuth Settings** dropdown menu.
* Click on **Consumer Key and Secret** and copy those for the Setup in Dust.

## Admin: Setup in Dust

Go to **Spaces** > **Tools** in your Dust workspace, click **Add Tools**, and select Salesforce. Fill in your Salesforce Instance URL and the Client ID & Secret generated from your External App.

Then choose the **Credentials Type**:

* **Personal** means that each user using the Salesforce tool will be required to log in to Salesforce first. We will use the user credential to execute the queries, meaning permissions defined on Salesforce are respected.
* **Workspace** means we will use the credentials of the admin setting up the tool for all queries (meaning all users share their permissions when executing queries on Salesforce).

You will then be redirected to an OAuth flow to connect an admin Salesforce account. In case of Personal credential type, this account will only be used during the set up and users won't be able to query Salesforce from this account.

By default this tool is added to the Company data Space, so accessible in all the workspace.

## Usage

Once the tool has been configured by the admin as described before, it can be selected on any agent: in the Agent Builder, simply click on **Add Tool** and select Salesforce.

When users use an agent with the Salesforce tool for the first time, they will get an error if the Credential type was set to **Personal**. They will have to click on the **Connect** button to connect their own Salesforce credentials, then click on the **Retry** button to replay the agent answer.

For details on API consumption and permissions, see [Salesforce: notes on API limits and permissions](/docs/user-documentation/admins/tools-management/salesforce/salesforce-notes-on-api-limit-and-permissions).
