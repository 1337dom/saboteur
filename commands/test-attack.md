---
name: test-attack
description: Design adversarial tests meant to break a planned or completed fix. Use when existing coverage only proves the happy path or misses edge-case behavior.
argument-hint: [planned fix | final patch summary]
disable-model-invocation: true
---

# Test Attack

Design tests that try to make the fix fail.

Input:

- planned fix
- final patch summary
- touched behavior

Behavior:

1. Restate the behavior the patch claims to fix.
2. Generate attack-style tests targeting ordering, stale state, retries, failures, and invariants.
3. Call out missing coverage explicitly.
4. Prioritize tests most likely to expose a false sense of safety.

Output:

- `# Test Attack`
- adversarial test ideas
- missing coverage list

Guardrails:

- target the patch’s weak spots
- prefer realistic failure modes
- do not implement changes unless explicitly asked elsewhere

Request:

`$ARGUMENTS`
