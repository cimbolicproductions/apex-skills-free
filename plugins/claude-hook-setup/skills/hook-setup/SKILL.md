---
name: hook-setup
description: "Use when setting up Claude Code hooks for auto-formatting, blocking dangerous commands, running lint/tests on stop, desktop notifications, context reinjection, or deterministic guardrails."
license: MIT
metadata:
  author: dominic-operator-pack
  version: '1.0'
---

# Claude Code Hook Setup

## When to Use This Skill

- The user wants automation around Claude Code tool use.
- The project needs hard safety controls that cannot rely on Claude remembering rules.
- The user asks for formatter, linter, test, notification, or dangerous-command hooks.

## When Not to Use This Skill

- A simple CLAUDE.md instruction is sufficient and mistakes are low-impact.
- The user cannot run shell scripts or modify Claude Code settings.

## Intake Questions

Ask only for missing information that changes the output. If enough context exists, proceed and state assumptions.

- Which hook event is needed: PreToolUse, PostToolUse, Stop, Notification, SessionStart, or UserPromptSubmit?
- Which tools or commands must be allowed, blocked, or auto-run?
- What platform is this on: macOS, Linux, Windows, WSL, or CI?

## Operating Workflow

- Choose deterministic hooks for enforcement and CLAUDE.md for advisory preferences.
- Use PreToolUse Bash hooks to block destructive commands before they run.
- Use PostToolUse Edit/Write hooks to format changed files.
- Use Stop hooks to run lint/tests and block completion when failures are actionable.
- Use Notification hooks for human attention, not noisy status spam.
- Define exit code semantics clearly: 0 proceeds, 2 blocks and returns stderr as feedback.
- Test each hook with a harmless command before trusting it.

## Output Contract

Always produce practical artifacts the user can copy, paste, configure, or hand to a contractor.

- Hook event selection table.
- .claude/settings.json snippet.
- Script template with safety comments.
- Manual test plan and rollback steps.

## Quality Checklist

Before finalizing, verify:

- Hooks are idempotent and fast.
- Blocked commands include a helpful explanation.
- Secrets are read from environment variables, never hardcoded.

## Research-Backed Defaults and Sources

- Anthropic Claude Code best practices: https://code.claude.com/docs/en/best-practices
- Anthropic Claude Code hooks guide: https://code.claude.com/docs/en/hooks-guide
- Anthropic Claude Code MCP guide: https://code.claude.com/docs/en/mcp
- Model Context Protocol server docs: https://modelcontextprotocol.io/docs/develop/build-server
- MCP security best practices: https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices
- HumanLayer CLAUDE.md guidance: https://www.humanlayer.dev/blog/writing-a-good-claude-md

