---
name: counterexample
description: Generate the strongest concrete counterexamples against a proposed fix, diff, or plan. Use when an idea already exists and you want the sharpest attack cases before implementation.
argument-hint: [fix idea | diff | patch summary]
disable-model-invocation: true
---

# Counterexample

Attack the current idea fast.

Input:

- a fix idea
- a diff summary
- a patch summary

Behavior:

1. Restate the proposal in one sentence.
2. Produce the strongest concrete counterexamples against it.
3. Prefer small, plausible break cases over broad speculation.
4. Explain what each counterexample implies about the proposal.

Output:

- `# Counterexample Report`
- top attack cases
- implications for the current idea

Guardrails:

- keep it concrete
- rank plausibility over novelty
- do not implement changes

Request:

`$ARGUMENTS`
