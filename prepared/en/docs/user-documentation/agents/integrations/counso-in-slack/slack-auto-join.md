# Automatically join new Slack channels

Slack Auto-Join can automatically join and synchronize new public channels whose names match a pattern. Before using it, a workspace administrator must configure the Slack Connection and enable Auto-Join for the workspace. The rule applies to channels created after the pattern is configured; check existing channels separately.

## Configure a channel pattern

1. Open the Slack integration settings and confirm that Auto-Join is enabled for the workspace.
2. Enter a pattern that identifies only the public channels intended for synchronization.
3. Create a test channel whose name matches the pattern and verify that the integration joins it and begins syncing.
4. Check that the synchronized channel is added to the intended Space and that its audience is appropriate.

For example, a pattern such as `support-*` can match newly created channels such as `support-questions`. Keep patterns specific: a broad pattern can add unrelated conversations to the synchronized data set. Slack administrator permissions may be required to configure or change the integration.

Auto-Join does not make a private channel public or replace the need to review the destination Space's access. Verify what data is synced before relying on the new channel in Agent answers.
