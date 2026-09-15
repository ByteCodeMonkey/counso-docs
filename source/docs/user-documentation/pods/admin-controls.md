> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Admin controls

Workspace administrators can configure two Pod-level policies from the **Admin settings**, under the **Capabilities** section.

***

## Pod visibility policy

Controls whether members can create Open Pods or are limited to Restricted (private) ones.

| Option                                | Effect                                                                                        |
| ------------------------------------- | --------------------------------------------------------------------------------------------- |
| **Private and open Pods** *(default)* | Members can create either Restricted or Open Pods                                             |
| **Private Pods only**                 | Members can only create Restricted Pods; the Open visibility toggle is disabled with a notice |

<Info>
  **Useful for large organizations where members might inadvertently make a Pod visible to everyone without realizing the scope. Setting this to "Private Pods only" ensures that sharing is always intentional.**

  Note: existing Open Pods are not force-closed when this policy is enabled. Editors can still switch them back to Restricted manually.
</Info>

***

## Pod files policy

Controls whether members can manually add files or linked data to a Pod's Files tab.

| Option                                 | Effect                                                                                    |
| -------------------------------------- | ----------------------------------------------------------------------------------------- |
| **Manual updates allowed** *(default)* | Members can upload files and link Company Data nodes to a Pod                             |
| **Manual updates disabled**            | The Add button is hidden; only agents and automated connectors can populate the Files tab |

<Info>
  **Useful for organizations with tight data governance rules, where knowledge in Pods should come exclusively from controlled, automated sources rather than ad-hoc member uploads.**

  ***
</Info>

Both settings default to the permissive option, so existing Pods and member workflows are unaffected unless an admin explicitly changes them.
