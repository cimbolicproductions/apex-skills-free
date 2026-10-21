---
name: blocker-snag-triage
description: "Use when the user is stuck, blocked, confused, debugging, hitting snags, avoiding a task, losing momentum, or needs a blocker turned into a structured action plan and vault snag ticket."
license: MIT
metadata:
  author: dominic-context-vault-pack
  version: '1.0'
---

# Blocker and Snag Triage

## Purpose

This skill turns scattered user context into a durable local context vault that future AI sessions can use. It should guide the user conversationally, reduce overwhelm, and produce organized markdown files, folder paths, templates, and next actions.

## When to Use This Skill

- The user says stuck, blocked, snag, issue, problem, confusing, broken, not working, or I keep avoiding this.
- The user needs to separate symptoms from root cause.
- The user needs a small next step rather than a giant plan.

## When Not to Use This Skill

- The user needs emergency help, legal/medical advice, or crisis support.
- The user has a clear bug report and only wants code implementation.

## Intake Questions

Ask progressively. Do not interrogate the user with every question at once. Start broad, then branch based on what they mention.

- What are you trying to make happen?
- What is happening instead?
- Where exactly does it break or slow down?
- What have you already tried?
- What evidence do you have: errors, screenshots, messages, logs, links, or examples?
- What would be the smallest useful resolution?

## Operating Workflow

- Restate the expected vs actual state.
- Classify the snag: knowledge gap, tool issue, permissions/auth, unclear decision, emotional friction, dependency, time/energy, technical bug, or market uncertainty.
- Ask only the missing questions needed to choose the next move.
- Create a snag ticket with evidence, suspected causes, next tests, and escalation path.
- Convert big blockers into the next 15-minute action.
- If the snag is recurring, recommend an SOP, checklist, hook, automation, or decision rule.
- File the snag under the project note and optionally summarize it for AI handoff.

## Local Vault Folder Targets

- `04_Projects/Active/<project>` for project-specific blocker notes.
- `08_Systems_and_SOPs/Templates` for repeated snag templates.
- `07_Decisions_and_Lessons/Failure_Modes` for recurring personal or workflow failure patterns.
- `06_AI_Context/Handoffs` for AI debugging briefs.

## Output Contract

- Snag ticket.
- Root-cause hypothesis list.
- Next diagnostic steps.
- Escalation/ask template.
- Prevent-it-next-time note if recurring.

## Quality Checklist

- The blocker is framed as an observable gap, not a vague feeling.
- The next action can be done in 15 minutes or less when possible.
- Evidence is captured before assumptions.
- Recurring blockers produce a system improvement suggestion.

## Recommended Source Principles

- PARA method by Tiago Forte for Projects, Areas, Resources, Archives style organization.
- Zettelkasten principles for atomic, linked permanent notes.
- Getting Things Done style inbox processing for capturing open loops before organizing them.
- Claude Code handoff patterns: maintain static project context separately from session handoff notes.
- Agent Skill best practice: make trigger descriptions concrete, include when-not-to-use boundaries, and keep reusable templates in files.


