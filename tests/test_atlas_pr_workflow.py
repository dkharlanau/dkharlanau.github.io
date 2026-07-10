from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PR_TEMPLATE = REPO_ROOT / ".github" / "PULL_REQUEST_TEMPLATE" / "atlas-signal-update.md"


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
