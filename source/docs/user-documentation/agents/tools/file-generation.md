> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# File Generation

## Overview

Dust agents can generate files from text content and convert files between different formats using the File Generation capability. This allows your agents to create downloadable documents in formats like PDF, Word, Excel, and more.

## Supported Formats

The File Generation capability supports the following output formats:

| Format     | Extension               | Description                       |
| ---------- | ----------------------- | --------------------------------- |
| PDF        | .pdf                    | Portable Document Format          |
| Word       | .docx                   | Microsoft Word Document           |
| Excel      | .xlsx, .xls             | Microsoft Excel Spreadsheet       |
| PowerPoint | .pptx                   | Microsoft PowerPoint Presentation |
| CSV        | .csv                    | Comma-Separated Values            |
| Markdown   | .md                     | Markdown text                     |
| Plain Text | .txt                    | Plain text file                   |
| HTML       | .html                   | Web page format                   |
| XML        | .xml                    | Extensible Markup Language        |
| Images     | .jpg, .png, .gif, .webp | Image formats                     |

## How to Enable File Generation

When creating or editing an agent:

1. In the Agent Builder, click on **Add Tools**
2. Select the **File Generation** capability
3. Save your agent

No additional configuration is required.

## How It Works

### Generating Files

The agent can generate files from text content you provide or content it creates. When generating files for binary formats (PDF, DOCX, XLSX, PPTX), the agent can accept content in:

| Tool         | Description                                 |
| ------------ | ------------------------------------------- |
| `Plain text` | Simple text content                         |
| `Markdown`   | Markdown-formatted text that gets converted |
| `HTML`       | HTML content for more complex formatting    |

### Converting Files

The agent can also convert files between different formats. For example:

* Convert a Markdown file to PDF
* Convert HTML to Word document
* Convert CSV to Excel

## Example Use Cases

**Creating a Report:**

```
Please create a PDF report summarizing the quarterly sales data we discussed.
```

**Converting a Document:**

```
Convert this markdown file to a Word document.
```

**Generating a Spreadsheet:**

```
Create an Excel file with the project timeline we outlined.
```

<Tip>
  Generated files appear in the conversation and can be downloaded directly. All
  files in a conversation are accessible via the folder icon.
</Tip>

## Limitations

* Maximum file content size is 64,000 characters for generated content
* Complex formatting in source content may not always convert perfectly between formats
* For interactive data visualizations, consider using [Frames](/docs/user-documentation/pods/frames) instead
