import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "config" / "ui-components.json"


def load_registry():
    return json.loads(REGISTRY.read_text(encoding="utf-8"))


def test_ui_component_validator_passes_repository_contract():
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate_ui_components.py")],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "UI component registry passed" in result.stdout


def test_core_reading_components_are_registered():
    data = load_registry()
    ids = {component["id"] for component in data["components"]}
    assert {
        "study-table",
        "page-faq",
        "research-section-intro",
        "boundary-note",
        "route-list",
        "source-register",
        "comparison-group",
        "determination-detail",
        "context-links",
    } <= ids


def test_agent_entry_points_reference_ui_contract():
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    for path in (
        "docs/editorial-design-system.md",
        "docs/ui-component-catalog.md",
        "config/ui-components.json",
        "docs/ui-agent-workflow.md",
        "docs/site-content-design-contract.md",
    ):
        assert path in agents
        assert (ROOT / path).is_file()


def test_study_table_is_used_on_master_data_reference():
    page = (ROOT / "labs" / "enterprise-context" / "master-data" / "index.html").read_text(
        encoding="utf-8"
    )
    assert 'class="table-scroll study-table"' in page
    assert 'class="study-table__table"' in page


def test_faq_uses_native_disclosure_and_readable_editorial_label():
    include = (ROOT / "_includes" / "page-faq.html").read_text(encoding="utf-8")
    css = (ROOT / "assets" / "page-faq.css").read_text(encoding="utf-8")
    assert "<details" in include
    assert "<summary>" in include
    assert ".page-faq__eyebrow" in css
    assert "text-transform: none" in css


def test_site_share_is_self_contained_and_centered():
    include = (ROOT / "_includes" / "site-share-widget.html").read_text(encoding="utf-8")
    css = (ROOT / "assets" / "css" / "layout.css").read_text(encoding="utf-8")
    layout = (ROOT / "_layouts" / "default.html").read_text(encoding="utf-8")

    assert 'class="site-share__content"' in include
    assert "{% include site-share-widget.html %}" in layout

    share_block = css.split(".site-share {", 1)[1].split("}", 1)[0]
    assert "display: grid;" in share_block
    assert "width: min(calc(100% - 2rem), var(--container-wide));" in share_block
    assert "margin: var(--space-9) auto 0;" in share_block
    assert "background: linear-gradient" in share_block
    assert "@media (max-width: 860px)" in css
