#!/usr/bin/env python3
"""Phase D audit data collector for search trust, entity authority, and internal linking.

Reads source frontmatter and built HTML, then emits a JSON summary of pages,
links, structured data, sitemap coverage, and LLM-surface coverage.

Output is written to reports/audit/phase-d-audit-data.json.
"""

from __future__ import annotations

import html
import json
import re
import sys
from collections import defaultdict
from datetime import date, datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

try:
    import yaml
except ImportError:
    print("PyYAML required: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

REPO = Path(__file__).resolve().parent.parent
SITE = REPO / "_site"
OUT = REPO / "reports" / "audit" / "phase-d-audit-data.json"

FRONT_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.IGNORECASE | re.DOTALL)
DESC_RE = re.compile(
    r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']',
    re.IGNORECASE | re.DOTALL,
)
ROBOTS_RE = re.compile(
    r'<meta[^>]+name=["\']robots["\'][^>]+content=["\'](.*?)["\']',
    re.IGNORECASE | re.DOTALL,
)
CANONICAL_RE = re.compile(
    r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\'](.*?)["\']',
    re.IGNORECASE | re.DOTALL,
)
OG_URL_RE = re.compile(
    r'<meta[^>]+property=["\']og:url["\'][^>]+content=["\'](.*?)["\']',
    re.IGNORECASE | re.DOTALL,
)
LINK_RE = re.compile(r'<a[^>]+href=["\'](.*?)["\'][^>]*>', re.IGNORECASE | re.DOTALL)
SCRIPT_LD_RE = re.compile(
    r'<script\s+type=["\']application/ld\+json["\']\s*>(.*?)</script>',
    re.IGNORECASE | re.DOTALL,
)

ORIGIN = "https://dkharlanau.github.io"

# Global entities that are intentionally referenced from many pages.
REUSABLE_IDS = {
    f"{ORIGIN}/#website",
    f"{ORIGIN}/#dkharlanau",
    "https://www.epam.com#organization",
}


class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (date, datetime)):
            return obj.isoformat()
        return super().default(obj)


def parse_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    match = FRONT_RE.match(text)
    if not match:
        return {}
    try:
        return yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        return {}


def iter_jsonld(obj):
    if isinstance(obj, dict):
        yield obj
        for v in obj.values():
            yield from iter_jsonld(v)
    elif isinstance(obj, list):
        for item in obj:
            yield from iter_jsonld(item)


def top_level_ids(obj):
    ids = []
    if isinstance(obj, dict):
        iid = obj.get("@id")
        if isinstance(iid, str):
            ids.append(iid)
        graph = obj.get("@graph")
        if isinstance(graph, list):
            for item in graph:
                if isinstance(item, dict):
                    gi = item.get("@id")
                    if isinstance(gi, str):
                        ids.append(gi)
    elif isinstance(obj, list):
        for item in obj:
            ids.extend(top_level_ids(item))
    return ids


def parse_sitemap(path: Path) -> set[str]:
    urls = set()
    if not path.exists():
        return urls
    text = path.read_text(encoding="utf-8")
    for loc in re.findall(r"<loc>(.*?)</loc>", text):
        parsed = urlparse(loc)
        urls.add(parsed.path or "/")
    return urls


def parse_llms_full(path: Path) -> set[str]:
    urls = set()
    if not path.exists():
        return urls
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("URL:"):
            value = line.replace("URL:", "").strip()
            parsed = urlparse(value)
            urls.add(parsed.path or value or "/")
    return urls


def parse_llms_manifest(path: Path) -> set[str]:
    urls = set()
    if not path.exists():
        return urls
    for line in path.read_text(encoding="utf-8").splitlines():
        for match in re.findall(r"https://[^\s|)\"'`>\]]+", line):
            parsed = urlparse(match.rstrip("."))
            if parsed.netloc == "dkharlanau.github.io":
                urls.add(parsed.path or "/")
    return urls


def source_for_html(rel: str) -> Path | None:
    """Best-guess source markdown path for a built HTML path."""
    candidate = rel.replace("index.html", "index.md").replace(".html", ".md")
    path = REPO / candidate
    if path.exists():
        return path
    # Collection documents: _site/atlas/glossary/term/index.html -> _glossary/term.md
    parts = candidate.split("/")
    if len(parts) >= 3 and parts[0] == "atlas" and parts[1] == "glossary":
        slug = parts[2]
        p = REPO / "_glossary" / f"{slug}.md"
        if p.exists():
            return p
    return None


def main():
    if not SITE.is_dir():
        print("Build the site first: bundle exec jekyll build", file=sys.stderr)
        sys.exit(1)

    OUT.parent.mkdir(parents=True, exist_ok=True)

    # Load sitemaps and LLM surfaces
    sitemap_pages = parse_sitemap(SITE / "sitemap-pages.xml")
    sitemap_atlas = parse_sitemap(SITE / "sitemap-atlas.xml")
    sitemap_data = parse_sitemap(SITE / "sitemap-data.xml")
    all_sitemap = sitemap_pages | sitemap_atlas | sitemap_data
    llms_full_urls = parse_llms_full(REPO / "llms-full.txt")
    llms_manifest_urls = parse_llms_manifest(REPO / "_includes" / "llms-manifest.txt")

    verified_inventory_path = REPO / "ai" / "verified-pages.json"
    verified_urls = set()
    verified_entries = []
    if verified_inventory_path.exists():
        data = json.loads(verified_inventory_path.read_text(encoding="utf-8"))
        verified_entries = data.get("entries", [])
        verified_urls = {urlparse(e["url"]).path or "/" for e in verified_entries}

    # Discover source files
    source_by_url: dict[str, dict] = {}
    for md_path in sorted(REPO.rglob("*.md")):
        rel = md_path.relative_to(REPO).as_posix()
        if any(
            rel.startswith(p)
            for p in ("_site/", ".git/", "vendor/", "node_modules/", "docs/templates/")
        ):
            continue
        fm = parse_frontmatter(md_path)
        if not fm:
            continue
        permalink = fm.get("permalink", "")
        if not permalink:
            continue
        source_by_url[permalink] = {
            "source": rel,
            "frontmatter": fm,
        }

    # Parse built HTML
    pages: list[dict] = []
    inlinks: dict[str, set[str]] = defaultdict(set)
    outlinks: dict[str, set[str]] = defaultdict(set)
    id_owners: dict[str, list[str]] = defaultdict(list)

    for html_path in sorted(SITE.rglob("*.html")):
        rel = html_path.relative_to(SITE).as_posix()
        content = html_path.read_text(encoding="utf-8", errors="ignore")

        robots = ""
        m = ROBOTS_RE.search(content)
        if m:
            robots = html.unescape(m.group(1)).strip().lower()
        is_noindex = "noindex" in robots

        canonical = ""
        m = CANONICAL_RE.search(content)
        if m:
            canonical = html.unescape(m.group(1)).strip()

        og_url = ""
        m = OG_URL_RE.search(content)
        if m:
            og_url = html.unescape(m.group(1)).strip()

        url = canonical or og_url or (ORIGIN + "/" + rel.replace("index.html", "").rstrip("/"))
        parsed = urlparse(url)
        path = parsed.path or "/"

        title = ""
        m = TITLE_RE.search(content)
        if m:
            title = html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip()

        description = ""
        m = DESC_RE.search(content)
        if m:
            description = html.unescape(m.group(1)).strip()

        jsonld_types = []
        jsonld_ids = []
        for block in SCRIPT_LD_RE.findall(content):
            try:
                data = json.loads(html.unescape(block))
            except json.JSONDecodeError:
                continue
            for item in iter_jsonld(data):
                if isinstance(item, dict):
                    t = item.get("@type")
                    if isinstance(t, str):
                        jsonld_types.append(t)
                    elif isinstance(t, list):
                        jsonld_types.extend(x for x in t if isinstance(x, str))
            for iid in top_level_ids(data):
                jsonld_ids.append(iid)
                id_owners[iid].append(path)

        links = set()
        for href in LINK_RE.findall(content):
            href = href.strip()
            if not href or href.startswith("#") or ":" in href.split("?")[0].split("#")[0]:
                continue
            # Normalize to path
            if href.startswith("/"):
                link_path = href.split("?")[0].split("#")[0]
            else:
                # Relative: resolve against page path
                base = path if not path.endswith("/") else path
                # Simple join for relative
                if "/" in base:
                    base_dir = base.rsplit("/", 1)[0]
                else:
                    base_dir = ""
                link_path = (base_dir + "/" + href).split("?")[0].split("#")[0]
                link_path = re.sub(r"/+", "/", link_path)
            links.add(link_path)
            outlinks[path].add(link_path)
            inlinks[link_path].add(path)

        source = source_for_html(rel)
        fm = parse_frontmatter(source) if source else {}

        pages.append(
            {
                "path": path,
                "html_path": rel,
                "source": source.relative_to(REPO).as_posix() if source else None,
                "title": title,
                "description": description,
                "robots": robots,
                "is_noindex": is_noindex,
                "canonical": canonical,
                "og_url": og_url,
                "jsonld_types": sorted(set(jsonld_types)),
                "jsonld_ids": jsonld_ids,
                "links": sorted(links),
                "frontmatter": fm,
                "in_sitemap_pages": path in sitemap_pages,
                "in_sitemap_atlas": path in sitemap_atlas,
                "in_sitemap_data": path in sitemap_data,
                "in_any_sitemap": path in all_sitemap,
                "in_llms_full": path in llms_full_urls,
                "in_llms_manifest": path in llms_manifest_urls,
                "in_verified_inventory": path in verified_urls,
            }
        )

    # Summary metrics
    indexable = [p for p in pages if not p["is_noindex"]]
    noindex = [p for p in pages if p["is_noindex"]]

    # Orphan / near-orphan indexable pages
    orphans = []
    near_orphans = []
    for p in indexable:
        incoming = inlinks.get(p["path"], set())
        # Only count incoming from indexable pages
        indexable_incoming = {src for src in incoming if not next((x for x in pages if x["path"] == src), {}).get("is_noindex", True)}
        if not indexable_incoming:
            orphans.append(p["path"])
        elif len(indexable_incoming) <= 2:
            near_orphans.append({"path": p["path"], "incoming": sorted(indexable_incoming)})

    # Verified inventory vs sitemap mismatches
    inventory_not_sitemap = sorted(verified_urls - all_sitemap)
    sitemap_not_inventory = sorted(all_sitemap & {p["path"] for p in indexable} - verified_urls)

    # llms-full vs sitemap mismatches
    llms_not_sitemap = sorted(llms_full_urls - all_sitemap)

    # Duplicate @id across pages (excluding intentionally reusable global entities)
    duplicate_ids = {k: v for k, v in id_owners.items() if len(v) > 1 and k not in REUSABLE_IDS}

    # Rich-result JSON-LD on noindex pages (beyond allowed)
    allowed_noindex_types = {"DefinedTerm", "DefinedTermSet"}
    noindex_rich = []
    for p in noindex:
        types = set(p["jsonld_types"])
        if not types:
            continue
        if types.issubset(allowed_noindex_types):
            continue
        noindex_rich.append({"path": p["path"], "types": sorted(types)})

    # Verified pages with weak metadata
    missing_last_reviewed = []
    missing_author = []
    missing_tags = []
    for p in indexable:
        fm = p.get("frontmatter") or {}
        if fm.get("verified") and fm.get("status") == "reviewed":
            if not fm.get("last_reviewed") and not fm.get("last_modified_at"):
                missing_last_reviewed.append(p["path"])
            if not fm.get("author"):
                missing_author.append(p["path"])
            if p["path"].startswith("/atlas/") and not fm.get("tags"):
                missing_tags.append(p["path"])

    # Glossary pages and links to them
    glossary_paths = {p["path"] for p in pages if "/atlas/glossary/" in p["path"]}
    glossary_incoming = {gp: sorted(inlinks.get(gp, set())) for gp in glossary_paths}

    # Hub references to verified Atlas pages
    hub_paths = {"/", "/about/", "/atlas/", "/skill-hub/", "/services/", "/ai/"}
    verified_atlas_paths = {
        p["path"]
        for p in indexable
        if p["path"].startswith("/atlas/")
        and (p.get("frontmatter") or {}).get("verified")
    }
    unlinked_from_hubs = []
    for vp in sorted(verified_atlas_paths):
        if not any(vp in outlinks.get(hub, set()) for hub in hub_paths):
            unlinked_from_hubs.append(vp)

    summary = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_pages": len(pages),
        "indexable_pages": len(indexable),
        "noindex_pages": len(noindex),
        "sitemap_pages_count": len(sitemap_pages),
        "sitemap_atlas_count": len(sitemap_atlas),
        "sitemap_data_count": len(sitemap_data),
        "verified_inventory_count": len(verified_urls),
        "llms_full_count": len(llms_full_urls),
        "llms_manifest_url_count": len(llms_manifest_urls),
        "orphan_indexable_pages": orphans,
        "near_orphan_indexable_pages": near_orphans,
        "inventory_not_in_sitemap": inventory_not_sitemap,
        "sitemap_not_in_inventory": sitemap_not_inventory,
        "llms_full_not_in_sitemap": llms_not_sitemap,
        "duplicate_jsonld_ids": duplicate_ids,
        "noindex_pages_with_rich_jsonld": noindex_rich,
        "verified_pages_missing_date": missing_last_reviewed,
        "verified_pages_missing_author": missing_author,
        "verified_atlas_pages_missing_tags": missing_tags,
        "glossary_incoming_links": glossary_incoming,
        "verified_atlas_pages_not_linked_from_hubs": unlinked_from_hubs,
        "pages": pages,
    }

    OUT.write_text(json.dumps(summary, indent=2, ensure_ascii=False, cls=DateTimeEncoder), encoding="utf-8")
    print(f"Wrote {OUT}")

    # Print concise findings
    print(f"\nPages: {len(pages)} total, {len(indexable)} indexable, {len(noindex)} noindex")
    print(f"Sitemaps: pages={len(sitemap_pages)} atlas={len(sitemap_atlas)} data={len(sitemap_data)}")
    print(f"Verified inventory: {len(verified_urls)} | llms-full: {len(llms_full_urls)} | llms-manifest local URLs: {len(llms_manifest_urls)}")
    print(f"\nOrphan indexable pages: {len(orphans)}")
    for o in orphans[:20]:
        print(f"  - {o}")
    print(f"\nNear-orphan indexable pages (<=2 indexable inlinks): {len(near_orphans)}")
    for o in near_orphans[:20]:
        print(f"  - {o['path']} from {o['incoming']}")
    print(f"\nVerified inventory not in sitemap: {len(inventory_not_sitemap)}")
    for u in inventory_not_sitemap[:20]:
        print(f"  - {u}")
    print(f"\nSitemap indexable pages not in verified inventory: {len(sitemap_not_inventory)}")
    for u in sitemap_not_inventory[:20]:
        print(f"  - {u}")
    print(f"\nDuplicate JSON-LD @id across pages: {len(duplicate_ids)}")
    for iid, owners in duplicate_ids.items():
        print(f"  - {iid}: {owners}")
    print(f"\nNoindex pages with rich JSON-LD: {len(noindex_rich)}")
    for item in noindex_rich[:20]:
        print(f"  - {item['path']}: {item['types']}")
    print(f"\nVerified pages missing date (last_reviewed/last_modified_at): {len(missing_last_reviewed)}")
    for u in missing_last_reviewed[:20]:
        print(f"  - {u}")
    print(f"\nVerified pages missing author: {len(missing_author)}")
    for u in missing_author[:20]:
        print(f"  - {u}")
    print(f"\nVerified Atlas pages missing tags: {len(missing_tags)}")
    for u in missing_tags[:20]:
        print(f"  - {u}")
    print(f"\nGlossary pages with non-zero incoming links: {sum(1 for v in glossary_incoming.values() if v)}")
    print(f"\nVerified Atlas pages not linked from top hubs: {len(unlinked_from_hubs)}")
    for u in unlinked_from_hubs[:20]:
        print(f"  - {u}")


if __name__ == "__main__":
    main()
