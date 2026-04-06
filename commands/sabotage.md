---
name: sabotage
description: Run the full Saboteur workflow on a task, bug, or patch summary. Use when you want counterexamples, regression risks, alternate root causes, a smaller safer plan, and only then implementation.
argument-hint: [task | bug | patch summary]
disable-model-invocation: true
---

# Sabotage

Break the current plan before touching code.

Input:

- task, bug report, patch summary, or implementation request

Workflow:

1. Summarize the task and current working hypothesis.
2. State the initial proposed fix.
3. Generate at least 3 concrete failure modes.
4. Generate edge cases, regression risks, hidden assumptions, and at least 1 alternative root-cause explanation.
5. Revise the plan into the smallest safer patch.
6. Implement only after the revised safer plan exists.
7. Finish with residual risk, confidence, and validation steps.

Output:

- the full `# Saboteur Report`
- a safer implementation plan
- implementation only after the revised plan exists

Guardrails:

- do not block trivial mechanical edits unless the user explicitly wants scrutiny
- do not recommend broad rewrites when a narrow patch can survive criticism
- do not leave the report vague; name files, functions, or surfaces when possible

Request:

`$ARGUMENTS`
