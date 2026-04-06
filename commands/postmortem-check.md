---
name: postmortem-check
description: Re-attack a finished patch and identify residual weaknesses. Use after implementation, before merge, or before handoff when you want one last adversarial pass.
argument-hint: [final diff | patch summary]
disable-model-invocation: true
---

# Postmortem Check

Try to break the patch after it already looks done.

Input:

- final diff
- touched files
- summary of changes

Behavior:

1. Revisit the earlier counterexamples.
2. Check whether the final patch still fails any of them.
3. State residual risks and confidence.
4. Recommend follow-up validation steps.

Output:

- `# Postmortem Check`
- residual risk review
- confidence level
- follow-up checks

Guardrails:

- focus on remaining weaknesses
- do not drift into unrelated style review
- do not implement new work unless explicitly requested

Request:

`$ARGUMENTS`
