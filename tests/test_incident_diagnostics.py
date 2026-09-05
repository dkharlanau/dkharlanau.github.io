from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "labs" / "incident-diagnostics" / "index.md"
SCRIPT = ROOT / "assets" / "js" / "incident-diagnostics.js"
STYLE = ROOT / "assets" / "css" / "incident-diagnostics.css"


def test_incident_diagnostics_publication_boundary():
    text = PAGE.read_text(encoding="utf-8")
    assert "permalink: /labs/incident-diagnostics/" in text
    assert "verified: false" in text
    assert "robots: noindex,follow" in text
    assert "sitemap: false" in text
    assert "career_impact: mapped" in text
    assert "integration-recovery" in text
    assert "integration-observability" in text
    assert "logistics-mdg" in text


def test_incident_diagnostics_reuses_canonical_sources():
    script = SCRIPT.read_text(encoding="utf-8")
    assert "/datasets/incident-lab/cases.json" in script
    assert "/labs/templates/data/catalog.json" in script
    assert "/atlas/manifest.json" in script
    assert "localStorage" not in script
    assert "sessionStorage" not in script
    assert "fetch(url" in script
    assert "method:" not in script


def test_incident_diagnostics_exposes_required_artifacts_and_safety_copy():
    text = PAGE.read_text(encoding="utf-8")
    for label in ["Incident brief", "Evidence checklist", "RCA draft", "Jira-ready Markdown"]:
        assert label in text
    assert "It cannot prove the root cause" in text
    assert "does not upload the input" in text
    assert "does not store it in localStorage" in text
    assert "raw text into generated artifacts" in text


def test_incident_diagnostics_assets_exist():
    assert SCRIPT.exists()
    assert STYLE.exists()
