#!/usr/bin/env python3
"""Tests for generate_radar_og_image.py."""

import pytest
import sys
from pathlib import Path

# Ensure the script under test is importable
SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

import generate_radar_og_image as gen


SAMPLE_FRONTMATTER = {
    "layout": "note",
    "title": "S/4HANA Compatibility Packs — Final Transition",
    "date": "2026-05-26",
    "source": "SAP S/4HANA What's New",
    "source_url": "https://help.sap.com/docs/SAP_S4HANA_CLOUD",
    "confidence": "high",
    "topics": ["sap_s4hana", "sap_compatibility_packs", "sap_upgrade"],
}

SAMPLE_MARKDOWN = f"""---
layout: note
title: "{SAMPLE_FRONTMATTER['title']}"
date: {SAMPLE_FRONTMATTER['date']}
source: "{SAMPLE_FRONTMATTER['source']}"
source_url: "{SAMPLE_FRONTMATTER['source_url']}"
confidence: {SAMPLE_FRONTMATTER['confidence']}
topics:
  - sap_s4hana
  - sap_compatibility_packs
  - sap_upgrade
---

SAP announces the final transition timeline.
"""


def test_parse_frontmatter_extracts_yaml():
    data = gen.parse_frontmatter(SAMPLE_MARKDOWN)
    assert data["title"] == "S/4HANA Compatibility Packs — Final Transition"
    assert data["confidence"] == "high"
    assert data["topics"] == ["sap_s4hana", "sap_compatibility_packs", "sap_upgrade"]


def test_parse_frontmatter_empty_for_plain_md():
    assert gen.parse_frontmatter("# No frontmatter\n") == {}


def test_fill_template_replaces_all_placeholders():
    template = "{{TITLE}} | {{DATE}} | {{SOURCE}} | {{CONFIDENCE}} | {{CATEGORY}} | {{CATEGORY_COLOR}} | {{CONFIDENCE_COLOR}}"
    result = gen.fill_template(template, SAMPLE_FRONTMATTER)
    assert "S/4HANA Compatibility Packs — Final Transition" in result
    assert "2026-05-26" in result
    assert "SAP S/4HANA What's New" in result
    assert "HIGH" in result
    assert "#SAP" in result
    assert "#2563eb" in result  # blue-600 for sap topics
    assert "#22c55e" in result  # green-500 for high confidence


def test_fill_template_escapes_html():
    bad = {**SAMPLE_FRONTMATTER, "title": "<script>alert(1)</script>"}
    result = gen.fill_template("{{TITLE}}", bad)
    assert "<script>" not in result
    assert "&lt;script&gt;" in result


def test_fill_template_missing_title_uses_default():
    result = gen.fill_template("{{TITLE}}", {})
    assert "Untitled Radar" in result


def test_pick_category_color_from_topics():
    assert gen.pick_category_color(["sap_s4hana"], None) == "#2563eb"
    assert gen.pick_category_color(["ai_tooling"], None) == "#10b981"


def test_pick_category_color_fallback():
    assert gen.pick_category_color(["unknown"], None) == "#64748b"
    assert gen.pick_category_color(None, None) == "#64748b"


def test_pick_confidence_color():
    assert gen.pick_confidence_color("high") == "#22c55e"
    assert gen.pick_confidence_color("medium") == "#f59e0b"
    assert gen.pick_confidence_color("low") == "#ef4444"
    assert gen.pick_confidence_color(None) == "#94a3b8"


def test_format_category_label_from_topics():
    assert gen.format_category_label(["sap_s4hana", "sap_upgrade"], None) == "#SAP"
    assert gen.format_category_label(["ai_ml"], None) == "#AI"


def test_format_category_label_from_tags():
    assert gen.format_category_label(None, ["signal"]) == "#SIGNAL"


def test_format_category_label_fallback():
    assert gen.format_category_label(None, None) == "#RADAR"


def test_generate_radar_og_image(tmp_path: Path):
    note = tmp_path / "2026-05-26-test.md"
    note.write_text(SAMPLE_MARKDOWN, encoding="utf-8")
    tmpl = tmp_path / "template.html"
    tmpl.write_text("{{TITLE}}|{{DATE}}|{{SOURCE}}|{{CONFIDENCE}}|{{CATEGORY}}|{{CATEGORY_COLOR}}|{{CONFIDENCE_COLOR}}", encoding="utf-8")
    out = tmp_path / "out.html"

    result = gen.generate_radar_og_image(str(note), str(out), str(tmpl))
    assert result == str(out)
    content = out.read_text(encoding="utf-8")
    assert "S/4HANA Compatibility Packs — Final Transition" in content
    assert "2026-05-26" in content


def test_generate_radar_og_image_auto_output(tmp_path: Path):
    note = tmp_path / "2026-05-26-test.md"
    note.write_text(SAMPLE_MARKDOWN, encoding="utf-8")
    tmpl = tmp_path / "template.html"
    tmpl.write_text("{{TITLE}}", encoding="utf-8")

    result = gen.generate_radar_og_image(str(note), None, str(tmpl))
    assert Path(result).exists()
    assert Path(result).name == "s4hana-compatibility-packs-final-transition-og.html"


def test_generate_radar_og_image_missing_note_raises():
    with pytest.raises(FileNotFoundError):
        gen.generate_radar_og_image("/does/not/exist.md")


def test_generate_radar_og_image_no_frontmatter_raises(tmp_path: Path):
    bad = tmp_path / "bad.md"
    bad.write_text("# No frontmatter\n", encoding="utf-8")
    tmpl = tmp_path / "template.html"
    tmpl.write_text("{{TITLE}}", encoding="utf-8")
    with pytest.raises(ValueError, match="No valid YAML frontmatter"):
        gen.generate_radar_og_image(str(bad), None, str(tmpl))


def test_main_cli(tmp_path: Path, capsys):
    note = tmp_path / "radar.md"
    note.write_text(SAMPLE_MARKDOWN, encoding="utf-8")
    tmpl = tmp_path / "template.html"
    tmpl.write_text("{{TITLE}}|{{DATE}}|{{CONFIDENCE}}|{{CATEGORY}}", encoding="utf-8")
    out = tmp_path / "out.html"

    rc = gen.main([str(note), "-o", str(out), "-t", str(tmpl)])
    assert rc == 0
    captured = capsys.readouterr()
    assert str(out) in captured.out


def test_main_cli_dry_run(tmp_path: Path, capsys):
    note = tmp_path / "radar.md"
    note.write_text(SAMPLE_MARKDOWN, encoding="utf-8")
    tmpl = tmp_path / "template.html"
    tmpl.write_text("{{TITLE}}|{{DATE}}|{{CONFIDENCE}}|{{CATEGORY}}", encoding="utf-8")

    rc = gen.main([str(note), "-t", str(tmpl), "--dry-run"])
    assert rc == 0
    captured = capsys.readouterr()
    assert "S/4HANA Compatibility Packs" in captured.out
    assert "HIGH" in captured.out
