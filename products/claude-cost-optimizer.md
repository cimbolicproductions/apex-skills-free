---
name: claude-cost-optimizer
description: "Use when Claude Code token usage, model spend, MCP overhead, subagent cost, or long-running agent loops seem high. Produces a cost and context reduction plan."
license: MIT
metadata:
  author: dominic-operator-pack
  version: '1.0'
---

# Claude Code Cost Optimizer

## When to Use This Skill

- The user asks how to reduce Claude Code cost or token usage.
- A session is using Opus for routine work or spawning broad subagents.
- MCP context, logs, or giant CLAUDE.md files are bloating every turn.

## When Not to Use This Skill

- The user explicitly prioritizes maximum quality and cost is irrelevant.
- There is no recurring workflow to optimize.

## Intake Questions

Ask only for missing information that changes the output. If enough context exists, proceed and state assumptions.

- Which tasks are expensive: planning, coding, tests, research, reviews, or MCP calls?
- Which models and MCP servers are currently enabled?
- Which outputs are noisy but only need summarized results?

## Operating Workflow

- Reduce always-loaded context first: CLAUDE.md, MCP servers, broad instructions, and huge pasted logs.
- Use stronger models for architecture and risky decisions, cheaper/default models for scoped edits and summaries.
- Give subagents file-scoped briefs and explicit stop conditions.
- Prefer CLI commands and saved artifacts for bulky data over dumping output into chat.
- Compact and clear between unrelated tasks.
- Track recurring expensive workflows and turn them into skills, scripts, or commands.

## Output Contract

Always produce practical artifacts the user can copy, paste, configure, or hand to a contractor.

- Cost drivers ranked by impact.
- Specific reductions: disable MCPs, split sessions, change model, reduce context, add scripts.
- A revised workflow with cheaper defaults and quality gates.

## Quality Checklist

Before finalizing, verify:

- Do not give numeric cost predictions unless the user provides pricing inputs.
- Never sacrifice safety checks for cost on payments, auth, data deletion, or production releases.
- The final workflow is simpler than the current one.

## Research-Backed Defaults and Sources

- Anthropic Claude Code best practices: https://code.claude.com/docs/en/best-practices
- Anthropic Claude Code hooks guide: https://code.claude.com/docs/en/hooks-guide
- Anthropic Claude Code MCP guide: https://code.claude.com/docs/en/mcp
- Model Context Protocol server docs: https://modelcontextprotocol.io/docs/develop/build-server
- MCP security best practices: https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices
- HumanLayer CLAUDE.md guidance: https://www.humanlayer.dev/blog/writing-a-good-claude-md

