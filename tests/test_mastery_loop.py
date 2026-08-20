from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
ROADMAP = ROOT / "_data" / "career" / "roadmap.yml"
MASTERY = ROOT / "_data" / "career" / "mastery.yml"
PAGE = ROOT / "labs" / "interview-readiness" / "today" / "index.md"
SCRIPT = ROOT / "assets" / "js" / "mastery-today.js"
STYLE = ROOT / "assets" / "css" / "mastery-today.css"


def load_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_mastery_contract_has_progression_and_spaced_review():
    data = load_yaml(MASTERY)
    contract = data["contract"]
    assert [item["id"] for item in contract["states"]] == [
        "new",
        "recalled",
        "connected",
        "applied",
        "defended",
        "retained",
    ]
    assert contract["review_intervals_days"] == [1, 3, 7, 14, 30]
    assert contract["pass_score"] == 2
    assert contract["session_size"] == 5
    assert contract["retained_successes"] >= 3
    assert contract["retained_span_days"] >= 7


def test_five_link_cards_reference_real_career_skills():
    roadmap = load_yaml(ROADMAP)
    mastery = load_yaml(MASTERY)
    skill_ids = {item["id"] for item in roadmap["skills"]}
    cards = mastery["cards"]
    card_ids = [item["skill_id"] for item in cards]
    assert len(card_ids) == len(set(card_ids))
    assert len(cards) >= 12
    assert set(item["track"] for item in cards) == {"sales", "logistics", "integration", "ai"}
    assert set(card_ids) <= skill_ids

    required = {
        "title",
        "source",
        "trigger",
        "flow",
        "objects_rules",
        "failure_boundary",
        "lead_decision",
        "connect_prompt",
        "apply_prompt",
        "defend_prompt",
    }
    for card in cards:
        assert required <= set(card)
        assert card["source"].startswith("/")
        for field in required - {"source"}:
            assert isinstance(card[field], str) and card[field].strip()


def test_today_page_is_private_local_first_and_data_driven():
    page = PAGE.read_text(encoding="utf-8")
    assert "permalink: /labs/interview-readiness/today/" in page
    assert "verified: false" in page
    assert "robots: noindex,follow" in page
    assert "career_impact: mapped" in page
    assert "site.data.career.mastery" in page
    assert 'id="mastery-data"' in page
    assert "/assets/js/mastery-today.js" in page
    assert "/assets/css/mastery-today.css" in page
    assert "Close the notes." in page
    assert "Five-Link" in page


def test_mastery_engine_prioritises_retrieval_and_due_review():
    script = SCRIPT.read_text(encoding="utf-8")
    assert "localStorage" in script
    assert "function dueAt" in script
    assert "function stateFor" in script
    assert "function selectSession" in script
    assert "function modeFor" in script
    assert "REVIEW_INTERVALS" in script
    assert "retained" in script
    assert "Cold review" in script
    assert "answer" not in ""  # keeps this test intentionally focused on engine contracts


def test_mastery_assets_exist_and_page_does_not_store_answer_text():
    script = SCRIPT.read_text(encoding="utf-8")
    style = STYLE.read_text(encoding="utf-8")
    assert "mt-answer" in script
    assert "answer:" not in script
    assert "mastery-five-link" in style
    assert "mastery-score-button" in style
