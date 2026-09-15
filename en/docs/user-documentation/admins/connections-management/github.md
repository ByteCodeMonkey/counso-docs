# Connect GitHub

The GitHub connection makes repository issues, discussions, and pull-request conversations searchable. Source-code synchronization is optional and uses the repository's default branch.

## Install and configure

The deployment administrator must register and configure the GitHub App used by this Counso deployment, including its callback and webhook addresses. A GitHub organization owner or administrator must be able to install that app for the repositories being connected.

1. With Counso admin access, open **Spaces > Connections > GitHub** and choose **Configure**.
2. Complete the GitHub authorization and install the app configured for this deployment.
3. In **Repository access**, select the repositories to include.
4. Turn on **Code synchronization** only for repositories whose source files should be indexed, then save.

The connection requests read access for repository content, issues, discussions, Pages, projects, and pull requests. Keep the installed app and connecting account authorized for the selected repositories.

## What is indexed

| Content | Included |
| --- | --- |
| Issues | Title, description, comments, and labels. |
| Discussions | Title, opening post, and comments. |
| Pull requests | Title, description, and top-level comments. Inline code-review comments are not included. |
| Code, when enabled | Files from the default branch. Files larger than 4 MiB are skipped. |

The connection does not provide a complete commit-history archive. If an agent needs a live repository operation, configure the appropriate GitHub tool separately.

## Change the selection

Open **Manage** beside GitHub in Connections. Use the data or permissions controls to adjust repository selection, and reauthorize when required. Save the selection after making changes. Removing app access in GitHub can prevent new synchronization even if the repository remains visible in Counso's settings.

Issues, discussions, and pull requests are updated through ongoing synchronization. Code is refreshed approximately every eight hours, so a recent code change may not yet appear in search.

## Filter by labels

Issue and pull-request labels are included with synchronized content. Additional labels identify the title, whether the item is a pull request, and the author, using forms such as `title:Fix search`, `isPullRequest:true`, and `author:@alex`. These can narrow [knowledge searches](../../agents/knowledge/search-data-sources.md).
