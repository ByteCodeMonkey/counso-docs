---
title: "Slab"
---
The Slab tool provides read access to posts, topics, and search results in the authorized Slab workspace. Private topics or posts not shared with the connected integration remain unavailable to the Agent.

An administrator adds Slab from **Spaces → Tools → Add Tools**, authorizes the intended workspace, and shares the tool with the Space that should search it. Add Slab to an Agent and begin with a topic search followed by a read of one known post. Confirm the connected identity and the topic's sharing settings.

If a search misses an expected post, check whether the integration can access its topic and whether the user has access in Slab. Do not assume that adding the tool grants broad access to all workspace content. Since this tool is read-only, use a Slab Connection if the workspace needs synchronized search across a selected knowledge collection.

## Available operations

The read-only actions are **Get Post**, **List Posts**, **Get Topic**, **List Topics**, and **Search**. Search a topic or list posts first, then retrieve the needed post. Private topics not shared with the integration remain outside the result set.
