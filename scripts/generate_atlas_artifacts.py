#!/usr/bin/env python3
"""
Atlas Artifact Generator for dkharlanau.github.io

Regenerates the static Atlas discovery layer:
  - atlas/manifest.json        — machine-readable index of all Atlas pages
  - llms-full.txt              — full-text concatenation of verified Atlas pages
  - ai/rag/related.json        — related-content graph from frontmatter
  - ai/atlas-compact-index.json — compact signal-matching index
  - ai/verified-pages.json     — site-wide inventory of reviewed, verified, indexable pages
  - ai/markdown-clusters.json  — cluster-aware readiness map for the complete Markdown corpus

Usage:
    python3 scripts/generate_atlas_artifacts.py
    python3 scripts/generate_atlas_artifacts.py --check

Requirements:
    PyYAML (pip install pyyaml)

Safety:
    - Never exposes source_files or private draft paths.
    - Only includes verified pages in llms-full.txt.
    - Validates that related links point to existing pages.
"""

import argparse
import copy
import json
import os
import re
import sys
from datetime import date, datetime
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. Install: pip install pyyaml", file=sys.stderr)
    sys.exit(1)


REPO_DIR = Path(__file__).resolve().parent.parent
ATLAS_DIR = REPO_DIR / "atlas"
BASE_URL = "https://dkharlanau.github.io"

CHECK_MODE_TIMESTAMP = "CHECK_MODE"
_DETERMINISTIC_TIMESTAMP = None


def discover_atlas_articles():
    """Dynamically discover public Atlas article pages under atlas/.

    Inclusion rules (all must be true):
      - path matches atlas/**/*.md
      - frontmatter has permalink starting with /atlas/
      - frontmatter has atlas_section
      - frontmatter has status
      - frontmatter has verified
      - not a section/index page (path does not end with /index.md)
      - not marked sitemap: false unless atlas_include: true is present

    Returns a sorted list of relative POSIX paths.
    """
    articles = []
    for md_path in sorted(ATLAS_DIR.rglob("*.md")):
        rel_path = md_path.relative_to(REPO_DIR).as_posix()

        # Exclude section/index pages by path pattern
        if rel_path.endswith("/index.md") or rel_path == "atlas/index.md":
            continue

        fm, _ = parse_frontmatter(md_path)
        if not fm:
            continue

        # Required frontmatter signals
        permalink = fm.get("permalink", "")
        if not permalink or not permalink.startswith("/atlas/"):
            continue
        if "atlas_section" not in fm:
            continue
        if "status" not in fm:
            continue
        if "verified" not in fm:
            continue

        # Exclude noindex/sitemap:false pages unless explicitly included
        # OR unless they have all required article frontmatter (article pages
        # may set sitemap:false while still belonging to the Atlas manifest).
        sitemap = fm.get("sitemap", True)
        atlas_include = fm.get("atlas_include", False)
        has_article_signals = all(k in fm for k in ("atlas_section", "status", "verified"))
        if sitemap is False and not atlas_include and not has_article_signals:
            continue

        articles.append(rel_path)

    return sorted(articles)


class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        return super().default(obj)


def parse_frontmatter(path):
    """Extract YAML frontmatter and body from a Markdown file."""
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    if not content.startswith("---\n"):
        return {}, content

    end = content.find("\n---\n", 4)
    if end == -1:
        return {}, content

    fm_text = content[4:end].strip()
    body = content[end + 5:].strip()

    try:
        fm = yaml.safe_load(fm_text) or {}
    except Exception as e:
        print(f"YAML parse error in {path}: {e}", file=sys.stderr)
        fm = {}

    return fm, body


def serialize_value(v):
    if isinstance(v, (date, datetime)):
        return v.isoformat()
    if isinstance(v, list):
        return [serialize_value(i) for i in v]
    if isinstance(v, dict):
        return {k: serialize_value(vv) for k, vv in v.items()}
    return v


def canonical_url(value):
    """Return a canonical production URL for a public path or URL."""
    text = str(value or "").strip()
    if not text:
        return ""
    if text.startswith("https://") or text.startswith("http://"):
        return text
    if not text.startswith("/"):
        text = f"/{text}"
    return f"{BASE_URL}{text}"


def strip_jekyll_and_html(text):
    """Remove Jekyll tags, HTML tags, and liquid markup for plain text."""
    text = re.sub(r'{%\s*include\s+[^%]+%}', '', text)
    text = re.sub(r'{%\s*assign\s+[^%]+%}', '', text)
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'{{[^}]+}}', '', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def extract_headings(body, max_headings=12):
    """Extract compact markdown/HTML headings for matching."""
    headings = []
    for line in body.splitlines():
        stripped = line.strip()
        md_match = re.match(r"^#{2,4}\s+(.+)$", stripped)
        html_match = re.match(r"^<h([2-4])[^>]*>(.*?)</h\1>$", stripped, re.I)
        text = ""
        if md_match:
            text = md_match.group(1)
        elif html_match:
            text = html_match.group(2)
        if text:
            clean = strip_jekyll_and_html(text)
            clean = re.sub(r"\s+", " ", clean).strip()
            if clean and clean not in headings:
                headings.append(clean)
        if len(headings) >= max_headings:
            break
    return headings


def _keyword_terms(*values):
    terms = []
    for value in values:
        if not value:
            continue
        if isinstance(value, list):
            candidates = value
        else:
            candidates = [value]
        for candidate in candidates:
            text = str(candidate).strip()
            if not text:
                continue
            normalized = re.sub(r"\s+", " ", text.lower())
            if normalized not in terms:
                terms.append(normalized)
    return terms


def _token_terms(text):
    tokens = re.findall(r"[a-z0-9][a-z0-9+-]{2,}", text.lower())
    stopwords = {
        "the", "and", "for", "with", "from", "that", "this", "how", "when",
        "where", "what", "why", "into", "page", "sap",
    }
    result = []
    for token in tokens:
        if token in stopwords:
            continue
        if token not in result:
            result.append(token)
    return result


def _matching_terms(fm, headings):
    phrase_terms = _keyword_terms(
        fm.get("title", ""),
        fm.get("description", ""),
        fm.get("domain", ""),
        fm.get("subdomain", ""),
        fm.get("concept_type", ""),
        fm.get("sap_area", ""),
        fm.get("business_process", ""),
        fm.get("tags", []) or [],
        headings,
    )
    token_text = " ".join(phrase_terms)
    token_terms = _token_terms(token_text)
    combined = []
    for term in phrase_terms + token_terms:
        if term and term not in combined:
            combined.append(term)
    return combined[:80]


def _sap_domain_keywords(fm):
    return _keyword_terms(
        fm.get("domain", ""),
        fm.get("subdomain", ""),
        fm.get("sap_area", ""),
        fm.get("business_process", ""),
        fm.get("tags", []) or [],
    )[:40]


def build_permalink_map():
    """Build a map of permalink -> file info for the whole site."""
    all_pages = {}
    for root, dirs, files in os.walk(REPO_DIR):
        # Skip generated and dependency dirs
        dirs[:] = [d for d in dirs if d not in {
            "_site", ".git", "vendor", "node_modules", 
            "Kimi_Agent_SAP Atlas Expansion",
        } and not d.startswith("Basic_LinkedInDataExport_") and not d.startswith("Basic_LinkInDataExport_")]
        for f in files:
            if f.endswith(".md"):
                abs_path = Path(root) / f
                rel_path = abs_path.relative_to(REPO_DIR).as_posix()
                if rel_path.startswith("docs/templates/"):
                    continue
                fm, _ = parse_frontmatter(abs_path)
                permalink = fm.get("permalink", "")
                if permalink:
                    all_pages[permalink] = {
                        "file": rel_path,
                        "title": fm.get("title", ""),
                        "fm": fm,
                    }
    return all_pages


def _discover_markdown_documents():
    """Discover site-facing Markdown, including drafts without a permalink.

    The regular permalink map intentionally contains only routable pages. The
    cluster index also needs to show research drafts and other source Markdown
    that is not yet a public route, so those documents can be fixed or
    deliberately deferred instead of disappearing from the audit.
    """
    documents = []
    excluded_roots = {"_site", ".git", "vendor", "node_modules", "docs", "agent-skills"}
    for root, dirs, files in os.walk(REPO_DIR):
        dirs[:] = [directory for directory in dirs if directory not in excluded_roots and not directory.startswith(".")]
        for filename in files:
            if not filename.endswith(".md"):
                continue
            abs_path = Path(root) / filename
            rel_path = abs_path.relative_to(REPO_DIR).as_posix()
            if rel_path.startswith("docs/templates/") or rel_path.startswith("reports/"):
                continue
            fm, body = parse_frontmatter(abs_path)
            if not fm:
                continue
            documents.append({"file": rel_path, "fm": fm, "body": body})
    return sorted(documents, key=lambda item: item["file"])


def generate_compact_signal_index(atlas_files, check_mode=False, all_pages=None):
    """Generate the public, retrieval-eligible Atlas matching index."""
    entries = []
    for rel_path in atlas_files:
        abs_path = REPO_DIR / rel_path
        fm, body = parse_frontmatter(abs_path)
        if not _is_retrieval_eligible(fm):
            continue
        headings = extract_headings(body)
        entry = {
            "path": rel_path,
            "url": canonical_url(fm.get("permalink", "")),
            "title": fm.get("title", ""),
            "description": fm.get("description", ""),
            "atlas_section": fm.get("atlas_section", ""),
            "domain": fm.get("domain", ""),
            "subdomain": fm.get("subdomain", ""),
            "concept_type": fm.get("concept_type", ""),
            "sap_area": fm.get("sap_area", ""),
            "business_process": fm.get("business_process", ""),
            "status": fm.get("status", ""),
            "verified": bool(fm.get("verified", False)),
            "last_reviewed": serialize_value(fm.get("last_reviewed", "")),
            "tags": fm.get("tags", []) or [],
            "headings": headings,
            "sap_domain_keywords": _sap_domain_keywords(fm),
            "matching_terms": _matching_terms(fm, headings),
        }
        if all_pages is not None:
            expert_context = build_expert_context(rel_path, fm, all_pages, body)
            if expert_context:
                entry["expert_context"] = _expert_public_metadata(expert_context)
        entries.append(entry)

    index = {
        "schema": "dkharlanau.atlas.compact_signal_index",
        "schema_version": "2.0",
        "generated_at": _now(check_mode),
        "canonical_url": "https://dkharlanau.github.io/ai/atlas-compact-index.json",
        "description": (
            "Compact public Atlas index for matching enriched professional "
            "signals to reviewed, verified, indexable Atlas pages. Built from "
            "public frontmatter and headings only; no unverified page metadata, "
            "private notes, draft content, or full body text."
        ),
        "eligibility_policy": "verified=true; status=reviewed; indexable; sitemap-enabled",
        "source": "scripts/generate_atlas_artifacts.py",
        "count": len(entries),
        "entries": entries,
        "fallback": {
            "decision": "needs_research",
            "reason": (
                "If no candidate clears the matcher threshold, do not update "
                "or create a page automatically."
            ),
        },
    }

    if not check_mode:
        out_path = REPO_DIR / "ai" / "atlas-compact-index.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(index, f, indent=2, ensure_ascii=False, cls=DateTimeEncoder)

    return index


def _now(check_mode):
    """Return a source-derived timestamp or a comparison placeholder."""
    if check_mode:
        return CHECK_MODE_TIMESTAMP

    global _DETERMINISTIC_TIMESTAMP
    if _DETERMINISTIC_TIMESTAMP is not None:
        return _DETERMINISTIC_TIMESTAMP

    latest_date = ""
    for info in build_permalink_map().values():
        fm = info["fm"]
        for field in ("last_modified_at", "last_reviewed", "updated", "date"):
            value = serialize_value(fm.get(field, ""))
            match = re.match(r"^(\d{4}-\d{2}-\d{2})", str(value))
            if match and match.group(1) > latest_date:
                latest_date = match.group(1)

    _DETERMINISTIC_TIMESTAMP = f"{latest_date or '1970-01-01'}T00:00:00Z"
    return _DETERMINISTIC_TIMESTAMP


def _derive_page_type(rel_path):
    """Derive a high-level page type from the source path."""
    parts = rel_path.split("/")
    if not parts:
        return "page"
    return parts[0]


def _derive_section(rel_path, fm):
    """Derive a section label from frontmatter or source path."""
    if fm.get("atlas_section"):
        return fm["atlas_section"]
    parts = rel_path.split("/")
    if len(parts) >= 2:
        return parts[1]
    return ""


MARKDOWN_CLUSTER_LABELS = {
    "ai": "AI routing and machine-readable pages",
    "sap-architecture-course": "SAP Architect Field Course",
    "sap-ams": "SAP AMS and operations",
    "sap-integration": "SAP integration and interoperability",
    "sap-master-data": "SAP master data and governance",
    "sap-process-operations": "SAP process and logistics operations",
    "ai-agents": "AI agents, MCP, and agent workflows",
    "atlas": "Knowledge Atlas",
    "skill-hub": "Skill Hub",
    "datasets": "Datasets and reusable evidence",
    "services": "Consulting services",
    "scenarios": "Business scenarios",
    "research": "Research and comparisons",
    "blog": "Blog and Journal",
    "notes": "Notes",
    "news": "News and signals",
    "radar": "Professional radar",
    "agent-tools": "Agent tools and public registries",
    "pages": "Public site pages",
}


def _markdown_cluster_ids(rel_path, fm):
    """Return controlled cluster IDs for a Markdown page.

    Cluster membership is deliberately additive: a course page can also be
    part of the architecture and AI clusters, while a dataset byte can be
    part of the AMS or agentic cluster. This keeps retrieval routing useful
    without duplicating page content.
    """
    normalized = rel_path.lower()
    signal_text = " ".join(
        str(fm.get(key, "")) for key in (
            "title", "description", "domain", "subdomain", "sap_area",
            "business_process", "tags", "cluster", "clusters",
        )
    ).lower()
    text = f"{normalized} {signal_text}"
    clusters = []

    def add(cluster):
        if cluster not in clusters:
            clusters.append(cluster)

    if normalized.startswith("ai/") or fm.get("intent_id"):
        add("ai")
    if "sap-architecture-course" in normalized or fm.get("sap_architecture_course"):
        add("sap-architecture-course")
    if normalized.startswith("skill-hub/"):
        add("skill-hub")
    if normalized.startswith("atlas/"):
        add("atlas")
    if normalized.startswith("datasets/"):
        add("datasets")
    if normalized.startswith("services/"):
        add("services")
    if normalized.startswith("scenarios/"):
        add("scenarios")
    if normalized.startswith("research/"):
        add("research")
    if normalized.startswith("_blog/") or normalized.startswith("blog/"):
        add("blog")
    if normalized.startswith("_notes/") or normalized.startswith("notes/"):
        add("notes")
    if normalized.startswith("_news/") or normalized.startswith("news/"):
        add("news")
    if normalized.startswith("_radar/") or normalized.startswith("radar/"):
        add("radar")
    if normalized.startswith("agent-tools/") or "mcp" in text:
        add("agent-tools")
    if normalized.startswith("mcp/") or "mcp" in text or "agent" in text:
        add("ai-agents")
    if any(term in text for term in ("sap ams", "ams-", "ams/", "application management service", "support operations")):
        add("sap-ams")
    if any(term in text for term in ("integration", "interface", "idoc", "aif", "api", "middleware", "event mesh")):
        add("sap-integration")
    if any(term in text for term in ("master data", "master-data", "mdg", "business partner", "customer master", "supplier master", "vendor master")):
        add("sap-master-data")
    if any(term in text for term in ("sd/mm", "order to cash", "o2c", "procure to pay", "p2p", "logistics", "pricing", "mrp", "ewm", "retail")):
        add("sap-process-operations")
    if not clusters:
        add("pages")
    return clusters


def _markdown_readiness(rel_path, fm, body):
    """Describe Markdown structure without exposing page body text."""
    title = str(fm.get("title", "")).strip()
    description = str(fm.get("description", "")).strip()
    permalink = str(fm.get("permalink", "")).strip()
    clean_body = strip_jekyll_and_html(body)
    headings = extract_headings(body, max_headings=16)
    h1_present = bool(re.search(r"(?:^#\s+|<h1(?:\s|>))", body, flags=re.IGNORECASE | re.MULTILINE))
    # Collection and intent pages render their H1 through a shared include or
    # layout; do not mark those source Markdown files as structurally missing it.
    if (
        fm.get("intent_id")
        or fm.get("home_locale")
        or rel_path == "index.md"
        or fm.get("layout") in {"note", "blog", "radar"}
        or rel_path.startswith(("_notes/", "_blog/", "_news/", "_radar/"))
    ):
        h1_present = True
    internal_links = len(re.findall(r"(?:href|\]\()\s*=?\s*[\"']?(/[^\"')\s]+)", body))
    structural_ready = bool(title and description and permalink and h1_present)
    substantive = len(clean_body) >= 600 or len(headings) >= 2 or bool(fm.get("intent_id"))
    route_available = bool(permalink)
    indexable = route_available and _is_indexable(fm)
    reviewed = route_available and _is_retrieval_eligible(fm)
    routing_eligible = bool(fm.get("intent_id")) and indexable
    if not route_available:
        decision = "deferred"
        reason = "No canonical permalink is defined for this Markdown source, so it is not a public search route."
    elif not indexable:
        decision = "deferred"
        reason = "Noindex or sitemap-disabled content is not exposed as a retrieval candidate."
    elif not structural_ready:
        decision = "needs_metadata"
        reason = "Add a title, description, permalink, and semantic H1 before relying on this page for search routing."
    elif not substantive:
        decision = "needs_depth"
        reason = "The page has basic metadata but needs more substantive, decision-useful Markdown content."
    else:
        decision = "ready"
        reason = "Markdown has the minimum title, description, permalink, heading, and substantive-content signals."
    return {
        "title_present": bool(title),
        "description_present": bool(description),
        "permalink_present": bool(permalink),
        "h1_present": h1_present,
        "substantive": substantive,
        "body_characters": len(clean_body),
        "heading_count": len(headings),
        "headings": headings,
        "internal_link_count": internal_links,
        "decision": decision,
        "reason": reason,
        "indexable": indexable,
        "reviewed_retrieval_eligible": reviewed,
        "routing_eligible": routing_eligible,
    }


def generate_markdown_clusters(all_pages, check_mode=False):
    """Generate a cluster-aware index for the complete public Markdown corpus."""
    entries = []
    cluster_entries = {cluster: [] for cluster in MARKDOWN_CLUSTER_LABELS}
    for document in _discover_markdown_documents():
        rel_path = document["file"]
        fm = document["fm"]
        body = document["body"]
        permalink = str(fm.get("permalink", "")).strip()
        clusters = _markdown_cluster_ids(rel_path, fm)
        readiness = _markdown_readiness(rel_path, fm, body)
        entry = {
            "source_file": rel_path,
            "canonical_url": canonical_url(permalink) if permalink else "",
            "title": fm.get("title", ""),
            "description": fm.get("description", ""),
            "content_type": _derive_page_type(rel_path),
            "section": _derive_section(rel_path, fm),
            "clusters": clusters,
            "primary_cluster": clusters[0],
            "tags": fm.get("tags", []) or [],
            "related_urls": fm.get("related", []) or [],
            "permalink": permalink,
            "status": fm.get("status", ""),
            "verified": bool(fm.get("verified") is True),
            "sitemap": fm.get("sitemap", True),
            "readiness": readiness,
        }
        entries.append(entry)
        for cluster in clusters:
            cluster_entries.setdefault(cluster, []).append(entry)

    summary = {
        "markdown_pages": len(entries),
        "indexable_pages": sum(1 for entry in entries if entry["readiness"]["indexable"]),
        "reviewed_retrieval_pages": sum(1 for entry in entries if entry["readiness"]["reviewed_retrieval_eligible"]),
        "routing_pages": sum(1 for entry in entries if entry["readiness"]["routing_eligible"]),
        "ready_pages": sum(1 for entry in entries if entry["readiness"]["decision"] == "ready"),
        "needs_metadata": sum(1 for entry in entries if entry["readiness"]["decision"] == "needs_metadata"),
        "needs_depth": sum(1 for entry in entries if entry["readiness"]["decision"] == "needs_depth"),
        "deferred_pages": sum(1 for entry in entries if entry["readiness"]["decision"] == "deferred"),
    }
    clusters = []
    for cluster, label in MARKDOWN_CLUSTER_LABELS.items():
        cluster_items = cluster_entries.get(cluster, [])
        if not cluster_items:
            continue
        clusters.append({
            "id": cluster,
            "label": label,
            "page_count": len(cluster_items),
            "indexable_count": sum(1 for entry in cluster_items if entry["readiness"]["indexable"]),
            "retrieval_count": sum(1 for entry in cluster_items if entry["readiness"]["reviewed_retrieval_eligible"]),
            "ready_count": sum(1 for entry in cluster_items if entry["readiness"]["decision"] == "ready"),
            "urls": [entry["canonical_url"] for entry in cluster_items if entry["canonical_url"]],
        })
    artifact = {
        "schema": "dkharlanau.markdown_clusters",
        "schema_version": "1.0",
        "generated_at": _now(check_mode),
        "canonical_url": f"{BASE_URL}/ai/markdown-clusters.json",
        "source": "scripts/generate_atlas_artifacts.py",
        "description": "Cluster-aware Markdown inventory for AI search routing. Readiness is structural; retrieval eligibility still requires the repository's reviewed, verified, indexable policy.",
        "summary": summary,
        "clusters": clusters,
        "entries": entries,
    }
    if not check_mode:
        with (REPO_DIR / "ai" / "markdown-clusters.json").open("w", encoding="utf-8") as f:
            json.dump(artifact, f, indent=2, ensure_ascii=False, cls=DateTimeEncoder)
    return artifact


def _is_indexable(fm):
    """Return True if frontmatter signals the page should be indexed."""
    robots = str(fm.get("robots", "")).lower()
    if "noindex" in robots:
        return False
    if fm.get("sitemap") is False:
        return False
    return True


def _is_retrieval_eligible(fm):
    """Return True only for reviewed, verified, indexable public content."""
    return (
        fm.get("verified") is True
        and fm.get("status") == "reviewed"
        and _is_indexable(fm)
    )


EXPERT_CONTEXT_COPY = {
    "sap-integration": (
        "a Senior SAP Consultant working with interface "
        "monitoring, IDoc and API diagnostics, integration ownership, and incident "
        "resolution. This guide uses a practitioner-oriented approach to isolating "
        "failures before escalation or reprocessing."
    ),
    "sap-master-data": (
        "a Senior SAP Consultant working with Business Partner, "
        "customer and supplier data, replication diagnostics, and master-data governance. "
        "This guide focuses on the evidence needed to separate data, mapping, and "
        "ownership problems."
    ),
    "sap-ams": (
        "a Senior SAP Consultant working with recurring incidents, "
        "operational ownership, support improvement, and reusable support knowledge. "
        "This guide frames AMS decisions around the operating conditions that create "
        "repeated effort."
    ),
    "ai-sap-operations": (
        "a Senior SAP Consultant working with controlled AI "
        "workflows for SAP operations, support knowledge systems, authorization "
        "boundaries, and human review. This guide treats AI as a governed support "
        "capability rather than an autonomous decision-maker."
    ),
    "sap-architecture": (
        "a Senior SAP Consultant working with SAP architecture decisions, integration "
        "boundaries, extension strategy, and practical transformation planning."
    ),
    "sap-process-operations": (
        "a Senior SAP Consultant working with SD/MM process diagnostics, logistics "
        "execution, document flow, and operational improvement."
    ),
    "enterprise-operations": (
        "a Senior SAP Consultant who builds practical working methods for enterprise "
        "analysis, delivery control, documentation, and AI-assisted support work."
    ),
}


EXPERT_DOMAIN_META = {
    "sap-integration": {
        "expertise": ["SAP integration diagnostics", "AIF and IDoc monitoring", "interface ownership"],
        "problems": ["recurring interface failures", "unclear incident ownership", "insufficient operational visibility"],
        "service_url": "/services/sap-integration-reliability-assessment/",
        "cta_variant": "integration-monitoring",
        "cta_heading": "Working on a related SAP integration problem?",
        "cta_copy": "Dzmitryi Kharlanau provides focused architecture reviews, incident diagnostics, monitoring design, and improvement planning for SAP integration landscapes.",
    },
    "sap-master-data": {
        "expertise": ["SAP master data", "Business Partner and MDG", "customer and supplier replication"],
        "problems": ["replication failures", "data-quality drift", "unclear ownership of master-data defects"],
        "service_url": "/services/sap-master-data-stability-assessment/",
        "cta_variant": "master-data-replication",
        "cta_heading": "Working on a related SAP master-data problem?",
        "cta_copy": "Dzmitryi Kharlanau provides focused master-data replication analysis, governance reviews, and practical stabilization planning for SAP landscapes.",
    },
    "sap-ams": {
        "expertise": ["SAP AMS operations", "incident diagnostics", "operational knowledge"],
        "problems": ["recurring incidents", "weak support ownership", "knowledge loss during handover"],
        "service_url": "/services/sap-ams-consulting/",
        "cta_variant": "ams-improvement",
        "cta_heading": "Working on a related SAP AMS problem?",
        "cta_copy": "Dzmitryi Kharlanau helps SAP AMS teams reduce recurring incidents, clarify ownership, strengthen diagnostics, and plan safe operating-model improvements.",
    },
    "ai-sap-operations": {
        "expertise": ["controlled AI-assisted SAP support", "operational knowledge systems", "human-review boundaries"],
        "problems": ["unsafe AI pilots", "unstructured support knowledge", "unclear authorization and escalation boundaries"],
        "service_url": "/services/sap-ai-ml-enablement/",
        "cta_variant": "ai-readiness",
        "cta_heading": "Working on a related SAP AI problem?",
        "cta_copy": "Dzmitryi Kharlanau provides AI-readiness reviews for SAP operations, with attention to evidence, authorization boundaries, evaluation, and human review.",
    },
    "sap-architecture": {
        "expertise": ["SAP architecture", "integration boundaries", "extension and transformation decisions"],
        "problems": ["fragmented architecture ownership", "high change cost", "unclear modernization boundaries"],
        "service_url": "/services/sap-integration-architecture/",
        "cta_variant": "architecture-review",
        "cta_heading": "Working on a related SAP architecture problem?",
        "cta_copy": "Dzmitryi Kharlanau provides focused architecture reviews, boundary decisions, and practical transformation planning for SAP landscapes.",
    },
    "sap-process-operations": {
        "expertise": ["SAP SD/MM process diagnostics", "logistics operations", "document-flow analysis"],
        "problems": ["process blocks", "master-data and configuration ambiguity", "cross-team diagnostic delays"],
        "service_url": "/services/sap-o2c-process-audit/",
        "cta_variant": "diagnostic-review",
        "cta_heading": "Working on a related SAP process problem?",
        "cta_copy": "Dzmitryi Kharlanau provides focused process diagnostics, document-flow reviews, and improvement planning for SAP SD/MM and logistics operations.",
    },
    "enterprise-operations": {
        "expertise": ["enterprise analysis", "delivery control", "AI-assisted work documentation"],
        "problems": ["unclear requirements", "weak handovers", "unreviewed delivery decisions"],
        "service_url": "/services/sap-ams-consulting/",
        "cta_variant": "focused-implementation",
        "cta_heading": "Working on a related delivery problem?",
        "cta_copy": "Dzmitryi Kharlanau provides practical analysis, documentation, review, and implementation support for enterprise delivery work around SAP.",
    },
}


def _expert_domain(rel_path, fm):
    """Infer a controlled expert domain from public taxonomy and topic signals."""
    explicit = (fm.get("expert_context") or {}).get("domain")
    if explicit in EXPERT_DOMAIN_META:
        return explicit
    text = " ".join(str(fm.get(k, "")) for k in ("title", "description", "domain", "subdomain", "sap_area", "business_process", "tags"))
    lower = f"{rel_path} {text}".lower()
    if any(term in lower for term in ("aif", "idoc", "integration", "interface", "middleware", "rfc", "api", "ale", "odata", "soap", "event-driven")):
        return "sap-integration"
    if any(term in lower for term in ("master data", "master-data", "mdg", "business partner", "customer master", "vendor master", "supplier")):
        return "sap-master-data"
    if any(term in lower for term in ("ai-operations", "ai-assisted", "ai agent", "ai agents", "ai/", "artificial intelligence", "automation", "operational memory", "mcp")):
        return "ai-sap-operations"
    if any(term in lower for term in ("architecture", "transformation", "extension", "clean core", "landscape", "capability mapping")):
        return "sap-architecture"
    if any(term in lower for term in ("sd", "mm", "o2c", "order to cash", "procure to pay", "logistics", "retail", "ewm", "mrp", "inventory", "pricing", "goods receipt", "purchase")):
        return "sap-process-operations"
    if any(term in lower for term in ("sap-ams", "ams", "incident", "support", "diagnostic", "runbook", "handover")):
        return "sap-ams"
    return "enterprise-operations" if rel_path.startswith("skill-hub/") else "sap-ams"


def _expert_candidate(rel_path, fm):
    """Return whether a reviewed page is substantial enough for contextual promotion."""
    if not _is_retrieval_eligible(fm):
        return False
    if rel_path.startswith("atlas/"):
        return not rel_path.endswith("/index.md")
    if rel_path.startswith("skill-hub/"):
        excluded = ("/index.md", "skill-page-template.md", "artifact-templates.md", "framework-map.md", "quality-rules.md", "agent-usage-guide.md")
        return not any(rel_path.endswith(suffix) for suffix in excluded)
    if rel_path.startswith("scenarios/"):
        return not rel_path.endswith("/index.md")
    if rel_path.startswith(("research/", "_blog/", "_notes/")):
        return True
    return bool((fm.get("expert_context") or {}).get("enabled"))


def _eligible_evidence(all_pages, expert, current_url, domain):
    """Resolve two to five reviewed evidence links, preferring explicit links."""
    urls = list(expert.get("evidence_urls") or [])
    related = expert.get("related") or []
    for candidate in related:
        if candidate not in urls:
            urls.append(candidate)
    same_domain = []
    for url, info in sorted(all_pages.items()):
        if url == current_url or not _is_retrieval_eligible(info["fm"]):
            continue
        if _expert_domain(info["file"], info["fm"]) == domain:
            same_domain.append(url)
    for candidate in same_domain:
        if candidate not in urls:
            urls.append(candidate)
    result = []
    for url in urls:
        target = all_pages.get(url)
        if not target or not _expert_candidate(target["file"], target["fm"]):
            continue
        result.append({"url": url, "title": target.get("title") or target["fm"].get("title", "")})
        if len(result) >= 5:
            break
    return result


def build_expert_context(rel_path, fm, all_pages, body=""):
    """Build the canonical, generated expert metadata for one public page."""
    if not _expert_candidate(rel_path, fm):
        return None
    explicit = fm.get("expert_context") or {}
    domain = _expert_domain(rel_path, fm)
    base = copy.deepcopy(EXPERT_DOMAIN_META[domain])
    base.update({k: serialize_value(v) for k, v in explicit.items() if k not in {"enabled", "domain", "evidence_urls"}})
    base["enabled"] = True
    base["domain"] = domain
    base["expertise"] = base.get("expertise") or base.get("topics") or EXPERT_DOMAIN_META[domain]["expertise"]
    base["problems"] = base.get("problems") or EXPERT_DOMAIN_META[domain]["problems"]
    base["service_url"] = explicit.get("service_url") or base["service_url"]
    evidence_source = dict(explicit)
    evidence_source["related"] = fm.get("related") or []
    base["evidence"] = _eligible_evidence(all_pages, evidence_source, fm.get("permalink", ""), domain)
    base["evidence_urls"] = [item["url"] for item in base["evidence"]]
    base["placement"] = "source" if "atlas/expert-context.html" in body else "layout"
    return base


def _expert_public_metadata(expert):
    if not expert:
        return None
    return {key: expert[key] for key in ("enabled", "domain", "expertise", "problems", "service_url", "evidence_urls", "cta_variant", "cta_heading", "cta_copy", "placement") if key in expert}


def expert_context_markdown(fm, rel_path, all_pages, body=""):
    """Return the public expert context represented by an enabled article block."""
    expert = build_expert_context(rel_path, fm, all_pages, body)
    if not expert:
        return ""

    context_copy = EXPERT_CONTEXT_COPY.get(expert.get("domain"))
    if not context_copy:
        return ""

    lines = [
        "EXPERT CONTEXT:",
        f"This guide was prepared by Dzmitryi Kharlanau, {context_copy}",
        "Professional website: https://dkharlanau.github.io/",
        "Profile and experience: https://dkharlanau.github.io/about/",
        "LinkedIn: https://www.linkedin.com/in/dkharlanau/",
        "",
        expert.get("cta_heading", "WORKING ON A RELATED SAP PROBLEM?").upper(),
        expert.get("cta_copy", "Dzmitryi Kharlanau provides focused diagnostics, architecture reviews, improvement planning, and practical implementation support."),
        f"Related service: {canonical_url(expert.get('service_url', ''))}",
    ]
    evidence_urls = expert.get("evidence_urls") or []
    if evidence_urls:
        lines.append("Related evidence:")
        lines.extend(f"- {canonical_url(url)}" for url in evidence_urls)
    return "\n".join(lines)


def generate_verified_inventory(all_pages, check_mode=False):
    """Generate ai/verified-pages.json — site-wide verified, indexable pages.

    Includes any page with verified=true and status=reviewed that is not
    marked noindex or sitemap=false. Source file paths are excluded.
    """
    entries = []
    for permalink, info in all_pages.items():
        rel_path = info["file"]
        fm = info["fm"]

        # Skip template and excluded paths
        if rel_path.startswith("docs/templates/"):
            continue
        if not fm.get("verified"):
            continue
        if fm.get("status") != "reviewed":
            continue
        if not _is_indexable(fm):
            continue

        page_type = _derive_page_type(rel_path)
        section = _derive_section(rel_path, fm)

        body = parse_frontmatter(REPO_DIR / rel_path)[1]
        expert_context = build_expert_context(rel_path, fm, all_pages, body)
        entry = {
            "url": canonical_url(permalink),
            "title": fm.get("title", ""),
            "description": fm.get("description", ""),
            "type": page_type,
            "section": section,
            "status": fm.get("status", ""),
            "verified": bool(fm.get("verified")),
            "last_reviewed": serialize_value(fm.get("last_reviewed", "")),
            "last_modified_at": serialize_value(fm.get("last_modified_at", "")),
            "author": fm.get("author", ""),
            "tags": fm.get("tags", []) or [],
        }
        if expert_context:
            entry["expert_context"] = _expert_public_metadata(expert_context)
        entries.append(entry)

    entries.sort(key=lambda e: (e["type"], e["section"], e["url"]))

    inventory = {
        "schema": "dkharlanau.site.verified_pages",
        "schema_version": "2.0",
        "generated_at": _now(check_mode),
        "canonical_url": "https://dkharlanau.github.io/ai/verified-pages.json",
        "description": (
            "Machine-readable inventory of all reviewed and verified indexable "
            "pages across the public site. Intended for AI agents and search "
            "crawlers that need to know which pages are trustworthy and "
            "retrieval-ready."
        ),
        "source": "scripts/generate_atlas_artifacts.py",
        "count": len(entries),
        "collections": sorted({e["type"] for e in entries}),
        "entries": entries,
    }

    if not check_mode:
        out_path = REPO_DIR / "ai" / "verified-pages.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(inventory, f, indent=2, ensure_ascii=False, cls=DateTimeEncoder)

    return inventory


def generate_manifest(all_pages, atlas_files, check_mode=False):
    """Generate the public manifest of retrieval-eligible Atlas pages."""
    entries = []
    for rel_path in atlas_files:
        abs_path = REPO_DIR / rel_path
        fm, body = parse_frontmatter(abs_path)

        if not _is_retrieval_eligible(fm):
            continue

        related = []
        for related_url in fm.get("related", []) or []:
            target = all_pages.get(related_url)
            if target and _is_retrieval_eligible(target["fm"]):
                related.append(canonical_url(related_url))
        tags = fm.get("tags", []) or []

        expert_context = build_expert_context(rel_path, fm, all_pages, body)
        entry = {
            "title": fm.get("title", ""),
            "description": fm.get("description", ""),
            "url": canonical_url(fm.get("permalink", "")),
            "atlas_section": fm.get("atlas_section", ""),
            "domain": fm.get("domain", ""),
            "subdomain": fm.get("subdomain", ""),
            "concept_type": fm.get("concept_type", ""),
            "sap_area": fm.get("sap_area", ""),
            "business_process": fm.get("business_process", ""),
            "status": fm.get("status", ""),
            "verified": bool(fm.get("verified", False)),
            "last_reviewed": serialize_value(fm.get("last_reviewed", "")),
            "author": fm.get("author", ""),
            "tags": tags,
            "related": serialize_value(related),
        }
        if expert_context:
            entry["expert_context"] = _expert_public_metadata(expert_context)
        entries.append(entry)

    manifest = {
        "schema": "dkharlanau.atlas.manifest",
        "schema_version": "2.0",
        "generated_at": _now(check_mode),
        "canonical_url": "https://dkharlanau.github.io/atlas/manifest.json",
        "description": (
            "Canonical manifest of reviewed, verified, indexable Atlas articles "
            "and their eligible public relationships."
        ),
        "count": len(entries),
        "verified_count": sum(1 for e in entries if e["verified"]),
        "unverified_count": sum(1 for e in entries if not e["verified"]),
        "eligibility_policy": "verified=true; status=reviewed; indexable; sitemap-enabled",
        "sections": sorted({e["atlas_section"] for e in entries}),
        "entries": entries,
    }

    if not check_mode:
        out_path = REPO_DIR / "atlas" / "manifest.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False, cls=DateTimeEncoder)

    return manifest


def generate_llms_full(all_pages, atlas_files, check_mode=False):
    """Generate llms-full.txt with verified pages only. Returns text. Writes to disk unless check_mode."""
    lines = []
    lines.append("Atlas Full-Text Manifest")
    lines.append("=" * 50)
    lines.append(f"Generated: {_now(check_mode)}")
    lines.append("Canonical: https://dkharlanau.github.io/llms-full.txt")
    lines.append("Source: https://dkharlanau.github.io/atlas/manifest.json")
    lines.append("")
    lines.append("This file contains the full text of reviewed and verified Atlas pages only.")
    lines.append("Pages with status=needs_verification or verified=false are excluded.")
    lines.append("Source file paths are excluded to protect private draft locations.")
    lines.append("")
    lines.append("=" * 50)
    lines.append("")

    verified_count = 0
    for rel_path in atlas_files:
        abs_path = REPO_DIR / rel_path
        fm, body = parse_frontmatter(abs_path)

        if not _is_retrieval_eligible(fm):
            continue

        verified_count += 1
        title = fm.get("title", "Untitled")
        url = canonical_url(fm.get("permalink", ""))
        tags = fm.get("tags", []) or []

        lines.append(f"PAGE: {title}")
        lines.append(f"URL: {url}")
        lines.append(f"SECTION: {fm.get('atlas_section', '')}")
        lines.append(f"DOMAIN: {fm.get('domain', '')}")
        lines.append(f"TYPE: {fm.get('concept_type', '')}")
        lines.append(f"SAP AREA: {fm.get('sap_area', '')}")
        lines.append(f"BUSINESS PROCESS: {fm.get('business_process', '')}")
        lines.append(f"TAGS: {', '.join(tags)}")
        lines.append(f"REVIEWED: {serialize_value(fm.get('last_reviewed', ''))}")
        lines.append("-" * 40)

        clean_body = strip_jekyll_and_html(body)
        lines.append("\n".join(line.rstrip() for line in clean_body.splitlines()))
        expert_block = expert_context_markdown(fm, rel_path, all_pages, body)
        if expert_block:
            lines.append("")
            lines.append(expert_block)
        lines.append("")
        lines.append("=" * 50)
        lines.append("")

    lines.append(f"END OF MANIFEST — {verified_count} verified pages included")

    text = "\n".join(lines)

    if not check_mode:
        out_path = REPO_DIR / "llms-full.txt"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)

    return text


def generate_expert_artifacts(all_pages, check_mode=False):
    """Generate the sitewide expert metadata, evidence index, and decision inventory."""
    promotion = {}
    evidence_by_domain = {domain: [] for domain in EXPERT_DOMAIN_META}
    inventory_entries = []

    for permalink, info in sorted(all_pages.items()):
        rel_path = info["file"]
        fm = info["fm"]
        body = parse_frontmatter(REPO_DIR / rel_path)[1]
        eligible = _is_retrieval_eligible(fm)
        candidate = _expert_candidate(rel_path, fm)
        expert = build_expert_context(rel_path, fm, all_pages, body) if candidate else None
        if expert:
            public_context = _expert_public_metadata(expert)
            promotion[permalink] = public_context
            domain = expert["domain"]
            domain_entry = {
                "title": fm.get("title", ""),
                "canonical_url": canonical_url(permalink),
                "content_type": _derive_page_type(rel_path),
                "verification_status": "reviewed",
                "url_path": permalink,
            }
            evidence_by_domain.setdefault(domain, []).append(domain_entry)
            decision = "enabled"
            reason = "Reviewed, verified, indexable, public-safe, and substantial enough to serve as professional evidence."
        elif eligible:
            decision = "excluded"
            reason = "Reviewed and indexable, but treated as navigation, template, thin, or non-article content."
        else:
            decision = "deferred"
            reason = "Not promoted until human verification and indexability requirements are met."

        inventory_entries.append({
            "source_file": rel_path,
            "content_type": _derive_page_type(rel_path),
            "canonical_url": canonical_url(permalink),
            "indexable": _is_indexable(fm),
            "verified": bool(fm.get("verified") is True),
            "status": fm.get("status", ""),
            "title": fm.get("title", ""),
            "expert_domain": expert.get("domain") if expert else (_expert_domain(rel_path, fm) if eligible else ""),
            "decision": decision,
            "reason": reason,
        })

    config = {
        "schema": "dkharlanau.expert_context",
        "schema_version": "1.0",
        "generated_by": "scripts/generate_atlas_artifacts.py",
        "entries": promotion,
    }
    evidence = {
        "schema": "dkharlanau.expert_evidence",
        "schema_version": "1.0",
        "canonical_url": f"{BASE_URL}/ai/expert-evidence.json",
        "expert": {
            "name": "Dzmitryi Kharlanau",
            "website": BASE_URL + "/",
            "profile": BASE_URL + "/about/",
            "linkedin": "https://www.linkedin.com/in/dkharlanau/",
        },
        "domains": [],
    }
    for domain, meta in EXPERT_DOMAIN_META.items():
        evidence["domains"].append({
            "id": domain,
            "label": domain.replace("-", " ").title(),
            "can_help_with": meta["problems"],
            "evidence": sorted(evidence_by_domain.get(domain, []), key=lambda item: item["canonical_url"]),
            "services": [canonical_url(meta["service_url"])],
        })
    inventory = {
        "schema": "dkharlanau.expert_promotion_inventory",
        "schema_version": "1.0",
        "canonical_url": f"{BASE_URL}/ai/expert-promotion-inventory.json",
        "summary": {
            "enabled": sum(1 for item in inventory_entries if item["decision"] == "enabled"),
            "excluded": sum(1 for item in inventory_entries if item["decision"] == "excluded"),
            "deferred": sum(1 for item in inventory_entries if item["decision"] == "deferred"),
        },
        "entries": inventory_entries,
    }

    if not check_mode:
        with (REPO_DIR / "_data" / "expert_context.yml").open("w", encoding="utf-8") as f:
            yaml.safe_dump(config, f, allow_unicode=True, sort_keys=False)
        with (REPO_DIR / "ai" / "expert-evidence.json").open("w", encoding="utf-8") as f:
            json.dump(evidence, f, indent=2, ensure_ascii=False, cls=DateTimeEncoder)
        with (REPO_DIR / "ai" / "expert-promotion-inventory.json").open("w", encoding="utf-8") as f:
            json.dump(inventory, f, indent=2, ensure_ascii=False, cls=DateTimeEncoder)
    return config, evidence, inventory


def generate_related(all_pages, atlas_files, check_mode=False):
    """Generate the public related graph for retrieval-eligible Atlas pages."""
    edges = []
    broken_links = []

    for rel_path in atlas_files:
        abs_path = REPO_DIR / rel_path
        fm, _ = parse_frontmatter(abs_path)
        permalink = fm.get("permalink", "")
        if not _is_retrieval_eligible(fm):
            continue
        title = fm.get("title", "")
        section = fm.get("atlas_section", "")
        tags = fm.get("tags", []) or []
        related = fm.get("related", []) or []

        for link in related:
            target = all_pages.get(link)
            edge_base = {
                "source_url": canonical_url(permalink),
                "source_title": title,
                "source_section": section,
                "source_status": fm.get("status", ""),
                "source_verified": bool(fm.get("verified", False)),
                "source_tags": tags,
            }
            if target and _is_retrieval_eligible(target["fm"]):
                edges.append({
                    **edge_base,
                    "target_url": canonical_url(link),
                    "target_title": target["title"],
                    "target_file": target["file"],
                    "relation_source": "frontmatter",
                    "valid": True,
                })
            else:
                # Try file-path resolution as fallback
                file_guess = link.strip("/") + ".md"
                abs_guess = REPO_DIR / file_guess
                if abs_guess.exists():
                    target_fm, _ = parse_frontmatter(abs_guess)
                    if _is_retrieval_eligible(target_fm):
                        edges.append({
                            **edge_base,
                            "target_url": canonical_url(link),
                            "target_title": target_fm.get("title", ""),
                            "target_file": file_guess,
                            "relation_source": "frontmatter",
                            "valid": True,
                        })
                else:
                    broken_links.append({
                        "source_url": canonical_url(permalink),
                        "source_title": title,
                        "target_url": canonical_url(link),
                        "reason": "target page not found",
                    })

    related_json = {
        "schema": "dkharlanau.atlas.related",
        "schema_version": "2.0",
        "generated_at": _now(check_mode),
        "canonical_url": "https://dkharlanau.github.io/ai/rag/related.json",
        "description": (
            "Static related-content graph for reviewed, verified, indexable "
            "Atlas pages. Generated from frontmatter 'related' fields for "
            "agent navigation and controlled RAG ingestion."
        ),
        "eligibility_policy": "source and target are verified, reviewed, indexable, and sitemap-enabled",
        "count": len(edges),
        "broken_link_count": len(broken_links),
        "edges": edges,
        "warnings": broken_links,
    }

    if not check_mode:
        out_dir = REPO_DIR / "ai" / "rag"
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "related.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(related_json, f, indent=2, ensure_ascii=False, cls=DateTimeEncoder)

    return edges, broken_links, related_json


def _normalize_timestamp_in_json(text):
    """Replace generated_at timestamp with CHECK_MODE placeholder for comparison."""
    return re.sub(
        r'"generated_at":\s*"[^"]+"',
        f'"generated_at": "{CHECK_MODE_TIMESTAMP}"',
        text,
    )


def _normalize_timestamp_in_llms(text):
    """Replace Generated: timestamp with CHECK_MODE placeholder for comparison."""
    return re.sub(
        r'^Generated:\s*\S+',
        f'Generated: {CHECK_MODE_TIMESTAMP}',
        text,
        flags=re.MULTILINE,
    )


def _load_json_file(path):
    """Load and return JSON file contents as string."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def _load_text_file(path):
    """Load and return text file contents as string."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def run_check(all_pages, atlas_files):
    """Validate existing artifacts against regenerated content. Returns list of issues."""
    issues = []

    # --- manifest.json ---
    print("\n[CHECK 1/6] manifest.json")
    manifest_generated = generate_manifest(all_pages, atlas_files, check_mode=True)
    manifest_path = REPO_DIR / "atlas" / "manifest.json"
    if not manifest_path.exists():
        issues.append("manifest.json: file missing")
    else:
        try:
            manifest_committed_text = _load_json_file(manifest_path)
            manifest_committed = json.loads(manifest_committed_text)
        except json.JSONDecodeError as e:
            issues.append(f"manifest.json: invalid JSON — {e}")
            manifest_committed = {}

        if manifest_committed:
            # Normalize timestamps
            gen_norm = json.loads(_normalize_timestamp_in_json(json.dumps(manifest_generated, indent=2, ensure_ascii=False, cls=DateTimeEncoder)))
            com_norm = json.loads(_normalize_timestamp_in_json(manifest_committed_text))
            if gen_norm != com_norm:
                issues.append("manifest.json: stale — committed file differs from source")
            else:
                print("  ✓ manifest.json is up to date")

        # Semantic checks — compare committed against generated expectations
        expected_count = manifest_generated.get("count")
        expected_verified = manifest_generated.get("verified_count")
        expected_unverified = manifest_generated.get("unverified_count")
        if manifest_committed.get("count") != expected_count:
            issues.append(f"manifest.json: expected {expected_count} entries, found {manifest_committed.get('count')}")
        if manifest_committed.get("verified_count") != expected_verified:
            issues.append(f"manifest.json: expected {expected_verified} verified, found {manifest_committed.get('verified_count')}")
        if manifest_committed.get("unverified_count") != expected_unverified:
            issues.append(f"manifest.json: expected {expected_unverified} unverified, found {manifest_committed.get('unverified_count')}")

    # --- llms-full.txt ---
    print("\n[CHECK 2/6] llms-full.txt")
    llms_generated = generate_llms_full(all_pages, atlas_files, check_mode=True)
    llms_path = REPO_DIR / "llms-full.txt"
    if not llms_path.exists():
        issues.append("llms-full.txt: file missing")
    else:
        llms_committed = _load_text_file(llms_path)
        gen_norm = _normalize_timestamp_in_llms(llms_generated)
        com_norm = _normalize_timestamp_in_llms(llms_committed)
        if gen_norm != com_norm:
            issues.append("llms-full.txt: stale — committed file differs from source")
        else:
            print("  ✓ llms-full.txt is up to date")

    # Semantic checks on committed file
    if llms_path.exists():
        # Verify only reviewed+verified pages included
        for rel_path in atlas_files:
            abs_path = REPO_DIR / rel_path
            fm, _ = parse_frontmatter(abs_path)
            title = fm.get("title", "")
            if _is_retrieval_eligible(fm):
                if f"PAGE: {title}" not in llms_committed:
                    issues.append(f"llms-full.txt: missing verified page '{title}'")
            else:
                if f"PAGE: {title}" in llms_committed:
                    issues.append(f"llms-full.txt: unverified page '{title}' should not be included")

        # Private path leak check
        leak_patterns = ["source_files", "private-source", "kb-drafts", "/Users/", ".env"]
        for pattern in leak_patterns:
            if pattern in llms_committed:
                issues.append(f"llms-full.txt: private leak — contains '{pattern}'")

        # LinkedIn export name check
        if "Basic_LinkedInDataExport" in llms_committed or "Basic_LinkInDataExport" in llms_committed:
            issues.append("llms-full.txt: contains LinkedIn export reference")

    # --- related.json ---
    print("\n[CHECK 3/6] related.json")
    edges, broken_links, related_generated = generate_related(all_pages, atlas_files, check_mode=True)
    related_path = REPO_DIR / "ai" / "rag" / "related.json"
    if not related_path.exists():
        issues.append("related.json: file missing")
    else:
        try:
            related_committed_text = _load_json_file(related_path)
            related_committed = json.loads(related_committed_text)
        except json.JSONDecodeError as e:
            issues.append(f"related.json: invalid JSON — {e}")
            related_committed = {}

        if related_committed:
            gen_norm = json.loads(_normalize_timestamp_in_json(json.dumps(related_generated, indent=2, ensure_ascii=False, cls=DateTimeEncoder)))
            com_norm = json.loads(_normalize_timestamp_in_json(related_committed_text))
            if gen_norm != com_norm:
                issues.append("related.json: stale — committed file differs from source")
            else:
                print("  ✓ related.json is up to date")

        # Semantic checks — compare committed against generated expectations
        expected_edges = len(edges)
        if related_committed.get("count") != expected_edges:
            issues.append(f"related.json: expected {expected_edges} edges, found {related_committed.get('count')}")
        if related_committed.get("broken_link_count") != 0:
            issues.append(f"related.json: expected 0 broken links, found {related_committed.get('broken_link_count')}")
        if related_committed.get("warnings"):
            issues.append(f"related.json: warnings array not empty")

        # Private path leak check
        for pattern in leak_patterns:
            if pattern in related_committed_text:
                issues.append(f"related.json: private leak — contains '{pattern}'")

    # --- compact signal index ---
    print("\n[CHECK 4/6] atlas-compact-index.json")
    compact_generated = generate_compact_signal_index(atlas_files, check_mode=True, all_pages=all_pages)
    compact_path = REPO_DIR / "ai" / "atlas-compact-index.json"
    compact_committed = {}
    compact_committed_text = ""
    if not compact_path.exists():
        issues.append("atlas-compact-index.json: file missing")
    else:
        try:
            compact_committed_text = _load_json_file(compact_path)
            compact_committed = json.loads(compact_committed_text)
        except json.JSONDecodeError as e:
            issues.append(f"atlas-compact-index.json: invalid JSON — {e}")

    if compact_committed:
        gen_norm = json.loads(_normalize_timestamp_in_json(json.dumps(compact_generated, indent=2, ensure_ascii=False, cls=DateTimeEncoder)))
        com_norm = json.loads(_normalize_timestamp_in_json(compact_committed_text))
        if gen_norm != com_norm:
            issues.append("atlas-compact-index.json: stale — committed file differs from source")
        else:
            print("  ✓ atlas-compact-index.json is up to date")

        expected_compact_count = len(compact_generated.get("entries", []))
        if compact_committed.get("count") != expected_compact_count:
            issues.append(f"atlas-compact-index.json: expected {expected_compact_count} entries, found {compact_committed.get('count')}")
        for entry in compact_committed.get("entries", []):
            path = entry.get("path", "")
            if not path or not (REPO_DIR / path).exists():
                issues.append(f"atlas-compact-index.json: entry path missing: {path}")
            if not entry.get("url", "").startswith(f"{BASE_URL}/atlas/"):
                issues.append(f"atlas-compact-index.json: invalid Atlas URL for {path}")
            if not entry.get("matching_terms"):
                issues.append(f"atlas-compact-index.json: missing matching_terms for {path}")

        for pattern in leak_patterns:
            if pattern in compact_committed_text:
                issues.append(f"atlas-compact-index.json: private leak — contains '{pattern}'")

    # --- expert promotion artifacts ---
    print("\n[CHECK 5/9] expert promotion artifacts")
    expert_config, expert_evidence, expert_inventory = generate_expert_artifacts(all_pages, check_mode=True)
    expert_config_path = REPO_DIR / "_data" / "expert_context.yml"
    expert_evidence_path = REPO_DIR / "ai" / "expert-evidence.json"
    expert_inventory_path = REPO_DIR / "ai" / "expert-promotion-inventory.json"
    if not expert_config_path.exists():
        issues.append("_data/expert_context.yml: file missing")
    else:
        committed = yaml.safe_load(expert_config_path.read_text(encoding="utf-8")) or {}
        if committed != expert_config:
            issues.append("_data/expert_context.yml: stale — committed file differs from source")
        else:
            print("  ✓ _data/expert_context.yml is up to date")
    for path, expected in ((expert_evidence_path, expert_evidence), (expert_inventory_path, expert_inventory)):
        if not path.exists():
            issues.append(f"{path.relative_to(REPO_DIR)}: file missing")
            continue
        try:
            committed = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            issues.append(f"{path.relative_to(REPO_DIR)}: invalid JSON — {exc}")
            continue
        if committed != expected:
            issues.append(f"{path.relative_to(REPO_DIR)}: stale — committed file differs from source")
        else:
            print(f"  ✓ {path.relative_to(REPO_DIR)} is up to date")

    # --- verified-pages.json ---
    print("\n[CHECK 6/9] verified-pages.json")
    inventory_generated = generate_verified_inventory(all_pages, check_mode=True)
    inventory_path = REPO_DIR / "ai" / "verified-pages.json"
    inventory_committed = {}
    inventory_committed_text = ""
    if not inventory_path.exists():
        issues.append("verified-pages.json: file missing")
    else:
        try:
            inventory_committed_text = _load_json_file(inventory_path)
            inventory_committed = json.loads(inventory_committed_text)
        except json.JSONDecodeError as e:
            issues.append(f"verified-pages.json: invalid JSON — {e}")

        if inventory_committed:
            gen_norm = json.loads(_normalize_timestamp_in_json(json.dumps(inventory_generated, indent=2, ensure_ascii=False, cls=DateTimeEncoder)))
            com_norm = json.loads(_normalize_timestamp_in_json(inventory_committed_text))
            if gen_norm != com_norm:
                issues.append("verified-pages.json: stale — committed file differs from source")
            else:
                print("  ✓ verified-pages.json is up to date")

        expected_inventory_count = len(inventory_generated.get("entries", []))
        if inventory_committed.get("count") != expected_inventory_count:
            issues.append(f"verified-pages.json: expected {expected_inventory_count} entries, found {inventory_committed.get('count')}")

        for entry in inventory_committed.get("entries", []):
            if not entry.get("url", "").startswith(f"{BASE_URL}/"):
                issues.append(f"verified-pages.json: invalid URL {entry.get('url')}")
            if not entry.get("title"):
                issues.append(f"verified-pages.json: missing title for {entry.get('url')}")
            if not entry.get("type"):
                issues.append(f"verified-pages.json: missing type for {entry.get('url')}")

        for pattern in leak_patterns:
            if pattern in inventory_committed_text:
                issues.append(f"verified-pages.json: private leak — contains '{pattern}'")

    # --- Markdown cluster index ---
    print("\n[CHECK 7/9] markdown-clusters.json")
    markdown_clusters_generated = generate_markdown_clusters(all_pages, check_mode=True)
    markdown_clusters_path = REPO_DIR / "ai" / "markdown-clusters.json"
    if not markdown_clusters_path.exists():
        issues.append("markdown-clusters.json: file missing")
    else:
        markdown_clusters_text = _load_json_file(markdown_clusters_path)
        try:
            markdown_clusters_committed = json.loads(markdown_clusters_text)
        except json.JSONDecodeError as e:
            issues.append(f"markdown-clusters.json: invalid JSON — {e}")
            markdown_clusters_committed = {}
        if markdown_clusters_committed:
            gen_norm = json.loads(_normalize_timestamp_in_json(json.dumps(markdown_clusters_generated, indent=2, ensure_ascii=False, cls=DateTimeEncoder)))
            com_norm = json.loads(_normalize_timestamp_in_json(markdown_clusters_text))
            if gen_norm != com_norm:
                issues.append("markdown-clusters.json: stale — committed file differs from source")
            else:
                print("  ✓ markdown-clusters.json is up to date")
            expected_markdown_pages = len(markdown_clusters_generated.get("entries", []))
            if markdown_clusters_committed.get("summary", {}).get("markdown_pages") != expected_markdown_pages:
                issues.append("markdown-clusters.json: page count does not match Markdown source discovery")
            for entry in markdown_clusters_committed.get("entries", []):
                if entry.get("canonical_url") and not entry.get("canonical_url", "").startswith(f"{BASE_URL}/"):
                    issues.append(f"markdown-clusters.json: invalid URL {entry.get('canonical_url')}")
                if not entry.get("clusters"):
                    issues.append(f"markdown-clusters.json: missing clusters for {entry.get('source_file')}")

    # --- Cross-validate manifest vs related ---
    print("\n[CHECK 8/9] Cross-validation")
    if manifest_committed and related_committed:
        manifest_urls = {e["url"] for e in manifest_committed.get("entries", [])}
        related_sources = {e["source_url"] for e in related_committed.get("edges", [])}
        related_targets = {e["target_url"] for e in related_committed.get("edges", [])}
        # All related sources must be in manifest
        orphan_sources = related_sources - manifest_urls
        if orphan_sources:
            issues.append(f"related.json: sources not in manifest: {orphan_sources}")
        else:
            print("  ✓ All related sources present in manifest")

    # --- Frontmatter tag consistency ---
    print("\n[CHECK 9/9] Frontmatter tag consistency")
    tag_issues = []
    for rel_path in atlas_files:
        abs_path = REPO_DIR / rel_path
        fm, _ = parse_frontmatter(abs_path)
        tags = fm.get("tags", []) or []
        if not tags:
            tag_issues.append(f"{rel_path}: no tags")
        for tag in tags:
            if not re.match(r'^[a-z0-9-]+$', tag):
                tag_issues.append(f"{rel_path}: invalid tag '{tag}'")
    if tag_issues:
        issues.extend(tag_issues)
    else:
        print(f"  ✓ All {len(atlas_files)} articles have valid tags")

    return issues


def main():
    parser = argparse.ArgumentParser(
        description="Regenerate Atlas static discovery artifacts."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate existing artifacts without regenerating.",
    )
    args = parser.parse_args()

    print("Atlas Artifact Generator")
    print("=" * 40)

    # Build permalink map for the whole site
    all_pages = build_permalink_map()
    print(f"Site pages indexed: {len(all_pages)}")

    # Discover Atlas articles dynamically
    atlas_files = discover_atlas_articles()
    print(f"Atlas articles discovered: {len(atlas_files)}")

    if args.check:
        print("\n[CHECK MODE] Validating existing artifacts...")
        issues = run_check(all_pages, atlas_files)
        print("\n" + "=" * 40)
        if issues:
            print(f"CHECK FAILED — {len(issues)} issue(s):")
            for issue in issues:
                print(f"  ✗ {issue}")
            sys.exit(1)
        else:
            print("CHECK PASSED — all artifacts are up to date and valid.")
            sys.exit(0)

    # Generate manifest
    print("\n[1/5] Generating atlas/manifest.json ...")
    manifest = generate_manifest(all_pages, atlas_files)
    print(f"  Entries: {manifest['count']}")
    print(f"  Verified: {manifest['verified_count']}")
    print(f"  Unverified: {manifest['unverified_count']}")

    # Generate llms-full.txt
    print("\n[2/5] Generating llms-full.txt ...")
    llms_full_text = generate_llms_full(all_pages, atlas_files)
    verified_count = len(re.findall(r"^PAGE: ", llms_full_text, flags=re.MULTILINE))
    print(f"  Verified pages included: {verified_count}")

    # Generate related.json
    print("\n[3/5] Generating ai/rag/related.json ...")
    edges, broken, _ = generate_related(all_pages, atlas_files)
    print(f"  Edges: {len(edges)}")
    print(f"  Broken links: {len(broken)}")
    if broken:
        for bl in broken:
            print(f"    BROKEN: {bl['source_url']} -> {bl['target_url']}")

    # Generate compact signal index
    print("\n[4/5] Generating ai/atlas-compact-index.json ...")
    compact_index = generate_compact_signal_index(atlas_files, all_pages=all_pages)
    print(f"  Entries: {compact_index['count']}")

    # Generate verified page inventory
    print("\n[5/5] Generating ai/verified-pages.json ...")
    inventory = generate_verified_inventory(all_pages)
    print(f"  Verified pages: {inventory['count']}")
    print(f"  Collections: {', '.join(inventory['collections'])}")

    print("\n[6/9] Generating expert promotion artifacts ...")
    _, expert_evidence, expert_inventory = generate_expert_artifacts(all_pages)
    print(f"  Enabled pages: {expert_inventory['summary']['enabled']}")
    print(f"  Deferred pages: {expert_inventory['summary']['deferred']}")

    print("\n[7/9] Generating Markdown cluster index ...")
    markdown_clusters = generate_markdown_clusters(all_pages)
    print(f"  Markdown pages: {markdown_clusters['summary']['markdown_pages']}")
    print(f"  Structurally ready: {markdown_clusters['summary']['ready_pages']}")
    print(f"  Retrieval-eligible: {markdown_clusters['summary']['reviewed_retrieval_pages']}")

    print("\n" + "=" * 40)
    print("All artifacts generated successfully.")
    print("Run 'git diff' to review changes before committing.")


if __name__ == "__main__":
    main()
