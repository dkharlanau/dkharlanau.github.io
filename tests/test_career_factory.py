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
    assert "/assets/js/career-roadmap.js" in page
    assert "Delivery & Operations" in ROADMAP.read_text(encoding="utf-8")
    assert "Career Factory" in page


def test_career_factory_ci_enforces_new_lab_impact():
    workflow = (ROOT / ".github" / "workflows" / "career-factory.yml").read_text(encoding="utf-8")
    assert "Career Factory" in workflow
    assert "--changed-from origin/${{ github.base_ref }}" in workflow
    assert "labs/**" in workflow
    contract = (ROOT / "labs" / "AGENTS.md").read_text(encoding="utf-8")
    assert "career_impact: mapped" in contract
    assert "career_impact: none" in contract
    assert "career_skills" in contract


def test_machine_readable_career_endpoint_exists():
    endpoint = (ROOT / "ai" / "career-roadmap.json").read_text(encoding="utf-8")
    assert "dkharlanau.career.roadmap" in endpoint
    assert "site.data.career.roadmap.skills" in endpoint
