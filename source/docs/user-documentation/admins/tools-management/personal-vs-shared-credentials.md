> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Personal vs Shared Credentials for Tools & MCP Servers

When adding tools that require authentication (like GitHub, HubSpot, or remote MCP servers), you have two credential configuration options. Understanding these options is crucial for managing data security and user access in your workspace.

## Shared Credentials

**What it means**: One set of credentials shared by all workspace users

**Setup**: Admin provides credentials during tool setup

**Usage**: All users access the external service using the same account

**Best for**: Centralized control, shared service accounts, or when you want consistent permissions across all users

ℹ These credentials will be used by all users who have access to the tool.

## Personal Level Credentials

**What it means**: Each user connects their own individual credentials

**Setup**: Admin completes initial OAuth flow, then each user authenticates individually

**Usage**: Users access external services with their personal accounts

**Best for**: User-specific data access, individual accountability, or when users need different permission levels

<Info>
  **Even with personal credentials, admins must complete the initial OAuth flow to verify the connection works and gather necessary metadata (like Slack team ID, Salesforce instance URL, etc.) that will be reused for individual user connections.**

  **Making the Decision**
</Info>

### Choose Shared when:

* You want centralized control over what data is accessible
* You're using a shared service account
* All users should have the same level of access
* You want to simplify user onboarding

### Choose Personal Level when:

* Users need access to their individual accounts (personal GitHub repos, individual HubSpot permissions, etc.)
* You want user actions to be attributed to the correct person
* Different users have different permission levels in the external service
* You want to maintain individual audit trails

## For Shared Credentials:

Navigate to Knowledge > Tools in your workspace\
Click Add Tools and select your desired tool\
Choose Shared credentials\
Complete the OAuth flow with the shared account

## For Personal Credentials:

Navigate to Knowledge > Tools in your workspace\
Click Add Tools and select your desired tool\
Choose Personal credentials\
Complete the admin OAuth flow to:

* Verify that the connection is working properly
* Gather necessary metadata (team IDs, instance URLs, etc.)
* Enable the tool for workspace users

Users will then authenticate individually when first using the tool

## Security Considerations

Shared credentials: Simpler to manage but less granular control\
Personal credentials: More secure attribution but requires both admin setup and individual user authentication\
Data sharing: Both options share the same data with external services; the difference is whose account performs the actions

You can change authentication settings for existing tools by:

Going to the tool's configuration page\
Updating the authentication method\
Re-authenticating as needed (admin OAuth flow required for personal credentials)

*Note that changing from shared to personal credentials will require the admin to complete the initial OAuth flow, followed by individual user authentication.*

## Managing Your Personal Credentials (For Users)

End users can view and disconnect their personal tool credentials from the Dust app:

Open your user menu and select Tools & Triggers

On this page, you'll see a list of tools you've connected, each with a Disconnect button. Use Disconnect when:

* An OAuth flow failed and you need to start fresh
* You connected the wrong account
* You keep seeing "authentication required" prompts even after connecting

After disconnecting, simply use the tool again and you'll be prompted to re‑connect.
