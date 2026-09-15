# Manage Microsoft tools

Microsoft tools use delegated access: an Agent operates through the signed-in Microsoft user, subject to that user's permissions and the actions enabled in the tool. Initial consent may require a Microsoft Entra Privileged Role Administrator or Application Administrator as well as a Counso workspace administrator.

## Complete administrator consent

From **Spaces → Tools → Add Tools**, select the Microsoft tool and begin the authorization flow. When shown, an Entra administrator can select **Consent on behalf of your organization**. If that option is unavailable, submit the consent request and have an Entra administrator approve it from the admin consent requests area. Approval may take time to appear; retry the tool setup after it is approved.

An Entra administrator may instead register and manage the enterprise application directly. In that case, use only the client and redirect values shown by the current Counso setup form. Do not reuse an application ID or callback URL from another environment.

## Permissions by tool

The requested delegated scopes depend on the selected capability. Common scopes include `User.Read` and `offline_access`. Outlook mail may request `Mail.ReadWrite` and `Mail.Send`, plus shared-mailbox scopes when needed. Calendar may request `Calendars.ReadWrite`, `Calendars.ReadWrite.Shared`, and `MailboxSettings.Read`. Drive/SharePoint may request `Files.ReadWrite.All`, `Sites.Read.All`, and `ExternalItem.Read.All`. Excel needs file and site access. Teams may request team, channel, chat, message, and user read/send scopes. Review the actual consent screen and approve only the capabilities the workspace intends to use.

Microsoft scopes do not by themselves make every file or message visible: the signed-in user must still have provider access. Test one permitted object for each tool, and review the user identity before enabling write operations.
