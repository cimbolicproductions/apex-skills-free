# Brand Voice Engine

Generate a complete brand voice and content engine for your business in one Claude session. Use when the buyer says 'build my brand voice', 'I need a content engine', 'set up my newsletter and blog voice', 'configure brand for my company', '/brand-voice-engine', or any request for brand identity + content workflow setup. Walks the buyer through a 15-question brand interview, researches their niche with whatever research tools the agent has, applies proven copywriting and writing methods (Halbert, Sugarman, Ogilvy, Parr, Handley, King, Graham, Ravikant and Kennedy) to their brand parameters, then generates a personalized brand voice document plus three companion content skills (newsletter, blog and tweet pipelines).

## Workflows

- [brand-voice-engine](skills/brand-voice-engine/SKILL.md): Generate a complete brand voice and content engine for your business in one Claude session. Use when the buyer says 'build my brand voice', 'I need a content engine', 'set up my newsletter and blog voice', 'configure brand for my company', '/brand-voice-engine', or any request for brand identity + content workflow setup. Walks the buyer through a 15-question brand interview, researches their niche with whatever research tools the agent has, applies proven copywriting and writing methods (Halbert, Sugarman, Ogilvy, Parr, Handley, King, Graham, Ravikant and Kennedy) to their brand parameters, then generates a personalized brand voice document plus three companion content skills (newsletter, blog and tweet pipelines).

## Install and use

Add the Apex Skills Free marketplace in Claude's Customize > Plugins, then select this plugin. In Claude Code, use:

```text
/plugin marketplace add https://github.com/cimbolicproductions/apex-skills-free.git
/plugin install apex-brand-voice-engine@apex-skills-free
```

Ask for the workflow in plain language or select its skill. Read the linked instructions and reference files to understand the procedure and required inputs.

## Tools and data

These are instructions for your AI agent. When invoked, the agent uses the tools and permissions available in your environment. Depending on the workflow, those instructions can ask it to read or write files, run commands, browse websites, or contact services. Review the selected skill before supplying data or granting access, and keep credentials and private customer information out of prompts.

This package declares no MCP server, hook, install command, or telemetry endpoint. It provides no Apex-hosted data storage. Your AI provider and any tools you choose to connect handle the information used during the task; their policies and your account settings apply.

## License

See [LICENSE](LICENSE) for this plugin's MIT terms. The marketplace contains products with different licenses; this folder's license applies to this plugin.

[Apex Skills](https://apexskills.dev) | [Source repository](https://github.com/cimbolicproductions/apex-skills-free)
