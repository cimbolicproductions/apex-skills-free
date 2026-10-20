---
name: guided-brain-dump-capture
description: "Use when the user wants to brain dump, unload thoughts, organize messy context, capture what they are working on, explain what they need help with, or turn scattered ideas into structured vault notes and next actions."
license: MIT
metadata:
  author: dominic-context-vault-pack
  version: '1.0'
---

# Guided Brain Dump Capture

## Purpose

This skill turns scattered user context into a durable local context vault that future AI sessions can use. It should guide the user conversationally, reduce overwhelm, and produce organized markdown files, folder paths, templates, and next actions.

## When to Use This Skill

- The user says brain dump, unload, organize my thoughts, help me think, capture this, or I have a lot going on.
- The user wants Claude to ask guiding questions instead of giving immediate advice.
- The user has many projects, snags, ideas, and open loops mixed together.

## When Not to Use This Skill

- The user asks a direct factual question.
- The user already provided a clean project brief and only needs implementation.
- The user is in crisis or needs mental health support; be supportive and recommend appropriate human help.

## Intake Questions

Ask progressively. Do not interrogate the user with every question at once. Start broad, then branch based on what they mention.

- What are you working on right now?
- What do you need help with most?
- What feels stuck, unclear, annoying, or heavy?
- What changed recently that AI should know?
- What decisions are you avoiding or circling?
- What would make the next 24 hours feel like a win?

## Operating Workflow

- Start by inviting an unfiltered dump. Tell the user grammar and order do not matter.
- Reflect back themes before organizing. Do not over-structure too early.
- Extract projects, tasks, decisions, blockers, people, dates, tools, and emotional/friction signals.
- Ask 3 to 5 targeted follow-up questions based on gaps.
- Route each item to vault destinations: inbox, project note, decision log, snag ticket, SOP, or AI handoff.
- Produce a cleaned brain dump note plus a prioritized next-action list.
- Ask whether to save as raw dump, processed project updates, or both.

## Local Vault Folder Targets

- `00_Inbox/Brain_Dumps` for raw captured dumps.
- `04_Projects/Active` for active project updates.
- `07_Decisions_and_Lessons/Decision_Log` for decisions surfaced.
- `08_Systems_and_SOPs/Templates` for repeated workflows.
- `06_AI_Context/Handoffs` for context briefs generated from the dump.

## Output Contract

- Raw brain dump note.
- Cleaned summary grouped by theme.
- Projects mentioned and where to file them.
- Blockers/snags list.
- Decisions needed.
- Next 3 to 7 actions.
- Suggested vault file paths.

## Quality Checklist

- The user feels less scattered after the output.
- No important open loop disappears.
- Next actions are concrete and small.
- The original raw context is preserved before summarization.

## Recommended Source Principles

- PARA method by Tiago Forte for Projects, Areas, Resources, Archives style organization.
- Zettelkasten principles for atomic, linked permanent notes.
- Getting Things Done style inbox processing for capturing open loops before organizing them.
- Claude Code handoff patterns: maintain static project context separately from session handoff notes.
- Agent Skill best practice: make trigger descriptions concrete, include when-not-to-use boundaries, and keep reusable templates in files.


