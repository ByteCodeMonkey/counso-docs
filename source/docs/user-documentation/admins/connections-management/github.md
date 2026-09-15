> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Github

<Danger>
  **Limitations**

  GitHub synchronization is limited to issues, discussions, and top-level pull request comments.\
  In-code comments in pull requests, the actual source code, and other GitHub-specific data, such as commit history, are not synchronized unless you enable it.
  Files larger than 4MiB are ignored.
</Danger>

## Overview

Dust integrates with Github to bring your repository's Issues, Pull Requests, Discussions, and (if enabled) codebase into Dust, so agents can search and use that content.
Only Github Admins can set up this connection due to permission restrictions.

## Setting up the Connection

### Initial Connection Setup

1. **Access Control**: Ensure you're a Dust Admin and have the necessary permissions on GitHub to establish connections.
2. **Navigate to Dust**: Go to `Spaces` > `Connections` > Select `GitHub` > Connect.
3. **Authenticate**: Click `Configure` and authenticate your GitHub account to grant Dust permission to access your GitHub data.

Github redirect to install and configure Dust.

Github redirect to install and configure Dust.

1. **Select your repos:** Give access to the repo you select from `Repository access`.

Github redirect: select all repos.

Github redirect: select granular repos you want to sync with your Dust workspace.

1. **Enable Code sync:** Optionally give access to your codebase by toggling `Code synchronization`.

Dust modal to enable code synchronization.

<Danger>
  **Permissions**

  Ensure the GitHub account used for the connection has ongoing access to the selected repositories. Changing permissions in GitHub may impact Dust’s ability to synchronize new data.
  The Github app will be created with the following permissions
  Repository content : **ReadOnly**\
  Issues : **ReadOnly**\
  Discussions : **ReadOnly**\
  Pages : **ReadOnly**\
  Projects : **ReadOnly**\
  Pull Requests : **ReadOnly**\
  All the rest : **No Access**
</Danger>

## Updating the Connection and Managing Permissions

To modify permissions and which repositories or types of data are synchronized:

1. Go to `Spaces` > `Connections`.
2. Click `Manage` next to GitHub.
3. Click Add/Remove Data, Manage permissions, re-auth, and follow the steps above.
4. Adjust your selections for repositories, then save your changes.

## Data Synchronization

* **Issues**: Titles, descriptions, comments, and tags.
* **Discussions**: Discussion titles, initial posts, and comments.
* **Pull Requests**: Titles, descriptions, and top-level comments (in-code comments not included).
* **Code Synchronization:** Repository code from the default branch

## Refresh and Sync Details

* **Refresh Rate**: Issues, Discussions and Pull-requests are maintained up to date in real-time. Code is synchronized every 8 hours.

Dust syncs the custom labels set on GitHub issues and Pull Requests, and include them in the document above the content itself.

It also automatically adds those labels:

`title:Title of the issue/pull request`,

`isPullRequest:true|false`,

`author:@githubHandle`.

**Labels**  allow for additional filtering on data sources selected on the [semantic search](/docs/user-documentation/agents/knowledge/search-data-sources) tool.

<Info>
  **Labels support was added Feb 11 2025**

  Issues and Pull Requests older than that won't have those labels ingested.
</Info>
