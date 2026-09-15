---
title: "Set up SAML single sign-on"
---
SAML single sign-on (SSO) lets members authenticate to the workspace through your organization's identity provider (IdP). An administrator with access to both the workspace settings and the IdP console should configure and test the connection.

## Before you begin

Prepare an IdP administrator and a test account whose email and name attributes are populated. Keep access to the workspace's SSO setup page while configuring the IdP; it supplies the service values that must match in both systems. Keep an administrator recovery sign-in available until testing succeeds.

## Create the SAML application

1. In the workspace administration area, open **People & Security** and then **Single Sign-On**. Choose the option to activate SSO so the workspace displays its SAML values.
2. Note the **ACS (Assertion Consumer Service) URL** and **Entity ID / Audience URI** shown there. Use these exact values in the new SAML 2.0 application in your IdP.
3. In the IdP, configure the application name and the service values from the workspace. Set its required attributes to identify the user consistently:
   - **Email** (`email`): the user's workspace email.
   - **First name** (`given_name`): map the IdP's given-name field.
   - **Last name** (`family_name`): map the IdP's surname field.
   - **Email verified** (`email_verified`): set the value required by the workspace's SAML setup.

Attribute labels and schema names can differ between identity providers. Use the mapping format expected by your IdP and the requirements shown in the workspace. For example, some providers use a name-identifier claim for email; make sure it resolves to the same email the member uses in the workspace.

4. From the IdP application, copy the **Single Sign-On URL** and **X.509 certificate**.
5. Return to the workspace SSO page, enter those IdP values, and choose **Create SAML Configuration**.

## Test before enforcement

Sign in with a dedicated test account in a private browser window. Confirm that authentication reaches the intended workspace and that the member is identified by the expected email and name. If automatic workspace joining is offered, review whether it matches your domain policy.

After the test succeeds, an administrator can enforce SAML for the workspace. Enforcement may sign out members who are using another sign-in method, so let members know how to use the IdP and keep a recovery route for administrators.

## Optional: IdP-initiated sign-in

Some organizations launch sign-in from the IdP rather than starting at the workspace. Use this flow only if the workspace's SSO configuration supports it. Check the security implications with your identity team, then ask workspace support to enable the flow for the specific connection if required. Otherwise, use the standard sign-in flow initiated from the workspace.

## Troubleshooting

- Compare the IdP's ACS URL and audience value with the exact values displayed in the workspace.
- Check that the email claim matches the member's workspace email and that required name and verification attributes are populated.
- Confirm the certificate and sign-in URL were copied from the intended IdP application.
- Keep SSO enforcement disabled until the test account and administrator recovery route both work.
