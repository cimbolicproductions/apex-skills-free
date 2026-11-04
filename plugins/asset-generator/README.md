# App Asset Prompt Architect

Turns a request for an app or web visual, such as an app icon, splash screen, hero image or social share image, into structured image-model prompts with style, composition and constraint tags plus the right aspect ratio. Use when the user needs prompts for Midjourney, DALL-E, Gemini or another image generator.

## Workflows

- [asset-generator](skills/asset-generator/SKILL.md): Turns a request for an app or web visual, such as an app icon, splash screen, hero image or social share image, into structured image-model prompts with style, composition and constraint tags plus the right aspect ratio. Use when the user needs prompts for Midjourney, DALL-E, Gemini or another image generator.

## Install and use

Add the Apex Skills Free marketplace in Claude's Customize > Plugins, then select this plugin. In Claude Code, use:

```text
/plugin marketplace add https://github.com/cimbolicproductions/apex-skills-free.git
/plugin install apex-asset-generator@apex-skills-free
```

Ask for the workflow in plain language or select its skill. Read the linked instructions and reference files to understand the procedure and required inputs.

## Tools and data

These are instructions for your AI agent. When invoked, the agent uses the tools and permissions available in your environment. Depending on the workflow, those instructions can ask it to read or write files, run commands, browse websites, or contact services. Review the selected skill before supplying data or granting access, and keep credentials and private customer information out of prompts.

This package declares no MCP server, hook, install command, or telemetry endpoint. It provides no Apex-hosted data storage. Your AI provider and any tools you choose to connect handle the information used during the task; their policies and your account settings apply.

## License

See [LICENSE](LICENSE) for this plugin's LicenseRef-Apex-Personal-Commercial-1.0 terms. The marketplace contains products with different licenses; this folder's license applies to this plugin.

[Apex Skills](https://apexskills.dev) | [Source repository](https://github.com/cimbolicproductions/apex-skills-free)
