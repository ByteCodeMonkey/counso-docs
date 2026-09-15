> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# SAML SSO

Dust supports SAML Single Sign-On (SSO) to manage your team's access to Dust through your existing Identity Provider (IdP), so authentication is managed in one place.

## Supported Identity Providers

While this guide focuses on generic SAML configuration, Dust works with all
major SAML-compliant Identity Providers including: \_ Okta \_ Azure AD \_
Google Workspace \_ OneLogin

To enable SSO for Dust using SAML, follow these steps to create a custom app integration in your Identity Provider (IdP).

## 1. Identify an Admin:

Choose an admin with full access to both your IdP admin dashboard and Dust admin. This is necessary as enabling SAML SSO requires creating a custom integration in your IdP.

## 2. Get Your Dust SAML Configuration Values

1. In Dust, navigate to Admin > People & Security > Single Sign-On > Activate Single Sign-On
2. You'll find all the necessary SAML configuration values that you'll need to set up your IdP:
   * **ACS (Assertion Consumer Service) URL**
   * **Entity ID / Audience URI**

Keep this page open as you'll need these values in the next step.

## 3. Create a Custom App Integration in your IdP

1. Navigate to your IdP's admin dashboard and locate the section for creating new applications or integrations.
2. Select **SAML 2.0** as the protocol when creating a new application.
3. Configure the following SAML settings using the values from Dust:
   * **Application Name:** Enter "Dust" as the app name
   * **ACS (Assertion Consumer Service) URL:** Copy from Dust
   * **Entity ID / Audience URI:** Copy from Dust
   * **Logo:** You can find our logo [here](https://dust.tt/static/AppIcon_228.png).

<Warning>
  **Keep your IdP configuration page open**

  You'll need to copy several pieces of information for the next step: IdP
  Single Sign-On URL, IdP Entity ID, X.509 Certificate.
</Warning>

### SAML Attributes Configuration

The following SAML attributes must be properly configured in your IdP for successful login.

<Info>
  **All attributes are required** to ensure that the SSO connection is functional

  * Make sure that the admin setting up the connection has these fields populated to complete the process
  * Even if EntraID does not require all fields, users must have values in these fields in order to be able to SSO into Dust.
</Info>

#### Required SAML Attributes

* **Email**
  * Claim name: `email`
  * Schema URI: `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier`
  * Used for user identification and authentication
  * Must match the user's email address

* **First Name**
  * Claim name: `given_name`
  * Accepted Schema URIs (any of the following):
    * `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname`
    * `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name`
  * Sets the user's first name in Dust

* **Last Name**
  * Claim name: `family_name`
  * Schema URI: `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname`
  * Sets the user's last name in Dust

* **Email verified**
  * Claim name: `email_verified`
  * Schema URI: `true`
  * Mark the user's email has verified. Required to have existing identities merging.

<Info>
  **Attribute Mapping Reference**

  For IdP administrators, here's the complete attribute mapping schema in JSON format:

  ```json theme={null}
  {
    "email": "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier",
    "given_name": [
      "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname",
      "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name"
    ],
    "family_name": "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname",
    "email_verified": true
  }
  ```
</Info>

Google Workspace SAML
When [setting up a SAML app in Google Workspace ](https://support.google.com/a/answer/6087519?hl=en), it is not possible to set the `email_verified` claim to `true`. This is a known issue in the Auth0 community, which can be bypassed by mapping a dynamic field such as `nameidentifier` to the `email_verified` field

## 4. Enabling SAML Single Sign-On (SSO) in Dust

1. Return to the Dust SSO configuration page (Admin > People & Security > Single Sign-On > Activate Single Sign-On)
2. Enter the following details from your IdP setup:
   * **IdP Single Sign-On URL**
   * **X.509 Certificate**

Once you've entered this information, click on **Create SAML Configuration**. SAML SSO is now enabled on your workspace.

If **Auto-join Workspace** is enabled, all members attempting to log in to Dust using their enterprise email addresses will be automatically redirected to your IdP for authentication.

## 5. Enforcing SAML Single Sign-On (SSO) in Dust

After enabling SSO, you have the option to enforce it across the entire workspace. This means that users will no longer be able to log in using their social media accounts. Please note that enabling this setting will log out all users who are not currently using SAML, and they will be required to log back in using their IdP credentials.

## 6. Using IdP-initiated flows rather than SP-initiated flows (optional)

By default, only SP-initiated flows are allowed on Dust's side. However, if your company is using IdP-initiated flows for convenience, [despite the known security flaws](https://auth0.com/docs/authenticate/protocols/saml/saml-sso-integrations/identity-provider-initiated-single-sign-on), Dust can support this way of authenticating.

ℹ Warning on IdP-initiated flows
If your company is allowing IdP-initiated flows, the message displayed in Dust will be "invalid\_request: IdP-initiated login is not enabled for connection "workspace- not enabled "

To enable IdP-initiated flows for your Dust SSO integration, you'll need to:

1. Contact Dust support to request enabling IdP-initiated login for your specific SSO connection
2. Confirm that you understand and accept the security implications of enabling IdP-initiated flows

The support team will be able to enable this feature for your SSO connection.
