# Tweet Builder

Craft the perfect tweet or thread for X/Twitter through Socratic questioning - the ideas come from the USER, not the AI. Use when the user wants to write a tweet, post on X, draft a thread, improve a tweet, or workshop a hook. The skill interviews the user one question at a time to draw out the angle, audience, and payoff, validates against documented character counts and 2026 algorithm best practices, and only then helps assemble and polish. Never auto-generate a finished tweet without first running the questioning loop.

## Workflows

- [perfect-tweet-socratic](skills/perfect-tweet-socratic/SKILL.md): Craft the perfect tweet or thread for X/Twitter through Socratic questioning - the ideas come from the USER, not the AI. Use when the user wants to write a tweet, post on X, draft a thread, improve a tweet, or workshop a hook. The skill interviews the user one question at a time to draw out the angle, audience, and payoff, validates against documented character counts and 2026 algorithm best practices, and only then helps assemble and polish. Never auto-generate a finished tweet without first running the questioning loop.

## Install and use

Add the Apex Skills Free marketplace in Claude's Customize > Plugins, then select this plugin. In Claude Code, use:

```text
/plugin marketplace add https://github.com/cimbolicproductions/apex-skills-free.git
/plugin install apex-tweet-builder@apex-skills-free
```

Ask for the workflow in plain language or select its skill. Read the linked instructions and reference files to understand the procedure and required inputs.

## Tools and data

These are instructions for your AI agent. When invoked, the agent uses the tools and permissions available in your environment. Depending on the workflow, those instructions can ask it to read or write files, run commands, browse websites, or contact services. Review the selected skill before supplying data or granting access, and keep credentials and private customer information out of prompts.

This package declares no MCP server, hook, install command, or telemetry endpoint. It provides no Apex-hosted data storage. Your AI provider and any tools you choose to connect handle the information used during the task; their policies and your account settings apply.

## License

See [LICENSE](LICENSE) for this plugin's MIT terms. The marketplace contains products with different licenses; this folder's license applies to this plugin.

[Apex Skills](https://apexskills.dev) | [Source repository](https://github.com/cimbolicproductions/apex-skills-free)
