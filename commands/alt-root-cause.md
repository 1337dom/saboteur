---
name: alt-root-cause
description: Generate alternative root-cause explanations for a bug or failure. Use when the current hypothesis is weak, inferred, or based on incomplete evidence.
argument-hint: [bug summary | current hypothesis]
disable-model-invocation: true
---

# Alternative Root Cause

Challenge the current explanation before you optimize the wrong thing.

Input:

- bug summary
- current hypothesis
- any available evidence

Behavior:

1. Restate the current hypothesis.
2. Generate alternative root-cause candidates.
3. Rank them by plausibility.
4. Name the evidence that would confirm or reject each one.

Output:

- `# Alternative Root Cause Review`
- ranked alternative explanations
- evidence gaps

Guardrails:

- no random guess pile
- say when the current hypothesis is still strongest
- do not implement changes

Request:

`$ARGUMENTS`
