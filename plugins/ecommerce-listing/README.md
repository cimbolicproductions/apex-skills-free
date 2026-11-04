# E-commerce Listing Optimizer

Writes a marketplace listing from item details or a photo: an 80-character keyword title, five to seven item specifics and a mobile-friendly description. Use when the user is listing an item on eBay, Poshmark or Shopify or wants a listing improved.

## Workflows

- [ecommerce-listing](skills/ecommerce-listing/SKILL.md): Writes a marketplace listing from item details or a photo: an 80-character keyword title, five to seven item specifics and a mobile-friendly description. Use when the user is listing an item on eBay, Poshmark or Shopify or wants a listing improved.

## Install and use

Add the Apex Skills Free marketplace in Claude's Customize > Plugins, then select this plugin. In Claude Code, use:

```text
/plugin marketplace add https://github.com/cimbolicproductions/apex-skills-free.git
/plugin install apex-ecommerce-listing@apex-skills-free
```

Ask for the workflow in plain language or select its skill. Read the linked instructions and reference files to understand the procedure and required inputs.

## Tools and data

These are instructions for your AI agent. When invoked, the agent uses the tools and permissions available in your environment. Depending on the workflow, those instructions can ask it to read or write files, run commands, browse websites, or contact services. Review the selected skill before supplying data or granting access, and keep credentials and private customer information out of prompts.

This package declares no MCP server, hook, install command, or telemetry endpoint. It provides no Apex-hosted data storage. Your AI provider and any tools you choose to connect handle the information used during the task; their policies and your account settings apply.

## License

See [LICENSE](LICENSE) for this plugin's LicenseRef-Apex-Personal-Commercial-1.0 terms. The marketplace contains products with different licenses; this folder's license applies to this plugin.

[Apex Skills](https://apexskills.dev) | [Source repository](https://github.com/cimbolicproductions/apex-skills-free)
