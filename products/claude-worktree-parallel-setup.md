---
name: claude-worktree-parallel-setup
description: "Use when running multiple Claude Code agents in parallel, using git worktrees, avoiding port/database collisions, or splitting features into independent AI workers."
license: MIT
metadata:
  author: dominic-operator-pack
  version: '1.0'
---

# Parallel Claude Worktree Setup

## When to Use This Skill

- The user wants multiple agents working on separate issues.
- Parallel sessions are colliding on ports, databases, Docker, or migrations.
- The user wants a scalable AI coding factory pattern.

## When Not to Use This Skill

- There is only one small edit and no need for parallelism.
- The repo cannot safely run multiple instances or has no test isolation.

## Intake Questions

Ask only for missing information that changes the output. If enough context exists, proceed and state assumptions.

- How many parallel tasks and what issue/ticket maps to each?
- What ports, databases, queues, and env vars does the app use?
- What branch naming and PR process should agents follow?

## Operating Workflow

- Create one issue or task contract per worktree before spawning agents.
- Use one worktree per task and never let two agents edit the same branch.
- Derive ports from a formula such as BASE_PORT + index times 10.
- Use isolated databases, database branches, schemas, or test containers per worktree.
- Install dependencies during setup, not mid-agent when possible.
- Run fresh-context review after each implementation. Do not let builders grade their own work.
- Merge only after tests pass and unrelated diffs are removed.

## Output Contract

Always produce practical artifacts the user can copy, paste, configure, or hand to a contractor.

- Worktree matrix: issue, branch, path, ports, database, owner, status.
- Setup commands.
- Agent prompt template for each worker.
- Review and merge checklist.

## Quality Checklist

Before finalizing, verify:

- No shared writable database or port collision remains.
- Each agent has a tight task contract.
- Review happens in a separate context from implementation.

## Research-Backed Defaults and Sources

- Anthropic Claude Code best practices: https://code.claude.com/docs/en/best-practices
- Anthropic Claude Code hooks guide: https://code.claude.com/docs/en/hooks-guide
- Anthropic Claude Code MCP guide: https://code.claude.com/docs/en/mcp
- Model Context Protocol server docs: https://modelcontextprotocol.io/docs/develop/build-server
- MCP security best practices: https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices
- HumanLayer CLAUDE.md guidance: https://www.humanlayer.dev/blog/writing-a-good-claude-md

