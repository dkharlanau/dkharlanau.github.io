from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
WORKFLOW_DOC = REPO_ROOT / "docs" / "atlas" / "ATLAS_SIGNAL_PR_WORKFLOW.md"
MAIN_WORKFLOW_DOC = REPO_ROOT / "docs" / "atlas" / "SIGNAL_DRIVEN_ATLAS_UPDATES.md"
PR_TEMPLATE = REPO_ROOT / ".github" / "PULL_REQUEST_TEMPLATE" / "atlas-signal-update.md"


def test_pr_workflow_doc_exists_and_defines_review_location():
    content = WORKFLOW_DOC.read_text(encoding="utf-8")
    assert "ai/atlas-proposals/review/" in content
    assert "ai/atlas-proposals/examples/" in content
    assert "Scratch proposals" in content
    assert "must not be committed" in content


def test_pr_workflow_doc_defines_approval_and_application_boundary():
    content = WORKFLOW_DOC.read_text(encoding="utf-8")
    for token in [
        "human reviewer",
        "Tool output alone is not approval",
        "Existing page update",
        "New page candidate",
        "robots: noindex,follow",
        "No direct pushes to `main`",
        "No unreviewed page creation",
    ]:
        assert token in content


def test_pr_workflow_doc_lists_validation_commands():
    content = WORKFLOW_DOC.read_text(encoding="utf-8")
    for command in [
        "tests/test_atlas_update_proposals.py tests/test_atlas_proposal_quality.py",
        "python3 scripts/generate_atlas_artifacts.py --check",
        "python3 scripts/check_public_repo.py",
        "bundle exec jekyll build",
        "python3 scripts/check_links.py _site",
        "python3 scripts/check_seo.py _site",
    ]:
        assert command in content


def test_atlas_signal_pr_template_contains_required_sections():
    content = PR_TEMPLATE.read_text(encoding="utf-8")
    for section in [
        "Source Signal(s)",
        "Target Atlas Page(s)",
        "Files Changed",
        "Evidence Summary",
        "Why This Belongs Here",
        "Quality Gates Passed",
        "Validation Commands",
        "Safety Note",
    ]:
        assert f"## {section}" in content


def test_atlas_signal_pr_template_contains_safety_checklist():
    content = PR_TEMPLATE.read_text(encoding="utf-8")
    for token in [
        "Source body opened",
        "At least two concrete facts present",
        "Duplicate-page check passed",
        "Generic commentary check passed",
        "Private-path/public-safety check passed",
        "No direct push to `main`",
        "No unreviewed page creation",
        "No automatic publishing",
    ]:
        assert token in content


def test_main_workflow_links_pr_workflow_doc():
    content = MAIN_WORKFLOW_DOC.read_text(encoding="utf-8")
    assert "docs/atlas/ATLAS_SIGNAL_PR_WORKFLOW.md" in content
