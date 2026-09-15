> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Salesforce - Notes on API limit and permissions

### How It Works

1. You ask a question in plain language (like "Give me an account summary of xx" or "What's the pipeline for this quarter?").
2. The agent translates your question into a Salesforce query (SOQL).
3. It fetches the relevant data from your Salesforce.
4. You get back a clear answer based on your current Salesforce data.

No need to write complex queries - the connection handles the technical parts for you!

### Data Synchronization

The connection maintains a smart link with your Salesforce - without needing to import Salesforce data in Dust:

* Every hour, it updates its understanding of your Salesforce structure (what Objects and fields are available).
* When you ask questions, it gets real-time data directly from your Salesforce.
* You don't need to sync or import data manually - the connection only fetches what's needed when you ask for it.

This ensures you always get current information while keeping the system efficient and responsive -  doing as few requests as possible on your Salesforce (which limits API calls).

### Salesforce API Limits

Depending on your Salesforce, you have a different [API limitations](https://developer.salesforce.com/docs/atlas.en-us.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_api.htm):

| [**Salesforce API limits**](https://developer.salesforce.com/docs/atlas.en-us.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_api.htm) | Per 24-hour period for an org.                                                       |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| Developer Edition                                                                                                                                                                            | 15000                                                                                |
| Enterprise Edition                                                                                                                                                                           | 100,000 + (number of licenses x calls per license type) + purchased API Call Add-Ons |
| Unlimited Edition                                                                                                                                                                            | 100,000 + (number of licenses x calls per license type) + purchased API Call Add-Ons |

You can view your daily API usage in the System Overview page in Setup. It indicates your org’s API usage over the preceding 24 hours and as a percentage of your Daily API Request Limit ([source](https://developer.salesforce.com/blogs/2024/11/api-limits-and-monitoring-your-api-usage)).

We are doing the minimum requests possible to keep your Salesforce structure up to date but it’s important to understand that you also query it each time you ping an agent associated with Salesforce data.

You can define [API Usage notifications](https://help.salesforce.com/s/articleView?id=sf.monitor_rate_limit.htm\&type=5) in your org to monitor your API usage against your API limits. An email notification will be sent when your org exceeds a specified threshold, as a percentage of the Daily API Request Limit, within a specified time period.

<Warning>
  **Important**

  Your actual API limits and costs may vary based on your Salesforce configuration and additional purchased API capacity. Please review your organization's specific Salesforce licensing terms and API allowances to ensure our integration aligns with your available quota and budget
</Warning>

### **Data Access Security**

* Queries are executed using the permissions of the connected Salesforce account.
* Access is limited to data visible to the authenticated user.

For best security practices, we recommend using a **dedicated Service Account**:

* Create a dedicated Salesforce Service Account for the Salesforce Connection.
* Configure minimum required permissions that will enable all the use cases you want to use on Dust.

All Dust users will use the dedicated service account to query data from your Salesforce.

### **Managing Access by Space**

As Admin, on top of using restrictions from the connected Salesforce account you are able to define the list of Objects that users are allowed to query on each open or restricted space.

See how [access controls and space permissions](/docs/user-documentation/admins/admin-governance/access-controls-and-permissions) work in Dust.

Example configurations:

* Restricted Sales Space: All members of the restricted space can access to Accounts, Opportunities, Cases, and Contacts.
* Restricted Marketing Space: All members of the restricted space can access to Campaigns, Leads, and Contacts.
* Open Sales Space: All members of the Dust workspace can access Notes.

[**Dust Salesforce Connection Setup**](/docs/user-documentation/admins/tools-management/salesforce/salesforce#/)

### Data Access and Queries

* Salesforce data is available through the tool "[Query Tables](/docs/user-documentation/agents/knowledge/table-queries)" in the Agent Builder.
* Note that not all fields are automatically queryable - they may need to be made accessible in your Salesforce configuration first

### Agent Understanding of the Data Structure

* Even though the agent is quite smart to discover the data structure, we recommend taking the time to properly explain what data is actually relevant for your use case in your agent instructions, especially if it involves Custom Objects. A relevant Account Summary can be very different from one business to another.
* When working with Custom Objects, note that custom field names typically end with "\_\_c". Document any important custom field mappings or relationships specific to your implementation in your agent instructions.

### **Performance Best Practices**

* Use appropriate filters directly in the chat bar when you write your query to avoid timeout issues and improve performance. For large data sets, consider limiting the number of records returned, for example, limiting to a certain date range.

### Handling Account Data

* For agents working with multiple Accounts sharing the same name: Ask the agent to confirm which specific Account the user is interested in before proceeding.
* Consider using unique identifiers (Account Number, external IDs) to distinguish between similar accounts.
