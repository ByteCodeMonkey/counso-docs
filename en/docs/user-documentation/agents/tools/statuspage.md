# Statuspage

The Statuspage tool lets an Agent read page and component information and, when authorized, create or update incidents. The acting account needs access to the intended Statuspage site, and write permissions should be limited to incident operators.

An administrator adds Statuspage under **Spaces → Tools**, provides the page/account details and authentication requested by the current form, and shares the tool with a restricted Space. Select the credential role appropriate to the task. Add it to an Agent and first read the page and component states.

Before creating an incident or publishing an update, confirm the page, component, status, impact, and public wording. After a change, retrieve the same incident by its identifier and verify the published state. If a page is missing or edits are unavailable, check the API key, account role, and page ownership. Do not let a general-purpose Agent publish incident communications without a review step.

## Available operations

The tool provides **Get Page**, **List Components**, **Get Component**, **List Incidents**, **Get Incident**, **Create Incident**, and **Update Incident**. Reading a page/component needs standard page access; creating or updating incidents requires an **Incident Manager** role. Scheduled maintenance may require **Maintenance Manager**. The API key belongs to a Statuspage user, so confirm that user's roles on the target page.
