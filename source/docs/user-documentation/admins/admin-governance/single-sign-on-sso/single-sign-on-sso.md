> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Single Sign-On (SSO)

## Overview

Dust supports Single Sign-On (SSO) to manage your team's access to Dust through your existing Identity Provider (IdP), so authentication is managed in one place.

## Setting up Single Sign-On (SSO)

To enable SSO for Dust, follow these steps to create a custom app integration in your Identity Provider (IdP).

### 1. Identify an Admin

Choose an admin with full access to both your IdP admin dashboard and Dust admin. This is necessary as enabling SAML SSO requires creating a custom integration in your IdP.

### 2. Get Your Dust SAML Configuration Values

1. In Dust, navigate to **Admin > People & Security > Domain and Members > Single Sign-On > Activate SSO**
2. Select your IdP from the list
3. Follow the steps to create the app in your IdP and configure it with Dust.

For a detailed walkthrough of the SAML setup, see [SAML SSO](/docs/user-documentation/admins/admin-governance/single-sign-on-sso/saml-sso).

### 3. Enforcing SAML Single Sign-On (SSO) in Dust

After enabling SSO, you have the option to enforce it across the entire workspace. This means that users will no longer be able to log in using their social media accounts.

<Warning>
  Enabling this setting will log out all users who are not currently using SAML,
  and they will be required to log back in using their IdP credentials.
</Warning>
