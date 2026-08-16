#!/usr/bin/env python3
"""Build and validate site-wide search/AI discovery metadata.

The loop is deliberately conservative:
- never edits homepage source/content data;
- only enriches reviewed + verified + indexable knowledge pages;
- keeps existing prose untouched;
- writes a clearly delimited managed front-matter block;
- generates per-page JSON sidecars under /ai/pages/;
- derives semantic links from existing page tags and hierarchy;
- derives source links only from explicit Enterprise Context source registries.

Run:
  python3 scripts/ai_search_trust_loop.py
  python3 scripts/ai_search_trust_loop.py --check
"""
from __future__ import annotations

import argparse
import copy
import json
import re
import sys
from collections import Counter
from datetime import date, datetime
from pathlib import Path
from urllib.parse import urlparse

import yaml

ROOT = Path(__file__).resolve().parents[1]
MANAGED_START = "# ai-discovery-managed:start"
MANAGED_END = "# ai-discovery-managed:end"
SIDE_DIR = ROOT / "ai" / "pages"
REPORT_JSON = ROOT / "reports" / "seo" / "ai-search-trust.json"
REPORT_MD = ROOT / "reports" / "seo" / "ai-search-trust.md"

EXCLUDED_DIRS = {
    ".git", "_site", "vendor", "node_modules", ".bundle", ".jekyll-cache", "reports"
}

# Stable entity ownership for the strongest public knowledge routes.
ROUTE_ENTITY = {
    "/labs/ai-ready/": "ai-architecture",
    "/labs/business-ai/": "business-ai",
    "/labs/enterprise-context/atp/": "advanced-atp",
    "/labs/enterprise-context/automotive-jit/": "sap-automotive-jit",
    "/labs/enterprise-context/billing/": "sap-billing",
    "/labs/enterprise-context/business-ai/": "sap-business-ai",
    "/labs/enterprise-context/business-ai/agents/": "sap-business-ai",
    "/labs/enterprise-context/credit/": "sap-credit-management",
    "/labs/enterprise-context/data-governance/": "sap-mdg",
    "/labs/enterprise-context/deployment-models/": "sap-s4hana",
    "/labs/enterprise-context/development/": "sap-s4hana",
    "/labs/enterprise-context/ewm/": "sap-ewm",
    "/labs/enterprise-context/finance-logistics/": "sap-s4hana",
    "/labs/enterprise-context/integration-operations/": "sap-integration",
    "/labs/enterprise-context/integrations/": "sap-integration",
    "/labs/enterprise-context/inventory-management/": "sap-inventory-management",
    "/labs/enterprise-context/logistics-capabilities/": "sap-s4hana",
    "/labs/enterprise-context/mdg/": "sap-mdg",
    "/labs/enterprise-context/mdg/interfaces/": "sap-mdg",
    "/labs/enterprise-context/pricing/": "sap-pricing",
    "/labs/enterprise-context/procurement/": "sap-procurement",
    "/labs/enterprise-context/production/": "sap-production",
    "/labs/enterprise-context/quality-management/": "sap-quality-management",
    "/labs/enterprise-context/sales-diagnostics/": "sales-diagnostics",
    "/labs/enterprise-context/sales-order/": "sap-sales",
    "/labs/enterprise-context/sales-processes/": "sap-sales",
    "/labs/enterprise-context/sales-processes/integrations/": "sap-integration",
    "/labs/enterprise-context/shipping/": "sap-shipping",
    "/labs/enterprise-context/transportation-management/": "sap-tm",
    "/labs/enterprise-context/transportation-management/integrations/": "sap-tm",
}

TAG_ENTITY = {
    "sap-s4hana": "sap-s4hana",
    "s4hana": "sap-s4hana",
    "sales": "sap-sales",
    "sap-sd": "sap-sales",
    "pricing": "sap-pricing",
    "aatp": "advanced-atp",
    "atp": "advanced-atp",
    "shipping": "sap-shipping",
    "procurement": "sap-procurement",
    "sap-mm": "sap-procurement",
    "ewm": "sap-ewm",
    "transportation-management": "sap-tm",
    "tm": "sap-tm",
    "mdg": "sap-mdg",
    "integration": "sap-integration",
    "integrations": "sap-integration",
    "business-ai": "business-ai",
    "ai": "ai-architecture",
    "jit": "sap-automotive-jit",
    "quality-management": "sap-quality-management",
    "production": "sap-production",
    "inventory-management": "sap-inventory-management",
    "credit": "sap-credit-management",
    "billing": "sap-billing",
    "diagnostics": "sales-diagnostics",
}

FRONT_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
URL_RE = re.compile(r"https?://[^\s\]\[\)\(<>\"']+")
SOURCE_ASSIGN_RE = re.compile(
    r"site\.data\.labs\.enterprise_context\.sources\.([A-Za-z0-9_]+)"
)
H1_RE = re.compile(r"<h1\b|^#\s+", re.I | re.M)


def json_default(value):
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    raise TypeError(type(value).__name__)


def iso(value) -> str | None:
    if value is None:
        return None
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    text = str(value).strip()
    return text or None


def parse_date(value):
    text = iso(value)
    if not text:
        return None
    try:
        return datetime.fromisoformat(text[:10])
    except ValueError:
        return None


def split_frontmatter(text: str):
    match = FRONT_RE.search(text)
    if not match:
        return None, None, None
    raw = match.group(1)
    try:
        data = yaml.safe_load(raw) or {}
    except yaml.YAMLError:
        return None, None, None
    if not isinstance(data, dict):
        return None, None, None
    return data, raw, text[match.end():]


def remove_managed(raw: str) -> str:
    pattern = re.compile(
        rf"\n?{re.escape(MANAGED_START)}.*?{re.escape(MANAGED_END)}\n?", re.S
    )
    cleaned = pattern.sub("\n", raw).rstrip()
    return cleaned


def derive_route(path: Path, fm: dict) -> str:
    permalink = fm.get("permalink")
    if permalink:
        route = str(permalink)
        if not route.startswith("/"):
            route = "/" + route
        return route
    rel = path.relative_to(ROOT).as_posix()
    if rel.endswith("/index.md") or rel.endswith("/index.html"):
        route = "/" + rel.rsplit("/index.", 1)[0] + "/"
    elif rel.endswith(".md"):
        route = "/" + rel[:-3] + "/"
    else:
        route = "/" + rel
    return route.replace("//", "/")


def iter_sources():
    for suffix in ("*.md", "*.html"):
        for path in ROOT.rglob(suffix):
            rel_parts = set(path.relative_to(ROOT).parts)
            if rel_parts & EXCLUDED_DIRS:
                continue
            text = path.read_text(encoding="utf-8")
            fm, raw, body = split_frontmatter(text)
            if fm is None:
                continue
            yield path, text, fm, raw, body


def is_public_reviewed(fm: dict) -> bool:
    robots = str(fm.get("robots", ""))
    return (
        fm.get("status") == "reviewed"
        and fm.get("verified") is True
        and "noindex" not in robots
        and fm.get("sitemap") is not False
    )


def is_knowledge_route(route: str) -> bool:
    return route.startswith(("/labs/", "/atlas/", "/skill-hub/", "/notes/", "/blog/"))


def sidecar_path(route: str) -> str:
    slug = route.strip("/").replace("/", "--") or "home"
    return f"/ai/pages/{slug}.json"


def load_yaml(path: Path):
    if not path.exists():
        return None
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError:
        return None


def load_json(path: Path):
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None


def load_intents() -> dict[str, str]:
    data = load_yaml(ROOT / "_data" / "labs" / "search_intents.yml") or {}
    result = {}
    # Accept either routes: {route: {primary: ...}} or a root route map.
    candidates = data.get("routes", data) if isinstance(data, dict) else {}
    if not isinstance(candidates, dict):
        return result
    for route, value in candidates.items():
        if not isinstance(route, str) or not route.startswith("/"):
            continue
        if isinstance(value, str):
            result[route] = value
        elif isinstance(value, dict):
            primary = value.get("primary") or value.get("intent") or value.get("search_intent")
            if primary:
                result[route] = str(primary)
    return result


def load_entities() -> dict:
    data = load_yaml(ROOT / "_data" / "knowledge_entities.yml") or {}
    return data.get("entities", {}) if isinstance(data, dict) else {}


def readiness_by_route() -> dict[str, dict]:
    data = load_json(ROOT / "labs" / "assessment" / "data" / "promotion-readiness.json") or {}
    items = data.get("items", []) if isinstance(data, dict) else []
    return {item.get("route"): item for item in items if isinstance(item, dict) and item.get("route")}


def extract_source_links(body: str) -> list[dict]:
    names = sorted(set(SOURCE_ASSIGN_RE.findall(body)))
    found = []
    seen = set()
    for name in names:
        path = ROOT / "_data" / "labs" / "enterprise_context" / "sources" / f"{name}.yml"
        data = load_yaml(path)
        if not data:
            continue

        def walk(node, inherited_title=None):
            if isinstance(node, dict):
                title = node.get("title") or node.get("name") or inherited_title or name.replace("_", " ").title()
                url = node.get("url") or node.get("href")
                if isinstance(url, str) and url.startswith("http") and url not in seen:
                    seen.add(url)
                    found.append({"title": str(title), "url": url})
                for value in node.values():
                    walk(value, title)
            elif isinstance(node, list):
                for value in node:
                    walk(value, inherited_title)
            elif isinstance(node, str):
                for url in URL_RE.findall(node):
                    url = url.rstrip(".,;:")
                    if url not in seen:
                        seen.add(url)
                        found.append({"title": inherited_title or name.replace("_", " ").title(), "url": url})

        walk(data)
    # Keep schema compact and deterministic.
    return found[:12]


def entity_mentions(fm: dict, primary: str | None, entities: dict) -> list[str]:
    mentions = []
    for tag in fm.get("tags", []) or []:
        key = TAG_ENTITY.get(str(tag).lower())
        if key and key in entities and key != primary and key not in mentions:
            mentions.append(key)
    return mentions[:8]


def relation_label(current: dict, other: dict) -> str:
    cr = current["route"]
    oroute = other["route"]
    title = other["title"].lower()
    if cr.startswith(oroute) and cr != oroute:
        return "Parent context"
    if oroute.startswith(cr) and cr != oroute:
        return "Deep dive"
    if "integration" in title or "/integrations/" in oroute:
        return "Integration view"
    if "diagnostic" in title:
        return "Diagnose with"
    if current.get("primary_topic") == other.get("primary_topic"):
        return "Same domain"
    return "Related topic"


def build_semantic_links(records: list[dict]) -> dict[str, list[dict]]:
    links = {}
    for current in records:
        scored = []
        ctags = current["tags"]
        for other in records:
            if other["route"] == current["route"]:
                continue
            shared = len(ctags & other["tags"])
            score = shared * 3
            if current.get("primary_topic") and current.get("primary_topic") == other.get("primary_topic"):
                score += 6
            if current["route"].startswith(other["route"]) or other["route"].startswith(current["route"]):
                score += 5
            # Same Enterprise Context family is useful but intentionally weak.
            if current["route"].startswith("/labs/enterprise-context/") and other["route"].startswith("/labs/enterprise-context/"):
                score += 1
            if score <= 0:
                continue
            scored.append((score, other["route"], other))
        scored.sort(key=lambda item: (-item[0], item[1]))
        selected = []
        used_labels = Counter()
        for _, _, other in scored:
            label = relation_label(current, other)
            # Avoid five identical weak relationships if more useful types exist.
            if label == "Related topic" and used_labels[label] >= 3:
                continue
            selected.append({"type": label, "title": other["title"], "url": other["route"]})
            used_labels[label] += 1
            if len(selected) >= 6:
                break
        links[current["route"]] = selected
    return links


def yaml_quote(value) -> str:
    return json.dumps(str(value), ensure_ascii=False)


def managed_block(record: dict, relations: list[dict], sources: list[dict], fm_without_managed: dict) -> str:
    lines = [MANAGED_START]
    if not isinstance(fm_without_managed.get("structured_data"), dict):
        lines.extend(["structured_data:", "  type: TechArticle"])
    lines.append(f"primary_topic: {yaml_quote(record['primary_topic'])}")
    lines.append(f"ai_sidecar: {yaml_quote(record['ai_sidecar'])}")
    if not fm_without_managed.get("search_intent") and record.get("search_intent"):
        lines.append(f"search_intent: {yaml_quote(record['search_intent'])}")
    if record.get("entity_mentions"):
        lines.append("entity_mentions:")
        for item in record["entity_mentions"]:
            lines.append(f"  - {yaml_quote(item)}")
    if relations:
        lines.append("semantic_links:")
        for relation in relations:
            lines.append(f"  - type: {yaml_quote(relation['type'])}")
            lines.append(f"    title: {yaml_quote(relation['title'])}")
            lines.append(f"    url: {yaml_quote(relation['url'])}")
    if sources:
        lines.append("source_links:")
        for source in sources:
            lines.append(f"  - title: {yaml_quote(source['title'])}")
            lines.append(f"    url: {yaml_quote(source['url'])}")
    lines.append(MANAGED_END)
    return "\n".join(lines)


def align_last_modified(raw: str, fm: dict) -> str:
    reviewed = parse_date(fm.get("last_reviewed"))
    modified = parse_date(fm.get("last_modified_at"))
    if not reviewed or (modified and modified >= reviewed):
        return raw
    value = reviewed.date().isoformat()
    pattern = re.compile(r"(?m)^last_modified_at:\s*.*$")
    if pattern.search(raw):
        return pattern.sub(f"last_modified_at: {value}", raw, count=1)
    return raw.rstrip() + f"\nlast_modified_at: {value}"


def render_source(text: str, raw: str, body: str, block: str, fm: dict) -> str:
    cleaned = remove_managed(raw)
    cleaned = align_last_modified(cleaned, fm)
    new_raw = cleaned.rstrip() + "\n" + block
    return f"---\n{new_raw}\n---\n{body}"


def patch_layout(text: str) -> str:
    if "{% include seo/page-machine-links.html %}" not in text:
        anchor = "  {% include head.html %}\n"
        insert = (
            anchor
            + "  {% include seo/page-machine-links.html %}\n"
            + "  {% unless page.url == '/' %}<link rel=\"stylesheet\" href=\"{{ '/assets/knowledge-trust.css' | relative_url }}\" />{% endunless %}\n"
        )
        if anchor not in text:
            raise RuntimeError("default layout head anchor not found")
        text = text.replace(anchor, insert, 1)
    if "{% include seo/trust-strip.html %}" not in text:
        anchor = "    {{ content }}\n"
        insert = anchor + "    {% include seo/trust-strip.html %}\n    {% include seo/semantic-related.html %}\n"
        if anchor not in text:
            raise RuntimeError("default layout content anchor not found")
        text = text.replace(anchor, insert, 1)
    if "{% include seo/structured-data-sitewide-graph.html %}" not in text:
        anchor = "  {% include seo/lab-breadcrumb-data.html %}\n"
        insert = anchor + "  {% include seo/structured-data-sitewide-graph.html %}\n"
        if anchor not in text:
            raise RuntimeError("default layout schema anchor not found")
        text = text.replace(anchor, insert, 1)
    return text


def patch_sitemap(text: str) -> str:
    text = text.replace(
        "page.last_modified_at | default: page.date | default: page.updated | default: nil",
        "page.last_reviewed | default: page.last_modified_at | default: page.date | default: page.updated | default: nil",
    )
    text = text.replace(
        "doc.last_modified_at | default: doc.date | default: doc.updated | default: nil",
        "doc.last_reviewed | default: doc.last_modified_at | default: doc.date | default: doc.updated | default: nil",
    )
    text = text.replace(
        "post.last_modified_at | default: post.date | default: post.updated | default: nil",
        "post.last_reviewed | default: post.last_modified_at | default: post.date | default: post.updated | default: nil",
    )
    return text


def sidecar_payload(record: dict, relations: list[dict], sources: list[dict], readiness: dict | None, entities: dict) -> dict:
    primary = entities.get(record["primary_topic"], {})
    factual = (readiness or {}).get("factual_review", {}) if readiness else {}
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "id": f"https://dkharlanau.github.io{record['route']}#knowledge",
        "url": f"https://dkharlanau.github.io{record['route']}",
        "title": record["title"],
        "description": record["description"],
        "language": "en",
        "author": {
            "id": "https://dkharlanau.github.io/#dkharlanau",
            "name": "Dzmitryi Kharlanau",
            "profile": "https://dkharlanau.github.io/about/",
        },
        "publication": {
            "status": "reviewed",
            "verified": True,
            "last_reviewed": record.get("last_reviewed"),
            "last_modified_at": record.get("effective_modified"),
            "evidence_review_mode": record.get("evidence_review_mode"),
            "publication_wave": record.get("publication_wave"),
        },
        "search": {
            "intent": record.get("search_intent"),
            "canonical": f"https://dkharlanau.github.io{record['route']}",
            "robots": record.get("robots"),
        },
        "primary_entity": {
            "key": record["primary_topic"],
            "id": f"https://dkharlanau.github.io{primary.get('id', '')}#entity" if primary else None,
            "name": primary.get("name"),
            "type": primary.get("type", "Thing"),
            "description": primary.get("description"),
            "same_as": primary.get("same_as", []),
        },
        "mentions": record.get("entity_mentions", []),
        "tags": sorted(record["tags"]),
        "relationships": relations,
        "sources": sources,
        "factual_review": {
            "status": factual.get("status"),
            "claim_count": factual.get("claim_count"),
            "source_supported_count": factual.get("source_supported_count"),
            "source_conflict_count": factual.get("source_conflict_count"),
            "evidence_classes": factual.get("evidence_classes", []),
        },
        "machine_readable": record.get("machine_readable", []),
    }


def validate(records: list[dict], expected_sidecars: dict[str, dict], entities: dict) -> list[str]:
    errors = []
    titles = Counter(r["title"].strip().lower() for r in records)
    descriptions = Counter(r["description"].strip().lower() for r in records)
    for record in records:
        route = record["route"]
        if titles[record["title"].strip().lower()] > 1:
            errors.append(f"{route}: duplicate title")
        if descriptions[record["description"].strip().lower()] > 1:
            errors.append(f"{route}: duplicate description")
        if len(record["description"].strip()) < 45:
            errors.append(f"{route}: description too short")
        if route.startswith("/labs/"):
            if record["primary_topic"] not in entities:
                errors.append(f"{route}: unknown primary_topic {record['primary_topic']}")
            if not record.get("search_intent"):
                errors.append(f"{route}: missing search_intent")
            if not record.get("last_reviewed"):
                errors.append(f"{route}: missing last_reviewed")
            if len(record.get("semantic_links", [])) < 2:
                errors.append(f"{route}: fewer than two semantic links")
            if not record.get("ai_sidecar"):
                errors.append(f"{route}: missing ai_sidecar")
        h1_count = len(H1_RE.findall(record["body"]))
        if route.startswith("/labs/") and h1_count != 1:
            errors.append(f"{route}: expected one source H1, found {h1_count}")
        payload = expected_sidecars.get(route)
        if not payload:
            errors.append(f"{route}: missing expected sidecar payload")
        elif payload.get("url") != f"https://dkharlanau.github.io{route}":
            errors.append(f"{route}: sidecar canonical mismatch")
    return errors


def write_or_check(path: Path, content: str, check: bool, changed: list[str]):
    current = path.read_text(encoding="utf-8") if path.exists() else None
    if current == content:
        return
    changed.append(path.relative_to(ROOT).as_posix())
    if not check:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if generated metadata is stale")
    args = parser.parse_args()

    intents = load_intents()
    entities = load_entities()
    readiness = readiness_by_route()

    source_rows = []
    source_lookup = {}
    for path, text, fm, raw, body in iter_sources():
        route = derive_route(path, fm)
        source_lookup[route] = (path, text, fm, raw, body)
        if route == "/" or not is_public_reviewed(fm) or not is_knowledge_route(route):
            continue
        primary = fm.get("primary_topic") or ROUTE_ENTITY.get(route)
        # Only enforce entity metadata on public Lab pages and pages that already opt in.
        if not primary:
            continue
        desc = str(fm.get("description") or fm.get("summary") or "").strip()
        title = str(fm.get("title") or "").strip()
        tags = {str(t).strip().lower() for t in (fm.get("tags") or []) if str(t).strip()}
        search_intent = fm.get("search_intent") or intents.get(route)
        ai_path = fm.get("ai_sidecar") or sidecar_path(route)
        reviewed = iso(fm.get("last_reviewed"))
        modified = iso(fm.get("last_modified_at"))
        dr, dm = parse_date(reviewed), parse_date(modified)
        effective = reviewed if dr and (not dm or dr >= dm) else modified
        mentions = entity_mentions(fm, str(primary), entities)
        source_rows.append({
            "route": route,
            "path": path.relative_to(ROOT).as_posix(),
            "title": title,
            "description": desc,
            "tags": tags,
            "primary_topic": str(primary),
            "entity_mentions": mentions,
            "search_intent": str(search_intent) if search_intent else None,
            "ai_sidecar": str(ai_path),
            "last_reviewed": reviewed,
            "effective_modified": effective,
            "evidence_review_mode": fm.get("evidence_review_mode"),
            "publication_wave": fm.get("publication_wave"),
            "robots": fm.get("robots"),
            "machine_readable": fm.get("machine_readable") or [],
            "body": body,
        })

    semantic = build_semantic_links(source_rows)
    expected_sidecars = {}
    changed = []

    for record in source_rows:
        route = record["route"]
        path, text, fm, raw, body = source_lookup[route]
        sources = extract_source_links(body)
        relations = semantic.get(route, [])
        record["semantic_links"] = relations

        clean_raw = remove_managed(raw)
        try:
            fm_clean = yaml.safe_load(clean_raw) or {}
        except yaml.YAMLError as exc:
            raise RuntimeError(f"{record['path']}: invalid front matter after managed-block removal") from exc
        block = managed_block(record, relations, sources, fm_clean)
        new_text = render_source(text, raw, body, block, fm)
        write_or_check(path, new_text, args.check, changed)

        payload = sidecar_payload(record, relations, sources, readiness.get(route), entities)
        expected_sidecars[route] = payload
        side_path = ROOT / record["ai_sidecar"].lstrip("/")
        content = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=False, default=json_default) + "\n"
        write_or_check(side_path, content, args.check, changed)

    # Remove stale generated sidecars that no longer map to a public knowledge page.
    expected_paths = {str((ROOT / r["ai_sidecar"].lstrip("/")).resolve()) for r in source_rows}
    if SIDE_DIR.exists():
        for side in SIDE_DIR.glob("*.json"):
            if str(side.resolve()) not in expected_paths:
                changed.append(side.relative_to(ROOT).as_posix())
                if not args.check:
                    side.unlink()

    layout_path = ROOT / "_layouts" / "default.html"
    if layout_path.exists():
        write_or_check(layout_path, patch_layout(layout_path.read_text(encoding="utf-8")), args.check, changed)

    sitemap_path = ROOT / "sitemap-pages.xml"
    if sitemap_path.exists():
        write_or_check(sitemap_path, patch_sitemap(sitemap_path.read_text(encoding="utf-8")), args.check, changed)

    errors = validate(source_rows, expected_sidecars, entities)

    report = {
        "id": "ai-search-trust-loop",
        "version": "1.0.0",
        "updated_at": "2026-08-16",
        "public_knowledge_pages": len(source_rows),
        "sidecars": len(expected_sidecars),
        "entity_registry_size": len(entities),
        "errors": errors,
        "changed_paths": sorted(set(changed)),
        "pages": [
            {
                "route": r["route"],
                "source": r["path"],
                "primary_topic": r["primary_topic"],
                "search_intent": r.get("search_intent"),
                "sidecar": r["ai_sidecar"],
                "semantic_link_count": len(r.get("semantic_links", [])),
                "last_reviewed": r.get("last_reviewed"),
            }
            for r in sorted(source_rows, key=lambda x: x["route"])
        ],
    }
    report_json = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    report_md = [
        "# AI Search & Trust Loop",
        "",
        f"- Public knowledge pages: **{len(source_rows)}**",
        f"- Generated sidecars: **{len(expected_sidecars)}**",
        f"- Canonical entities: **{len(entities)}**",
        f"- Validation errors: **{len(errors)}**",
        "",
        "## Pages",
        "",
        "| Route | Entity | Semantic links | Sidecar |",
        "|---|---|---:|---|",
    ]
    for r in sorted(source_rows, key=lambda x: x["route"]):
        report_md.append(f"| `{r['route']}` | `{r['primary_topic']}` | {len(r.get('semantic_links', []))} | `{r['ai_sidecar']}` |")
    if errors:
        report_md.extend(["", "## Errors", ""] + [f"- {e}" for e in errors])
    report_md.append("")

    write_or_check(REPORT_JSON, report_json, args.check, changed)
    write_or_check(REPORT_MD, "\n".join(report_md), args.check, changed)

    if args.check and changed:
        print("AI search/trust metadata is stale:")
        for path in sorted(set(changed)):
            print(f" - {path}")
        return 1
    if errors:
        print("AI search/trust validation errors:")
        for err in errors:
            print(f" - {err}")
        return 2

    print(
        f"AI search/trust loop OK: pages={len(source_rows)} sidecars={len(expected_sidecars)} "
        f"entities={len(entities)} changed={len(set(changed))}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
