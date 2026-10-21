#!/usr/bin/env python3
"""
Bootstrap a Personal Context Vault folder structure.

Usage:
  python bootstrap_context_vault.py ~/ContextVault

If no path is provided, creates ./ContextVault in the current directory.
"""
from pathlib import Path
import sys
from datetime import date

root = Path(sys.argv[1]).expanduser() if len(sys.argv) > 1 else Path.cwd() / "ContextVault"

folders = [
    "00_Inbox/Brain_Dumps",
    "00_Inbox/Raw_Captures",
    "00_Inbox/To_Process",
    "01_Command_Center",
    "01_Command_Center/Daily",
    "01_Command_Center/Weekly",
    "01_Command_Center/Monthly",
    "02_Self_Context",
    "02_Self_Context/Profile",
    "02_Self_Context/Preferences",
    "02_Self_Context/Strengths_and_Weaknesses",
    "02_Self_Context/Health_Energy_Routines",
    "02_Self_Context/Decision_Principles",
    "03_Work_and_Business",
    "03_Work_and_Business/Businesses",
    "03_Work_and_Business/Offers",
    "03_Work_and_Business/Customers",
    "03_Work_and_Business/Sales_and_Marketing",
    "03_Work_and_Business/Operations",
    "03_Work_and_Business/Finance",
    "04_Projects",
    "04_Projects/Active",
    "04_Projects/Backlog",
    "04_Projects/Paused",
    "04_Projects/Completed",
    "05_Knowledge_Base",
    "05_Knowledge_Base/People",
    "05_Knowledge_Base/Companies",
    "05_Knowledge_Base/Tools",
    "05_Knowledge_Base/Concepts",
    "05_Knowledge_Base/Research_Notes",
    "06_AI_Context",
    "06_AI_Context/Claude_Code",
    "06_AI_Context/ChatGPT",
    "06_AI_Context/Perplexity",
    "06_AI_Context/Reusable_Prompts",
    "06_AI_Context/Handoffs",
    "07_Decisions_and_Lessons",
    "07_Decisions_and_Lessons/Decision_Log",
    "07_Decisions_and_Lessons/Lessons_Learned",
    "07_Decisions_and_Lessons/Failure_Modes",
    "08_Systems_and_SOPs",
    "08_Systems_and_SOPs/Checklists",
    "08_Systems_and_SOPs/Automations",
    "08_Systems_and_SOPs/Templates",
    "09_Archive",
]

templates = {
    "01_Command_Center/README.md": """# Command Center

Use this folder for current priorities, reviews, dashboards, and quick navigation.

## Current Focus
- 

## This Week
- 

## Open Loops
- 
""",
    "02_Self_Context/Profile/user-profile.md": """# User Profile

## Identity
- Name:
- Location/timezone:
- Roles:

## Current Season of Life

## What AI Should Know About Me

## Communication Preferences

## Avoid / Do Not Assume
""",
    "04_Projects/project-template.md": """# Project: {{name}}

## One-Sentence Goal

## Why This Matters

## Current Status
- Stage:
- Last updated:
- Owner:

## Desired Outcome

## Constraints

## Key Context

## Decisions Made

## Open Questions

## Snags / Blockers

## Next Actions
- [ ] 

## Useful Links / Files
""",
    "00_Inbox/Brain_Dumps/brain-dump-template.md": """# Brain Dump - {{date}}

## Raw Dump

## Themes

## Projects Mentioned

## Decisions Needed

## Snags / Blockers

## Next Actions
- [ ] 

## Where This Should Be Filed
""",
    "06_AI_Context/Handoffs/ai-handoff-template.md": """# AI Handoff - {{date}}

## Objective

## Background Context

## Current State

## Relevant Files / Links

## Constraints and Preferences

## What Has Already Been Tried

## Known Failure Modes

## Requested Next Step
""",
    "07_Decisions_and_Lessons/Decision_Log/decision-template.md": """# Decision - {{date}} - {{title}}

## Decision

## Context

## Options Considered

## Why This Choice

## Risks

## Review Date

## Outcome / Follow-Up
""",
    "08_Systems_and_SOPs/Templates/snagticket-template.md": """# Snag Ticket - {{title}}

## Problem

## Where It Happens

## Expected Behavior

## Actual Behavior

## What I Tried

## Evidence

## Suspected Cause

## Next Best Actions
- [ ] 

## Escalation / Ask
""",
}

root.mkdir(parents=True, exist_ok=True)
for folder in folders:
    (root / folder).mkdir(parents=True, exist_ok=True)

for rel, content in templates.items():
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(content.replace("{{date}}", str(date.today())), encoding="utf-8")

index = root / "VAULT_INDEX.md"
if not index.exists():
    index.write_text(f"""# Personal Context Vault Index

Created: {date.today()}

## Start Here
- `01_Command_Center/README.md`
- `02_Self_Context/Profile/user-profile.md`
- `04_Projects/project-template.md`
- `06_AI_Context/Handoffs/ai-handoff-template.md`

## Folder Map
- `00_Inbox`: raw thoughts, screenshots, transcripts, unprocessed captures
- `01_Command_Center`: current priorities, daily/weekly/monthly reviews
- `02_Self_Context`: user profile, preferences, routines, principles
- `03_Work_and_Business`: businesses, offers, customers, sales, ops, finance
- `04_Projects`: active/backlog/paused/completed projects
- `05_Knowledge_Base`: people, companies, tools, concepts, research notes
- `06_AI_Context`: AI handoffs, prompts, Claude Code context, reusable instructions
- `07_Decisions_and_Lessons`: decisions, lessons, failure modes
- `08_Systems_and_SOPs`: checklists, automations, templates
- `09_Archive`: inactive historical material
""", encoding="utf-8")

print(f"Context vault created at: {root}")
