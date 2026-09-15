# Connect Salesforce

The Salesforce tool lets an Agent query records using a Salesforce identity. Salesforce controls the identity's record, object, field, and API access. Choose personal credentials when each user should act with their own Salesforce permissions, or workspace credentials when an approved integration user should provide shared access.

## Create the Salesforce app

In Salesforce Setup, open **External Client App Manager** and create an External Client App. Give it a name, keep the distribution state at the setting appropriate for your organization, and enable OAuth. Add the callback URL shown in the Counso Salesforce tool setup form; callbacks can differ by deployment.

Add the identity, API, refresh-token/offline-access, and custom-permission scopes required by the tool. Use these scope groups: `id`, `profile`, `email`, `address`, `phone`; `api`; `refresh_token` / `offline_access`; and `custom_permissions`.

Under **Flow Enablement & Security**, enable the settings required by this connector:

- **Enable Client Credentials Flow**
- **Enable Authorization Code and Credentials Flow**
- **Require secret for Web Server Flow**
- **Require secret for Refresh Token Flow**
- **Require Proof Key for Code Exchange (PKCE) extension for Supported Authorization Flows**

Create the app, then open **Settings > Edit > OAuth Settings > Consumer Key and Secret** and securely record those values. The app settings support the OAuth connection; the personal or workspace choice in Counso controls whose connected Salesforce account is used.

## Configure the tool

In **Spaces > Tools > Add Tools > Salesforce**, enter the Salesforce instance URL and the app credentials. Select **Personal** or **Workspace** credentials and complete the authorization shown by Counso.

With **Personal** credentials, the administrator's setup authorization initializes the integration; it is not the identity used for every member's query. Each user connects their own Salesforce account on first use and retries the request. With **Workspace** credentials, queries use the Salesforce account authorized by the administrator during setup. All permitted users share that account's Salesforce access. Give it only the object and field access the Agent needs.

Share the tool only with the intended Spaces and add it to an Agent. Test a read from one known Account or Contact. If data is missing, check the active Salesforce identity, object permission, field-level security, and API limits. For details, see [Salesforce query limits and access](salesforce-notes-on-api-limit-and-permissions.md).
