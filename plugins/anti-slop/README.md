# Slop Killer

Scan any AI-generated text for tell-tale slop words, hedge phrases, em-dash overuse, sycophancy, rule-of-three structure, staccato fragment crutch, and generic AI cadence - then run a holistic vibe check and rewrite cleanly in the user's voice. Use when the user says 'remove the slop', 'make this sound human', 'this sounds like AI', 'kill the fluff', 'clean this up', 'detect AI slop', or pastes a draft and asks for a human pass. Outputs a flagged report + a clean rewrite.

## Workflows

- [anti-slop](skills/anti-slop/SKILL.md): Scan any AI-generated text for tell-tale slop words, hedge phrases, em-dash overuse, sycophancy, rule-of-three structure, staccato fragment crutch, and generic AI cadence - then run a holistic vibe check and rewrite cleanly in the user's voice. Use when the user says 'remove the slop', 'make this sound human', 'this sounds like AI', 'kill the fluff', 'clean this up', 'detect AI slop', or pastes a draft and asks for a human pass. Outputs a flagged report + a clean rewrite.

## Install and use

Add the Apex Skills Free marketplace in Claude's Customize > Plugins, then select this plugin. In Claude Code, use:

```text
/plugin marketplace add https://github.com/cimbolicproductions/apex-skills-free.git
/plugin install apex-anti-slop@apex-skills-free
```

Ask for the workflow in plain language or select its skill. Read the linked instructions and reference files to understand the procedure and required inputs.

## Tools and data

These are instructions for your AI agent. When invoked, the agent uses the tools and permissions available in your environment. Depending on the workflow, those instructions can ask it to read or write files, run commands, browse websites, or contact services. Review the selected skill before supplying data or granting access, and keep credentials and private customer information out of prompts.

This package declares no MCP server, hook, install command, or telemetry endpoint. It provides no Apex-hosted data storage. Your AI provider and any tools you choose to connect handle the information used during the task; their policies and your account settings apply.

## License

See [LICENSE](LICENSE) for this plugin's MIT terms. The marketplace contains products with different licenses; this folder's license applies to this plugin.

[Apex Skills](https://apexskills.dev) | [Source repository](https://github.com/cimbolicproductions/apex-skills-free)
