> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Allowing an agent to send an email

**Dust Apps are being deprecated.** Only Dust Apps that were created before October 2025 are accessible to users. The creation of new Dust Apps is now deactivated.

Here’s a short Dust app to send email, we’ve use Make to do this example (but you can use any other tool, such as Zapier).

### Steps

1/ Configure a new scenario in Make with their [Email module](https://www.make.com/en/help/tools/email).

2/ Configure a new dust app, we called our “send\_email”.

3/ Use this Dust App from an agent!

In the prompt of your agent, you can say:

*You have the ability to send emails. Only use this if the user explicitly asked you to do it, and only if the recipient of the email is not ambiguous. If the recipient is not obvious based on recent conversation content, ask for confirmation or precision. Never invent an email address. You must always ask for the email address of the recipient if it is not obvious from the conversation history.*

### Here’s the code required in the Dust app.
