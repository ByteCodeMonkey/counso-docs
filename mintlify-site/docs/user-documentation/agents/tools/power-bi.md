---
title: "Power BI"
---
Power BI MCP lets an Agent read permitted Power BI workspaces, dashboards, reports, and semantic models. Setup requires a Microsoft Entra application, delegated Power BI permissions, and the MCP endpoint enabled in the Power BI tenant. The Entra app alone does not grant access to a report or model.

## Register the application

An Entra administrator registers an app for **accounts in this organisational directory only** and records its Application (client) ID and Directory (tenant) ID. Configure the web redirect URI using the callback displayed by Counso's tool form. Enable **Allow public client flows**, create a client secret, then add Power BI Service delegated permissions `Dataset.Read.All`, `Report.Read.All`, `Dashboard.Read.All`, and `Workspace.Read.All`. Grant admin consent.

In the Power BI/Fabric admin portal, enable **Users can use the Power BI Model Context Protocol server endpoint** for the intended users or group. The remote MCP endpoint is `https://api.fabric.microsoft.com/v1/mcp/powerbi`.

## Add the remote server

In **Spaces → Tools → Add Tools → Add MCP Server**, enter the Power BI endpoint and choose OAuth. Use the Entra client ID and secret. The authorization and token URLs follow the tenant's Microsoft Identity v2 endpoints; the scope is `https://analysis.windows.net/powerbi/api/.default offline_access`. The scope uses the Power BI API resource, not the Fabric MCP host. Save and complete user authorization, then add the available Power BI tools to an Agent in the intended Space.

If the app cannot be found, check that the Application ID—not the Secret ID or Object ID—was entered. If the server feature is unavailable, verify the tenant MCP setting. If connection discovery fails, check whether XMLA endpoints are enabled. When prompted for personal sign-in, complete authorization and retry the Agent request.
