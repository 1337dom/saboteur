<p align="center">
  <img src="https://em-content.zobj.net/source/apple/391/hammer-and-wrench_1f6e0-fe0f.png" width="120" />
</p>

<h1 align="center">Saboteur</h1>

<p align="center">
  <strong>break your own fix first</strong>
</p>

<p align="center">
  <a href="https://github.com/1337dom/saboteur/stargazers"><img src="https://img.shields.io/github/stars/1337dom/saboteur?style=flat&color=yellow" alt="Stars"></a>
  <a href="https://github.com/1337dom/saboteur/commits/main"><img src="https://img.shields.io/github/last-commit/1337dom/saboteur?style=flat" alt="Last Commit"></a>
</p>

<p align="center">
  <a href="#install">Install</a> •
  <a href="#before--after">Before / After</a> •
  <a href="#commands">Commands</a> •
  <a href="#workflow">Workflow</a> •
  <a href="#why">Why</a>
</p>

---

Saboteur is a coding-agent skill for one job: force self-critique before implementation.

It slows down the wrong part of the process on purpose. Not typing. Certainty.

Instead of rewarding the first plausible fix, Saboteur makes the agent:

- state the current hypothesis
- attack the plan with counterexamples
- look for alternate root causes
- map likely regressions
- shrink the patch to the smallest safer change

**Same fix target. Less false confidence.**

## Before / After

<table>
<tr>
<td width="50%">

### Fast Agent

> "The search bug is probably caused by too many requests firing while the user types. I'll increase the debounce, clean up the input handler, and add a basic test."

</td>
<td width="50%">

### Saboteur

> "Hypothesis weak. More debounce may hide race, not fix it. Counterexample: older response can still overwrite newer state. Safer patch: guard stale responses, keep debounce, add out-of-order regression test."

</td>
</tr>
<tr>
<td>

### Fast Agent

> "There is duplicated authorization logic here. I'll centralize everything into one helper so the rules stay consistent."

</td>
<td>

### Saboteur

> "Maybe not duplication problem. Maybe one endpoint intentionally different. Risk: centralized helper drops audit logging or changes 404/403 behavior. Extract pure predicate only."

</td>
</tr>
</table>

**Same engineering problem. More adversarial thinking.**

**Sometimes fix is fine. Sometimes fix too eager:**

<table>
<tr>
<td width="33%">

#### Quick

> "This change is mechanical. Saboteur bypass."

</td>
<td width="33%">

#### Full

> "Generate the full Saboteur report, revise the plan, then implement."

</td>
<td width="33%">

#### Postmortem

> "Patch done. Try to break it anyway."

</td>
</tr>
</table>

**Not every task need full sabotage. Pick pressure level.**

## Install

```bash
npx skills add 1337dom/saboteur --skill saboteur
```

Direct GitHub URL also works:

```bash
npx skills add https://github.com/1337dom/saboteur --skill saboteur
```

Manual install still works if you want local control:

### Codex

```bash
mkdir -p "$CODEX_HOME/skills"
cp -R saboteur "$CODEX_HOME/skills/saboteur"
```

### Claude Code

```bash
mkdir -p ~/.claude/skills
cp -R saboteur ~/.claude/skills/saboteur
```

Optional wrapper commands:

```bash
mkdir -p ~/.claude/commands
cp commands/*.md ~/.claude/commands/
```

One install. Use whenever a fix looks too neat.

## Commands

| Command | What it does |
|--------|---------------|
| `/saboteur` | Full workflow: hypothesis, sabotage, safer plan, execute, post-check |
| `/sabotage` | Full-workflow alias |
| `/counterexample` | Attack the current idea with the strongest concrete failure cases |
| `/regression-scan` | Map blast radius and likely behavior drift |
| `/alt-root-cause` | Rank alternate explanations before you optimize the wrong thing |
| `/minimal-fix` | Cut a broad solution down to the smallest safer patch |
| `/test-attack` | Design tests meant to break the change |
| `/postmortem-check` | Re-attack the final patch and name residual weaknesses |

## Workflow

Saboteur always runs the same discipline:

1. **Hypothesis**  
   Summarize the bug or task, state the current root-cause story, name likely files or functions, and commit to an initial fix idea.

2. **Sabotage**  
   Generate counterexamples, alternate explanations, hidden assumptions, regression risks, edge cases, and likely missing tests.

3. **Safer Plan**  
   Revise the plan, explain why it is safer, define the minimal patch scope, and name explicit non-goals.

4. **Execute**  
   Implement only after the safer plan exists. Keep edits minimal. Avoid unrelated cleanup.

5. **Post-Change Check**  
   Re-test earlier objections against the final patch. State residual risk and confidence.

## What Saboteur Produces

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

The point is not more text. The point is better pressure.

## Test Prompts

Trigger with:

- `/saboteur fix stale search results when typing quickly`
- `/counterexample add a debounce to stop duplicate requests in the search box`
- `/alt-root-cause login sometimes hangs after submit; current hypothesis is slow password hashing`
- `/minimal-fix refactor the whole permissions layer to fix one missing admin check`
- `/test-attack retry helper now stops after 3 attempts`

What good output looks like:

- starts with a concrete hypothesis instead of code
- finds the smallest break case instead of generic worry
- narrows the patch instead of widening it
- states residual risk instead of pretending certainty

## File Layout

```text
saboteur/
├── SKILL.md
├── README.md
├── agents/openai.yaml
├── commands/
├── examples/
└── scripts/
```

Notes:

- `SKILL.md` is the published skill.
- `commands/` contains optional wrapper commands for environments that support them.
- `examples/` shows the skill in bug-fix, refactor, and test-design scenarios.
- `scripts/` contains tiny helpers for scaffolding and formatting Saboteur reports.
- `agents/openai.yaml` is optional UI metadata, not a discovery requirement.

## Why

```text
┌────────────────────────────────────────┐
│  SHALLOW FIX RISK        ████████ high │
│  SELF-CRITIQUE           ████████ high │
│  PATCH SIZE              ████ smaller  │
│  FALSE CONFIDENCE        ██ lower      │
└────────────────────────────────────────┘
```

- **Find weak plans earlier** — before they become commits, reviews, or regressions
- **Reduce blast radius** — smaller safer patches survive better than “while I’m here” rewrites
- **Improve debugging quality** — alternate explanations keep you from fixing the wrong thing
- **Strengthen tests** — attack-style tests reveal confidence theater fast
- **Stay honest** — residual risk and confidence are part of the output, not hidden in tone

## Examples

- [Bug fix walkthrough](examples/bugfix-example.md)
- [Refactor walkthrough](examples/refactor-example.md)
- [Test design walkthrough](examples/test-example.md)

## Helper Scripts

Create a report scaffold:

```bash
python3 scripts/saboteur_template.py sabotage
python3 scripts/saboteur_template.py regression-scan --output report.md
```

Normalize an existing draft:

```bash
python3 scripts/format_saboteur_report.py --mode sabotage draft.md
python3 scripts/format_saboteur_report.py --mode test-attack --input draft.md --output clean.md
```

## Limitations

- Saboteur does not replace evidence. Weak logs still mean weak confidence.
- It should not turn typo fixes and obvious renames into a ritual.
- It is opinionated by design. If you want open-ended brainstorming, use something else.

## Star This Repo

If Saboteur saved you from one smug wrong fix, leave a star.

## License

Open repo. Sharp skill. Use it well.
