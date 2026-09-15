> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# [Beta] Import Guru Cards

## Guru Cards Importer for Dust

This script imports your Guru cards into a Dust folder and keeps them in sync.

This open-source script, **available on GitHub at[dust-tt/dust-labs/guru](https://github.com/dust-tt/dust-labs/tree/main/guru)**, automates the process of exporting all of your cards and importing them into a Dust datasource. It fetches each card's full metadata, like so:

```
Card ID: 6a7b8c9d-1234-5678-90ab-cdef12345678

Title: Setting Up Two-Factor Authentication
Owner: jane.smith@company.com
First Name: Jane
Last Name: Smith
Verifier: john.doe@company.com
Collection: Security Guidelines
Boards:
  - Security Best Practices
  - Employee Onboarding
Verification Date: 2024-03-18T15:30:00.000Z
Verification State: verified
Verification Interval: 90
Link: https://app.getguru.com/card/6a7b8c9d-1234-5678-90ab-cdef12345678

Content:
Two-factor authentication (2FA) adds an extra layer of security to your account.
Follow these steps to enable 2FA:

1. Log into your account settings
2. Navigate to Security > Two-Factor Authentication
3. Choose your preferred 2FA method:
   - Authenticator app (recommended)
   - SMS verification
   - Security key
4. Follow the setup wizard to complete configuration

Remember to save your backup codes in a secure location.
```

The script then formats and uploads this data to Dust.

Run the script on a schedule to keep your Dust knowledge base up to date with the latest information from Guru. Your agents can then use the card data to analyze trends and improve response quality. The script includes rate limiting and error handling, so it stays reliable even with large volumes of Guru cards.
