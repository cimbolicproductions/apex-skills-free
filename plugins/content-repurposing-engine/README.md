# Content Multiplier

Turn one piece of long-form content (blog post, YouTube video, podcast, transcript, newsletter) into a full week of distribution: LinkedIn post, X thread, newsletter draft, short-form video script, Instagram/Threads post, and email teaser. Use when the user says 'repurpose this', 'turn this into social', 'make this into a thread', 'I have a blog post and need posts for the week', or pastes a transcript/URL and asks for distribution.

## Workflows

- [content-repurposing-engine](skills/content-repurposing-engine/SKILL.md): Turn one piece of long-form content (blog post, YouTube video, podcast, transcript, newsletter) into a full week of distribution: LinkedIn post, X thread, newsletter draft, short-form video script, Instagram/Threads post, and email teaser. Use when the user says 'repurpose this', 'turn this into social', 'make this into a thread', 'I have a blog post and need posts for the week', or pastes a transcript/URL and asks for distribution.

## Install and use

Add the Apex Skills Free marketplace in Claude's Customize > Plugins, then select this plugin. In Claude Code, use:

```text
/plugin marketplace add https://github.com/cimbolicproductions/apex-skills-free.git
/plugin install apex-content-repurposing-engine@apex-skills-free
```

Ask for the workflow in plain language or select its skill. Read the linked instructions and reference files to understand the procedure and required inputs.

## Tools and data

These are instructions for your AI agent. When invoked, the agent uses the tools and permissions available in your environment. Depending on the workflow, those instructions can ask it to read or write files, run commands, browse websites, or contact services. Review the selected skill before supplying data or granting access, and keep credentials and private customer information out of prompts.

This package declares no MCP server, hook, install command, or telemetry endpoint. It provides no Apex-hosted data storage. Your AI provider and any tools you choose to connect handle the information used during the task; their policies and your account settings apply.

## License

See [LICENSE](LICENSE) for this plugin's MIT terms. The marketplace contains products with different licenses; this folder's license applies to this plugin.

[Apex Skills](https://apexskills.dev) | [Source repository](https://github.com/cimbolicproductions/apex-skills-free)
