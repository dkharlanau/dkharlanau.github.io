#!/usr/bin/env python3
"""Render a deterministic 1280x640 repository social-preview PNG from JSON."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


WIDTH = 1280
HEIGHT = 640
SCHEMA_VERSION = "1.0"
MOTIFS = {"composition", "visual", "evidence", "control", "insight"}
FONT_CANDIDATES = {
    "regular": (
        "/System/Library/Fonts/HelveticaNeue.ttc",
        "/Library/Fonts/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "C:/Windows/Fonts/arial.ttf",
    ),
    "bold": (
        "/System/Library/Fonts/HelveticaNeue.ttc",
        "/Library/Fonts/Arial Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "C:/Windows/Fonts/arialbd.ttf",
    ),
}


class PreviewError(ValueError):
    """Raised when a preview configuration cannot be rendered safely."""


def load_font(kind: str, size: int) -> ImageFont.FreeTypeFont:
    for candidate in FONT_CANDIDATES[kind]:
        path = Path(candidate)
        if path.exists():
            return ImageFont.truetype(str(path), size=size)
    raise PreviewError(f"no supported {kind} font found")


def color(value: str, field: str) -> str:
    if not isinstance(value, str) or not re.fullmatch(r"#[0-9a-fA-F]{6}", value):
        raise PreviewError(f"{field} must be a six-digit hex color")
    return value.lower()


def load_config(path: Path) -> dict:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("schema_version") != SCHEMA_VERSION:
        raise PreviewError(f"schema_version must be {SCHEMA_VERSION}")
    if payload.get("dimensions") != {"width": WIDTH, "height": HEIGHT}:
        raise PreviewError(f"dimensions must be {WIDTH}x{HEIGHT}")
    for field in ("track", "title", "subtitle", "repository", "author"):
        if not isinstance(payload.get(field), str) or not payload[field].strip():
            raise PreviewError(f"{field} must be a non-empty string")
    if payload.get("motif") not in MOTIFS:
        raise PreviewError(f"motif must be one of {sorted(MOTIFS)}")
    for field in ("background", "ink", "muted", "accent", "panel"):
        payload[field] = color(payload.get(field), field)
    if len(payload["title"]) > 56 or len(payload["subtitle"]) > 118:
        raise PreviewError("title or subtitle exceeds the social-preview copy budget")
    return payload


def round_rect(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], fill: str, outline: str, width: int = 2, radius: int = 18) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], ink: str, width: int = 4) -> None:
    draw.line((start, end), fill=ink, width=width)
    x, y = end
    draw.polygon(((x, y), (x - 13, y - 8), (x - 13, y + 8)), fill=ink)


def draw_motif(draw: ImageDraw.ImageDraw, payload: dict) -> None:
    ink = payload["ink"]
    muted = payload["muted"]
    accent = payload["accent"]
    panel = payload["panel"]
    motif = payload["motif"]
    x0, y0, x1, y1 = 790, 110, 1190, 520
    round_rect(draw, (x0, y0, x1, y1), panel, ink, width=3, radius=28)

    if motif == "composition":
        labels = ("CONTEXT", "CONSTRAINTS", "EVIDENCE")
        small = load_font("bold", 18)
        for index, label in enumerate(labels):
            top = 154 + index * 78
            round_rect(draw, (830, top, 980, top + 48), payload["background"], muted, radius=10)
            draw.text((850, top + 13), label, font=small, fill=ink)
            arrow(draw, (988, top + 24), (1032, 276), accent, width=3)
        round_rect(draw, (1028, 220, 1162, 332), accent, accent, radius=18)
        draw.text((1048, 249), "COMPOSE", font=load_font("bold", 16), fill=payload["background"])
        draw.text((1072, 280), "WHY", font=load_font("bold", 22), fill=payload["background"])
        arrow(draw, (1093, 342), (1093, 424), ink)
        draw.text((1007, 444), "BLUEPRINT + TRACE", font=small, fill=ink)

    elif motif == "visual":
        nodes = ((840, 170, "MODEL"), (1040, 170, "VIEW"), (840, 360, "MEANING"), (1040, 360, "SVG"))
        node_font = load_font("bold", 20)
        for x, y, label in nodes:
            round_rect(draw, (x, y, x + 120, y + 68), payload["background"], ink, radius=14)
            draw.text((x + 20, y + 22), label, font=node_font, fill=ink)
        arrow(draw, (960, 204), (1034, 204), accent)
        arrow(draw, (900, 244), (900, 354), accent)
        arrow(draw, (1100, 244), (1100, 354), accent)
        arrow(draw, (960, 394), (1034, 394), accent)
        draw.line((900, 463, 1100, 463), fill=muted, width=3)
        draw.text((870, 478), "SEMANTICS BEFORE LAYOUT", font=load_font("bold", 17), fill=ink)

    elif motif == "evidence":
        labels = ("REQ", "DECISION", "CHANGE", "TEST", "EVIDENCE")
        node_font = load_font("bold", 16)
        for index, label in enumerate(labels):
            y = 152 + index * 68
            x = 845 + (index % 2) * 105
            round_rect(draw, (x, y, x + 174, y + 44), payload["background"], ink if index != 2 else accent, radius=10)
            draw.text((x + 16, y + 12), label, font=node_font, fill=ink)
            if index:
                previous_y = 152 + (index - 1) * 68 + 44
                previous_x = 845 + ((index - 1) % 2) * 105 + 87
                arrow(draw, (previous_x, previous_y + 3), (x + 87, y - 5), accent, width=3)
        draw.text((835, 492), "TRACE WHAT CHANGED — AND WHY", font=load_font("bold", 17), fill=ink)

    elif motif == "control":
        center = (990, 306)
        for radius, outline, width in ((155, muted, 2), (116, ink, 3), (76, accent, 5)):
            draw.ellipse((center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius), outline=outline, width=width)
        draw.text((947, 278), "BOUND", font=load_font("bold", 22), fill=ink)
        draw.text((930, 310), "AUTONOMY", font=load_font("bold", 22), fill=ink)
        for text_value, position in (("EVIDENCE", (835, 135)), ("POLICY", (1070, 166)), ("VERIFY", (1080, 438)), ("CAPABILITY", (818, 446))):
            draw.text(position, text_value, font=load_font("bold", 16), fill=ink)

    elif motif == "insight":
        steps = ("SOURCE", "MAP", "DELTA", "REVIEW", "INSIGHT")
        step_font = load_font("bold", 16)
        for index, label in enumerate(steps):
            left = 820 + index * 50
            top = 170 + index * 60
            round_rect(draw, (left, top, left + 150, top + 52), payload["background"], accent if index == 4 else ink, radius=12)
            draw.text((left + 18, top + 16), label, font=step_font, fill=ink)
            if index < len(steps) - 1:
                arrow(draw, (left + 75, top + 58), (left + 143, top + 105), accent, width=3)
        draw.text((855, 475), "PROVENANCE STAYS VISIBLE", font=load_font("bold", 17), fill=ink)


def render(payload: dict) -> Image.Image:
    image = Image.new("RGB", (WIDTH, HEIGHT), payload["background"])
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, 22, HEIGHT), fill=payload["accent"])
    draw.text((78, 62), "DKHARLANAU · OPEN-SOURCE SYSTEMS", font=load_font("bold", 20), fill=payload["muted"])
    draw.text((78, 109), payload["track"].upper(), font=load_font("bold", 18), fill=payload["accent"])

    title_font = load_font("bold", 62)
    words = payload["title"].split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if draw.textbbox((0, 0), candidate, font=title_font)[2] <= 620:
            current = candidate
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    if len(lines) > 3:
        raise PreviewError("title does not fit in three lines")
    y = 154
    for line in lines:
        draw.text((78, y), line, font=title_font, fill=payload["ink"])
        y += 70

    subtitle_font = load_font("regular", 24)
    subtitle_words = payload["subtitle"].split()
    subtitle_lines: list[str] = []
    current = ""
    for word in subtitle_words:
        candidate = f"{current} {word}".strip()
        if draw.textbbox((0, 0), candidate, font=subtitle_font)[2] <= 620:
            current = candidate
        else:
            subtitle_lines.append(current)
            current = word
    if current:
        subtitle_lines.append(current)
    for line in subtitle_lines[:3]:
        draw.text((80, y + 16), line, font=subtitle_font, fill=payload["muted"])
        y += 34

    draw.line((78, 548, 724, 548), fill=payload["ink"], width=2)
    draw.text((78, 568), payload["author"], font=load_font("bold", 18), fill=payload["ink"])
    repository = f"github.com/dkharlanau/{payload['repository']}"
    draw.text((340, 568), repository, font=load_font("regular", 18), fill=payload["muted"])
    draw_motif(draw, payload)
    return image


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("config", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    payload = load_config(args.config)
    output = args.output or args.config.with_suffix(".png")
    image = render(payload)
    output.parent.mkdir(parents=True, exist_ok=True)
    if args.check:
        if not output.exists():
            raise PreviewError(f"missing output: {output}")
        import io

        buffer = io.BytesIO()
        image.save(buffer, format="PNG", optimize=True)
        if output.read_bytes() != buffer.getvalue():
            raise PreviewError(f"stale output: {output}")
    else:
        image.save(output, format="PNG", optimize=True)
    digest = hashlib.sha256(output.read_bytes()).hexdigest()
    size = output.stat().st_size
    if size >= 1_000_000:
        raise PreviewError(f"output exceeds GitHub's 1 MB recommendation: {size} bytes")
    print(f"social preview {'current' if args.check else 'rendered'}: {output} ({size} bytes, sha256:{digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
