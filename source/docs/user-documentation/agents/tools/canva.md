> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Canva

## Overview

Tools to create, search, edit, and export Canva designs via the official Canva MCP (AI Connector).

Canva's MCP integration lets agents create new designs with Canva AI, autofill brand templates, find existing designs, and export designs as PDFs, images, or video, all without leaving the conversation. The connector is built on the Model Context Protocol (MCP) and aligns with Canva's Connect API endpoints. Over time, it will support the full suite of Connect API functionality.

<Info>
  When enabled by your Canva admin, the AI Connector can access design metadata
  and folders, create and edit designs, and use template autofill (if available
  in your plan).
</Info>

## Connection Setup (Admin)

Set up Canva as a Remote MCP Server in Dust.

1. In Dust, go to Spaces Administration Tools and click Add Tools.
2. Choose Add Remote MCP Server.
3. Select Canva from the dropdown
4. Complete the OAuth authorization flow in your browser to allow the Canva AI Connector to access your Canva account.
5. (Optional) Choose between Personal or Workspace credentials based on your policy. Dust supports both for Remote MCP servers that implement OAuth.

Once connected, the toolset will be available to add to agents in spaces you grant access to.

## Adding Tools to Agents

* Admins can make the Canva toolset available to specific spaces or organization-wide.
* Builders can then add the toolset to an agent from the Agent Builder.

## Available Tools

The Canva MCP exposes the following capabilities in supported AI assistants. Functionality maps to Canva's Connect API and may evolve.

* Generate design: Create new visuals from a prompt (documents, presentations, social posts, video intros, etc.).
* Search designs: Find designs by title, content, or metadata.
* Search designs with ID: Retrieve details and shareable links by design ID.
* Get a design: Fetch full text and image content of a design (by ID).
* Resize a design: Convert to preset or custom dimensions (e.g., A4, 16:9, 1080×1920).
* View the pages of a design: List pages/slides and thumbnails for multi‑page designs.
* Import a design from URL: Import PDFs, PowerPoints, Docs, etc., as editable Canva designs.
* Export a design: Export as PDF, PNG/JPG, MP4, PPTX, etc.
* Create a folder: Create folders at root or nested under existing folders.
* Move item to a folder: Move designs or folders.
* List folder items: List contents of a folder with filters.
* View and reply to comments: Retrieve and respond to design comments; filter unresolved, by page, etc.
* Search brand templates: Discover available brand templates.
* Autofill a templated design: Fill brand templates at scale with datasets (CSV, inventory, etc.).
* See brand template dataset: View the data schema/fields required for a brand template.

## Security, Permissions, and Admin Controls

* In Canva, the AI Connector is a third‑party integration that admins can enable/disable under Controls and Permissions. When enabled, it can access design metadata, create/edit designs, and use autofill features (if included in your plan).
* The connector uses the same endpoints as the Canva Connect API and is being expanded to cover the full feature set over time.
* In Dust, you can manage access using space‑based restrictions under a tool's Sharing tab.
* Stake levels: For actions that create or modify Canva content (e.g., Generate design, Resize, Autofill), set High stake so users approve calls. For read‑only actions (e.g., Search designs, Get a design), Low stake is typically appropriate.

## Troubleshooting

* If authentication fails or the connector isn't visible, re‑run the OAuth flow and confirm the tool is shared with the target space(s).
* Feature availability depends on your Canva plan; some capabilities (e.g., template autofill) may require specific entitlements.
