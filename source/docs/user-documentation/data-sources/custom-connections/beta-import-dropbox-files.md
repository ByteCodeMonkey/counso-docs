> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# [Beta] Import Dropbox Files

This script imports your Dropbox files into a Dust folder and keeps them in sync.

This open-source script, **available on GitHub at[dust-tt/dust-labs/dropbox](https://github.com/dust-tt/dust-labs/tree/main/dropbox)**, automates the process of exporting your Dropbox files (including Paper docs) and importing them into a Dust datasource. It supports multiple file types and preserves file metadata, like so:

```
File Name: Getting Started with Two-Factor Authentication.paper
Path: /Security/Authentication/Getting Started with Two-Factor Authentication.paper
File ID: id:a4bVxYzW2cQ9dE3fG1hJ2kL3
Client Modified: 2024-03-18T15:30:00.000Z
Server Modified: 2024-03-18T15:30:00.000Z
Format: paper

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

The script then formats and uploads this data to Dust, maintaining the original file structure and content integrity.

### Key Features

* **Multiple File Type Support**: Works with various file formats including:
  * Dropbox Paper documents (.paper)
  * Markdown files (.md)
  * Word documents (.docx)
  * Text files (.txt)
* **Metadata Preservation**: Maintains important file information:
  * Original file names and IDs
  * Full file paths and folder structure
  * Creation and modification dates
  * File format details
* **Smart Processing**:
  * Concurrent file processing for improved performance
  * Rate limiting to respect API constraints
  * Error handling with retries
  * Extension-based filtering options\
    Run the script on a schedule to keep your Dust knowledge base synchronized with your Dropbox content. Your agents can then use the imported documents for analysis, content discovery, and knowledge management. The script handles large volumes of Dropbox files reliably.

### Getting Started

1. **Prerequisites**:
   * Node.js (v14 or higher)
   * npm (Node Package Manager)
   * Dropbox account with API access
   * Dust account with API access
2. **Installation**:

```
git clone [git@github.com](mailto:git@github.com):dust-tt/dust-labs.git
cd dust-labs/dropbox
npm install
```

3. **Configuration**:\
   Create a .env file with your credentials:

```
DROPBOX_API_KEY=your_dropbox_api_key
DUST_API_KEY=your_dust_api_key
DUST_WORKSPACE_ID=your_workspace_id
DUST_DATASOURCE_ID=your_datasource_id
DUST_SPACE_ID=your_space_id
```

4. **Usage**:\
   To sync all files:

```Text code theme={null}
npm run sync
```

To sync specific file types (e.g., only Paper docs):

```
npm run sync -- --ext .paper
```

### Best Practices

1. Start Small: Begin with a specific file type or folder to test the integration
2. Monitor Progress: Watch the console output for sync status and any potential issues
3. Regular Updates: Schedule periodic syncs to keep your Dust knowledge base current
4. Error Handling: Check logs for any failed imports and address issues promptly

The script is actively maintained and handles large-scale document synchronization while preserving data integrity.
