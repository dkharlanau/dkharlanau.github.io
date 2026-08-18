import json
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
ROADMAP = ROOT / "_data" / "career" / "roadmap.yml"


def load_roadmap():
    return yaml.safe_load(ROADMAP.read_text(encoding="utf-8"))


def test_career_roadmap_has_lead_level_scope():
    data = load_roadmap()
    assert set(data["tracks"]) == {"sales", "logistics", "integration", "ai", "delivery", "leadership"}
    assert [stage["id"] for stage in data["stages"]] == ["know", "diagnose", "design", "lead"]
    skill_ids = {skill["id"] for skill in data["skills"]}
    assert len(skill_ids) >= 40
    assert "delivery-cicd" in skill_ids
    assert "integration-recovery" in skill_ids
    assert "ai-agents-mcp" in skill_ids
    assert "lead-stakeholders" in skill_ids


def test_every_career_skill_has_interview_signal_and_sources():
    data = load_roadmap()
    for skill in data["skills"]:
        assert skill["title"].strip()
        assert skill["why"].strip()
        assert skill["interview_signal"].strip()
        assert skill["capabilities"]
        assert skill["sources"]
        for source in skill["sources"]:
            assert source["kind"]
            assert source["label"]
            assert source["href"].startswith("/") or source["href"].startswith("https://")


def test_career_factory_validator_passes_repository_model():
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "check_career_factory.py")],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Career Factory passed" in result.stdout


def test_career_roadmap_page_is_data_driven():
    page = (ROOT / "labs" / "interview-readiness" / "roadmap" / "index.md").read_text(encoding="utf-8")
    assert "site.data.career.roadmap" in page
    assert 'id="career-roadmap-data"' in page
    assert 'id="career-factory-control"' in page
    assert "/assets/js/career-roadmap.js" in page
    assert "/ai/career-factory.json" in page
    assert "Delivery & Operations" in ROADMAP.read_text(encoding="utf-8")
    assert "Career Factory" in page


def test_career_factory_ci_enforces_new_lab_impact_and_inventory():
    workflow = (ROOT / ".github" / "workflows" / "career-factory.yml").read_text(encoding="utf-8")
    assert "Career Factory" in workflow
    assert "--changed-from origin/${{ github.base_ref }}" in workflow
    assert "generate_career_factory.py --check" in workflow
    assert "ai/career-factory.json" in workflow
    assert "labs/**" in workflow
    contract = (ROOT / "labs" / "AGENTS.md").read_text(encoding="utf-8")
    assert "career_impact: mapped" in contract
    assert "career_impact: none" in contract
    assert "career_skills" in contract
    assert "index.html" in contract
    assert "lab_exclusions" in contract
    assert "Required agent loop" in contract
    assert "suggested_skills" in contract
    validator = (ROOT / "scripts" / "check_career_factory.py").read_text(encoding="utf-8")
    assert "changed_lab_content" in validator
    assert "candidate.endswith(\".html\")" in validator
    assert "new static Lab route" in validator


def test_machine_readable_career_endpoint_exists():
    endpoint = (ROOT / "ai" / "career-roadmap.json").read_text(encoding="utf-8")
    assert "dkharlanau.career.roadmap" in endpoint
    assert "site.data.career.roadmap.skills" in endpoint


def test_career_factory_inventory_is_current_and_agent_usable():
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "generate_career_factory.py"), "--check"],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    payload = json.loads((ROOT / "ai" / "career-factory.json").read_text(encoding="utf-8"))
    assert payload["schema"] == "dkharlanau.career.factory"
    assert payload["summary"]["skills"] >= 40
    assert payload["summary"]["lab_pages"] > 0
    assert payload["summary"]["decision_coverage_percent"] >= 0
    assert set(payload["track_stats"]) == {"sales", "logistics", "integration", "ai", "delivery", "leadership"}
    for item in payload["lab_inventory"]:
        assert item["state"] in {"mapped", "excluded", "needs_decision"}
        if item["state"] == "needs_decision":
            assert "suggested_skills" in item


def test_career_roadmap_ui_reads_factory_inventory():
    script = (ROOT / "assets" / "js" / "career-roadmap.js").read_text(encoding="utf-8")
    style = (ROOT / "assets" / "css" / "career-roadmap.css").read_text(encoding="utf-8")
    assert "fetch('/ai/career-factory.json'" in script
    assert "decision_coverage_percent" in script
    assert "career-factory-metrics" in style
    assert "career-factory-queue" in style
