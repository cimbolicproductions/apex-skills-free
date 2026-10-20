---
name: ai-handoff-brief-builder
description: "Use when creating AI-ready context briefs for Claude, Claude Code, ChatGPT, Perplexity, subagents, coding agents, contractors, or future sessions from a user's vault notes and project context."
license: MIT
metadata:
  author: dominic-context-vault-pack
  version: '1.0'
---

# AI Handoff Brief Builder

## Purpose

This skill turns scattered user context into a durable local context vault that future AI sessions can use. It should guide the user conversationally, reduce overwhelm, and produce organized markdown files, folder paths, templates, and next actions.

## When to Use This Skill

- The user says make a prompt, brief Claude, create context, hand this off, summarize for Claude Code, or prepare for another AI.
- A project needs enough background for a fresh AI session to work without rereading everything.
- The user wants repeatable assistant context for a task, project, or workflow.

## When Not to Use This Skill

- The user only wants a human-facing summary.
- The source context is not yet organized and needs brain-dump capture first.

## Intake Questions

Ask progressively. Do not interrogate the user with every question at once. Start broad, then branch based on what they mention.

- Which AI/tool will receive this: Claude Code, Claude Desktop, ChatGPT, Perplexity, Cursor, or a subagent?
- What should the AI do next?
- What context must it know, and what should it ignore?
- What files, links, commands, constraints, and failure modes matter?

## Operating Workflow

- Gather only task-relevant context. Do not dump the whole vault.
- Write the brief with objective, background, current state, constraints, relevant files, what was tried, known failure modes, and requested next step.
- Put critical constraints near the top.
- Include explicit non-goals and do-not-do rules.
- If for Claude Code, include repo path, commands, tests, environment, branch, and handoff from last session.
- If for research/writing AI, include source links, tone, audience, and expected deliverable format.
- Save the brief under `06_AI_Context/Handoffs` with date and project name.

## Local Vault Folder Targets

- `06_AI_Context/Handoffs` for paste-ready briefs.
- `06_AI_Context/Claude_Code` for coding-specific context.
- `06_AI_Context/Reusable_Prompts` for repeated prompt patterns.
- `04_Projects/Active` for source project context.

## Output Contract

- Paste-ready AI handoff prompt.
- Short context version under 300 words.
- Expanded context version when needed.
- Relevant file/link list.
- Checklist of what the receiving AI should verify first.

## Quality Checklist

- The brief tells the next AI exactly what to do first.
- It contains enough context but avoids unrelated vault material.
- Constraints, preferences, and failure modes are explicit.
- The output can be pasted into a new session without explanation.

## Recommended Source Principles

- PARA method by Tiago Forte for Projects, Areas, Resources, Archives style organization.
- Zettelkasten principles for atomic, linked permanent notes.
- Getting Things Done style inbox processing for capturing open loops before organizing them.
- Claude Code handoff patterns: maintain static project context separately from session handoff notes.
- Agent Skill best practice: make trigger descriptions concrete, include when-not-to-use boundaries, and keep reusable templates in files.


