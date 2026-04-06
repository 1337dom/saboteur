# Saboteur

Break your own fix first.

Saboteur is a lightweight coding-agent skill that forces deliberate self-critique before implementation. It exists to stop shallow first-attempt fixes from sailing straight into regressions.

Instead of rewarding the first plausible answer, Saboteur asks the agent to do harder work first:

- find the smallest counterexample
- find the most likely regression
- challenge the current root-cause story
- cut the patch down to the smallest safer change

The result is not more ceremony. The result is fewer confident mistakes.

## Why It Exists

Coding agents are good at producing plausible fixes quickly. They are also good at overfitting to the first explanation that sounds right.

Saboteur is designed for the moment before that becomes expensive.

It enforces a compact falsification pass:

1. State the current hypothesis.
2. Attack it.
3. Revise the plan.
4. Implement only after the revised plan exists.

## Who Should Use It

Saboteur is useful for:

- software engineers fixing bugs under time pressure
- agents working in unfamiliar repositories
- maintainers reviewing risky refactors
- test authors designing adversarial coverage
- anyone who wants smaller, safer patches instead of wide “cleanup” fixes

It is especially useful when the first idea feels a little too clean.

## Philosophy

Saboteur is skeptical, disciplined, and practical.

- Favor falsification over confidence.
- Favor robustness over cleverness.
- Favor small patches over sweeping rewrites.
- Favor explicit residual risk over fake certainty.

This is not generic QA language. It is a behavioral mode for attacking weak plans before code lands.

## Quick Start

Use the main skill:

```text
/saboteur fix stale search results when typing quickly
```

Or the full alias:

```text
/sabotage fix stale search results when typing quickly
```

Expected flow:

1. The agent summarizes the task and working hypothesis.
2. The agent generates counterexamples, edge cases, regression risks, hidden assumptions, and alternative root causes.
3. The agent revises the plan into the smallest safer patch.
4. Only then does implementation begin.

## File Structure

```text
saboteur/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
├── commands/
│   ├── sabotage.md
│   ├── counterexample.md
│   ├── regression-scan.md
│   ├── alt-root-cause.md
│   ├── minimal-fix.md
│   ├── test-attack.md
│   └── postmortem-check.md
├── examples/
│   ├── bugfix-example.md
│   ├── refactor-example.md
│   └── test-example.md
└── scripts/
    ├── saboteur_template.py
    └── format_saboteur_report.py
```

## Main Workflow

Saboteur runs in five phases:

1. Hypothesis
2. Sabotage
3. Safer plan
4. Execute
5. Post-change check

The required report format is:

```markdown
# Saboteur Report

## Task
## Working Hypothesis
## Initial Proposed Fix
## Counterexamples
## Alternative Explanations
## Hidden Assumptions
## Regression Risks
## Edge Cases
## Likely Missing Tests
## Revised Safer Plan
## Minimal Patch Scope
## Non-Goals
## Validation Plan
## Residual Risk
## Confidence
```

## Slash Commands

`/saboteur`

- Main entrypoint.
- Runs the full workflow.
- Best when you want critique and implementation together.

`/sabotage`

- Full-workflow alias.
- Same behavior as `/saboteur`.

`/counterexample`

- Generates the strongest attack cases against the current idea or patch summary.
- Good when a proposed fix already exists and you want to stress it fast.

`/regression-scan`

- Maps blast radius and likely behavior drift.
- Good before touching shared modules or abstractions.

`/alt-root-cause`

- Produces alternative explanations ranked by plausibility.
- Good when the current hypothesis is mostly inference.

`/minimal-fix`

- Shrinks a broad plan into a smaller safer patch.
- Good when the solution is drifting into cleanup or redesign.

`/test-attack`

- Designs adversarial tests meant to break the fix.
- Good when existing coverage only proves the happy path.

`/postmortem-check`

- Re-attacks the final patch and names residual weaknesses.
- Good right before merge or handoff.

The focused commands are included as portable wrapper files in [commands/](commands/). In environments that support command files, they can be installed as standalone slash commands.

## Example Workflow

Request:

```text
/saboteur fix duplicate notifications after reconnect
```

Typical shape of the response:

1. Working hypothesis: reconnect handler re-subscribes without tearing down the old listener.
2. Counterexample: duplicate notifications still happen if the root cause is server replay, not client listeners.
3. Alternative explanation: replay window and dedupe key mismatch may be more plausible than double subscription.
4. Revised safer plan: instrument subscription count, patch teardown ordering, add a duplicate-event regression test, avoid refactoring the notification service.

## Practical Use Cases

- Bug fix in async UI code where stale state or request ordering may be involved
- Refactor of auth, caching, retries, or state transitions where blast radius is hard to see
- Test design for fragile recovery, cancellation, backoff, or idempotency behavior
- Patch review when the diff “looks fine” but the failure mode is still ambiguous

## Limitations

- Saboteur does not replace debugging evidence. If logs, traces, or reproduction are weak, confidence should stay weak.
- It can slow down trivial work if used indiscriminately, which is why the skill includes a bypass for safe mechanical edits.
- It is intentionally opinionated. If you want a broad exploratory brainstorm, this is the wrong tool.

## Install

### Codex

Copy or symlink this directory into your Codex skills folder:

```bash
mkdir -p "$CODEX_HOME/skills"
cp -R saboteur "$CODEX_HOME/skills/saboteur"
```

If your Codex setup uses the default home directory, that typically resolves under `~/.codex/skills/saboteur`.

### Claude Code

Install as a personal or project skill:

```bash
mkdir -p ~/.claude/skills
cp -R saboteur ~/.claude/skills/saboteur
```

Or inside a repository:

```bash
mkdir -p .claude/skills
cp -R saboteur .claude/skills/saboteur
```

To expose the focused slash commands as standalone command files, also copy the wrappers:

```bash
mkdir -p ~/.claude/commands
cp commands/*.md ~/.claude/commands/
```

## Helper Scripts

Create a fresh report scaffold:

```bash
python3 scripts/saboteur_template.py sabotage
python3 scripts/saboteur_template.py regression-scan --output report.md
```

Normalize an existing report into stable section order:

```bash
python3 scripts/format_saboteur_report.py --mode sabotage draft.md
python3 scripts/format_saboteur_report.py --mode test-attack --input draft.md --output clean.md
```

## Contribution Ideas

- add more high-signal examples from real repositories
- add optional icons and brand assets for UI catalogs
- add a tiny validation script for skill package consistency
- add language-specific test-attack heuristics without bloating the core skill

## One Practical Invocation

```text
/minimal-fix refactor the whole permissions layer to fix one missing admin check in the billing export endpoint
```

Expected result:

- strip the plan back to the billing export path
- preserve existing side effects and audit logging
- define non-goals
- identify the minimal safer patch before any refactor happens
