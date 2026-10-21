---
name: weekly-context-review
description: "Use when running a weekly review of a personal context vault, cleaning inbox notes, updating projects, surfacing decisions, archiving stale context, choosing priorities, and preparing next-week AI-ready plans."
license: MIT
metadata:
  author: dominic-context-vault-pack
  version: '1.0'
---

# Weekly Context Review

## Purpose

This skill turns scattered user context into a durable local context vault that future AI sessions can use. It should guide the user conversationally, reduce overwhelm, and produce organized markdown files, folder paths, templates, and next actions.

## When to Use This Skill

- The user wants a weekly reset, review, cleanup, planning session, or vault maintenance.
- The vault has inbox clutter, stale projects, unprocessed brain dumps, or too many open loops.
- The user wants to choose priorities for the next week.

## When Not to Use This Skill

- The user needs urgent triage for one blocker.
- The vault has not been created yet; use context-vault-architect.

## Intake Questions

Ask progressively. Do not interrogate the user with every question at once. Start broad, then branch based on what they mention.

- What went well this week?
- What moved forward?
- What stayed stuck?
- What new context needs to be filed?
- Which projects are active, paused, completed, or no longer relevant?
- What are the top 1 to 3 priorities for next week?

## Operating Workflow

- Process `00_Inbox` first: delete, archive, convert to project note, decision, snag, SOP, or knowledge note.
- Review active projects and update status, last touched date, next action, and blockers.
- Promote important decisions to the decision log.
- Archive stale notes that are not actionable or reference-worthy.
- Identify recurring failure modes or patterns from the week.
- Create next-week focus list with no more than 3 primary priorities.
- Generate an AI briefing for the next week if the user uses assistants daily.

## Local Vault Folder Targets

- `00_Inbox/To_Process` for cleanup.
- `01_Command_Center/Weekly` for review notes.
- `04_Projects/Active` for status updates.
- `07_Decisions_and_Lessons` for decisions and lessons.
- `09_Archive` for stale or completed material.

## Output Contract

- Weekly review note.
- Inbox processing decisions.
- Updated project status list.
- Decisions/lessons captured.
- Next-week priority plan.
- AI weekly brief.

## Quality Checklist

- The inbox is reduced or every remaining item has a reason.
- No more than 3 priorities are selected.
- Every active project has a next action or is paused.
- Lessons and decisions are separated from temporary notes.

## Recommended Source Principles

- PARA method by Tiago Forte for Projects, Areas, Resources, Archives style organization.
- Zettelkasten principles for atomic, linked permanent notes.
- Getting Things Done style inbox processing for capturing open loops before organizing them.
- Claude Code handoff patterns: maintain static project context separately from session handoff notes.
- Agent Skill best practice: make trigger descriptions concrete, include when-not-to-use boundaries, and keep reusable templates in files.


