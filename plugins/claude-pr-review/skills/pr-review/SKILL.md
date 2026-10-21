---
name: pr-review
description: "Use when reviewing a pull request, checking recent changes, verifying implementation against a ticket, spotting fake success, or preparing review comments. Always prefer fresh-context review."
license: MIT
metadata:
  author: dominic-operator-pack
  version: '1.0'
---

# Claude PR Review

## When to Use This Skill

- The user asks to review a PR, diff, patch, or recent implementation.
- A builder agent completed work and needs independent verification.
- The user wants an adversarial review for correctness, security, or hidden regressions.

## When Not to Use This Skill

- The user is still asking to implement the feature, not review it.
- There is no diff, branch, PR, or spec to compare against.

## Intake Questions

Ask only for missing information that changes the output. If enough context exists, proceed and state assumptions.

- What is the original ticket or acceptance criteria?
- What branch, PR, or diff should be reviewed?
- What risks matter most: security, data loss, payments, performance, UX, or test coverage?

## Operating Workflow

- Start from the ticket/spec, not from the implementation narrative.
- Check for unrelated changes and hidden broad refactors.
- Inspect failure paths, not just happy paths.
- Look for silent fallback, mock data, swallowed errors, auth bypasses, and missing idempotency.
- Run or request the relevant tests and note exactly what passed or failed.
- Classify findings as blocking, high, medium, low, or nit.
- Suggest concrete fixes, not vague feedback.

## Output Contract

Always produce practical artifacts the user can copy, paste, configure, or hand to a contractor.

- Review summary and recommendation.
- Findings grouped by severity.
- Line/file references where available.
- Test results and unverified areas.

## Quality Checklist

Before finalizing, verify:

- Every blocking issue ties back to user impact or acceptance criteria.
- No approval is given if tests were not run unless explicitly labeled.
- Feedback is actionable and minimal.

## Research-Backed Defaults and Sources

- Anthropic Claude Code best practices: https://code.claude.com/docs/en/best-practices
- Anthropic Claude Code hooks guide: https://code.claude.com/docs/en/hooks-guide
- Anthropic Claude Code MCP guide: https://code.claude.com/docs/en/mcp
- Model Context Protocol server docs: https://modelcontextprotocol.io/docs/develop/build-server
- MCP security best practices: https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices
- HumanLayer CLAUDE.md guidance: https://www.humanlayer.dev/blog/writing-a-good-claude-md

