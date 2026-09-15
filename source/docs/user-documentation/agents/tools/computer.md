> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Computer

Computer is a base capability of Dust agents. It gives an agent a safe, temporary workspace where it can run code, inspect files, create new files, process data, and return finished artifacts to the conversation.

You do not need to ask for Computer explicitly. When you work with files, Dust will often use Computer behind the scenes because it is the preferred way for agents to process files.

Computer is useful when the final output is a real file, such as a cleaned spreadsheet or a generated slide deck. It is also useful when the final output is text, but that text needs to be computed deterministically, for example a calculation, a mathematical result, or an analysis computed from an Excel file.

<Info>
  Think of Computer as a controlled workbench for your agent. The agent can open files with software, transform them with code, and bring the finished result back into the conversation.
</Info>

## When Computer helps

Computer is a good fit when you want an agent to:

* Clean or transform an Excel workbook or CSV.
* Edit an existing PowerPoint deck.
* Create a PowerPoint deck from notes, a spreadsheet, or meeting context.
* Update a Word document or extract information from a PDF.
* Process many files or an archive at once.
* Create charts, reports, or downloadable files.
* Run exact calculations or math.
* Compute an answer from an Excel file or other structured data.
* Process a large tool output with code, then return only the useful result.

Computer is usually not needed for short questions, simple summaries, or tasks that do not require files, code, exact calculations, or generated artifacts.

## Work with Excel and CSV files

Computer can inspect, calculate, clean, transform, and export spreadsheets with code. This makes it especially useful for tasks where every row matters or where you need the result to be repeatable.

Common examples include:

* Cleaning messy data.
* Adding columns, formulas, or summary tables.
* Computing exact totals, cohorts, or business metrics.
* Splitting or merging sheets.
* Creating charts from spreadsheet data.
* Returning an updated `.xlsx` or `.csv` file.

For best results, upload the file and describe the change you want. If formatting and formulas matter, ask Dust to edit the existing workbook instead of rebuilding it from scratch. You can also ask Dust to explain what it changed and validate key calculations before returning the final file.

### Example prompts

```text theme={null}
Clean this Excel workbook, remove duplicate customer rows, add a summary sheet by region, and return an updated .xlsx file.
```

```text theme={null}
Use the uploaded spreadsheet to calculate total ARR by segment. Return the answer in text and include the formulas or assumptions you used.
```

```text theme={null}
Update this workbook in place: keep the formatting, add a new column for gross margin, and create a chart on a new sheet.
```

## Work with PowerPoint files

Computer can create and edit real `.pptx` files. This is useful when the output needs to be a deck rather than a text outline.

Common examples include:

* Creating a deck from notes, a CSV, or an Excel workbook.
* Filling a template deck.
* Updating slides in an existing deck.
* Adding charts, tables, and screenshots.
* Preparing QBRs, reporting decks, and customer-facing summaries.

For branded decks, upload an existing deck and ask Dust to use it as a template. Ask Dust to preserve layouts and styles where possible. You should still review the final deck before sending it externally, especially when brand precision or slide design matters.

### Example prompts

```text theme={null}
Use this PowerPoint as a template and this CSV as the data source. Create a 10-slide QBR deck with charts and a final recommendations slide.
```

```text theme={null}
Update slides 4 through 7 with the new metrics from this Excel workbook. Keep the same layout and return an updated .pptx.
```

```text theme={null}
Turn these meeting notes into a short executive deck. Use the uploaded deck as the style reference.
```

## Work with other file types

Computer can also help with other file workflows, including:

* Word documents, for drafting, editing, or filling templates.
* PDFs, for extracting text, reviewing content, or converting pages into images when needed.
* Images and generated charts, for analysis or report creation.
* Archives such as `.zip` files, for extracting and processing many files at once.
* Generated artifacts, such as reports, CSV exports, charts, or converted files.

When the task involves a template, ask Dust to preserve the existing structure. When the task involves many files, ask Dust to keep intermediate work inside Computer and return only the final useful outputs.

## Get exact text answers with code

Computer is not only for returning files. Sometimes the best final answer is plain text, but the work behind it needs exact computation.

Use Computer for text answers when you need:

* Calculations that should not rely on mental math.
* Math or data transformations.
* Results computed from every row in a spreadsheet.
* A conclusion based on a large CSV, JSON file, or tool output.
* A repeatable workflow that should produce the same answer if run again.

Example:

```text theme={null}
Using the uploaded Excel file, calculate the weighted average contract value by customer segment. Return only the final table and explain how you computed it.
```

## Network access

Some tasks require Computer to contact an external service, for example an API, a website, or a file storage system. Dust keeps this controlled with an allowlist.

Computer does not get open internet access by default. Before it can contact a website or API, Dust checks whether that domain has been allowed.

A domain can be allowed in two ways:

* A workspace admin can preapprove trusted domains for the workspace.
* If admins enable it, an agent can ask you to approve a specific domain for the current conversation only.

If you do not approve a requested domain, Computer cannot use that domain. If a request is blocked, the agent can see which domain was denied and explain what needs to be allowed.

<Info>
  Temporary user-approved domains apply only to the current Computer. They do not change workspace-wide admin settings.
</Info>

<details>
  <summary>Technical detail: how domain access works</summary>

  Computer checks outbound requests against allowed domains. A domain can be allowed because it is part of Dust's default system allowlist, because a workspace admin added it to the workspace allowlist, or because a user approved it for the current Computer. Workspace admins can add exact domains, such as `api.openai.com`, or wildcard domains, such as `*.example.com`. A temporary user approval is scoped to the current Computer and does not change workspace settings.
</details>

For admin setup instructions, see [Computer admin setup](/docs/user-documentation/admins/tools-management/computer-admin-setup).

## Configuration variables and secrets

Admins can configure values that are available to Computer. There are two kinds: configuration variables and HTTPS secrets.

A configuration variable is for non-sensitive configuration, such as a public endpoint, a region, an identifier, or a model name. It can be read by the agent and by code running in Computer, so it should not contain credentials.

An HTTPS secret is for credentials, such as API keys and tokens. Computer sees only a placeholder, not the real secret. When Computer makes an approved HTTPS request to a domain configured for that secret, Dust substitutes the real secret on the way out.

A simple way to think about it:

A configuration variable is like a label on the workbench: it tells Computer which setting to use. A secret is different. It is like a sealed envelope that can only be delivered to an approved service. The agent can use the envelope to make the request, but it cannot open the envelope and read the credential inside.

<details>
  <summary>Technical detail: configuration variables vs. HTTPS secrets</summary>

  `DST_*` variables are mounted as normal environment variables. Use them for non-sensitive values such as public endpoints, feature flags, identifiers, regions, or model names.

  `DSEC_*` variables are placeholders for HTTPS secrets. Code running in Computer should send the placeholder in an HTTPS request to an approved domain. Dust substitutes the real secret only for approved outbound HTTPS requests to domains configured for that secret. The raw secret is not exposed inside Computer.
</details>

For setup instructions, see [Computer admin setup](/docs/user-documentation/admins/tools-management/computer-admin-setup).

## Advanced workflows with dsbx

For advanced workflows, Computer includes `dsbx`, a command-line interface that helps code running in Computer interact with the Dust environment.

This is useful when a workflow needs to process large files, large tool outputs, or many intermediate results. Instead of copying everything into the conversation, the agent can run code, filter the data, and bring back only the final answer or finished file.

Examples include:

* Processing a large CSV locally and returning only a summary and cleaned file.
* Querying or calling a tool, storing the raw result locally, and computing a smaller final answer.
* Using `dsbx env` to list configured variable names and approved domains without printing secret values.

## Best practices

Use these practices to get better results with Computer:

* Be explicit about the output you want, for example `.xlsx`, `.pptx`, `.csv`, PDF, or a text summary.
* When editing a template, upload the existing file and ask Dust to preserve structure and style.
* For spreadsheets, ask Dust to validate formulas and totals.
* For decks, review the final result before sending externally.
* Do not paste credentials into prompts. Ask an admin to configure HTTPS secrets instead.
* For API requests, make sure the domain is allowed or approve the domain when prompted.
* Use Computer for exact calculations instead of relying on the model to do math in text.

## Common pitfalls

Computer can handle a wide range of tasks, but it is still worth reviewing generated files. Keep these points in mind:

* Complex decks may not be pixel-perfect on the first attempt. Ask Dust to iterate and review the final file.
* If workbook formatting and formulas matter, ask Dust to edit the original workbook rather than recreate it.
* Do not use configuration variables for credentials. Use HTTPS secrets.
* If a request is blocked, check whether the domain needs to be allowed.
* If a request reaches the external service but returns an authorization error, the issue is usually credentials or permissions, not domain access.
