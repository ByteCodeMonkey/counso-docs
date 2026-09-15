> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Google Drive

<Danger>
  **Recommended method**

  The recommended approach to creating a Google Drive Connection is to provision a user [dust-admin@yourdomain.com](mailto:dust-admin@yourdomain.com) in your Google workspace and use that identity to connect Dust to your various data sources. The IT/CISO/(name the right function here) will update Dust data access using that account.\
  This will help them control what Dust has access to by managing the permission of that account on Google Drive.
  The connection between Dust and Google Drive is subject to the initial user's permission. Any changes to a user's Drive permissions could affect the data accessibility on Dust. It's crucial to manage permissions carefully to maintain a stable connection.
</Danger>

You can sync Dust with Shared Google Drive to enable access to documents, spreadsheets, and presentations within your workspace. Only the content within the scope of the admin's Drive permissions will be available in Dust. The admin can granularly select the exact data they want to make available to Dust.

Dust doesn't take into account files with more than 2MB of extracted text. Supported files include GDocs, GSlides, docx, pptx, .txt and .md files and PDFs that contain text.

You can activate the PDF text indexing at Spaces > Connected data > Manage Google Drive

To set up the Google Drive connection, follow these steps:

1. Dust and Google popups to authorize Dust access to your Google workspace data.

2. Google Authorization Acknowledgment

3. Google Sign in modal

4. Google Authorization modal

5. A modal to select the exact data you want to sync with Dust.

Dust modal to select the data you want to sync with your Dust workspace.

* Admins should either designate a single individual to manage Drive permissions for Dust or utilize a virtual user (e.g., [dust@workspace.com](mailto:dust@workspace.com)) for consistent access management. This approach avoids unintentional permission resets and data disconnections.

*  **The email address used to manage permissions should have edition & download rights** on the desired documents to allow them to be read by Dust.

* Sometimes, downloads are blocked for specific documents. **If you don’t see a document in your Gdrive Data Source tree**, you can check that it is **downloadable** by following the path described in this toggle.

*Go in Gdrive > right click on your file > click on “File information” > “Details” > click on the settings wheel (top right) > tick the box "Viewers and commenters can see the option to download, print, and copy”*

Right click on the document for which you want to check access

Click on the wheel on the top right-hand corner

Make sure the boxes are ticked

### Converting Excels to Gsheets automatically

Dust only syncs Google Sheets but is currently not compatible with Excel native format. For a file to be synced by Dust and used in table queries, you need to convert it to GSheet.

**This can be done automatically in your GDrive settings if needed.**\\

If the Google Drive is very large, it is normal for the first synchronisation process to be quite long (over 24 hours, up to several days for extremely large Drives).

* *My synchronisation is taking longer than expected. What should I do?*

<Info>
  **Sync times**

  If your Google Drive contains over c.50k files, the sync time can get long.

  1. Consider syncing only the part of your drive you want to use with Dust.
  2. If you still have such a high number of files, do not hesitate to flag this to us so we can support the process the best way.
</Info>

## Refresh Rate

Data sync between Google Drive and Dust can take a few minutes.

Any additions or removals of data sources are not immediately reflected in Dust.

<Info>
  **File Deletion Timeline**
  Google Drive's deletion runs during the data sync process, which can take a few minutes.
</Info>

## Size limitations

There's a file size limit of 128 MB for Google Spreadsheets and PDFs.

Dust supports up to 50,000 rows per Google sheet. If your spreadsheet has multiple sheets, each sheet is processed individually, so you can have up to 50,000 rows per sheet.

## OCR

The Google Drive connection in Dust will ignore files that do not contain text (documents scanned as images for example).\
For such use cases, OCR can be achieved by directly uploading the pdf to a conversation

## Labels

Labels on google drive items will be used as tags that you can use to filter documents in your agents.

<Info>
  **Custom labels support was added June 13 2025**

  You need to reconnect your google drive (edit permissions) to allow fetching the labels. And update a document to have it re-synced.
</Info>
