from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from analyze_business_ai_portfolio import build_report
from build_business_ai_portfolio_reports import render_markdown, write_reports


def test_portfolio_report_separates_case_strength_from_evidence_strength():
    report = build_report()
    summary = report["summary"]
    assert "strong_case_count" in summary
    assert "strong_catalog_evidence_count" in summary
    assert "strong_scenario_evidence_count" in summary
    assert report["method"]["strong_case_rule"] != report["method"]["strong_evidence_rule"]


def test_observed_negative_and_plausible_risk_are_separate():
    report = build_report()
    negative = report["negative_evidence"]
    assert negative["observed_records"]
    assert negative["plausible_risks"]
    observed_ids = {item["id"] for item in negative["observed_records"]}
    risk_ids = {item["id"] for item in negative["plausible_risks"]}
    assert observed_ids.isdisjoint(risk_ids)
    assert all(item.get("scenario_id") for item in negative["observed_records"])
    assert all(not item.get("scenario_id") for item in negative["plausible_risks"])


def test_priority_model_is_ranked_and_explainable():
    priorities = build_report()["research_priorities"]
    assert priorities
    assert [item["rank"] for item in priorities] == list(range(1, len(priorities) + 1))
    assert all("score" in item and "reasons" in item for item in priorities)
    assert priorities == sorted(priorities, key=lambda row: (-row["score"], row["id"]))


def test_trend_contract_and_dimensions_are_stable_outputs():
    report = build_report()
    assert report["snapshot_key"]
    assert report["trend_contract"]
    for key in ["domains", "processes", "patterns", "industries", "evidence_grades", "implementation_maturity", "case_autonomy"]:
        assert key in report["dimensions"]


def test_markdown_scorecard_explains_negative_evidence_boundary():
    text = render_markdown(build_report())
    assert "# Business AI Portfolio Scorecard" in text
    assert "Research priority matrix" in text
    assert "Strong case count and strong evidence count are intentionally separate" in text
    assert "Plausible risks are architecture hypotheses" in text


def test_report_builder_writes_json_and_markdown(tmp_path):
    json_path = tmp_path / "portfolio.json"
    md_path = tmp_path / "portfolio.md"
    report = write_reports(json_path, md_path)
    assert json_path.exists()
    assert md_path.exists()
    assert str(report["summary"]["catalog_case_count"]) in md_path.read_text(encoding="utf-8")
