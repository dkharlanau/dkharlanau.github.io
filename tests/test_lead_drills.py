import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]

DRILL_PAGES = {
    "hub": ROOT / "labs/interview-readiness/drills/index.md",
    "decisions": ROOT / "labs/interview-readiness/decision-cards/index.md",
    "diagnostics": ROOT / "labs/interview-readiness/diagnostic-lab/index.md",
    "boss_battles": ROOT / "labs/interview-readiness/boss-battles/index.md",
    "evidence": ROOT / "labs/interview-readiness/evidence-bank/index.md",
}


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    assert text.startswith("---\n"), path
    end = text.find("\n---\n", 4)
    assert end > 0, path
    return yaml.safe_load(text[4:end]) or {}


def liquid_json(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    end = text.find("\n---\n", 4)
    return json.loads(text[end + 5 :])


def test_lead_drill_pages_are_browser_safe_utility_surfaces():
    for path in DRILL_PAGES.values():
        assert path.exists(), path
        data = frontmatter(path)
        assert data["status"] == "draft"
        assert data["verified"] is False
        assert data["robots"] == "noindex,follow"
        assert data["sitemap"] is False
        assert data["career_impact"] == "mapped"
        assert data["career_skills"]


def test_drills_hub_links_all_drill_routes():
    hub = DRILL_PAGES["hub"].read_text(encoding="utf-8")
    for route in (
        "/labs/interview-readiness/decision-cards/",
        "/labs/interview-readiness/diagnostic-lab/",
        "/labs/interview-readiness/boss-battles/",
        "/labs/interview-readiness/evidence-bank/",
    ):
        assert f'href="{route}"' in hub


def test_decision_cards_cover_cross_boundary_choices_and_pressure():
    text = DRILL_PAGES["decisions"].read_text(encoding="utf-8")
    for decision in (
        "IDoc vs API vs Event",
        "Synchronous vs Asynchronous",
        "Embedded vs Decentralised EWM",
        "Standard Extension vs Custom Development",
        "RAG vs Fine-tuning",
        "Agent Autonomy vs Human Approval",
    ):
        assert decision in text
    assert text.count("<strong>Pressure:</strong>") >= 8
    assert "Failure mode" in text


def test_diagnostic_lab_uses_progressive_evidence_and_explicit_evidence_levels():
    text = DRILL_PAGES["diagnostics"].read_text(encoding="utf-8")
    for case_id in (
        "idoc-51",
        "duplicate-orders",
        "billing-block",
        "atp-stock",
        "stock-mismatch",
        "po-ack",
        "api-timeout",
        "queue-backlog",
    ):
        assert case_id in text
    for level in ("Source fact", "Supported inference", "Proof gap", "Lead conclusion"):
        assert level in text
    assert "Reveal next evidence" in text


def test_boss_battles_change_constraints_and_keep_history_browser_local():
    text = DRILL_PAGES["boss_battles"].read_text(encoding="utf-8")
    for battle in (
        "Global Order Fulfilment Failure",
        "Supplier Confirmation and Inventory Crisis",
        "AI Agent Wants Production Authority",
    ):
        assert battle in text
    assert "Executive pressure" in text or "Sponsor pressure" in text
    assert "four-hour" in text
    assert "localStorage" in text
    assert "dkharlanau-boss-battle-history-v1" in text


def test_evidence_bank_never_equates_story_completeness_with_proof():
    text = DRILL_PAGES["evidence"].read_text(encoding="utf-8")
    assert "structural coverage, not truth" in text
    assert "never upgrades a story to “proof” automatically" in text
    for level in ("source fact", "supported inference", "runtime proof", "unsupported claim", "proof gap"):
        assert level in text.lower()
    assert "IR.storyBank()" in text


def test_professional_intelligence_contract_exposes_drill_layer():
    payload = liquid_json(ROOT / "ai/professional-intelligence.json")
    assert payload["schema_version"] == "1.1"
    layer = payload["drill_layer"]
    assert layer["hub"].endswith("/labs/interview-readiness/drills/")
    assert layer["decision_cards"].endswith("/decision-cards/")
    assert layer["diagnostic_lab"].endswith("/diagnostic-lab/")
    assert layer["boss_battles"].endswith("/boss-battles/")
    assert layer["evidence_bank"].endswith("/evidence-bank/")
    assert payload["privacy"]["browser_local_boss_battle_history"] is True


def test_machine_layer_links_human_drill_hub():
    machine = (ROOT / "machine/index.md").read_text(encoding="utf-8")
    assert 'href="/labs/interview-readiness/drills/"' in machine
    assert "SAP Lead Drill Layer" in machine
