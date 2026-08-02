#!/usr/bin/env python3
"""Deterministic publication-quality and AI-search readiness pipeline.

This is the single entry point for source-content audits, CI checks, reports,
safe derived-artifact regeneration, and historical warning baselines. It is
deliberately heuristic: it validates publication structure and evidence
signals, not the truth of technical claims.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))

from lib.content_model import (  # noqa: E402
    ContentPage,
    canonical_url,
    discover_pages,
    normalize_text,
    stable_fingerprint,
    word_count,
)


CONFIG_PATH = REPO_ROOT / "config" / "content-quality.yml"
REPORT_DIR = REPO_ROOT / "reports"
BASE_URL = "https://dkharlanau.github.io"


@dataclass
class Finding:
    rule_id: str
    severity: str
    message: str
    path: str
    location: str = ""
    remediation: str = ""
    safe_fixable: bool = False
    fingerprint: str = ""

    def as_dict(self) -> dict[str, Any]:
        return {
            "rule_id": self.rule_id,
            "severity": self.severity,
            "message": self.message,
            "source_path": self.path,
            "location": self.location,
            "remediation": self.remediation,
            "safe_fixable": self.safe_fixable,
            "fingerprint": self.fingerprint,
        }


def load_config() -> dict[str, Any]:
    with CONFIG_PATH.open(encoding="utf-8") as handle:
        config = yaml.safe_load(handle) or {}
    required = {"canonical", "content_models", "weights", "guidance", "private_patterns", "prompt_injection_patterns"}
    missing = required - set(config)
    if missing:
        raise ValueError(f"content-quality.yml missing required sections: {', '.join(sorted(missing))}")
    return config


def add_finding(findings: list[Finding], page: ContentPage | None, rule_id: str, severity: str, message: str, location: str = "", remediation: str = "", safe_fixable: bool = False, path: str = "") -> None:
    source = path or (page.relative_path if page else "repository")
    fingerprint = stable_fingerprint(rule_id, page, location) if page else stable_fingerprint(rule_id, ContentPage(Path(source)), location)
    findings.append(Finding(rule_id, severity, message, source, location, remediation, safe_fixable, fingerprint))


def semantic_signal_groups(page: ContentPage) -> dict[str, tuple[str, ...]]:
    model = page.content_model
    base = {
        "problem": ("problem", "pain", "symptom", "why it matters", "objective", "goal"),
        "context": ("context", "scope", "prerequisite", "when to use", "assumption"),
        "causes": ("cause", "root cause", "failure mode", "why", "reason"),
        "checks": ("check", "where to check", "evidence", "diagnos", "inspect", "verify"),
        "workflow": ("workflow", "process", "step", "sequence", "method"),
        "actions": ("next step", "action", "fix", "remediation", "recommend", "what to do"),
        "limitations": ("limitation", "boundary", "not a", "risk", "caveat", "release-specific"),
        "requirements": ("requirement", "constraint", "non-functional", "acceptance"),
        "flow": ("data flow", "control flow", "integration", "interface", "component"),
        "security": ("security", "authoriz", "permission", "identity", "secret"),
        "failure_handling": ("failure", "recovery", "retry", "fallback", "resilien"),
        "tradeoffs": ("trade-off", "tradeoff", "option", "choice", "downside"),
        "ownership": ("owner", "ownership", "responsib", "accountab"),
        "question": ("research question", "question", "hypothesis"),
        "scope": ("scope", "method", "methodology", "in scope"),
        "findings": ("finding", "observed", "result", "signal"),
        "sources": ("source", "reference", "citation", "official documentation", "informed by"),
        "conclusion": ("conclusion", "implication", "takeaway", "next action"),
        "deliverables": ("deliverable", "output", "will receive", "what we produce"),
        "cta": ("contact", "engagement", "service", "work with", "related service"),
        "schema": ("schema", "field", "json", "yaml", "column", "interface"),
        "usage": ("usage", "install", "run", "how to use", "example"),
        "update": ("updated", "version", "last reviewed", "changelog"),
        "related": ("related", "further reading", "continue", "see also"),
        "thesis": ("i argue", "the point", "thesis", "position", "view"),
        "identity": ("profile", "about", "author", "experience", "role"),
        "target_situation": ("who this is for", "fit", "situation", "teams"),
        "pain": ("business pain", "cost", "delay", "blocked", "friction"),
        "process_context": ("process context", "business process", "order to cash", "procure to pay"),
        "touchpoints": ("sap touchpoint", "transaction", "table", "interface", "integration"),
        "solution": ("solution", "pattern", "approach", "improvement"),
    }
    return base


def page_text(page: ContentPage) -> str:
    return normalize_text(f"{page.title} {page.description} {page.body}")


def _freshness_limit(config: dict[str, Any], page: ContentPage) -> int | None:
    key = {
        "technical_guide": "technical_guide_days",
        "architecture": "architecture_days",
        "research": "research_days",
        "service": "service_days",
        "reference": "stable_reference_days",
    }.get(page.content_model)
    return int(config.get("freshness", {}).get(key)) if key and config.get("freshness", {}).get(key) else None


def check_source_pages(pages: list[ContentPage], parse_errors: list[dict[str, Any]], config: dict[str, Any]) -> tuple[list[Finding], dict[str, Any]]:
    findings: list[Finding] = []
    for error in parse_errors:
        add_finding(findings, None, "FM001_INVALID_YAML", "error", "Invalid YAML front matter.", path=error["path"], remediation="Fix the front matter before publication.")

    by_permalink: dict[str, list[ContentPage]] = defaultdict(list)
    by_title: dict[str, list[ContentPage]] = defaultdict(list)
    by_description: dict[str, list[ContentPage]] = defaultdict(list)
    for page in pages:
        if page.permalink:
            by_permalink[page.permalink.rstrip("/")].append(page)
        if page.title:
            by_title[normalize_text(page.title)].append(page)
        if page.description:
            by_description[normalize_text(page.description)].append(page)

    for permalink, duplicates in by_permalink.items():
        if len(duplicates) > 1:
            for page in duplicates:
                add_finding(findings, page, "FM003_DUPLICATE_CANONICAL", "error", f"Canonical permalink is duplicated: {permalink}", remediation="Give each public page a unique permalink.")

    for page in pages:
        text = page_text(page)
        indexable_candidate = page.is_indexable and (page.permalink or page.verified or page.sitemap_enabled)
        if indexable_candidate and not page.permalink:
            add_finding(findings, page, "FM002_MISSING_PERMALINK", "error", "Indexable content has no canonical permalink.", remediation="Add a stable public permalink or mark the source as an internal draft.")
        if page.is_indexable and page.permalink and not page.canonical_url.startswith(f"{BASE_URL}/"):
            add_finding(findings, page, "SEO001_INVALID_CANONICAL", "error", f"Canonical is not the configured production HTTPS URL: {page.canonical_url}", remediation="Use the configured production domain.")
        if page.verified and page.status != "reviewed":
            add_finding(findings, page, "FM004_UNSUPPORTED_VERIFIED_STATE", "error", "verified: true requires status: reviewed.", remediation="Complete human review or remove the verified flag.")
        if "noindex" in page.robots.lower() and page.sitemap_enabled:
            add_finding(findings, page, "SEO004_NOINDEX_IN_SITEMAP", "error", "Noindex content is sitemap-enabled.", remediation="Set sitemap: false until the page is reviewed and indexable.")
        if page.is_indexable and not page.title:
            add_finding(findings, page, "FM005_MISSING_TITLE", "error", "Indexable page has no title.", remediation="Add a specific human-readable title.")
        if page.is_indexable and not page.description and page.content_model not in {"landing_page", "news"}:
            add_finding(findings, page, "FM006_MISSING_DESCRIPTION", "warning", "Indexable page has no description.", remediation="Add a concise description of the page's decision or problem.")
        guidance = config["guidance"]
        if page.title and not (guidance["title_min"] <= len(page.title) <= guidance["title_max"]):
            add_finding(findings, page, "SEO003_TITLE_LENGTH", "warning", f"Title length is {len(page.title)} characters; guidance is {guidance['title_min']}–{guidance['title_max']}.", remediation="Shorten or sharpen the title without keyword stuffing.")
        if page.description and not (guidance["description_min"] <= len(page.description) <= guidance["description_max"]):
            add_finding(findings, page, "SEO004_DESCRIPTION_LENGTH", "warning", f"Description length is {len(page.description)} characters; guidance is {guidance['description_min']}–{guidance['description_max']}.", remediation="Rewrite the description around the page's actual problem and audience.")
        h1s = re.findall(r"^#\s+(.+)$|<h1(?:\s[^>]*)?>(.*?)</h1>", page.body, flags=re.IGNORECASE | re.MULTILINE)
        if page.is_indexable and page.content_model not in {"landing_page", "profile"} and not page.frontmatter.get("intent_id") and len(h1s) == 0 and page.frontmatter.get("layout") not in {"note", "blog", "radar"} and not page.relative_path.startswith(("_notes/", "_blog/", "_news/", "_radar/")):
            add_finding(findings, page, "CONTENT002_MISSING_H1", "warning", "Source content has no page-level H1 signal.", remediation="Add one clear H1 or use an established layout that renders it.")
        headings = re.findall(r"^(#{1,6})\s+(.+)$", page.body, flags=re.MULTILINE)
        levels = [len(item[0]) for item in headings]
        for previous, current in zip(levels, levels[1:]):
            if current > previous + 1:
                add_finding(findings, page, "CONTENT003_HEADING_JUMP", "warning", f"Heading level jumps from H{previous} to H{current}.", remediation="Keep heading hierarchy navigable for readers and retrieval systems.")
                break
        for marker in ("TODO", "FIXME", "TBD", "lorem ipsum"):
            if marker.lower() in text:
                add_finding(findings, page, "CONTENT005_PLACEHOLDER", "warning", f"Placeholder marker found: {marker}.", remediation="Resolve the placeholder or move the source to a private draft area.")
                break
        for pattern in config["private_patterns"]:
            if pattern.lower() in text:
                add_finding(findings, page, "PRIVACY001_PRIVATE_PATH", "error", "Private or internal path pattern exposed.", remediation="Remove the private reference; reports intentionally omit the matched value.")
                break
        for pattern in config.get("sensitive_regex_patterns", []):
            if re.search(pattern, page.body, re.MULTILINE):
                add_finding(findings, page, "PRIVACY002_SENSITIVE_VALUE", "error", "Possible credential or secret pattern found in published content.", remediation="Remove the sensitive value; the report intentionally redacts it.")
                break
        injection = next((pattern for pattern in config["prompt_injection_patterns"] if pattern.lower() in text), None)
        if injection:
            # A page that explicitly teaches prompt-injection handling may quote
            # an attack string. Treat that as an editorial warning, while active
            # directives in ordinary content remain publication blockers.
            educational = bool(
                re.search(r"^#{1,6}\s+[^\n]*(prompt injection|prompt attack|guardrail|ai security)", page.body, re.I | re.M)
                or any(term in page.title.lower() for term in ("prompt injection", "guardrail", "ai security", "security for generated"))
            )
            add_finding(findings, page, "AI010_PROMPT_INJECTION", "warning" if educational else "error", "Prompt-injection or model-directive language detected.", remediation="If educational, keep it clearly framed as an example; otherwise remove it from published content.")
        if page.date_modified == "" and page.is_indexable and page.content_model not in {"landing_page", "dataset"}:
            add_finding(findings, page, "FM007_MISSING_MODIFIED_DATE", "warning", "Indexable article has no modification or review date.", remediation="Add a meaningful last_modified_at or last_reviewed date.")
        limit = _freshness_limit(config, page)
        freshness_value = page.last_reviewed or page.date_modified or page.date_published
        if limit and freshness_value and page.is_indexable:
            try:
                reviewed = dt.date.fromisoformat(freshness_value[:10])
                age = (dt.date.today() - reviewed).days
                if age > limit:
                    add_finding(findings, page, "FRESHNESS001_STALE_CONTENT", "warning", f"Last review signal is {age} days old; configured limit is {limit} days.", remediation="Review the page for changed terminology, links, release context, and operational boundaries. Do not update the date without a real review.")
            except ValueError:
                add_finding(findings, page, "FM009_INVALID_DATE", "warning", "Publication or review date is not ISO-formatted.", remediation="Use an ISO date or timestamp.")
        if not page.tags and page.content_model in {"diagnostic", "technical_guide", "architecture", "research", "opinion"}:
            add_finding(findings, page, "FM008_MISSING_TOPIC_TAGS", "warning", "Substantial page has no tags or topic signals.", remediation="Add a small, accurate topic set.")
        groups = semantic_signal_groups(page)
        missing = [name for name, terms in groups.items() if name in config["content_models"].get(page.content_model, {}).get("required_signals", []) and not any(term in text for term in terms)]
        for signal in missing:
            add_finding(findings, page, f"CONTENT_{signal.upper()}", "warning", f"Missing semantic content signal: {signal}.", remediation=f"Add a useful section or paragraph covering {signal}; do not copy a template mechanically.")
        if page.expert_context_enabled:
            if not page.service_url:
                add_finding(findings, page, "AI001_MISSING_AUTHOR_CONTEXT", "error", "Expert promotion is enabled without a service mapping.", remediation="Add a relevant service URL or disable promotion.")
            if not page.evidence_urls:
                add_finding(findings, page, "EVIDENCE001_NO_SOURCES", "warning", "Expert promotion has no evidence URLs.", remediation="Link two to five reviewed public evidence pages.")
            if any(url.rstrip("/") == "https://www.linkedin.com/in/dkharlanau" for url in page.evidence_urls):
                add_finding(findings, page, "AI003_INVALID_LINKEDIN", "error", "LinkedIn URL is being used without the canonical trailing slash.", remediation="Use https://www.linkedin.com/in/dkharlanau/.")

    for title, duplicates in by_title.items():
        if len(duplicates) > 1 and title:
            for page in duplicates:
                add_finding(findings, page, "SEARCH003_DUPLICATE_TITLE", "warning", "Title is shared by multiple pages and may cannibalize intent.", remediation="Differentiate the page's subject or consolidate it.")
    for description, duplicates in by_description.items():
        if len(duplicates) > 1 and description:
            for page in duplicates:
                add_finding(findings, page, "SEO010_DUPLICATE_DESCRIPTION", "warning", "Meta description is shared by multiple pages.", remediation="Describe the distinct question answered by this page.")

    return findings, {"pages": pages, "parse_errors": parse_errors}


def extract_links(page: ContentPage) -> list[tuple[str, str]]:
    links = []
    for match in re.finditer(r"\[[^\]]*\]\(([^)\s]+)(?:\s+['\"][^)]*['\"])?\)|href=[\"']([^\"']+)", page.body, flags=re.IGNORECASE):
        target = match.group(1) or match.group(2) or ""
        if target:
            links.append((target.split("#", 1)[0], "contextual"))
    return links


def _built_target_exists(site_dir: Path | None, target: str) -> bool:
    """Resolve routes emitted by Jekyll and static/generated public files."""
    if target in {"", "/"}:
        return True if site_dir is None else (site_dir / "index.html").is_file()
    known_generated = (
        target.startswith("/datasets/view/"),
        target.startswith("/datasets/") and target.endswith((".json", ".yml")),
        target.startswith("/ai/") and target.endswith((".json", ".yml")),
        target in {"/cv/", "/llms.txt", "/llms-full.txt", "/feed.xml", "/sitemap.xml"},
    )
    if any(known_generated) and site_dir is None:
        return True
    if site_dir is None:
        clean = target.split("?", 1)[0].strip("/")
        source_candidates = [
            REPO_ROOT / clean,
            REPO_ROOT / f"{clean}.md",
            REPO_ROOT / clean / "index.md",
            REPO_ROOT / f"{clean}.html",
            REPO_ROOT / clean / "index.html",
            REPO_ROOT / f"{clean}.json",
        ]
        return any(path.is_file() for path in source_candidates)
    if not site_dir or not site_dir.is_dir():
        return False
    clean = target.split("?", 1)[0].strip("/")
    candidates = [site_dir / clean]
    if not Path(clean).suffix:
        candidates.extend((site_dir / clean / "index.html", site_dir / f"{clean}.html"))
    return any(path.is_file() for path in candidates)


def build_link_graph(pages: list[ContentPage], findings: list[Finding], site_dir: Path | None = None) -> dict[str, Any]:
    by_url = {page.permalink.rstrip("/"): page for page in pages if page.permalink}
    edges = []
    inbound = Counter()
    for page in pages:
        for target, link_type in extract_links(page):
            if not target.startswith("/") or target.startswith(("/assets/", "/static/")):
                continue
            target_key = target.rstrip("/") or "/"
            target_page = by_url.get(target_key)
            if not target_page:
                # Not every public route is backed by a Markdown page: datasets,
                # feeds, resumes, static pages and the home route are generated
                # artifacts. Resolve those against the built site before calling
                # a source link broken.
                if "{{" in target or "{%" in target or target.rstrip("/").startswith("/datasets/view") or _built_target_exists(site_dir, target):
                    edges.append({"source": page.permalink, "target": target, "link_type": link_type, "resolved": True, "generated_route": True})
                    continue
                add_finding(findings, page, "LINK001_BROKEN_INTERNAL_LINK", "error", f"Internal link does not resolve: {target}", remediation="Fix the target or remove the link.")
                edges.append({"source": page.permalink, "target": target, "link_type": link_type, "resolved": False})
                continue
            inbound[target_key] += 1
            edges.append({"source": page.permalink, "target": target_page.permalink, "link_type": link_type, "resolved": True, "target_retrieval_eligible": target_page.retrieval_eligible})
    orphans = []
    for page in pages:
        if page.is_indexable and page.permalink and page.content_model not in {"landing_page", "profile", "dataset"} and inbound[page.permalink.rstrip("/")] == 0:
            orphans.append(page.permalink)
            add_finding(findings, page, "LINK005_ORPHAN_PAGE", "warning", "Indexable article has no inbound contextual link in source Markdown.", remediation="Add one strong contextual link from a relevant hub or related article.")
    return {"nodes": [{"url": p.canonical_url, "source_path": p.relative_path, "cluster": p.content_model, "retrieval_eligible": p.retrieval_eligible} for p in pages if p.permalink], "edges": edges, "orphans": orphans}


def audit_built_site(site_dir: Path, findings: list[Finding]) -> dict[str, Any]:
    result = {"html_files": 0, "localhost_values": 0, "jsonld_errors": 0, "missing_h1": 0}
    if not site_dir.is_dir():
        return result
    title_re = re.compile(r"<title>(.*?)</title>", re.I | re.S)
    canonical_re = re.compile(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\'](.*?)["\']', re.I | re.S)
    og_re = re.compile(r'<meta[^>]+property=["\']og:url["\'][^>]+content=["\'](.*?)["\']', re.I | re.S)
    for path in sorted(site_dir.rglob("*.html")):
        result["html_files"] += 1
        text = path.read_text(encoding="utf-8", errors="ignore")
        urls = canonical_re.findall(text) + og_re.findall(text)
        if any("localhost" in html.unescape(value) or "127.0.0.1" in html.unescape(value) for value in urls):
            result["localhost_values"] += 1
            add_finding(findings, None, "SEO002_LOCALHOST_CANONICAL", "error", "Built HTML contains a localhost canonical or Open Graph URL.", path=str(path.relative_to(site_dir)))
        h1_count = len(re.findall(r"<h1(?:\s[^>]*)?>", text, flags=re.I))
        if h1_count == 0 and title_re.search(text):
            result["missing_h1"] += 1
        for block in re.findall(r'<script[^>]+application/ld\+json[^>]*>(.*?)</script>', text, flags=re.I | re.S):
            try:
                json.loads(html.unescape(block).strip())
            except json.JSONDecodeError:
                result["jsonld_errors"] += 1
                add_finding(findings, None, "SEO020_MALFORMED_JSONLD", "error", "Built HTML contains malformed JSON-LD.", path=str(path.relative_to(site_dir)))
    return result


def audit_generated_artifacts(findings: list[Finding], pages: list[ContentPage]) -> dict[str, Any]:
    artifact_result = {"checked": [], "missing": [], "unverified_in_llms": False, "localhost_values": 0, "malformed_json": []}
    generated = ("llms-full.txt", "llms.txt", "ai/expert-evidence.json", "ai/expert-promotion-inventory.json", "ai/markdown-clusters.json", "ai/verified-pages.json", "ai/catalog.json")
    for rel in generated:
        path = REPO_ROOT / rel
        if path.exists():
            artifact_result["checked"].append(rel)
            text = path.read_text(encoding="utf-8", errors="ignore")
            if "localhost" in text or "127.0.0.1" in text:
                artifact_result["localhost_values"] += 1
                add_finding(findings, None, "SEO002_LOCALHOST_CANONICAL", "error", "Generated AI or LLM artifact contains a localhost reference.", path=rel)
            if path.suffix == ".json":
                # Some JSON endpoints are Markdown-like Liquid sources with a
                # front matter header. Validate the rendered endpoint when it
                # exists; the source template is not itself JSON.
                rendered = (REPO_ROOT / "_site" / rel) if (REPO_ROOT / "_site" / rel).is_file() else path
                json_text = rendered.read_text(encoding="utf-8", errors="ignore")
                try:
                    json.loads(json_text)
                except json.JSONDecodeError:
                    artifact_result["malformed_json"].append(rel)
                    add_finding(findings, None, "PUBLICATION003_MALFORMED_JSON", "error", f"Generated artifact is malformed JSON: {rel}", path=rel)
        else:
            artifact_result["missing"].append(rel)
            if rel in {"llms-full.txt", "ai/expert-evidence.json", "ai/expert-promotion-inventory.json", "ai/markdown-clusters.json"}:
                add_finding(findings, None, "PUBLICATION002_STALE_ARTIFACT", "error", f"Generated artifact is missing: {rel}", path=rel)
    llms = REPO_ROOT / "llms-full.txt"
    if llms.exists():
        text = llms.read_text(encoding="utf-8", errors="ignore")
        for page in pages:
            if page.collection == "atlas" and page.permalink and not page.retrieval_eligible and f"URL: {page.canonical_url}" in text:
                artifact_result["unverified_in_llms"] = True
                add_finding(findings, None, "PUBLICATION001_UNVERIFIED_IN_LLMS", "error", "Unverified Atlas content appears in llms-full.txt.", path="llms-full.txt")
                break
    for rel in ("ai/expert-evidence.json", "ai/expert-promotion-inventory.json"):
        path = REPO_ROOT / rel
        if not path.exists():
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            add_finding(findings, None, "PUBLICATION003_MALFORMED_JSON", "error", f"Generated artifact is malformed JSON: {rel}", path=rel)
            continue
        if rel.endswith("expert-evidence.json"):
            for domain in data.get("domains", []):
                for item in domain.get("evidence", []):
                    if item.get("verification_status") != "reviewed":
                        add_finding(findings, None, "PUBLICATION004_UNVERIFIED_EXPERT_EVIDENCE", "error", "Unreviewed content appears in expert evidence index.", path=rel)
                        break
    return artifact_result


def score_page(page: ContentPage, page_findings: list[Finding], link_graph: dict[str, Any]) -> dict[str, Any]:
    text = page_text(page)
    words = word_count(page.body)
    errors = sum(item.severity == "error" for item in page_findings)
    warnings = sum(item.severity == "warning" for item in page_findings)
    headings = len(re.findall(r"^#{2,6}\s+|<h[2-6](?:\s|>)", page.body, flags=re.I | re.M))
    content = min(30, 10 + (10 if words >= 400 else 5 if words >= 180 else 0) + (5 if headings >= 3 else 0) + (5 if page.description else 0))
    evidence = min(20, (8 if page.verified else 2) + (5 if page.evidence_urls or "source" in text or "reference" in text else 0) + (4 if "limitation" in text or "boundary" in text else 0) + (3 if page.last_reviewed or page.date_modified else 0))
    search = min(20, (5 if page.title else 0) + (5 if page.description else 0) + (4 if page.permalink else 0) + (3 if page.tags else 0) + (3 if page.is_indexable else 0))
    ai = min(15, (4 if page.retrieval_eligible else 1) + (3 if headings >= 2 else 0) + (3 if page.author or page.expert_context_enabled else 0) + (3 if page.evidence_urls else 0) + (2 if page.description else 0))
    internal = min(15, (6 if page.permalink and page.permalink.rstrip("/") not in link_graph.get("orphans", []) else 1) + (5 if extract_links(page) else 0) + (4 if page.content_model in {"service", "diagnostic", "technical_guide", "scenario"} else 2))
    total = max(0, min(100, content + evidence + search + ai + internal - errors * 20 - warnings * 2))
    if errors:
        classification = "blocked"
    elif total >= 85:
        classification = "strong"
    elif total >= 70:
        classification = "publishable"
    elif total >= 50:
        classification = "needs_improvement"
    else:
        classification = "weak"
    return {"total": total, "classification": classification, "dimensions": {"content_usefulness": content, "technical_evidence_trust": evidence, "search_readiness": search, "ai_retrieval_readiness": ai, "internal_discovery_conversion": internal}, "word_count": words, "finding_count": len(page_findings)}


def git_changed_paths(ref: str | None) -> set[str]:
    if not ref:
        return set()
    try:
        result = subprocess.run(["git", "diff", "--name-only", f"{ref}...HEAD"], cwd=REPO_ROOT, capture_output=True, text=True, check=True)
        return {line.strip() for line in result.stdout.splitlines() if line.strip()}
    except (subprocess.CalledProcessError, FileNotFoundError):
        return set()


def run_audit(site_dir: Path | None = None, changed_from: str | None = None) -> dict[str, Any]:
    config = load_config()
    pages, parse_errors = discover_pages(REPO_ROOT, config.get("excluded_paths", []))
    findings, context = check_source_pages(pages, parse_errors, config)
    link_graph = build_link_graph(pages, findings, site_dir)
    built = audit_built_site(site_dir, findings) if site_dir else {"html_files": 0}
    artifacts = audit_generated_artifacts(findings, pages)
    by_page: dict[str, list[Finding]] = defaultdict(list)
    for finding in findings:
        by_page[finding.path].append(finding)
    page_records = []
    for page in pages:
        page_findings = by_page.get(page.relative_path, [])
        page_records.append({"source_path": page.relative_path, "permalink": page.permalink, "canonical_url": page.canonical_url, "collection": page.collection, "content_model": page.content_model, "content_model_inferred": not bool(page.frontmatter.get("content_model")), "language": page.language, "title": page.title, "status": page.status, "verified": page.verified, "indexable": page.is_indexable, "retrieval_eligible": page.retrieval_eligible, "expert_context_enabled": page.expert_context_enabled, "score": score_page(page, page_findings, link_graph), "findings": [item.as_dict() for item in page_findings]})
    changed = git_changed_paths(changed_from)
    changed_findings = [finding for finding in findings if finding.path in changed or not changed]
    distribution = Counter(record["score"]["classification"] for record in page_records)
    hard_count = sum(1 for finding in findings if finding.severity == "error")
    warning_count = sum(1 for finding in findings if finding.severity == "warning")
    indexable_pages = sum(page.is_indexable for page in pages)
    retrieval_pages = sum(page.retrieval_eligible for page in pages)
    inventory_count = 0
    inventory_enabled = 0
    inventory_path = REPO_ROOT / "ai" / "expert-promotion-inventory.json"
    if inventory_path.exists():
        try:
            inventory_data = json.loads(inventory_path.read_text(encoding="utf-8"))
            inventory_count = len(inventory_data.get("entries", []))
            inventory_enabled = int(inventory_data.get("summary", {}).get("enabled", 0))
        except json.JSONDecodeError:
            inventory_count = 0
    summary = {"files_inspected": len(pages) + len(parse_errors), "public_pages": len(pages), "indexable_pages": indexable_pages, "retrieval_eligible_pages": retrieval_pages, "expert_promotion_pages": sum(page.expert_context_enabled for page in pages), "expert_inventory_entries": inventory_count, "expert_inventory_enabled": inventory_enabled, "sitemap_eligible_pages": sum(page.sitemap_enabled and page.is_indexable for page in pages), "llms_retrieval_coverage_percent": round((retrieval_pages / indexable_pages) * 100, 1) if indexable_pages else 0.0, "hard_blockers": hard_count, "warnings": warning_count, "stale_pages": sum(item.rule_id == "FRESHNESS001_STALE_CONTENT" for item in findings), "orphan_pages": len(link_graph.get("orphans", [])), "duplicate_candidates": sum(item.rule_id in {"SEARCH003_DUPLICATE_TITLE", "SEO010_DUPLICATE_DESCRIPTION"} for item in findings), "quality_distribution": dict(distribution), "changed_paths": sorted(changed), "changed_findings": len(changed_findings)}
    baseline_fingerprints: set[str] = set()
    baseline_path = REPO_ROOT / "config" / "content-quality-baseline.json"
    if baseline_path.exists():
        try:
            baseline_fingerprints = set(json.loads(baseline_path.read_text(encoding="utf-8")).get("items", {}))
        except json.JSONDecodeError:
            baseline_fingerprints = set()
    summary["new_regressions"] = sum(item.severity == "warning" and item.fingerprint not in baseline_fingerprints and (not changed or item.path in changed) for item in findings)
    return {"generated_at": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(), "config": str(CONFIG_PATH.relative_to(REPO_ROOT)), "summary": summary, "pages": page_records, "findings": [finding.as_dict() for finding in findings], "built_site": built, "artifacts": artifacts, "link_graph": link_graph}


def write_reports(audit: dict[str, Any]) -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    summary = audit["summary"]
    (REPORT_DIR / "content-quality.json").write_text(json.dumps(audit, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (REPORT_DIR / "content-quality-summary.json").write_text(json.dumps({"generated_at": audit["generated_at"], **summary}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (REPORT_DIR / "content-link-graph.json").write_text(json.dumps(audit["link_graph"], indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    queue = sorted((finding for finding in audit["findings"] if finding["severity"] in {"error", "warning"}), key=lambda item: (0 if item["severity"] == "error" else 1, item["source_path"], item["rule_id"]))
    queue_lines = ["# Content Review Queue", "", "Generated by `python scripts/content_quality.py audit`.", ""]
    for finding in queue[:500]:
        queue_lines.append(f"- **{finding['severity']} {finding['rule_id']}** `{finding['source_path']}` — {finding['message']} Suggested action: {finding['remediation']}")
    (REPORT_DIR / "content-review-queue.md").write_text("\n".join(queue_lines) + "\n", encoding="utf-8")
    lines = ["---", "layout: default", "title: Content Quality Report", "description: Noindex report of publication quality, search readiness, and AI retrieval checks.", "robots: noindex,follow", "sitemap: false", "---", "", "# Content Quality Report", "", f"Generated: {audit['generated_at']}", "", "| Metric | Count |", "|---|---:|", f"| Files inspected | {summary['files_inspected']} |", f"| Public pages | {summary['public_pages']} |", f"| Indexable pages | {summary['indexable_pages']} |", f"| Retrieval-eligible pages | {summary['retrieval_eligible_pages']} |", f"| Strong | {summary['quality_distribution'].get('strong', 0)} |", f"| Publishable | {summary['quality_distribution'].get('publishable', 0)} |", f"| Needs improvement | {summary['quality_distribution'].get('needs_improvement', 0)} |", f"| Blocked | {summary['quality_distribution'].get('blocked', 0)} |", f"| Hard blockers | {summary['hard_blockers']} |", f"| Warnings | {summary['warnings']} |", f"| New regressions | {summary['new_regressions']} |", f"| Stale pages | {summary['stale_pages']} |", f"| Orphan pages | {summary['orphan_pages']} |", f"| Duplicate candidates | {summary['duplicate_candidates']} |", f"| Sitemap-eligible pages | {summary['sitemap_eligible_pages']} |", f"| AI retrieval coverage | {summary['llms_retrieval_coverage_percent']}% of indexable pages |", f"| Expert-promotion source pages | {summary['expert_promotion_pages']} |", f"| Expert-promotion enabled inventory | {summary['expert_inventory_enabled']} |", "", "This report validates publication process and structure. It does not prove technical correctness.", "", "## Priority findings", ""]
    lines.extend(f"- **{item['severity']} {item['rule_id']}** `{item['source_path']}` — {item['message']}" for item in queue[:100])
    (REPORT_DIR / "content-quality.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    top_candidates = [record for record in audit["pages"] if record["score"]["classification"] in {"weak", "needs_improvement"}][:20]
    initial = ["# Content Quality Initial Rollout", "", "This report records the first deterministic audit and points to the machine-readable report for page-level findings.", "", f"- Files inspected: {summary['files_inspected']}", f"- Public pages: {summary['public_pages']}", f"- Collections found: {len({record['collection'] for record in audit['pages']})}", f"- Strong / publishable / needs improvement / weak: {summary['quality_distribution'].get('strong', 0)} / {summary['quality_distribution'].get('publishable', 0)} / {summary['quality_distribution'].get('needs_improvement', 0)} / {summary['quality_distribution'].get('weak', 0)}", f"- Hard blockers: {summary['hard_blockers']}", f"- Warnings: {summary['warnings']}", f"- New regressions: {summary['new_regressions']}", f"- Stale pages: {summary['stale_pages']}", f"- Duplicate candidates: {summary['duplicate_candidates']}", f"- Orphan pages: {summary['orphan_pages']}", f"- Expert-promotion coverage: {summary['expert_promotion_pages']} source pages; {summary['expert_inventory_enabled']} enabled inventory entries", f"- Sitemap coverage: {summary['sitemap_eligible_pages']} indexable pages eligible", f"- AI retrieval coverage: {summary['retrieval_eligible_pages']} pages ({summary['llms_retrieval_coverage_percent']}% of indexable pages)", f"- Changed paths in scope: {len(summary['changed_paths'])}", "- Safe fixes applied: none to article prose; derived artifacts are refreshed only by explicit `fix --safe`.", "- Historical non-critical findings should be reviewed into `config/content-quality-baseline.json` only after safety blockers are fixed.", "", "## Highest-priority manual candidates", ""]
    initial.extend(f"- `{record['source_path']}` — score {record['score']['total']} ({record['score']['classification']})" for record in top_candidates)
    initial.extend(["", "See `reports/content-review-queue.md` for the actionable queue."])
    (REPORT_DIR / "content-quality-initial-rollout.md").write_text("\n".join(initial) + "\n", encoding="utf-8")


def baseline(audit: dict[str, Any]) -> Path:
    path = REPO_ROOT / "config" / "content-quality-baseline.json"
    existing = {}
    if path.exists():
        try:
            existing = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            existing = {}
    today = dt.date.today().isoformat()
    items = {item["fingerprint"]: {"fingerprint": item["fingerprint"], "rule_id": item["rule_id"], "source_path": item["source_path"], "first_seen": existing.get("items", {}).get(item["fingerprint"], {}).get("first_seen", today), "last_seen": today} for item in audit["findings"] if item["severity"] == "warning"}
    payload = {"schema": "dkharlanau.content_quality_baseline", "schema_version": "1.0", "generated_at": audit["generated_at"], "items": items}
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


def safe_fix(dry_run: bool) -> int:
    print("Safe fixes are limited to deterministic generated-artifact refresh; article prose, verification, dates, robots, and evidence are never rewritten.")
    if dry_run:
        print("DRY RUN: would regenerate Atlas/AI/LLM derived artifacts after source review.")
        return 0
    command = [sys.executable, str(REPO_ROOT / "scripts" / "generate_atlas_artifacts.py")]
    return subprocess.run(command, cwd=REPO_ROOT).returncode


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["audit", "check", "report", "fix", "baseline"])
    parser.add_argument("--site-dir", default="_site")
    parser.add_argument("--changed-from", default=None)
    parser.add_argument("--safe", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)

    if args.command == "fix":
        if not args.safe:
            print("Refusing to modify content without --safe.", file=sys.stderr)
            return 2
        return safe_fix(args.dry_run)

    try:
        audit = run_audit(Path(args.site_dir) if Path(args.site_dir).is_dir() else None, args.changed_from)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        print(f"content_quality: {exc}", file=sys.stderr)
        return 2
    if args.command in {"audit", "report"}:
        write_reports(audit)
    if args.command == "baseline":
        path = baseline(audit)
        print(f"Baseline written: {path.relative_to(REPO_ROOT)}")
        return 0
    if args.command == "check":
        changed = set(audit["summary"].get("changed_paths", []))
        errors = [item for item in audit["findings"] if item["severity"] == "error" and (not changed or item["source_path"] in changed or item["source_path"] in {"reports/content-quality.json", "llms-full.txt"})]
        baseline_path = REPO_ROOT / "config" / "content-quality-baseline.json"
        baseline_items = set()
        if baseline_path.exists():
            try:
                baseline_items = set(json.loads(baseline_path.read_text(encoding="utf-8")).get("items", {}))
            except json.JSONDecodeError:
                pass
        new_changed_warnings = [item for item in audit["findings"] if item["severity"] == "warning" and item["fingerprint"] not in baseline_items and (not changed or item["source_path"] in changed)]
        if errors or new_changed_warnings:
            print(f"Content quality check failed: {len(errors)} hard blocker(s), {len(new_changed_warnings)} new changed warning(s).")
            for item in (errors + new_changed_warnings)[:100]:
                print(f"- {item['rule_id']} {item['source_path']}: {item['message']}")
            return 2
        print(f"Content quality check passed: {audit['summary']['public_pages']} pages, no new hard blockers.")
        return 0
    print(f"Audited {audit['summary']['public_pages']} public pages: {audit['summary']['hard_blockers']} hard blocker(s), {audit['summary']['warnings']} warning(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
