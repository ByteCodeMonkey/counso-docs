> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Users and groups provisioning

Dust supports automated user and group management through SCIM 2.0 (System for Cross-domain Identity Management). With this enterprise feature, users are created, updated, and deactivated in Dust automatically from your IdP.

SCIM provisioning can be enabled for enterprise users. You'll need administrative access to both Dust and your IdP.

1. In Dust, navigate to Admin > People & Security > Domain and Members > User provisioning > Setup Directory sync
2. Select you identity provider (IdP) from the list
3. Follow the steps
4. **Important note for Enterprise customers:** to enable department-segmented analytics, customers must provision relevant groups to Dust.

<Info>
  Check your IdP documentation along the way The setup experience may vary depending on the selected IdP. We recommend checking the documentation of your IdP (specifically the sections about SSO, SAML and SCIM) as each might have specificities. (*For example, [Okta (OIDC)](https://help.okta.com/en-us/content/topics/apps/apps_app_integration_wizard_scim.htm) might require you to create 2 applications - one for SSO, one for SCIM*)
</Info>

## Assign roles from groups

You can automatically grant the **Admin** or **Manager** role to your users based on their group membership. In Dust, go to **Settings & Governance > Roles** (admin only) and map any workspace group to a role:

* Members of a group mapped to a role inherit that role.
* A user always keeps the highest role granted across their groups (admin > manager).
* A group can grant at most one role.

Any workspace group can be mapped to a role — it does not need to be provisioned from your IdP, so manually managed groups work too. For provisioned groups, create the group in your IdP, assign the appropriate members, and synchronize it, then map it to a role in Dust.

<Info>
  This replaces the previous behavior where roles were assigned through groups named exactly "**dust-admins**" and "**dust-managers**".
</Info>
