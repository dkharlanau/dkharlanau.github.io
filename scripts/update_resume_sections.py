#!/usr/bin/env python3
"""Refresh selected resume sections using a LinkedIn data export."""
from __future__ import annotations

import argparse
from collections import OrderedDict
from pathlib import Path
from typing import Dict, Iterable, List, Mapping, Sequence, Tuple

from li2resume import (
    dump_yaml,
    format_date,
    load_csv,
    normalise_url,
    parse_date,
    pick,
    split_highlights,
)

DEFAULT_SECTIONS: Tuple[str, ...] = ("skills", "certifications", "projects", "courses")


def extract_skills(input_dir: Path, limit: int = 40) -> List[str]:
    rows = load_csv(input_dir, "Skills.csv").rows
    seen: OrderedDict[str, None] = OrderedDict()
    for row in rows:
        name = pick(row, ["name", "skill", "title"])
        if not name:
            continue
        if name not in seen:
            seen[name] = None
    return list(seen.keys())[:limit]


def extract_certifications(input_dir: Path, limit: int = 25) -> List[Dict[str, object]]:
    rows = load_csv(input_dir, "Certifications.csv").rows
    certs: List[Dict[str, object]] = []
    for row in rows:
        name = pick(row, ["name", "certification", "title"])
        issuer = pick(row, ["authority", "issuer"])
        if not name:
            continue
        issued = format_date(parse_date(pick(row, ["started on", "issue date", "date"])) )
        entry: Dict[str, object] = {
            "name": name,
        }
        if issuer:
            entry["issuer"] = issuer
        if issued:
            entry["issued"] = issued
        url = normalise_url(pick(row, ["url", "link"]))
        if url:
            entry["url"] = url
        certs.append(entry)
    certs.sort(key=lambda item: item.get("issued") or "0000", reverse=True)
    return certs[:limit]


def extract_projects(input_dir: Path, limit: int = 12) -> List[Dict[str, object]]:
    rows = load_csv(input_dir, "Projects.csv").rows
    projects: List[Dict[str, object]] = []
    for row in rows:
        title = pick(row, ["title", "name"])
        if not title:
            continue
        summary, highlights = split_highlights(pick(row, ["description", "summary"]), limit=4)
        entry: Dict[str, object] = {
            "title": title,
        }
        start = format_date(parse_date(pick(row, ["started on", "start date"])))
        end = format_date(parse_date(pick(row, ["finished on", "end date"])))
        if summary:
            entry["summary"] = summary
        if highlights:
            entry["highlights"] = highlights
        if start:
            entry["start"] = start
        if end:
            entry["end"] = end
        url = normalise_url(pick(row, ["url", "link"]))
        if url:
            entry["url"] = url
        projects.append(entry)
    projects.sort(key=lambda item: (item.get("start") or "0000", item.get("end") or "9999"), reverse=True)
    return projects[:limit]


def extract_courses(input_dir: Path, limit: int = 40) -> List[Dict[str, object]]:
    rows = load_csv(input_dir, "Courses.csv").rows
    seen: OrderedDict[str, Dict[str, object]] = OrderedDict()
    for row in rows:
        name = pick(row, ["name", "course", "title"])
        if not name:
            continue
        key = name
        if key in seen:
            continue
        entry: Dict[str, object] = {"name": name}
        code = pick(row, ["number", "code", "id"])
        if code:
            entry["number"] = code
        seen[key] = entry
    return list(seen.values())[:limit]


def replace_section_block(source: str, section: str, replacement: str) -> str:
    replacement = replacement.strip("\n")
    replacement_lines = replacement.split("\n") if replacement else [f"{section}:"]
    lines = source.split("\n")
    header = f"{section}:"
    start = None
    for idx, line in enumerate(lines):
        if line == header:
            start = idx
            break
    if start is None:
        if lines and lines[-1] != "":
            lines.append("")
        lines.extend(replacement_lines)
        return "\n".join(lines).rstrip("\n") + "\n"
    end = start + 1
    while end < len(lines):
        line = lines[end]
        stripped = line.strip()
        if stripped == "":
            end += 1
            continue
        if line.startswith(" ") or line.startswith("\t") or stripped.startswith("-"):
            end += 1
            continue
        if stripped.startswith("#"):
            break
        if ":" in line:
            break
        end += 1
    had_separator = False
    check_idx = end - 1
    while check_idx > start and lines[check_idx].strip() == "":
        had_separator = True
        check_idx -= 1
    while end > start + 1 and lines[end - 1].strip() == "":
        end -= 1
    new_lines = lines[:start] + replacement_lines
    if had_separator:
        new_lines.append("")
    new_lines.extend(lines[end:])
    return "\n".join(new_lines).rstrip("\n") + "\n"


def render_section(name: str, data: object) -> str:
    return dump_yaml({name: data})


def split_front_matter(text: str) -> Tuple[str, str]:
    if not text.startswith("---"):
        return "", text
    lines = text.split("\n")
    front: List[str] = []
    end_idx = None
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            end_idx = idx
            break
        front.append(lines[idx])
    if end_idx is None:
        return text, ""
    body = "\n".join(lines[end_idx + 1:])
    fm = "\n".join(["---"] + front + ["---"])
    if body and not body.endswith("\n"):
        body += "\n"
    return fm + "\n", body


def join_front_matter(front: str, body: str) -> str:
    base = front or "---\nlayout: null\npermalink: /ai/resume.yml\nsitemap: true\n---\n"
    if not base.endswith("\n"):
        base += "\n"
    return base + body.lstrip("\n")


def build_updates(input_dir: Path, sections: Sequence[str]) -> Dict[str, object]:
    updates: Dict[str, object] = {}
    for section in sections:
        key = section.lower()
        if key == "skills":
            updates["skills"] = extract_skills(input_dir)
        elif key == "certifications":
            updates["certifications"] = extract_certifications(input_dir)
        elif key == "projects":
            updates["projects"] = extract_projects(input_dir)
        elif key == "courses":
            updates["courses"] = extract_courses(input_dir)
        else:
            raise ValueError(f"Unsupported section '{section}'")
    return updates


def apply_updates(resume_path: Path, updates: Mapping[str, object]) -> str:
    original = resume_path.read_text(encoding="utf-8")
    updated = original
    for name, data in updates.items():
        block = render_section(name, data)
        updated = replace_section_block(updated, name, block)
    if updated != original:
        resume_path.write_text(updated, encoding="utf-8")
    return updated


def sync_ai_resume(ai_path: Path, resume_body: str) -> None:
    if ai_path.exists():
        front, _ = split_front_matter(ai_path.read_text(encoding="utf-8"))
    else:
        front = ""
    ai_content = join_front_matter(front, resume_body)
    ai_path.write_text(ai_content, encoding="utf-8")


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Update resume sections from LinkedIn export")
    parser.add_argument("--input", default="Linkedin.zip", help="LinkedIn export directory")
    parser.add_argument("--resume", default="_data/resume.yml", help="Resume YAML path")
    parser.add_argument("--ai-resume", default="ai/resume.yml", help="AI resume YAML path to sync")
    parser.add_argument(
        "--sections",
        nargs="+",
        default=list(DEFAULT_SECTIONS),
        help="Resume sections to refresh",
    )
    return parser.parse_args(argv)


def resolve_input_path(path_str: str) -> Path:
    path = Path(path_str).expanduser()
    if path.exists():
        return path
    alt = path / "Linkedin.zip"
    if alt.exists():
        return alt
    raise SystemExit(f"Input directory '{path_str}' not found")


def main(argv: Sequence[str] | None = None) -> None:
    args = parse_args(argv)

    input_dir = resolve_input_path(args.input)
    if not input_dir.is_dir():
        raise SystemExit(f"Expected '{input_dir}' to be a directory of CSV files")

    resume_path = Path(args.resume)
    ai_path = Path(args.ai_resume)

    updates = build_updates(input_dir, args.sections)
    new_body = apply_updates(resume_path, updates)
    sync_ai_resume(ai_path, new_body)

    for name, data in updates.items():
        count = len(data) if isinstance(data, Iterable) and not isinstance(data, (str, bytes, dict)) else 1
        print(f"Updated {name}: {count}")


if __name__ == "__main__":
    main()
