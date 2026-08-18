from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    assert text.startswith("---\n"), f"{path} has no front matter"
    end = text.find("\n---\n", 4)
    assert end != -1, f"{path} has invalid front matter"
    data = yaml.safe_load(text[4:end]) or {}
    assert isinstance(data, dict)
    return data


def test_public_career_surfaces_are_reviewed_and_indexable():
    paths = [
        ROOT / "labs" / "interview-readiness" / "index.md",
        ROOT / "labs" / "interview-readiness" / "roadmap" / "index.md",
    ]
    for path in paths:
        data = frontmatter(path)
        assert data.get("status") == "reviewed"
        assert data.get("verified") is True
        assert "noindex" not in str(data.get("robots", "")).lower()
        assert data.get("sitemap") is True
        assert data.get("search_intent")
        assert (data.get("structured_data") or {}).get("type") == "TechArticle"
        assert data.get("primary_topic")
        assert data.get("ai_sidecar")
        assert len(data.get("semantic_links") or []) >= 2


def test_career_roadmap_connects_labs_skill_hub_and_assessment():
    text = (ROOT / "labs" / "interview-readiness" / "roadmap" / "index.md").read_text(encoding="utf-8")
    assert "/labs/assessment/" in text
    assert "/skill-hub/architecture/" in text
    assert "/skill-hub/integration-architecture/" in text
    assert "/skill-hub/business-analysis/" in text
    assert "/skill-hub/decision-validation/" in text
    assert "/skill-hub/problem-solving-operations/" in text
    assert "/skill-hub/ai-assisted-analysis/" in text
    assert "/ai/career-roadmap.json" in text
    assert "/ai/career-factory.json" in text


def test_career_sidecars_exist():
    assert (ROOT / "ai" / "pages" / "labs--interview-readiness.json").exists()
    assert (ROOT / "ai" / "pages" / "labs--interview-readiness--roadmap.json").exists()


def test_primary_navigation_exposes_career_route():
    text = (ROOT / "_includes" / "header.html").read_text(encoding="utf-8")
    assert 'href="/labs/interview-readiness/"' in text
    assert ">Career</a>" in text
    assert "career_nav_active" in text
    assert "/labs/assessment/" in text


def test_ci_enforces_career_factory_contract_and_inventory():
    text = (ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
    assert "scripts/check_career_factory.py --changed-from origin/main" in text
    assert "scripts/generate_career_factory.py --check" in text
