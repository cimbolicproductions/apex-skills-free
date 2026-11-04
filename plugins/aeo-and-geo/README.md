# AEO and GEO

Aeo and Geo (formerly seo-answer-engine). Audit and improve website answers for extractability by ChatGPT, Gemini, Perplexity, Copilot and AI Overviews. Use for 'get cited by ChatGPT', 'AI search', 'answer engine optimization', 'AEO', 'GEO', 'LLM SEO', 'why does ChatGPT recommend my competitor', 'show up in AI results', 'get a local business recommended by ChatGPT or Copilot', 'Bing Places for ChatGPT', or when a page ranks but earns no clicks and no mentions. Audits a page for extractability, finds what incumbents hide, rewrites so a model can lift the answer whole, and for local businesses enforces the local entity layer in order: Optimized GBP Gate (local-gbp-optimizer), then that GBP imported into Bing Places (seo-bing-places), then Bing Webmaster Tools. Includes companion listing and research workflows for local businesses. Includes a complete workflow for the task.

## Workflows

- [aeo-and-geo](skills/aeo-and-geo/SKILL.md): Aeo and Geo (formerly seo-answer-engine). Audit and improve website answers for extractability by ChatGPT, Gemini, Perplexity, Copilot and AI Overviews. Use for 'get cited by ChatGPT', 'AI search', 'answer engine optimization', 'AEO', 'GEO', 'LLM SEO', 'why does ChatGPT recommend my competitor', 'show up in AI results', 'get a local business recommended by ChatGPT or Copilot', 'Bing Places for ChatGPT', or when a page ranks but earns no clicks and no mentions. Audits a page for extractability, finds what incumbents hide, rewrites so a model can lift the answer whole, and for local businesses enforces the local entity layer in order: Optimized GBP Gate (local-gbp-optimizer), then that GBP imported into Bing Places (seo-bing-places), then Bing Webmaster Tools. Includes companion listing and research workflows for local businesses. Includes a complete workflow for the task.

## Install and use

Add the Apex Skills Free marketplace in Claude's Customize > Plugins, then select this plugin. In Claude Code, use:

```text
/plugin marketplace add https://github.com/cimbolicproductions/apex-skills-free.git
/plugin install apex-aeo-and-geo@apex-skills-free
```

Ask for the workflow in plain language or select its skill. Read the linked instructions and reference files to understand the procedure and required inputs.

## Tools and data

These are instructions for your AI agent. When invoked, the agent uses the tools and permissions available in your environment. Depending on the workflow, those instructions can ask it to read or write files, run commands, browse websites, or contact services. Review the selected skill before supplying data or granting access, and keep credentials and private customer information out of prompts.

This package declares no MCP server, hook, install command, or telemetry endpoint. It provides no Apex-hosted data storage. Your AI provider and any tools you choose to connect handle the information used during the task; their policies and your account settings apply.

Included scripts (inspect before running):

- [skills/aeo-and-geo/scripts/audit.py](skills/aeo-and-geo/scripts/audit.py)

## License

See [LICENSE](LICENSE) for this plugin's MIT terms. The marketplace contains products with different licenses; this folder's license applies to this plugin.

[Apex Skills](https://apexskills.dev) | [Source repository](https://github.com/cimbolicproductions/apex-skills-free)
