#!/usr/bin/env python3
"""Normalize Saboteur report section order without changing the content."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys

ORDERS = {
    "sabotage": [
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
    "counterexample": [
        "Proposal",
        "Counterexamples",
        "Weakest Assumptions",
        "Implications",
        "Recommended Adjustment",
    ],
    "regression-scan": [
        "Change Summary",
        "Touched Surfaces",
        "Regression Risks",
        "Blast Radius",
        "Validation Priorities",
    ],
    "alt-root-cause": [
        "Bug Summary",
        "Current Hypothesis",
        "Alternative Explanations",
        "Evidence Needed",
        "Most Plausible Next Step",
    ],
    "minimal-fix": [
        "Current Plan",
        "Risky Expansion",
        "Revised Safer Plan",
        "Minimal Patch Scope",
        "Non-Goals",
    ],
    "test-attack": [
        "Patch Claim",
        "Likely Missing Tests",
        "Adversarial Test Ideas",
        "Priority Cases",
        "Residual Blind Spots",
    ],
    "postmortem-check": [
        "Change Summary",
        "Earlier Counterexamples",
        "What Still Fails",
        "Residual Risk",
        "Confidence",
        "Follow-Up Checks",
    ],
}

TITLES = {
    "sabotage": "# Saboteur Report",
    "counterexample": "# Counterexample Report",
    "regression-scan": "# Regression Scan",
    "alt-root-cause": "# Alternative Root Cause Review",
    "minimal-fix": "# Minimal Fix Review",
    "test-attack": "# Test Attack",
    "postmortem-check": "# Postmortem Check",
}

HEADING_RE = re.compile(r"^##\s+(.*\S)\s*$")


def parse_sections(text: str) -> tuple[list[str], dict[str, list[str]]]:
    preamble: list[str] = []
    sections: dict[str, list[str]] = {}
    current = preamble
    current_name = ""

    for line in text.splitlines():
        match = HEADING_RE.match(line)
        if match:
            current_name = match.group(1)
            current = sections.setdefault(current_name, [])
            continue
        current.append(line)

    return preamble, sections


def normalize(mode: str, text: str) -> str:
    preamble, sections = parse_sections(text)
    lines: list[str] = [TITLES[mode], ""]

    filtered_preamble = [line for line in preamble if not line.startswith("# ")]
    cleaned_preamble = "\n".join(line.rstrip() for line in filtered_preamble).strip()
    if cleaned_preamble:
        lines.extend([cleaned_preamble, ""])

    for section in ORDERS[mode]:
        body = "\n".join(line.rstrip() for line in sections.get(section, [])).strip()
        lines.append(f"## {section}")
        lines.append("")
        lines.append(body if body else "- ")
        lines.append("")

    extras = [name for name in sections if name not in ORDERS[mode]]
    for name in extras:
        body = "\n".join(line.rstrip() for line in sections[name]).strip()
        lines.append(f"## {name}")
        lines.append("")
        lines.append(body if body else "- ")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", required=True, choices=sorted(ORDERS), help="Report mode to normalize.")
    parser.add_argument(
        "input",
        nargs="?",
        help="Optional input file. If omitted, read from stdin.",
    )
    parser.add_argument("--output", type=Path, help="Optional output file.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.input:
        source = Path(args.input).read_text(encoding="utf-8")
    else:
        source = sys.stdin.read()

    normalized = normalize(args.mode, source)
    if args.output:
        args.output.write_text(normalized, encoding="utf-8")
        print(f"Wrote {args.output}")
    else:
        sys.stdout.write(normalized)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
