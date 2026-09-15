> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# BigQuery

ℹ Dust does not synchronize or store any of your BigQuery data. We only store metadata, such as datasets and table names.

You can connect Dust to your BigQuery data warehouse to enable your agents to perform [Table queries](/docs/user-documentation/agents/knowledge/table-queries) on your BigQuery tables.

Agents can now use table and column descriptions set in BigQuery to better understand your data structure. This feature can be enabled in the BigQuery connection management screen.

Dust agents are able to use the output from these queries to answer quantitative questions:

The agents can also use the results to create visualizations, such as charts:

The "Tools inspection" button allows to view the reasoning and SQL query used by the agent to retrieve the data:

## Key BigQuery Concepts

Let's review some essential concepts:

* **Project**: A container for your BigQuery resources
* **Dataset**: A container for tables and other objects (similar to a schema in other databases)
* **Location**: Each BigQuery dataset lives in a location (region or multi-region, e.g., US, EU, us-central1). Queries can only reference tables from datasets in the same location.
* **Table**: A structure that stores data in rows and columns
* **Service Account**: An account for programmatic access to BigQuery
* **IAM Role**: A collection of permissions that can be assigned to users and service accounts

## Step-by-Step Guide

### Setup on Google Cloud's side

<Info>
  **We recommend creating a dedicated service account for Dust. Dust allow one connection, and this connection will have access to all BigQuery tables.**

  In individual Spaces, the admin can choose to not allow specific tables to be used
</Info>

#### Create a service account

1. Go to the IAM & Admin > Service Accounts section of the Google Cloud Console
2. Click "Create Service Account"
3. Enter a name (e.g., "dust-service-account")
4. Click "Create and Continue"

#### Assign roles to the service account

The service account needs at least two roles:

* `roles/bigquery.user` (to run queries)
* `roles/bigquery.dataViewer` (to access data)
* Note: if you use certains types of underlying storage, such as [Delta Lake tables in GCS,](https://cloud.google.com/bigquery/docs/create-delta-lake-table#iam-permissions) you may need additional roles.

1. In the IAM section, find your service account
2. Click the edit (pencil) icon
3. Click "Add another role"
4. Add both required roles
5. Click "Save"

#### Create and download credentials

1. Go back to the service account details
2. Go to the "Keys" tab
3. Click "Add Key" > "Create new key"
4. Choose JSON format
5. Click "Create"

The key file will download automatically. Keep it secure as it provides access to your BigQuery data.

### Setup on Dust's side

1. Navigate to Dust's **Spaces** > **Connections**
2. Click on "Add Connections" and select BigQuery
3. Paste your service account key into the box (**Note:** you may have to wait a few seconds for the key to register)
4. Select the BigQuery location (region or multi-region) for this connection. Dust can only query datasets in the selected location. All datasets you connect here must be in that same location.

ℹ **BigQuery limitation**
BigQuery prevents cross-location queries. A single query cannot reference tables from datasets in different locations (for example, US and EU). If your data spans multiple locations, select only the datasets from one location for this connection. [Learn more](https://cloud.google.com/bigquery/docs/datasets-intro#dataset_location)

5. Select the datasets and tables you want to make available in Dust
6. You can enable the "Use BigQuery descriptions" option to allow agents to use table and column descriptions that are set in BigQuery. This can help agents better understand your data structure without requiring additional documentation.
