---
name: claude-session-handoff
description: "Use when ending a Claude Code session, resuming a project later, summarizing what was done, creating HANDOVER.md, or preserving decisions between sessions. Do not use for general project documentation."
license: MIT
metadata:
  author: dominic-operator-pack
  version: '1.0'
---

# Claude Code Session Handoff

## When to Use This Skill

- The user says they are done for today, wants to pick it up later, or needs a resume prompt.
- Claude Code finished a meaningful subtask and should record state before context is cleared.
- A project needs durable continuity across multiple AI sessions.

## When Not to Use This Skill

- The user needs a public README or formal documentation.
- No work has happened yet and there is nothing to preserve.

## Intake Questions

Ask only for missing information that changes the output. If enough context exists, proceed and state assumptions.

- What was the original task or ticket?
- What files changed, commands ran, and tests passed or failed?
- What decisions were made and what remains blocked?

## Operating Workflow

- Separate permanent facts from temporary session state.
- Update CLAUDE.md only for durable repo rules, architecture, commands, or gotchas.
- Update HANDOVER.md with a dated entry for completed work, changed files, test status, decisions, blockers, and next step.
- Create a one-paragraph paste-ready prompt for the next session.
- If there are unresolved risks, label them as blockers, watch items, or nice-to-haves.

## Output Contract

Always produce practical artifacts the user can copy, paste, configure, or hand to a contractor.

- HANDOVER.md entry in markdown.
- Resume prompt that starts with the exact next action.
- Short list of commands/tests the next Claude session should run first.

## Quality Checklist

Before finalizing, verify:

- The handoff can be understood without reading the entire chat.
- The next action is explicit and testable.
- Unverified claims are labeled as unverified.

## Research-Backed Defaults and Sources

- Anthropic Claude Code best practices: https://code.claude.com/docs/en/best-practices
- Anthropic Claude Code hooks guide: https://code.claude.com/docs/en/hooks-guide
- Anthropic Claude Code MCP guide: https://code.claude.com/docs/en/mcp
- Model Context Protocol server docs: https://modelcontextprotocol.io/docs/develop/build-server
- MCP security best practices: https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices
- HumanLayer CLAUDE.md guidance: https://www.humanlayer.dev/blog/writing-a-good-claude-md

