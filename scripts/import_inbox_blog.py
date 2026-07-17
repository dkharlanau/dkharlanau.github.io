#!/usr/bin/env python3
"""Create canonical Jekyll blog review candidates from inbox inputs."""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INBOX, OUTPUT = ROOT / "inbox", ROOT / "_blog"
REPORT = ROOT / "docs/blog-migration-2026-07-17.md"
DATE = "2026-07-17"

def category(n: int) -> str:
    if n <= 10: return "SAP AMS operations"
    if n <= 19: return "SAP automation"
    if n <= 22: return "SAP commercial processes"
    if n <= 34: return "SAP integration architecture"
    if n <= 38: return "SAP logistics"
    if n in {39, 40, 41, 42, 45, 49}: return "SAP solution architecture"
    if n in {43, 44, 47, 48}: return "SAP industry solutions"
    return "SAP data and AI"

def tags(title: str, cat: str) -> list[str]:
    low, out = title.lower(), [cat.lower().replace("sap ", "sap-").replace(" ", "-")]
    rules = {
        "sap-ams": ("ams", "support", "incident", "sla", "knowledge"),
        "automation": ("automate", "automation"),
        "ai-operations": ("ai", "agent", "workflow"),
        "integration": ("integration", "interface", "api", "idoc", "event", "mapping"),
        "master-data": ("master data", "distribution"),
        "sap-sd": ("sales", "pricing", "billing", "atp", "brim"),
        "supply-chain": ("logistics", "inventory", "warehouse", "transportation", "mrp"),
        "sap-architecture": ("architecture", "clean core", "rise", "landscape", "cloud"),
        "retail": ("retail", "car"), "data-platforms": ("business data cloud", "data products", "bw"),
        "quality-management": ("quality management", "inspection", "supplier quality"), "automotive": ("automotive",),
    }
    for tag, needles in rules.items():
        if any(needle in low for needle in needles) and tag not in out: out.append(tag)
    return out[:5]

def description(body: str, title: str) -> str:
    body = re.sub(r"^# .*?$|^#{2,} .*?$", "", body, flags=re.M)
    body = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", body)
    parts = [re.sub(r"\s+", " ", p).strip(" -") for p in body.split("\n\n")]
    value = next((p for p in parts if len(p) >= 80 and not p.startswith(("*Reviewed", "Sources"))), f"A practical SAP article about {title.lower()}.")
    sentences, selected = re.split(r"(?<=[.!?])\s+", value), []
    for sentence in sentences:
        if len(" ".join(selected + [sentence])) > 155: break
        selected.append(sentence)
    return " ".join(selected) or value[:150].rsplit(" ", 1)[0] + "."

def heading_id(value: str) -> str:
    value = re.sub(r"[`*_]", "", value).lower()
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", value)).strip("-")

def list_yaml(values: list[str]) -> str:
    return "\n".join(f"  - {value}" for value in values)

def main() -> int:
    manifest = json.loads((INBOX / "manifest.json").read_text(encoding="utf-8"))
    rows = []
    for item in manifest:
        source = INBOX / item["filename"]
        raw = source.read_text(encoding="utf-8")
        match = re.match(r"^#\s+(.+?)\s*\n", raw)
        if not match: raise ValueError(f"{source.name}: leading H1 is required")
        slug = re.sub(r"^\d{3}-", "", source.stem)
        title, cat = match.group(1), category(item["sequence"])
        rows.append({**item, "title": title, "slug": slug, "category": cat, "tags": tags(title, cat), "body": raw[match.end():].lstrip(), "description": description(raw, title)})
    if len(rows) != 49 or len({r["slug"] for r in rows}) != 49: raise ValueError("inbox completeness or slug uniqueness check failed")
    for i, row in enumerate(rows):
        related = [r for r in rows if r["category"] == row["category"] and r is not row][:2]
        if len(related) < 2: related += [r for r in rows if r is not row and r not in related][:2-len(related)]
        previous, following = (rows[i-1] if i else None), (rows[i+1] if i + 1 < len(rows) else None)
        links = [f"- [{related[0]['title']}](/blog/{related[0]['slug']}/)", "- [Knowledge Atlas](/atlas/)", "- [SAP services](/services/)"]
        if previous: links.append(f"- Previous in the migration: [{previous['title']}](/blog/{previous['slug']}/)")
        if following: links.append(f"- Next in the migration: [{following['title']}](/blog/{following['slug']}/)")
        frontmatter = f'''---
layout: blog
title: {json.dumps(row["title"])}
description: {json.dumps(row["description"])}
slug: {row["slug"]}
permalink: /blog/{row["slug"]}/
date: {DATE}
author: "Dzmitryi Kharlanau"
language: en
category: {json.dumps(row["category"])}
tags:
{list_yaml(row["tags"])}
canonical_url: https://dkharlanau.github.io/blog/{row["slug"]}/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
reading_time_minutes: {max(1, round(row["word_count"] / 220))}
migration_sequence: {row["sequence"]}
migration_date_decision: "No reliable original publication date was present; date records the 2026-07-17 integration."
related_articles:
{list_yaml([f"/blog/{r['slug']}/" for r in related])}
---
'''
        headings = re.findall(r"^##\s+(.+?)\s*$", row["body"], flags=re.M)
        toc = "## On this page\n\n" + "\n".join(f"- [{heading}](#{heading_id(heading)})" for heading in headings) + "\n\n"
        body = toc + row["body"].rstrip() + "\n\n## Continue exploring\n\n" + "\n".join(links) + "\n"
        (OUTPUT / f"{row['slug']}.md").write_text(frontmatter + "\n" + body, encoding="utf-8")
    categories, all_tags = Counter(r["category"] for r in rows), Counter(t for r in rows for t in r["tags"])
    report = ["# Blog inbox migration report", "", f"Migration date: {DATE}", "", "## Outcome", "", "- Inbox files discovered: 51 (49 article inputs, `manifest.json`, and `EXTRACTION_REPORT.md`).", "- Articles created: 49.", "- Merged as duplicates: 0.", "- Deferred: 0.", "- Every article is a public review candidate (`needs_verification`, `verified: false`, `noindex`, `sitemap: false`). Promotion requires human factual review.", "- No reliable original publication date was supplied; every article uses the integration date. No modified date was asserted.", "", "## Taxonomy", ""]
    report += [f"- {name}: {count} articles" for name, count in sorted(categories.items())]
    report += ["", "## Article register", "", "| Input file | Route | Title | Category | Tags | Date decision | Source links | Duplicate / merge decision |", "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in rows: report.append(f"| `{r['filename']}` | `/blog/{r['slug']}/` | {r['title']} | {r['category']} | {', '.join(r['tags'])} | integration date {DATE} | {r['source_conversation_url']} | {r['duplicate_decision']} |")
    report += ["", "## Non-article inbox files", "", "| File | Decision | Reason |", "| --- | --- | --- |", "| `manifest.json` | retained migration input | machine-readable extraction inventory; not an article |", "| `EXTRACTION_REPORT.md` | retained migration input | extraction audit and provenance; not an article |", "", "## Manual review required", "", "- Verify SAP-specific claims and source references before promotion.", "- Confirm taxonomy and contextual links during editorial review.", "", "## Tag counts", ""]
    report += [f"- {tag}: {count}" for tag, count in sorted(all_tags.items())]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(report) + "\n", encoding="utf-8")
    print(f"Created {len(rows)} blog entries and {REPORT.relative_to(ROOT)}")
    return 0

if __name__ == "__main__": raise SystemExit(main())
