"""Regression contracts for source fixes found by the real production build."""
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
DESIGN_INPUTS = (
    "docs/design/kimi-code-prompt-martenweave-style.md",
    "docs/design/martenweave-style-adoption-brief.md",
)
SIGNAL = "_radar/2026-10-06-harness-engineering-software-factory-dru-knox.md"
TARGET = "/radar/harness-engineering-maintainability-human-judgment/"


def test_design_working_inputs_are_retained_but_excluded():
    config = yaml.safe_load((ROOT / "_config.yml").read_text())
    for path in DESIGN_INPUTS:
        assert (ROOT / path).is_file()
        assert path in config["exclude"]


def test_related_signal_uses_collection_slug_route():
    config = yaml.safe_load((ROOT / "_config.yml").read_text())
    assert config["collections"]["radar"]["permalink"] == "/radar/:slug/"
    assert (ROOT / "_radar/2026-09-17-harness-engineering-maintainability-human-judgment.md").is_file()
    source = (ROOT / SIGNAL).read_text()
    assert f"]({TARGET})" in source
    assert "/radar/2026-09-17-harness-engineering-maintainability-human-judgment/" not in source


def test_rendered_publication_boundary():
    site = ROOT / "_site"
    if not site.is_dir():
        pytest.skip("requires real Jekyll build")
    for path in DESIGN_INPUTS:
        assert not (site / path).exists()
        assert not (site / path.removesuffix(".md")).exists()
    target = site / TARGET.strip("/") / "index.html"
    assert target.is_file()
    signal = site / "radar/harness-engineering-software-factory-dru-knox/index.html"
    assert f'href="{TARGET}"' in signal.read_text()
