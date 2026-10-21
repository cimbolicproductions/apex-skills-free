---
name: context-vault-architect
description: "Use when the user wants to create, restructure, or maintain a personal local context vault, second brain, AI memory folder, Obsidian vault, project knowledge base, or source-of-truth folder system. Creates folder trees, templates, naming rules, and bootstrap scripts."
license: MIT
metadata:
  author: dominic-context-vault-pack
  version: '1.0'
---

# Context Vault Architect

## Purpose

This skill turns scattered user context into a durable local context vault that future AI sessions can use. It should guide the user conversationally, reduce overwhelm, and produce organized markdown files, folder paths, templates, and next actions.

## When to Use This Skill

- The user wants a local computer folder structure for personal context, projects, goals, businesses, AI handoffs, or knowledge.
- The user says they need a vault, second brain, command center, personal OS, or AI source of truth.
- The user wants Claude to create templates and folders that make future AI sessions easier.

## When Not to Use This Skill

- The user only needs one note summarized.
- The user wants a full app or website rather than a local folder system.
- The user already has a mature vault and only needs one brain dump routed; use vault-ingestion-router.

## Intake Questions

Ask progressively. Do not interrogate the user with every question at once. Start broad, then branch based on what they mention.

- Where should the vault live on the local computer?
- Do you prefer Obsidian-style markdown, Notion import markdown, plain folders, or a hybrid?
- What are the main life/business areas the vault must support?
- Do you want a minimal structure or a power-user structure?

## Operating Workflow

- Explain that the vault should have one inbox, one command center, durable self-context, active projects, knowledge, AI context, decisions, SOPs, and archive.
- Create or recommend the folder tree from the bootstrap script in `scripts/bootstrap_context_vault.py`.
- Keep raw capture separate from processed notes to prevent chaos from polluting source-of-truth files.
- Create a `VAULT_INDEX.md` that lists where each kind of context belongs.
- Create templates before asking the user to fill every folder.
- Define naming rules: `YYYY-MM-DD-topic.md` for dated notes, `project-name.md` for active projects, and `decision-YYYY-MM-DD-title.md` for decisions.
- Create a maintenance rhythm: daily capture, weekly review, monthly archive.

## Local Vault Folder Targets

- `00_Inbox` for raw captures, brain dumps, screenshots, transcripts, and unprocessed notes.
- `01_Command_Center` for current priorities and review dashboards.
- `02_Self_Context` for user profile, preferences, communication style, routines, principles, strengths, and constraints.
- `03_Work_and_Business` for businesses, offers, customers, sales, operations, and finance context.
- `04_Projects` for active, backlog, paused, and completed projects.
- `05_Knowledge_Base` for people, companies, tools, concepts, and research notes.
- `06_AI_Context` for Claude Code, ChatGPT, Perplexity, prompts, and handoff briefs.
- `07_Decisions_and_Lessons` for decisions, lessons learned, and failure modes.
- `08_Systems_and_SOPs` for checklists, automations, and templates.
- `09_Archive` for inactive historical material.

## Output Contract

- A local folder tree plan.
- Bootstrap command for creating folders and templates.
- Starter index file.
- Maintenance rules and naming conventions.
- A first-pass migration plan for existing notes.

## Quality Checklist

- The structure is deep enough to scale but not so complex the user avoids it.
- Every folder has a clear purpose and a when-to-file-here rule.
- Raw capture and processed knowledge are separated.
- The user can start with one command, one inbox, and one weekly review.

## Recommended Source Principles

- PARA method by Tiago Forte for Projects, Areas, Resources, Archives style organization.
- Zettelkasten principles for atomic, linked permanent notes.
- Getting Things Done style inbox processing for capturing open loops before organizing them.
- Claude Code handoff patterns: maintain static project context separately from session handoff notes.
- Agent Skill best practice: make trigger descriptions concrete, include when-not-to-use boundaries, and keep reusable templates in files.

## Bundled Script

Use `scripts/bootstrap_context_vault.py` to create the folder tree and starter templates. Ask before running commands that modify the user's local filesystem.

