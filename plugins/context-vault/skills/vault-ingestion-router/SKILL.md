---
name: vault-ingestion-router
description: "Use when deciding where to file new context in a local vault: notes, transcripts, screenshots, links, meeting notes, ideas, decisions, customer feedback, code context, research, or random captures."
license: MIT
metadata:
  author: dominic-context-vault-pack
  version: '1.0'
---

# Vault Ingestion Router

## Purpose

This skill turns scattered user context into a durable local context vault that future AI sessions can use. It should guide the user conversationally, reduce overwhelm, and produce organized markdown files, folder paths, templates, and next actions.

## When to Use This Skill

- The user has a new note, link, transcript, screenshot, file, idea, or piece of context and asks where it goes.
- The inbox is messy and needs routing.
- The user wants to convert raw material into one or more structured vault notes.

## When Not to Use This Skill

- The vault structure does not exist yet; use context-vault-architect.
- The user wants a full weekly review of everything.

## Intake Questions

Ask progressively. Do not interrogate the user with every question at once. Start broad, then branch based on what they mention.

- What is this item?
- Why might it matter later?
- Is it tied to a project, person, decision, workflow, or general knowledge?
- Does it require action, reference, review, archive, or deletion?

## Operating Workflow

- Classify the item as action, project update, decision, lesson, reference, person/company, tool, SOP, AI context, or archive.
- If it requires action, extract the next action and link it to a project.
- If it is evidence for a decision, file it with a decision note.
- If it is reusable knowledge, convert it into an atomic knowledge note.
- If it is raw and unclear, keep it in inbox with a review date.
- Suggest the exact folder path and filename.
- If one capture contains multiple concepts, split it into separate notes and link them.

## Local Vault Folder Targets

- `00_Inbox/To_Process` for unclear raw material.
- `04_Projects` for project-specific context.
- `05_Knowledge_Base` for reusable reference notes.
- `07_Decisions_and_Lessons` for decisions and lessons.
- `08_Systems_and_SOPs` for repeatable workflows.
- `09_Archive` for inactive material.

## Output Contract

- Routing decision.
- Suggested file path and filename.
- Processed note draft.
- Extracted actions/decisions/links.
- Backlinks or related-note suggestions.

## Quality Checklist

- Every item has a reason to keep, act, archive, or delete.
- File paths are specific.
- Actions are separated from reference.
- Duplicate context is linked, not copied everywhere.

## Recommended Source Principles

- PARA method by Tiago Forte for Projects, Areas, Resources, Archives style organization.
- Zettelkasten principles for atomic, linked permanent notes.
- Getting Things Done style inbox processing for capturing open loops before organizing them.
- Claude Code handoff patterns: maintain static project context separately from session handoff notes.
- Agent Skill best practice: make trigger descriptions concrete, include when-not-to-use boundaries, and keep reusable templates in files.


