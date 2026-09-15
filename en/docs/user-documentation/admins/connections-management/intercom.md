# Connect Intercom

The Intercom connection synchronizes Help Center articles and closed conversations. Setup requires Counso admin access and the Intercom permission to install, configure, and delete apps.

## Select what to synchronize

Open Intercom in **Spaces > Connections**, authorize access, then select the required teams and top-level Help Center collections. The initial save can take longer while permissions and content are being prepared.

For conversations, selecting **Conversations** includes all teams. Selecting individual teams limits synchronization to conversations attached to one of those teams. A conversation must also be closed and have been opened within the past 90 days.

For the Help Center, only published articles in the selected top-level collections are included.

## Content included

A conversation contains messages, author names, notes, tags, and its source. You can turn off note synchronization in the connection configuration. Review this choice if internal support notes should stay out of the knowledge available to agents.

An article contributes its title and body. Draft and unpublished articles are excluded.

## Updates and labels

Changing the selected teams or collections starts synchronization or removal of the affected content. Completion can take several minutes depending on volume. Newly closed conversations in an authorized team are processed after the Intercom notification arrives, normally within seconds. Help Center content is refreshed hourly, so a new article can take up to an hour to appear.

Conversation attributes become labels in the form `attribute:name:value`; tags use `tag:name`. Agents can use these in [knowledge search filters](../../agents/knowledge/search-data-sources.md).
