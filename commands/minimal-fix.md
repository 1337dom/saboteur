---
name: minimal-fix
description: Shrink a broad implementation idea into the smallest safer patch. Use when a fix is expanding into cleanup, refactor, or redesign beyond what the issue requires.
argument-hint: [current implementation plan]
disable-model-invocation: true
---

# Minimal Fix

Cut the plan down until only the necessary behavior change remains.

Input:

- current implementation plan
- bug summary if relevant

Behavior:

1. Identify which parts of the plan are essential.
2. Remove cleanup, abstraction, and redesign work that is not required.
3. Define patch boundaries and non-goals.
4. Explain why the smaller plan is safer.

Output:

- `# Minimal Fix Review`
- reduced patch scope
- explicit non-goals
- smaller safer plan

Guardrails:

- smaller must still solve the issue
- preserve safety checks and necessary tests
- do not implement changes

Request:

`$ARGUMENTS`
