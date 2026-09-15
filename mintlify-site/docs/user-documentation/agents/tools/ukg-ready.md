---
title: "UKG Ready"
---
The UKG Ready tool supports read access and PTO workflows; it does not expose the full UKG Ready feature set, and UKG Pro is not covered. Available operations include **Get My Info**, **View PTO Requests**, **Create PTO Request**, **Delete PTO Request**, **View PTO Request Notes**, **Get Accrual Balances**, **Get Schedules**, and **Get Employees**.

## Create and connect an OAuth app

In UKG Ready, go to **Settings → Global Setup → Company Setup → OAuth Applications** and create an **Interactive** application. UKG generates the client ID. Add the callback displayed in the Counso tool setup form. In **Spaces → Tools**, add UKG Ready and enter the instance URL, Company ID, and generated client ID. The Company ID can be identified in the tenant URL. Share the tool with the approved Space and add it to the Agent.

PTO requests can be created or cancelled; keep these operations within an approved HR workflow. Employee, accrual, and schedule details remain limited by the connected UKG user's permissions.
