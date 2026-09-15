> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Val Town

| Tool                    | Description                                                                                           |
| ----------------------- | ----------------------------------------------------------------------------------------------------- |
| `Function Creation`     | Create and deploy serverless JavaScript/TypeScript functions (vals) directly from agent conversations |
| `Code Execution`        | Run vals with parameters and get real-time results                                                    |
| `Val Discovery`         | Search and browse existing vals across the Val Town platform                                          |
| `Serverless Automation` | Build APIs, scheduled tasks, and automation workflows without infrastructure management               |

## :compass: Use case examples

<Cards columns={3}>
  <Card title="Rapid API Prototyping" icon="fa-rocket" target="\_blank">
    Create and deploy HTTP endpoints instantly without server setup
  </Card>

  <Card title="Automated Data Processing" icon="fa-gears">
    Build serverless functions that process data on demand
  </Card>

  <Card title="Webhook Endpoints" icon="fa-plug">
    Generate webhook receivers for third-party integrations in seconds
  </Card>

  <Card title="Natural Language Development" icon="fa-brain">
    Describe functions in plain English and let Dust generate the code
  </Card>

  <Card title="Real-time Testing" icon="fa-flask">
    Execute and test your vals immediately within Dust conversations
  </Card>
</Cards>

***

Go to Spaces > Tools in your Dust workspace, click `Add Tools`, and select *Val Town*.

## Authentication

Val Town’s REST API supports Bearer Token authentication. You can create and manage your Val Town API tokens on the [API Tokens page](https://www.val.town/settings/api). In order to use all available tools, the token will need read and write permissions for vals.

Your Val Town API token must be stored as a Dust developer secret. Go to Admin -> Builder Tools Management -> Secrets, and select *Create Secret* to store your Val Town API token.

Once the tool has been configured by the admin as described before, it can be selected on any agent. In the Agent Builder, click on `Add Tool` and select Val Town. You will be required to select a developer secret that will be used as a bearer token for all API calls.

## Create Val

Creates a new val in Val Town. Use create\_file to add files to the val.

## Get Val

Gets a specific val by its ID

## List Vals

Lists vals available to the user's account

## Search Vals

Searches for vals by name, description, or content

## List Val Files

Lists all files in a specific val

## Get File Content

Gets the content of a specific file in a val using the Val Town API

## Delete File

Deletes a specific file from a val using the Val Town API

## Update File Content

Updates the content of a specific file in a val. Note: To change file type (e.g., to HTTP), use the file\_update tool instead.

## Write File

The primary function for writing content to files and updating file metadata. Use this to add content, change file type, rename files, or move files. For HTTP type: return value from serve handler must be a response or a promise resolving to a response.

## Create File

Creates a new empty file in an existing val. Use write\_file to add content and set the file type.

## Call Http Endpoint

Runs an HTTP val endpoint by getting the file's endpoint link and making a request to it
