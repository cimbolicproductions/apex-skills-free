# Automated SEO Orchestrator

Runs a staged SEO pipeline on a website: site audit, keyword research from free sources, topic clusters with pillar pages, and an exact on-page plan for each URL, with an optional apply mode that edits the code and opens a pull request. Use when the user wants an SEO audit, keyword research, a content cluster plan or on-page SEO fixes. Start in plan-only mode.

## Workflows

- [seo-keyword-fix](skills/seo-keyword-fix/SKILL.md): Runs a staged SEO pipeline on a website: site audit, keyword research from free sources, topic clusters with pillar pages, and an exact on-page plan for each URL, with an optional apply mode that edits the code and opens a pull request. Use when the user wants an SEO audit, keyword research, a content cluster plan or on-page SEO fixes. Start in plan-only mode.

## Install and use

Add the Apex Skills Free marketplace in Claude's Customize > Plugins, then select this plugin. In Claude Code, use:

```text
/plugin marketplace add https://github.com/cimbolicproductions/apex-skills-free.git
/plugin install apex-seo-keyword-fix@apex-skills-free
```

Ask for the workflow in plain language or select its skill. Read the linked instructions and reference files to understand the procedure and required inputs.

## Tools and data

These are instructions for your AI agent. When invoked, the agent uses the tools and permissions available in your environment. Depending on the workflow, those instructions can ask it to read or write files, run commands, browse websites, or contact services. Review the selected skill before supplying data or granting access, and keep credentials and private customer information out of prompts.

This package declares no MCP server, hook, install command, or telemetry endpoint. It provides no Apex-hosted data storage. Your AI provider and any tools you choose to connect handle the information used during the task; their policies and your account settings apply.

## License

See [LICENSE](LICENSE) for this plugin's LicenseRef-Apex-Personal-Commercial-1.0 terms. The marketplace contains products with different licenses; this folder's license applies to this plugin.

[Apex Skills](https://apexskills.dev) | [Source repository](https://github.com/cimbolicproductions/apex-skills-free)
