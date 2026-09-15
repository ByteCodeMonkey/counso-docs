---
title: "Set up single sign-on"
---
Single sign-on (SSO) lets members authenticate through the identity provider (IdP) used by their organization. An administrator with access to both the workspace administration area and the IdP console should set up the connection.

## Configure SSO

1. In workspace administration, open **People & Security**, then **Domain and Members**, and choose **Single Sign-On**.
2. Select **Activate SSO** and choose the identity provider shown in the setup flow.
3. Keep the setup page open and follow its instructions to create a SAML application in the IdP and enter the values shown by the workspace.
4. Complete the IdP fields, return to the workspace, and save the configuration.
5. Test sign-in with an account whose identity attributes match its workspace membership.

For the detailed SAML attribute and application setup, see [SAML SSO](/docs/user-documentation/admins/admin-governance/single-sign-on-sso/saml-sso).

## Enforce SSO only after testing

After SSO is configured, an administrator can enforce it across the workspace. This prevents members from signing in through other sign-in methods. Enforcement may sign out people who are not already using SAML, so first confirm that a test member and an administrator can sign in through the IdP and retain an administrator recovery route.
