#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from analyze_business_ai_portfolio import build_report

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "reports" / "business-ai-portfolio.json"
DEFAULT_MARKDOWN = ROOT / "reports" / "business-ai-portfolio.md"


def render_markdown(report: dict) -> str:
    summary = report["summary"]
    priorities = report.get("research_priorities", [])
    lines = [
        "# Business AI Portfolio Scorecard",
        "",
        f"Snapshot: `{report['snapshot_key']}`",
        "",
        "## Portfolio summary",
        "",
        f"- Catalog cases: **{summary['catalog_case_count']}**",
        f"- Strong cases: **{summary['strong_case_count']}**",
        f"- Strong catalog evidence: **{summary['strong_catalog_evidence_count']}**",
        f"- Strong scenario evidence: **{summary['strong_scenario_evidence_count']}**",
        f"- Cases with reported metrics: **{summary['catalog_metric_case_count']}**",
        f"- Cases with explicit limitations: **{summary['catalog_limitation_case_count']}**",
        f"- Observed negative or mixed records: **{summary['observed_negative_count']}**",
        f"- Plausible risk records: **{summary['plausible_risk_count']}**",
        "",
        "> Strong case count and strong evidence count are intentionally separate. A useful scenario is not automatically strong public proof.",
        "",
        "## Research priority matrix",
        "",
        "| Rank | Slice | Score | Strong evidence | Observed negative | Control coverage | Reasons |",
        "|---:|---|---:|---:|---:|---:|---|",
    ]
    for row in priorities:
        reasons = "; ".join(row.get("reasons", [])) or "No material gap"
        lines.append(
            "| {rank} | {id} | {score} | {strong} | {negative} | {control} | {reasons} |".format(
                rank=row["rank"],
                id=row["id"],
                score=row["score"],
                strong=row.get("strong_evidence_case_count", 0),
                negative=row.get("observed_negative_count", 0),
                control=row.get("case_control_count", 0),
                reasons=reasons.replace("|", "/"),
            )
        )

    lines.extend([
        "",
        "## Negative evidence boundary",
        "",
        "Observed failure, mixed outcome, and limited pilot records are source-linked evidence records. Plausible risks are architecture hypotheses. They stay in separate collections and must not be reported as observed incidents.",
        "",
        "## Trend use",
        "",
        "The JSON report keeps stable dimensions, a snapshot key, and method metadata so future snapshots can compare coverage without changing the scoring definition silently.",
        "",
    ])
    return "\n".join(lines)


def write_reports(json_path: Path, markdown_path: Path) -> dict:
    report = build_report()
    json_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(report, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    markdown_path.write_text(render_markdown(report), encoding="utf-8")
    return report


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Build Business AI portfolio JSON and Markdown scorecards.")
    parser.add_argument("--json-output", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--markdown-output", type=Path, default=DEFAULT_MARKDOWN)
    args = parser.parse_args(argv)
    report = write_reports(args.json_output, args.markdown_output)
    print(
        "Business AI portfolio reports built: "
        f"{report['summary']['catalog_case_count']} cases, "
        f"{report['summary']['observed_negative_count']} observed negative records, "
        f"{len(report['research_priorities'])} ranked research slices."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
