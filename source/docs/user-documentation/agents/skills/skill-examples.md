> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Skill Examples

This page contains a few examples of skills that you can re-create and tweak to fit your use cases.

## Example 1: Add CRM Deal Entry

In a Sales team, maintaining good hygiene of a CRM can be a challenge, and using multiple Agents to fill in CRM deal entries can lead to variable levels of quality.

In this example, we are creating a “CRM Deal entry” Skill, which we will give to all agents involved in writing data in our CRM. One central place to maintain the skill, no more inconsistencies!
The skill instructions can be basic at first, and be updated later, all agents will benefit from it.

### Step 1: Describe the CRM Skill

Giving a clear description to the Skill will allow your agents to quickly decide if it should be used in a given situation. For this skill, let’s use the following description :

```
This skill contains the best way to add a deal in our CRM, including best practices from the company.
```

### Step 2: Add guidelines

For this skill’s instructions, lets’s focus on describing our company’s specificities like non standard field names (SPQR in this example) or our qualification of deal sizes, which are different from other companies :

***

```
**Purpose**
Guide correct formatting for adding deals to the CRM system.

**Key Field Rules**
The following fields are required in order to create a deal entry in the CRM

1- Deal Amount (amount_usd)
- Numeric only, no symbols
- Example: 15000

2- Deal Size (size_bucket)
- small: < $2,000
- big: ≥ $2,000

Example: $2,500  big

3- SPQR Stage (spqr_stage)
"SPQR" = Sales Pipeline Qualification Rating (legacy name)
Values: suspect | prospect | qualified | ready_to_close

4-Close Date (close_date)
- Format: YYYY-MM-DD

**Example Deal**
Deal Name : Acme Corp - Enterprise
Amount Usd : 15000
Size Bucket : big
Spqr Stage : qualified
Close Date : 2026-03-15

**Common mistakes**:
- Setting a $1,800 deal as "big" (should be "small")
```

### Step 3: Add tools

This skill is all about interactions with our CRM, so let’s add the CRM as a tool. It could be HubSpot or Salesforce, for example.

The skill is now ready, it can be included in any agent that interacts with the Sales pipeline!

***

## Example 2: Branded Frame Creation

Many teams create visualizations and presentations through Dust agents, but maintaining consistent brand identity across different agents and team members can be challenging. Colors, fonts, and styling vary, leading to inconsistent outputs.

In this example, we're creating a "Branded Frames" Skill that ensures all visualizations follow your company's visual identity guidelines. Give this skill to any agent that creates charts, dashboards, or presentations, and maintain your brand consistency from one central place.

### Step 1: Describe the Branded Frames Skill

A clear description helps agents know when to apply your brand guidelines:

```
Use this skill to create Frames that follow the company's branding and visual guidelines.
```

### Step 2: Add guidelines

This section assumes you have already created a Frames template and saved it in a Dust folder.

To use this template in every Frame created via the skill, you can mention its existence directly in the guidelines

Include your specific brand colors, fonts, and design principles, along with instructions to use your template:

```
Use the following template to create new Frames: /
```

Hitting `/` in the guidelines section will cause a dropdown to open. From there you can search for your template (title-based). Just start typing the name of the template you saved and save it.

If needed, you can add additional guidelines in natural language, for instance to describe the kind of layout that is expected, to explain the meaning of each color and what they are used for, etc..

The skill is now ready to be included in any agent that creates visualizations, reports, or presentations!

This approach makes it much more practical - users can maintain their actual brand template in one place and all agents will use it consistently.

## Example 3: Company Tone of Voice

Different team members and agents may communicate with varying tones, leading to inconsistent messaging both internally and with customers. Some messages might be too formal, others too casual, creating a disjointed company voice.

In this example, we're creating a "Tone of Voice" Skill that ensures all communications reflect your company's personality and values. Apply this skill to customer-facing agents, internal communication assistants, and content creation agents to maintain a consistent voice.

### Step 1: Describe the Tone of Voice Skill

A clear description helps agents understand when to apply your tone guidelines:

```
Use this skill when communicating externally with customers, prospects, or partners. This ensures all outbound communications follow our company's tone of voice, balancing professionalism with approachability while reflecting our core values.
```

### Step 2: Add instructions

Define your company's specific voice characteristics and provide concrete examples (this is an example, needs to be customize to fit your actual internal guidelines):

```
**Purpose**
Maintain consistent tone of voice across all external communications that reflects our company personality.

**Our Voice Principles**
1. **Clear, not corporate**: Use simple language. Avoid jargon unless necessary.
2. **Helpful, not robotic**: Be warm and human. Show you care about solving problems.
3. **Confident, not arrogant**: Be direct and knowledgeable without being condescending.
4. **Professional, not stuffy**: Maintain professionalism while being approachable.

**Word Choices**

Prefer:
- Help, assist (not "facilitate" or "leverage")
- Use (not "utilize")
- Simple (not "simplistic")
- Fix, resolve (not "remediate")
- Show, explain (not "demonstrate")
- We recommend (not "we would suggest that you might consider")

**Sentence Structure**
- Keep sentences short and scannable
- Use active voice: "We built this" not "This was built"
- Front-load important information
- Break long content into bullet points or sections

**Tone by Context**

**Customer Support:**
- Lead with empathy: "I understand this is frustrating"
- Take ownership: "I'll make sure we resolve this"
- Be specific about next steps and timelines

**Product Updates:**
- Lead with benefits, not features
- Use "you" and "your" to stay user-focused
- Celebrate improvements: "You can now..." instead of "We added..."

**Sales & Prospects:**
- Focus on value and outcomes, not features
- Be consultative, not pushy
- Ask questions to understand their needs

**Examples**

Bad - Too Corporate:
"We are pleased to inform you that the requested functionality has been implemented pursuant to your feedback."

Good - Our Voice:
"Good news! We've added the feature you asked for. Here's how to use it..."

Bad - Too Casual:
"Hey! So yeah, we totally messed up on that deployment lol. Our bad!"

Good - Our Voice:
"We made a mistake with yesterday's deployment and some features were temporarily unavailable. We've fixed the issue and added checks to prevent this in the future. Thanks for your patience."

**Common mistakes to avoid:**
- Using corporate buzzwords like "synergy," "leverage," "circle back"
- Being overly apologetic (one "sorry" is enough)
- Using passive voice to avoid responsibility
- Exclamation marks in every sentence!!
```

### Step 3: Add tools

This skill doesn't require specific tools: it's about how agents communicate. You can add communication tools to pull examples of past communications such as:

* **Slack** - for internal messages
* **Gmail** or **Outlook** - for email communications
* **HubSpot** or **Zendesk** - for customer communications

***
