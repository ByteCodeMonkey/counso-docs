# Manage Spaces

Spaces organize data and define which members can use it. A connected source is not automatically shared with the workspace; it must be added to a Space. The Space audience also affects which members can see and use Agents whose Tools rely on that Space.

## Open and restricted Spaces

- **Open Spaces** are available to workspace members. Use them for material intended for broad internal access. The default **Company Data** Space is always open and cannot be restricted or modified.
- **Restricted Spaces** are available only to selected members or groups. Use them where a project or data source has a narrower audience. If directory provisioning is configured, you may be able to use provisioned groups to manage membership from the identity provider.

## Create a Space

Workspace administrators manage Spaces. Open **Spaces**, choose **New**, enter a name, select **Open** or **Restricted**, add members or groups when restricted, and create the Space.

## Add data

An administrator adds connected data to a Space:

1. Open the Space and choose **Connected Data**.
2. Select **Add data from connections**.
3. Choose only the folders, channels, or other connected content that belongs in this Space.
4. Save and check that the expected data appears.

For folders, websites, or other sources, who can add material can depend on whether the Space is open or restricted and on the member's role. Check the access shown by the workspace when adding it.

## Use Spaces with Agents

An Agent is available only to members who can access the Spaces used by its Tools. Before publishing, check every source and Space in its configuration, then confirm that its intended users are members of those Spaces. Keep sources with different audiences in separate Spaces.
