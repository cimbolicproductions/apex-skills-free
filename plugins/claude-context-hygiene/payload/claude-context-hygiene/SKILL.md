---
name: claude-context-hygiene
description: "Use when Claude Code is losing track, repeating itself, contradicting prior decisions, context is high, a task is getting long, or the user asks to compact, clear, resume, or manage context. Do not use for ordinary one-shot coding edits."
license: MIT
metadata:
  author: dominic-operator-pack
  version: '1.0'
---

# Claude Code Context Hygiene

## When to Use This Skill

- Claude appears to enter the agent dumb zone: repeating questions, ignoring constraints, or making careless mistakes.
- A coding session has grown beyond one coherent subtask.
- The user asks how to use /compact, /clear, /resume, or reduce token waste.
- Noisy test logs, build output, or MCP tool schemas are crowding the session.

## When Not to Use This Skill

- The user only needs a single answer with no ongoing session state.
- A fresh session is already scoped to a tiny edit and has no context pressure.

## Intake Questions

Ask only for missing information that changes the output. If enough context exists, proceed and state assumptions.

- What is the current goal and what must not be forgotten?
- What changed since the last commit or checkpoint?
- Which MCP servers, logs, files, or instructions are currently relevant?

## Operating Workflow

- Identify the active objective in one sentence and list the 3 to 7 facts that must survive compaction.
- Recommend manual compaction around 50 percent context for ongoing work, not only at emergency auto-compact thresholds.
- Move stable project rules into CLAUDE.md and volatile session state into HANDOVER.md or TASKS.md.
- Disable unrelated MCP servers before continuing. Keep only tools needed for the current repo and task.
- Route noisy exploration, logs, and broad grep tasks to subagents or saved files, then return only summaries to the main session.
- After each completed subtask, commit or checkpoint, update handoff notes, then clear before starting unrelated work.

## Output Contract

Always produce practical artifacts the user can copy, paste, configure, or hand to a contractor.

- Context diagnosis: what is bloating or confusing the session.
- A compact prompt containing the goal, decisions, files, constraints, and next action.
- A cleanup sequence: checkpoint, compact, disable MCPs, delegate noise, clear, or resume.

## Quality Checklist

Before finalizing, verify:

- The compact prompt is paste-ready and under 300 words unless the task is complex.
- Critical constraints are near the top, not buried.
- No generic advice is given without a concrete next command or prompt.

## Research-Backed Defaults and Sources

- Anthropic Claude Code best practices: https://code.claude.com/docs/en/best-practices
- Anthropic Claude Code hooks guide: https://code.claude.com/docs/en/hooks-guide
- Anthropic Claude Code MCP guide: https://code.claude.com/docs/en/mcp
- Model Context Protocol server docs: https://modelcontextprotocol.io/docs/develop/build-server
- MCP security best practices: https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices
- HumanLayer CLAUDE.md guidance: https://www.humanlayer.dev/blog/writing-a-good-claude-md

