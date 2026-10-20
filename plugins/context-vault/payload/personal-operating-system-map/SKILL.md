---
name: personal-operating-system-map
description: "Use when mapping a user's personal operating system: roles, businesses, projects, tools, routines, responsibilities, goals, constraints, people, recurring workflows, and what AI should remember."
license: MIT
metadata:
  author: dominic-context-vault-pack
  version: '1.0'
---

# Personal Operating System Map

## Purpose

This skill turns scattered user context into a durable local context vault that future AI sessions can use. It should guide the user conversationally, reduce overwhelm, and produce organized markdown files, folder paths, templates, and next actions.

## When to Use This Skill

- The user wants AI to understand their life, work, businesses, tools, and recurring responsibilities.
- The user is onboarding a new AI assistant or building durable memory/context.
- The user has many ventures, roles, workflows, and platforms that need one organized map.

## When Not to Use This Skill

- The user only needs a project note.
- The user does not want personal context stored locally.

## Intake Questions

Ask progressively. Do not interrogate the user with every question at once. Start broad, then branch based on what they mention.

- What roles do you currently play?
- What businesses/projects are active?
- What tools/platforms do you rely on?
- What recurring workflows happen weekly or monthly?
- Who are the important people, customers, collaborators, or stakeholders?
- What preferences should AI always respect?

## Operating Workflow

- Map context by roles first, then projects, then workflows, then tools.
- Capture stable identity and preferences separately from current projects.
- Create a relationship map for people and organizations.
- Create a tool stack map with purpose, login location, integrations, and failure notes.
- Create recurring workflow notes for tasks the user repeats.
- Create an AI preferences note that assistants should load before personalized work.

## Local Vault Folder Targets

- `02_Self_Context/Profile` for stable user context.
- `02_Self_Context/Preferences` for AI and communication preferences.
- `03_Work_and_Business` for businesses, offers, customers, and operations.
- `05_Knowledge_Base/People` and `Companies` for relationship context.
- `05_Knowledge_Base/Tools` for tool stack notes.
- `08_Systems_and_SOPs` for recurring workflows.

## Output Contract

- Personal OS overview.
- Role map.
- Business/project map.
- Tool stack map.
- People/company map.
- Recurring workflow list.
- AI should know note.

## Quality Checklist

- Stable context is not mixed with temporary tasks.
- Every role or business has a current status.
- Tools are connected to actual workflows.
- The final map helps future AI personalize without asking the same questions repeatedly.

## Recommended Source Principles

- PARA method by Tiago Forte for Projects, Areas, Resources, Archives style organization.
- Zettelkasten principles for atomic, linked permanent notes.
- Getting Things Done style inbox processing for capturing open loops before organizing them.
- Claude Code handoff patterns: maintain static project context separately from session handoff notes.
- Agent Skill best practice: make trigger descriptions concrete, include when-not-to-use boundaries, and keep reusable templates in files.


