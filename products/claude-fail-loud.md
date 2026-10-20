---
name: claude-fail-loud
description: "Use when building API integrations, database calls, file parsers, payment flows, auth, external services, or any code that might silently fake success. Enforces fail-loud error handling and no mock-data deception."
license: MIT
metadata:
  author: dominic-operator-pack
  version: '1.0'
---

# Fail Loud, Never Fake

## When to Use This Skill

- Code talks to APIs, databases, auth providers, payments, files, queues, or external systems.
- Claude proposes fallback mock data, broad try/catch blocks, swallowed errors, or placeholder success states.
- The user complains that something says done but is not actually working.

## When Not to Use This Skill

- Pure deterministic utility functions with no I/O and no user-visible state.
- Intentional test doubles inside a test file clearly marked as mocks.

## Intake Questions

Ask only for missing information that changes the output. If enough context exists, proceed and state assumptions.

- What real service, credential, endpoint, table, or file is the source of truth?
- What should the user see when the service fails?
- What telemetry or logs should capture the failure?

## Operating Workflow

- Remove silent catch-all fallbacks that return empty arrays, default objects, or fake success.
- Make failures visible at the right layer: log details server-side, show safe user-facing errors client-side.
- If using fallback data, label it clearly in UI, logs, and return metadata.
- Preserve the original exception message, failing operation, request id, and service name in logs.
- Add tests for failure paths, not only happy paths.
- Refuse to mark done until a real integration path is exercised or the untested gap is explicitly stated.

## Output Contract

Always produce practical artifacts the user can copy, paste, configure, or hand to a contractor.

- Risk assessment of where fake success could occur.
- Concrete error-handling policy for the feature.
- Suggested tests for API failure, timeout, bad credentials, bad schema, and empty-state cases.

## Quality Checklist

Before finalizing, verify:

- No broad catch block hides the cause of failure.
- Mocks are confined to tests or clearly marked demo mode.
- The final answer distinguishes verified working behavior from assumptions.

## Research-Backed Defaults and Sources

- Anthropic Claude Code best practices: https://code.claude.com/docs/en/best-practices
- Anthropic Claude Code hooks guide: https://code.claude.com/docs/en/hooks-guide
- Anthropic Claude Code MCP guide: https://code.claude.com/docs/en/mcp
- Model Context Protocol server docs: https://modelcontextprotocol.io/docs/develop/build-server
- MCP security best practices: https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices
- HumanLayer CLAUDE.md guidance: https://www.humanlayer.dev/blog/writing-a-good-claude-md

