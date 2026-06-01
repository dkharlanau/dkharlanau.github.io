#!/usr/bin/env python3
"""Generate OG image HTML from a radar note's frontmatter.

from __future__ import annotations

Reads a radar post (Markdown with YAML frontmatter), fills the HTML template,
and writes the result to an output path. No image generation — just template filling.
"""

import argparse
import os
import re
import sys
from pathlib import Path
from typing import Any, List, Optional

import yaml


# ---------------------------------------------------------------------------
# Color maps
# ---------------------------------------------------------------------------

CATEGORY_COLORS: dict[str, str] = {
    "sap": "#2563eb",           # blue-600
    "ai": "#10b981",            # emerald-500
    "signal": "#f59e0b",        # amber-500
    "knowledge": "#8b5cf6",     # violet-500
    "news": "#ef4444",          # red-500
    "default": "#64748b",       # slate-500
}

CONFIDENCE_COLORS: dict[str, str] = {
    "high": "#22c55e",          # green-500
    "medium": "#f59e0b",        # amber-500
    "low": "#ef4444",           # red-500
    "default": "#94a3b8",       # slate-400
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _resolve_repo_root() -> Path:
    """Resolve the repository root from the script location."""
    script_dir = Path(__file__).resolve().parent
    # repo root is two levels up: professional-radar/scripts/ -> repo/
    return script_dir.parent.parent


def _default_template_path() -> Path:
    return _resolve_repo_root() / "professional-radar" / "templates" / "radar_og_image_template.html"


def _slugify(text: str) -> str:
    """Simple slug for filenames."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[-\s]+", "-", text)
    return text[:80]


def parse_frontmatter(markdown_text: str) -> dict:
    """Extract YAML frontmatter from a Markdown file."""
    if not markdown_text.startswith("---"):
        return {}
    parts = markdown_text.split("---", 2)
    if len(parts) < 3:
        return {}
    try:
        return yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        return {}


def pick_category_color(topics: Optional[List[str]], tags: Optional[List[str]]) -> str:
    """Pick a category color based on topics or tags."""
    keywords = [t.lower() for t in (topics or tags or [])]
    for kw in keywords:
        for key, color in CATEGORY_COLORS.items():
            if key != "default" and key in kw:
                return color
    return CATEGORY_COLORS["default"]


def pick_confidence_color(confidence: Optional[str]) -> str:
    """Pick a confidence badge color."""
    if not confidence:
        return CONFIDENCE_COLORS["default"]
    return CONFIDENCE_COLORS.get(confidence.lower(), CONFIDENCE_COLORS["default"])


def format_category_label(topics: Optional[List[str]], tags: Optional[List[str]]) -> str:
    """Derive a short category hashtag from topics or tags."""
    keywords = [t.lower() for t in (topics or tags or [])]
    for kw in keywords:
        if "sap" in kw:
            return "#SAP"
        if "ai" in kw or "ml" in kw:
            return "#AI"
    if tags:
        return f"#{tags[0].upper()}"
    if topics:
        return f"#{topics[0].upper()}"
    return "#RADAR"


def escape_html(text: str) -> str:
    """Minimal HTML escape for safe interpolation."""
    return (
        text.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
    )


def fill_template(template: str, frontmatter: dict[str, Any]) -> str:
    """Substitute template placeholders with frontmatter values."""
    title = escape_html(str(frontmatter.get("title", "Untitled Radar")))
    date = str(frontmatter.get("date", ""))
    source = escape_html(str(frontmatter.get("source", "Professional Radar")))
    confidence = str(frontmatter.get("confidence", "default")).lower()
    topics = frontmatter.get("topics", [])
    tags = frontmatter.get("tags", [])

    category = format_category_label(topics, tags)
    category_color = pick_category_color(topics, tags)
    confidence_color = pick_confidence_color(confidence)

    return (
        template
        .replace("{{TITLE}}", title)
        .replace("{{DATE}}", date)
        .replace("{{SOURCE}}", source)
        .replace("{{CONFIDENCE}}", confidence.upper() if confidence else "UNKNOWN")
        .replace("{{CATEGORY}}", category)
        .replace("{{CATEGORY_COLOR}}", category_color)
        .replace("{{CONFIDENCE_COLOR}}", confidence_color)
    )


def generate_radar_og_image(
    radar_note_path: str,
    output_path: Optional[str] = None,
    template_path: Optional[str] = None,
) -> str:
    """Read a radar note, fill the template, write the output HTML.

    Returns the absolute path of the written file.
    """
    note_path = Path(radar_note_path).expanduser().resolve()
    if not note_path.exists():
        raise FileNotFoundError(f"Radar note not found: {note_path}")

    tmpl = Path(template_path).expanduser().resolve() if template_path else _default_template_path()
    if not tmpl.exists():
        raise FileNotFoundError(f"Template not found: {tmpl}")

    markdown_text = note_path.read_text(encoding="utf-8")
    frontmatter = parse_frontmatter(markdown_text)
    if not frontmatter:
        raise ValueError(f"No valid YAML frontmatter found in {note_path}")

    template = tmpl.read_text(encoding="utf-8")
    filled = fill_template(template, frontmatter)

    if output_path:
        out = Path(output_path).expanduser().resolve()
    else:
        slug = _slugify(str(frontmatter.get("title", "radar-og")))
        out = note_path.parent / f"{slug}-og.html"

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(filled, encoding="utf-8")
    return str(out)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Generate radar OG-image HTML from frontmatter")
    parser.add_argument("radar_note", help="Path to the radar markdown note")
    parser.add_argument("-o", "--output", help="Output HTML file path (default: auto-generated)")
    parser.add_argument("-t", "--template", help="Path to custom HTML template")
    parser.add_argument("--dry-run", action="store_true", help="Print filled HTML to stdout instead of writing")
    args = parser.parse_args(argv)

    try:
        result = generate_radar_og_image(args.radar_note, args.output, args.template)
    except (FileNotFoundError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if args.dry_run:
        print(Path(result).read_text(encoding="utf-8"))
        # remove the auto-generated file in dry-run mode
        if not args.output:
            Path(result).unlink()
    else:
        print(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
