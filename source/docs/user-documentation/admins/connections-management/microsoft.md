> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Microsoft

You can connect Dust to your Microsoft suite to enable access to the documents, spreadsheets, and presentations hosted in your Sharepoint drives. Only the content within the scope of the admin's Drive permissions will be available in Dust. The admin can granularly select the exact data they want to make available to Dust.

Dust doesn't take into account files with more than \~800Kb of extracted text. Supported files include text files (docx, pptx, .txt...), but also PDFs. You can activate PDF indexation at Spaces > Connected data and click on Manage Microsoft). xlsx files are parsed and each worksheet is available for table queries.

To set up the Microsoft connection, follow these steps:

1. Navigate to Spaces > Connections > Microsoft
2. Acknowledge dust access to your Microsoft data
3. Login to your microsoft account and authorise permission. Only organisational accounts are supported, not personal ones.
   NB : If you're not an admin on your Microsoft workspace, will have to ask your administrator to consent Dust permissions for you. Once you clicked on "Request Admin consent", you will have to wait for the administrator to validate your request in their Azure admin panel (nb : this might take a few minutes before showing up on the Azure admin panel)Once authorised, perform step 3 again. This time around, the connection will finalize.
4. You can now select the data you want to synchronise with Dust :

## Entra ID details

<Info>
  Alternative setup outside of Dust

  Entra admins can also decide to create the application in Entra themselves, and will need the following consent URL :

  ```text theme={null}
  https://login.microsoftonline.com/{{your-entra-tenant-id}}/adminconsent
    ?client_id=04c0e2b8-9852-4fad-9a5c-b97b29e95492
    &scope=https://graph.microsoft.com/Files.Read.All
           https://graph.microsoft.com/Sites.Read.All
           https://graph.microsoft.com/User.Read
           offline_access
    &redirect_uri=https://{{eu. when in Europe}}dust.tt/oauth/microsoft/finalize
  ```
</Info>

When setting up a connection, Dust will create an App in Entra ID called **Dust connector**. It will have the following permissions, that the Entra Admin will grant either directly by setting up the connection from Dust, or by accepting the Admin consent request

Here is the list of permissions requested

| **API name**    | **Claim value** | **Permission**                     | **Type**      | **Granted through** | **Granted by**   | Comment                                                |
| --------------- | --------------- | ---------------------------------- | ------------- | ------------------- | ---------------- | ------------------------------------------------------ |
| Microsoft Graph | Files.Read.All  | Read all files that user can a...  | **Delegated** | Admin consent       | An administrator | For the connector to access files to ingest            |
| Microsoft Graph | Sites.Read.All  | Read items in all site collecti... | **Delegated** | Admin consent       | An administrator | For the connector to access Sharepoint sites to ingest |
| Microsoft Graph | User.Read       | Sign in and read user profile      | **Delegated** | Admin consent       | An administrator | For the connector to log in as the service account     |
| Microsoft Graph | offline\_access | Maintain access to data you...     | **Delegated** | Admin consent       | An administrator | For the refresh of the connection after timing out     |

## Managing permissions

* You should use a **dedicated microsoft account** (eg. [dust-account@yourdomain.com](mailto:dust-account@yourdomain.com)) to manage permissions for Dust. This will dictate which sites are visible to the connection in Dust.
  * All Public Sharepoint sites and groups will be seen
  * All Private Sharepoint sites where the dedicated microsoft account is "Member" or more will be seen in the Microsoft connection
  * All Teams channels that the microsoft account is part of (Standard, Shared and Private) will be seen in the Microsoft connection
  * The dedicated microsoft account needs read permission on the files. All files and documents visible by the user will be available for Dust.

<Info>
  **Group memberships in Sharepoint**

  In Sharepoint, access in not always granted by direct addition of the Microsoft account to the member list of the Sharepoint site/group, and is often inherited from group memberships. Make sure that you review the groups that [dust-account@yourdomain.com](mailto:dust-account@yourdomain.com) belongs to, in order to tightly control what the Dust connection will be able to see
</Info>

***

You can also use a [Service Principal ](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal) to login : fill in your tenant ID, client ID, the secret to use, and optionally the list of sites your service principal has access to, if you're using the `Sites.Selected` permission.

Step 1 : Create an App Registration in Entra with the following **Application** permissions on the **Microsoft Graph API**

Use the following URL as redirect URI : [https://dust.tt/oauth/microsoft/finalize](https://dust.tt/oauth/microsoft/finalize) or [https://eu.dust.tt/oauth/microsoft/finalize](https://eu.dust.tt/oauth/microsoft/finalize)

| **API name**    | **Claim value**                             | **Permission**                     | **Type**      | **Granted through** | **Granted by**   | Comment                                                |
| --------------- | ------------------------------------------- | ---------------------------------- | ------------- | ------------------- | ---------------- | :----------------------------------------------------- |
| Microsoft Graph | Files.Read.All                              | Read all files that user can a...  | **Delegated** | Admin consent       | An administrator | For the connector to access files to ingest            |
| Microsoft Graph | Sites.Read.All <br />or<br />Sites.Selected | Read items in all site collecti... | **Delegated** | Admin consent       | An administrator | For the connector to access Sharepoint sites to ingest |
| Microsoft Graph | User.Read                                   | Sign in and read user profile      | **Delegated** | Admin consent       | An administrator | For the connector to log in as the service account     |
| Microsoft Graph | offline\_access                             | Maintain access to data you...     | **Delegated** | Admin consent       | An administrator | For the refresh of the connection after timing out     |

And Grant admin consent for these permissions

Step 2 : In Security & Credentials, create a secret

Step 3 : Fill in the details in Dust

**Tenant ID**: Directory (tenant) ID from Step 1

**Client ID**: Application (client) ID from Step 1

**Service Account secret**: Secret Value from Step 2

**Selected SharePoint site(Optional)**: Site IDs allowed for Dust to ingest - one per line

NB : In Sharepoint admin, you will need to Select the Sites that your app has access to. Check out the [Microsoft documentation](https://learn.microsoft.com/en-us/graph/permissions-selected-overview?tabs=http)

This is usually done by API or Powershell using the `Grant-PnpAzureADAppSitePermission` command. Check out the [Microsoft documentation](https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins-modernize/understanding-rsc-for-msgraph-and-sharepoint-online#granting-permissions-via-pnp-powershell)

A synchronization happens every 5 minutes. All files created, modified or deleted during this period will not be updated immediately, but changes will be reflected only once a new synchronization is executed.

If a lot of files have been added or modified, the synchronization will take longer time.

## Labels

Dust will sync the custom columns set on files when used in Sharepoint lists. They will be expose as **labels** and included in the document above the content itself.

**Tags**  allow for keyword search and filtering while prepending them to the document content will expose them to the [semantic search](/docs/user-documentation/agents/knowledge/search-data-sources) tool.
