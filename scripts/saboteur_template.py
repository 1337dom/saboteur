#!/usr/bin/env python3
"""Emit Markdown scaffolds for Saboteur reports."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

TEMPLATES = {
    "sabotage": (
        "# Saboteur Report",
        [
            "Task",
            "Working Hypothesis",
            "Initial Proposed Fix",
            "Counterexamples",
            "Alternative Explanations",
            "Hidden Assumptions",
            "Regression Risks",
            "Edge Cases",
            "Likely Missing Tests",
            "Revised Safer Plan",
            "Minimal Patch Scope",
            "Non-Goals",
            "Validation Plan",
            "Residual Risk",
            "Confidence",
        ],
    ),
    "counterexample": (
        "# Counterexample Report",
        [
            "Proposal",
            "Counterexamples",
            "Weakest Assumptions",
            "Implications",
            "Recommended Adjustment",
        ],
    ),
    "regression-scan": (
        "# Regression Scan",
        [
            "Change Summary",
            "Touched Surfaces",
            "Regression Risks",
            "Blast Radius",
            "Validation Priorities",
        ],
    ),
    "alt-root-cause": (
        "# Alternative Root Cause Review",
        [
            "Bug Summary",
            "Current Hypothesis",
            "Alternative Explanations",
            "Evidence Needed",
            "Most Plausible Next Step",
        ],
    ),
    "minimal-fix": (
        "# Minimal Fix Review",
        [
            "Current Plan",
            "Risky Expansion",
            "Revised Safer Plan",
            "Minimal Patch Scope",
            "Non-Goals",
        ],
    ),
    "test-attack": (
        "# Test Attack",
        [
            "Patch Claim",
            "Likely Missing Tests",
            "Adversarial Test Ideas",
            "Priority Cases",
            "Residual Blind Spots",
        ],
    ),
    "postmortem-check": (
        "# Postmortem Check",
        [
            "Change Summary",
            "Earlier Counterexamples",
            "What Still Fails",
            "Residual Risk",
            "Confidence",
            "Follow-Up Checks",
        ],
    ),
}


def build_report(mode: str, task: str | None) -> str:
    title, sections = TEMPLATES[mode]
    lines = [title, ""]
    if task:
        lines.extend(["_Prompt_", "", task.strip(), ""])
    for section in sections:
        lines.extend([f"## {section}", "", "- ", ""])
    return "\n".join(lines).rstrip() + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=sorted(TEMPLATES), help="Report mode to scaffold.")
    parser.add_argument(
        "task",
        nargs="?",
        help="Optional task or summary to place under a _Prompt_ section.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Write the scaffold to a file instead of stdout.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    report = build_report(args.mode, args.task)
    if args.output:
        args.output.write_text(report, encoding="utf-8")
        print(f"Wrote {args.output}")
    else:
        sys.stdout.write(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
