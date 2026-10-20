---
name: project-context-captain
description: "Use when creating or updating project context pages, defining what a user is working on, capturing goals, current status, decisions, constraints, files, blockers, next actions, and AI-ready project briefs."
license: MIT
metadata:
  author: dominic-context-vault-pack
  version: '1.0'
---

# Project Context Captain

## Purpose

This skill turns scattered user context into a durable local context vault that future AI sessions can use. It should guide the user conversationally, reduce overwhelm, and produce organized markdown files, folder paths, templates, and next actions.

## When to Use This Skill

- The user mentions a specific project, business, app, client, automation, build, or campaign.
- The user wants Claude to understand a project deeply before helping.
- The project has scattered notes, code, links, tasks, and decisions.

## When Not to Use This Skill

- The user is only doing a general life brain dump with no project focus.
- The project is complete and only needs archival; use weekly-context-review or context-vault-architect.

## Intake Questions

Ask progressively. Do not interrogate the user with every question at once. Start broad, then branch based on what they mention.

- What is this project called?
- What is the one-sentence outcome?
- Why does it matter now?
- What stage is it in: idea, validation, build, launch, operations, paused, or cleanup?
- What are the known constraints, deadlines, tools, files, and stakeholders?
- What is the next visible milestone?

## Operating Workflow

- Create a canonical project note under the correct project status folder.
- Capture the goal, why, status, scope, non-goals, constraints, stakeholders, links, and tools.
- Separate decisions made from open questions.
- Capture snags as separate snag tickets when they require investigation.
- Define the next milestone and next 3 actions.
- Create an AI handoff summary if the project will be used in Claude Code or another assistant.
- Update the project note after major work sessions rather than creating endless duplicate notes.

## Local Vault Folder Targets

- `04_Projects/Active` for active project pages.
- `04_Projects/Backlog` for ideas not yet committed.
- `04_Projects/Paused` for parked work with restart conditions.
- `04_Projects/Completed` for finished projects with outcomes.
- `06_AI_Context/Handoffs` for project-specific AI briefs.

## Output Contract

- Project note markdown.
- Status snapshot.
- Decision log entries.
- Open questions.
- Blocker list.
- Next action list.
- AI handoff brief if needed.

## Quality Checklist

- A stranger or future AI can understand the project in under 2 minutes.
- The current status is clearly different from desired outcome.
- Next actions are not vague research placeholders unless research is truly next.
- Links/files/tools are captured with enough context to be useful later.

## Recommended Source Principles

- PARA method by Tiago Forte for Projects, Areas, Resources, Archives style organization.
- Zettelkasten principles for atomic, linked permanent notes.
- Getting Things Done style inbox processing for capturing open loops before organizing them.
- Claude Code handoff patterns: maintain static project context separately from session handoff notes.
- Agent Skill best practice: make trigger descriptions concrete, include when-not-to-use boundaries, and keep reusable templates in files.


