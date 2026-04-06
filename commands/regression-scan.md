---
name: regression-scan
description: Identify likely regressions, blast radius, and affected surfaces for an intended change. Use before touching shared modules, abstractions, state flows, or behavior with hidden callers.
argument-hint: [change summary | touched files]
disable-model-invocation: true
---

# Regression Scan

Map what the change can accidentally break.

Input:

- intended change
- touched files
- affected modules or interfaces

Behavior:

1. Summarize the behavioral change.
2. Identify callers, invariants, and coupled surfaces likely to drift.
3. Rank the most likely regressions first.
4. Recommend validation priorities.

Output:

- `# Regression Scan`
- regression map
- blast-radius summary
- validation priorities

Guardrails:

- prefer likely regressions over theoretical ones
- avoid exhaustive dependency dumps
- do not implement changes

Request:

`$ARGUMENTS`
