from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "_data" / "career" / "learning_science.yml"
TODAY_PATH = ROOT / "labs" / "interview-readiness" / "today" / "index.md"
SCIENCE_PATH = ROOT / "labs" / "interview-readiness" / "learning-science" / "index.md"
JS_PATH = ROOT / "assets" / "js" / "mastery-today.js"
CSS_PATH = ROOT / "assets" / "css" / "mastery-today.css"


def load_data():
    return yaml.safe_load(DATA_PATH.read_text(encoding="utf-8"))


def test_evidence_registry_has_required_learning_mechanisms_and_sources():
    data = load_data()
    principles = {item["id"]: item for item in data["principles"]}
    required = {
        "retrieval",
        "spacing",
        "interleaving",
        "pretesting",
        "feedback",
        "error_contrast",
        "confidence",
        "mismatch",
        "sleep",
        "movement",
        "biometrics_boundary",
    }
    assert required <= principles.keys()
    for principle in principles.values():
        assert principle["rule"]
        assert principle["product_use"]
        assert principle["avoid"]
        assert principle["sources"]
        assert all(source["href"].startswith("https://") for source in principle["sources"])


def test_backlog_is_unique_prioritised_and_starts_with_p0_execution():
    backlog = load_data()["backlog"]
    ids = [item["id"] for item in backlog]
    assert len(ids) == len(set(ids))
    assert {item["priority"] for item in backlog} <= {"P0", "P1", "P2", "P3"}
    p0 = [item for item in backlog if item["priority"] == "P0"]
    assert len(p0) >= 5
    assert all(item["status"] == "in_progress" for item in p0)
    assert any(item["title"] == "Confidence before reveal" for item in p0)
    assert any(item["title"] == "Delayed repair queue" for item in p0)


def test_learning_science_page_is_draft_data_driven_and_has_physiology_boundary():
    text = SCIENCE_PATH.read_text(encoding="utf-8")
    assert "permalink: /labs/interview-readiness/learning-science/" in text
    assert "status: draft" in text
    assert "verified: false" in text
    assert "robots: noindex,follow" in text
    assert "sitemap: false" in text
    assert "site.data.career.learning_science.principles" in text
    assert "site.data.career.learning_science.backlog" in text
    assert "we do not turn HR, HRV, cortisol" in text
    assert "/labs/interview-readiness/today/" in text
    assert "/labs/interview-readiness/memory-atlas/" in text


def test_mastery_today_commits_confidence_before_feedback_and_collects_mismatch():
    page = TODAY_PATH.read_text(encoding="utf-8")
    assert 'id="mt-confidence"' in page
    assert "Confidence before feedback" in page
    assert "Commit confidence and reveal" in page
    assert 'id="mt-mismatch"' in page
    assert 'id="mt-repair-note"' in page
    assert "This text is not saved to history" in page
    assert "/labs/interview-readiness/learning-science/" in page


def test_mastery_engine_stores_calibration_metadata_but_not_answer_or_repair_text():
    js = JS_PATH.read_text(encoding="utf-8")
    assert "confidence," in js
    assert "mismatch," in js
    assert "calibrationGap" in js
    assert "averageCalibrationGap" in js
    assert "repair_after" in js
    assert "repairDeferred" in js
    assert "repairReady" in js
    assert "ordinal + 2" in js
    assert "crossedCalendarDay" in js
    assert "row.answer" not in js
    assert "repair_note" not in js
    assert "repairNote," not in js
    assert "version: 3" in js
    assert "scheduler_version:" in js


def test_major_mismatch_cannot_advance_mastery_and_weak_repair_requires_explanation():
    js = JS_PATH.read_text(encoding="utf-8")
    assert "row.score >= PASS_SCORE && Number(row.mismatch || 0) < 2" in js
    assert "numericScore < PASS_SCORE || mismatch === 2" in js
    assert "repairNote.length < 12" in js
    assert "Explain the important mismatch" in js


def test_mastery_styles_cover_confidence_and_repair_controls():
    css = CSS_PATH.read_text(encoding="utf-8")
    assert ".mastery-confidence" in css
    assert ".mastery-repair" in css
    assert ".mastery-repair-status" in css
