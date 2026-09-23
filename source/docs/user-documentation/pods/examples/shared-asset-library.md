> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Shared asset library

**Audience:** Design, Brand, and Platform teams

**Goal:** Centralise logos, Frame templates, images, and other reusable assets in one place so that any agent in the workspace can use them from any conversation or Pod, without duplicating files or coordinating manually.

## Setup

* One **Open** Pod (e.g. "Brand Assets" or "Shared Templates")
* Editors: the Design or Platform team members who own and maintain the assets
* Visibility: Open; any workspace member can browse and read the Pod's content without being explicitly added as a member
* Files tab: organise by type:
  * `images/`: logos, illustrations, product screenshots
  * `frames/`: canonical Frame templates (.tsx) for reports, dashboards, and slides
  * `brand/`: color palettes, typography guides, brand guidelines
  * `data/`: shared reference tables or lookup CSVs agents may need
* Pod description: list what each folder contains so agents know where to look

## Usage

**Light: shared library, manual use**

Upload your assets once and let teams access them directly. Any workspace member can open the Pod, browse the Files tab, and download what they need. Agents can also be pointed to a specific file: "use the logo from the Brand Assets Pod."

**Medium: template-based agent output**

From any conversation or Pod, ask an agent to start from a canonical template: "use the BrandedReport Frame from the shared asset Pod as the base for this quarterly review." The agent copies the template into the current context, adapts it, and saves the result locally; the shared original is never modified. The design team updates a template once; all future agent runs automatically pick up the latest version.

**Heavy: workspace-wide brand consistency**

* Brief every agent that produces visual output to always check the shared asset Pod for the latest templates before generating a Frame or document
* Set up an agent in the asset Pod that monitors the Files tab and posts a conversation whenever a template is updated, so dependent Pods and workflows know to refresh
* Use the Pod description as a changelog: record the latest version and what changed each time a template is updated

## Outcome

Any agent in the workspace produces on-brand output without extra instructions. The Design team maintains a single source of truth instead of chasing copies scattered across conversations and Pods.
