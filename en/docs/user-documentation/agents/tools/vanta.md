# Vanta

The Vanta tool provides **read-only** access to security and compliance data. It uses workspace-level credentials shared by users who can access the tool. A Vanta administrator creates an OAuth application in **Settings → Developer Console**, selects **Manage Vanta**, and records the client ID and secret. The documented scope is `vanta-api.all:read`.

In **Spaces → Tools**, add Vanta and enter the client ID and secret. Keep the tool within the Space whose members are authorized to see the account's compliance data. The secret can authenticate to Vanta endpoints, so share it only with trusted administrators and rotate it through Vanta when needed.

Available operations include listing tests and test entities, controls and control tests, control documents, documents and linked resources, integrations, frameworks and framework controls, people, risks, and vulnerabilities. Use these reads to locate evidence and status; the tool does not change a test or certify that a control is complete.
