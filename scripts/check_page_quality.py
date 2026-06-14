#!/usr/bin/env python3
"""Strict technical page-quality gate for indexable content pages.

Checks built HTML for technical metadata and article-quality structure,
with page-type-aware severity. Complements check_seo.py and
scripts/check_structured_data.py.

Usage:
    python3 scripts/check_page_quality.py [--site-dir _site] [--fail-on-critical]
    python3 scripts/check_page_quality.py [--site-dir _site] [--fail-on-critical] [--warning-budget 40]
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import urlparse

SITE_ORIGIN = "https://dkharlanau.github.io"
EXPECTED_AUTHOR = "Dzmitryi Kharlanau"

TITLE_RE = re.compile(r"<title>(.*?)</title>", re.IGNORECASE | re.DOTALL)
META_DESC_RE = re.compile(
    r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']',
    re.IGNORECASE | re.DOTALL,
)
META_DESC_RE_ALT = re.compile(
    r'<meta[^>]+content=["\'](.*?)["\'][^>]+name=["\']description["\']',
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
OG_TITLE_RE = re.compile(
    r'<meta[^>]+property=["\']og:title["\'][^>]+content=["\'](.*?)["\']',
    re.IGNORECASE | re.DOTALL,
)
OG_DESC_RE = re.compile(
    r'<meta[^>]+property=["\']og:description["\'][^>]+content=["\'](.*?)["\']',
    re.IGNORECASE | re.DOTALL,
)
OG_URL_RE = re.compile(
    r'<meta[^>]+property=["\']og:url["\'][^>]+content=["\'](.*?)["\']',
    re.IGNORECASE | re.DOTALL,
)
OG_TYPE_RE = re.compile(
    r'<meta[^>]+property=["\']og:type["\'][^>]+content=["\'](.*?)["\']',
    re.IGNORECASE | re.DOTALL,
)
OG_IMAGE_RE = re.compile(
    r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\'](.*?)["\']',
    re.IGNORECASE | re.DOTALL,
)
TWITTER_CARD_RE = re.compile(
    r'<meta[^>]+name=["\']twitter:card["\'][^>]+content=["\'](.*?)["\']',
    re.IGNORECASE | re.DOTALL,
)
H1_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.IGNORECASE | re.DOTALL)
SCRIPT_LD_RE = re.compile(
    r'<script\s+type=["\']application/ld\+json["\']\s*>(.*?)</script>',
    re.IGNORECASE | re.DOTALL,
)
LINK_HREF_RE = re.compile(r'<a[^>]+href=["\'](.*?)["\'][^>]*>', re.IGNORECASE | re.DOTALL)
VISIBLE_TEXT_RE = re.compile(r">([^<]{2,})<", re.DOTALL)

PLACEHOLDER_PATTERNS = [
    re.compile(r"\bTODO[:\s]", re.IGNORECASE),
    re.compile(r"\bFIXME[:\s]", re.IGNORECASE),
    re.compile(r"\bTBD[:\s\.\-]", re.IGNORECASE),
    re.compile(r"\blorem\s+ipsum\b", re.IGNORECASE),
    re.compile(r"\bcoming\s+soon\b", re.IGNORECASE),
]
# Patterns that strongly indicate a real private-path or local leak.
# Generic documentation terms such as "private-source" or "source_files" are
# intentionally excluded from automatic critical checks because they appear in
# public safety-policy docs as examples.
PRIVATE_PATH_PATTERNS = [
    "/Users/",
    ".env.local",
    "Kimi_Agent_SAP Atlas Expansion",
    "Basic_LinkedInDataExport",
    "Basic_LinkInDataExport",
    "li2resume.local",
]
LOCALHOST_PATTERNS = ["localhost", "127.0.0.1", "0.0.0.0"]


def collect_url_values(page: Page) -> list[str]:
    """Gather values that should be production URLs."""
    values = [
        page.canonical, page.og_url, page.og_image,
    ]
    # Internal link hrefs are also URL values that must not point to private/local paths.
    values.extend(page.internal_links)
    # JSON-LD URL-like fields
    url_keys = {"url", "image", "contentUrl", "mainEntityOfPage", "sameAs"}
    for block in page.jsonld_blocks:
        for item in iter_jsonld_items(block):
            if isinstance(item, dict):
                for key, value in item.items():
                    if key in url_keys and isinstance(value, str):
                        values.append(value)
    return [v for v in values if v]


def iter_jsonld_items(obj: object):
    if isinstance(obj, dict):
        yield obj
        for value in obj.values():
            yield from iter_jsonld_items(value)
    elif isinstance(obj, list):
        for item in obj:
            yield from iter_jsonld_items(item)


def text_outside_code_blocks(content: str) -> str:
    """Return visible text with <code>, <pre>, <samp>, <kbd> contents removed."""
    stripped = re.sub(r"<(code|pre|samp|kbd)[^>]*>.*?</\1>", "", content, flags=re.IGNORECASE | re.DOTALL)
    return extract_visible_text(stripped)
GENERIC_DESCRIPTIONS = {
    "description",
    "page description",
    "meta description",
    "coming soon",
    "under construction",
}


@dataclass
class Finding:
    rule: str
    severity: str  # critical, warning, info
    path: str
    message: str
    fix: str = ""

    def __str__(self) -> str:
        base = f"[{self.severity.upper()}] {self.rule} /{self.path}/\n  {self.message}"
        if self.fix:
            base += f"\n  Suggested fix: {self.fix}"
        return base


@dataclass
class Page:
    path: str
    url: str
    content: str
    title: str = ""
    description: str = ""
    robots: str = ""
    canonical: str = ""
    og_title: str = ""
    og_description: str = ""
    og_url: str = ""
    og_type: str = ""
    og_image: str = ""
    twitter_card: str = ""
    h1_texts: list[str] = field(default_factory=list)
    jsonld_types: list[str] = field(default_factory=list)
    jsonld_blocks: list[dict] = field(default_factory=list)
    visible_text: str = ""
    internal_links: list[str] = field(default_factory=list)

    @property
    def is_noindex(self) -> bool:
        return "noindex" in self.robots.lower()

    @property
    def word_count(self) -> int:
        return len(re.findall(r"\b\w+\b", self.visible_text))


def pick(pattern: re.Pattern, text: str) -> str:
    match = pattern.search(text)
    if not match:
        return ""
    return html.unescape(re.sub(r"<[^>]+>", "", match.group(1))).strip()


def pick_all(pattern: re.Pattern, text: str) -> list[str]:
    matches = pattern.findall(text)
    return [html.unescape(re.sub(r"<[^>]+>", "", m)).strip() for m in matches]


def extract_visible_text(content: str) -> str:
    # Strip script/style, then pull text between tags
    no_scripts = re.sub(r"<script[^>]*>.*?</script>", "", content, flags=re.IGNORECASE | re.DOTALL)
    no_styles = re.sub(r"<style[^>]*>.*?</style>", "", no_scripts, flags=re.IGNORECASE | re.DOTALL)
    parts = VISIBLE_TEXT_RE.findall(no_styles)
    return " ".join(p.strip() for p in parts if p.strip())


def parse_page(html_path: Path, site_dir: Path) -> Page:
    rel = html_path.relative_to(site_dir).as_posix()
    content = html_path.read_text(encoding="utf-8", errors="ignore")

    page = Page(path=rel, url=f"{SITE_ORIGIN}/{rel}", content=content)
    page.title = pick(TITLE_RE, content)
    page.description = pick(META_DESC_RE, content) or pick(META_DESC_RE_ALT, content)
    page.robots = pick(ROBOTS_RE, content)
    page.canonical = pick(CANONICAL_RE, content)
    page.og_title = pick(OG_TITLE_RE, content)
    page.og_description = pick(OG_DESC_RE, content)
    page.og_url = pick(OG_URL_RE, content)
    page.og_type = pick(OG_TYPE_RE, content)
    page.og_image = pick(OG_IMAGE_RE, content)
    page.twitter_card = pick(TWITTER_CARD_RE, content)
    page.h1_texts = pick_all(H1_RE, content)
    page.visible_text = extract_visible_text(content)

    for block in SCRIPT_LD_RE.findall(content):
        try:
            data = json.loads(html.unescape(block))
        except json.JSONDecodeError:
            continue
        page.jsonld_blocks.append(data)
        if isinstance(data, dict):
            t = data.get("@type")
            if isinstance(t, str):
                page.jsonld_types.append(t)
            elif isinstance(t, list):
                page.jsonld_types.extend(t)

    for href in LINK_HREF_RE.findall(content):
        if href.startswith("/") and not href.startswith("//"):
            page.internal_links.append(href)

    return page


def classify_page(page: Page) -> str:
    path = page.path
    lower = path.lower()

    if page.is_noindex:
        if "/atlas/" in lower or "/scenarios/" in lower or "/diagnostics/" in lower:
            return "noindex_review_candidate"
        if "/notes/" in lower or "/blog/" in lower or "/news/" in lower or "/radar/" in lower or "/research/" in lower:
            return "noindex_research_or_draft"
        return "utility_page"

    # Indexable pages
    if "/about/" in lower or "/cv/" in lower or "/services/" in lower:
        return "indexable_service_or_profile"

    if "/datasets/" in lower:
        if path.endswith("/index.html") and path != "datasets/index.html":
            return "indexable_collection"
        return "indexable_dataset_detail"

    if "TechArticle" in page.jsonld_types:
        return "indexable_atlas_verified"

    if "Article" in page.jsonld_types or "/skill-hub/" in lower:
        return "indexable_skill_hub"

    if "CollectionPage" in page.jsonld_types or path.endswith("/index.html"):
        return "indexable_collection"

    if path == "index.html":
        return "utility_page"

    return "indexable_article"


def is_generic_description(text: str) -> bool:
    lower = text.lower().strip()
    return not text or lower in GENERIC_DESCRIPTIONS or len(text) < 20


def has_visible_author(page: Page) -> bool:
    # Look for expected author name in visible text (outside JSON-LD)
    # A simple heuristic: author appears in visible text near a by-line pattern
    text_lower = page.visible_text.lower()
    return EXPECTED_AUTHOR.lower() in text_lower


def has_lead_or_summary(page: Page) -> bool:
    # Look for common lead/summary/subtitle classes or a strong intro paragraph
    if re.search(r'class=["\']([^"\']*\b)(lead|subtitle|summary|intro|abstract|description)(\b[^"\']*)["\']', page.content, re.IGNORECASE):
        return True
    # First non-empty visible text snippet is long enough to be a summary
    snippets = [s.strip() for s in page.visible_text.split(".") if s.strip()]
    if snippets and len(snippets[0]) >= 40:
        return True
    return False


def article_jsonld(page: Page) -> dict | None:
    for block in page.jsonld_blocks:
        if isinstance(block, dict) and block.get("@type") in {"Article", "TechArticle", "NewsArticle", "BlogPosting"}:
            return block
    return None


def check_indexable_article(page: Page, page_type: str) -> list[Finding]:
    findings: list[Finding] = []

    # Title
    if not page.title:
        findings.append(Finding(
            "ARTICLE_TITLE_MISSING", "critical", page.path,
            "Indexable article-like page has no <title>.",
            "Add a title front matter or template title."
        ))
    elif len(page.title) < 10:
        findings.append(Finding(
            "ARTICLE_TITLE_TOO_SHORT", "warning", page.path,
            f"Title is very short ({len(page.title)} chars): {page.title!r}",
            "Use a descriptive title of 35–70 characters."
        ))
    elif len(page.title) > 70:
        findings.append(Finding(
            "ARTICLE_TITLE_TOO_LONG", "warning", page.path,
            f"Title is long ({len(page.title)} chars): {page.title!r}",
            "Consider shortening to 70 characters or less."
        ))

    # H1
    h1_count = len(page.h1_texts)
    if h1_count == 0:
        findings.append(Finding(
            "ARTICLE_H1_MISSING", "critical", page.path,
            "Indexable article-like page has no visible <h1>.",
            "Add a single <h1> that matches the page title."
        ))
    elif h1_count > 1:
        findings.append(Finding(
            "ARTICLE_H1_DUPLICATE", "critical", page.path,
            f"Indexable article-like page has {h1_count} <h1> elements.",
            "Reduce to a single <h1> per page."
        ))
    else:
        h1 = page.h1_texts[0]
        if not h1:
            findings.append(Finding(
                "ARTICLE_H1_EMPTY", "critical", page.path,
                "Indexable article-like page has an empty <h1>.",
                "Populate the <h1> with descriptive text."
            ))
        elif page.title and h1.lower() not in page.title.lower() and page.title.lower() not in h1.lower():
            findings.append(Finding(
                "ARTICLE_H1_TITLE_MISMATCH", "warning", page.path,
                f"H1 ({h1!r}) is not aligned with title ({page.title!r}).",
                "Align the H1 with the HTML <title>."
            ))

    # Meta description
    if not page.description:
        findings.append(Finding(
            "ARTICLE_META_DESCRIPTION_MISSING", "critical", page.path,
            "Indexable article-like page has no meta description.",
            "Add description front matter."
        ))
    elif is_generic_description(page.description):
        findings.append(Finding(
            "ARTICLE_META_DESCRIPTION_GENERIC", "critical", page.path,
            f"Meta description is generic or too short: {page.description!r}",
            "Write a specific, 80–170 character description."
        ))
    elif len(page.description) < 80:
        findings.append(Finding(
            "ARTICLE_META_DESCRIPTION_SHORT", "warning", page.path,
            f"Meta description is short ({len(page.description)} chars).",
            "Expand to at least 80 characters."
        ))
    elif len(page.description) > 170:
        findings.append(Finding(
            "ARTICLE_META_DESCRIPTION_LONG", "warning", page.path,
            f"Meta description is long ({len(page.description)} chars).",
            "Shorten to 170 characters or less."
        ))

    # Subtitle / lead
    if not has_lead_or_summary(page):
        findings.append(Finding(
            "ARTICLE_LEAD_MISSING", "warning", page.path,
            "No visible lead, subtitle, or summary block detected.",
            "Add a lead paragraph or summary near the top of the page."
        ))

    # Author
    art = article_jsonld(page)
    if not art:
        findings.append(Finding(
            "ARTICLE_JSONLD_MISSING", "critical", page.path,
            "Indexable article-like page has no Article/TechArticle JSON-LD.",
            "Emit Article or TechArticle structured data."
        ))
    else:
        author = art.get("author")
        if not author:
            findings.append(Finding(
                "ARTICLE_AUTHOR_MISSING", "critical", page.path,
                "Article JSON-LD has no author.",
                "Add author to the Article structured data."
            ))
        elif isinstance(author, dict) and not author.get("name") and "@id" not in author:
            findings.append(Finding(
                "ARTICLE_AUTHOR_NAME_MISSING", "critical", page.path,
                "Article JSON-LD author has no name or @id reference.",
                "Provide author name or a valid @id reference."
            ))

        publisher = art.get("publisher")
        if not publisher:
            findings.append(Finding(
                "ARTICLE_PUBLISHER_MISSING", "critical", page.path,
                "Article JSON-LD has no publisher.",
                "Add publisher to the Article structured data."
            ))
        elif isinstance(publisher, dict) and not publisher.get("name") and "@id" not in publisher:
            findings.append(Finding(
                "ARTICLE_PUBLISHER_NAME_MISSING", "critical", page.path,
                "Article JSON-LD publisher has no name or @id reference.",
                "Provide publisher name or a valid @id reference."
            ))

        if page.title and art.get("headline") and art["headline"] not in page.title and page.title not in art["headline"]:
            findings.append(Finding(
                "ARTICLE_HEADLINE_MISMATCH", "warning", page.path,
                f"JSON-LD headline ({art['headline']!r}) does not align with title ({page.title!r}).",
                "Align headline with HTML <title>."
            ))

        if page.description and art.get("description"):
            meta_norm = re.sub(r"\s+", " ", page.description.strip().lower())
            ld_norm = re.sub(r"\s+", " ", art["description"].strip().lower())
            # Allow JSON-LD description to be a truncated version of the meta description.
            shorter = min(len(meta_norm), len(ld_norm))
            if shorter > 0 and not (meta_norm.startswith(ld_norm[:shorter]) or ld_norm.startswith(meta_norm[:shorter])):
                findings.append(Finding(
                    "ARTICLE_DESCRIPTION_MISMATCH", "warning", page.path,
                    "JSON-LD description does not align with meta description.",
                    "Align structured-data description with meta description."
                ))

    if not has_visible_author(page):
        findings.append(Finding(
            "ARTICLE_AUTHOR_NOT_VISIBLE", "warning", page.path,
            "Author is present in structured data but not visible on the page.",
            "Consider rendering a by-line or author block."
        ))

    # Dates
    if art:
        dp = art.get("datePublished")
        dm = art.get("dateModified")
        if dp and dm and dp > dm:
            findings.append(Finding(
                "ARTICLE_DATE_ORDER_INVALID", "critical", page.path,
                f"dateModified ({dm}) is earlier than datePublished ({dp}).",
                "Correct date order in front matter or structured data."
            ))

    # Canonical
    if not page.canonical:
        findings.append(Finding(
            "ARTICLE_CANONICAL_MISSING", "critical", page.path,
            "Indexable article-like page has no canonical link.",
            "Add a canonical URL."
        ))
    else:
        if not page.canonical.startswith("https://"):
            findings.append(Finding(
                "ARTICLE_CANONICAL_NOT_ABSOLUTE", "critical", page.path,
                f"Canonical URL is not absolute HTTPS: {page.canonical!r}",
                "Use an absolute https:// canonical URL."
            ))
        if "localhost" in page.canonical or "127.0.0.1" in page.canonical:
            findings.append(Finding(
                "ARTICLE_CANONICAL_LOCALHOST", "critical", page.path,
                f"Canonical URL points to localhost: {page.canonical!r}",
                "Replace localhost with the production origin."
            ))

    # Robots sanity
    if page.is_noindex:
        findings.append(Finding(
            "ARTICLE_UNEXPECTED_NOINDEX", "critical", page.path,
            "Page classified as indexable article but has robots noindex.",
            "Resolve robots directive or page classification."
        ))

    # OG / Twitter
    for label, value in [("og:title", page.og_title), ("og:description", page.og_description),
                         ("og:url", page.og_url), ("og:type", page.og_type)]:
        if not value:
            findings.append(Finding(
                f"ARTICLE_OG_{label.upper().replace(':', '_')}_MISSING", "warning", page.path,
                f"Open Graph {label} is missing.",
                f"Add <meta property=\"{label}\">."
            ))
    if not page.twitter_card:
        findings.append(Finding(
            "ARTICLE_TWITTER_CARD_MISSING", "warning", page.path,
            "Twitter card meta tag is missing.",
            "Add <meta name=\"twitter:card\">."
        ))
    if page.og_image:
        if "localhost" in page.og_image or "127.0.0.1" in page.og_image:
            findings.append(Finding(
                "ARTICLE_OG_IMAGE_LOCALHOST", "critical", page.path,
                f"Open Graph image points to localhost: {page.og_image!r}",
                "Use a production image URL."
            ))
        elif page.og_image.startswith("http://"):
            findings.append(Finding(
                "ARTICLE_OG_IMAGE_INSECURE", "warning", page.path,
                f"Open Graph image uses HTTP: {page.og_image!r}",
                "Use HTTPS for the OG image."
            ))

    # Content structure
    if page.word_count < 150:
        findings.append(Finding(
            "ARTICLE_CONTENT_TOO_THIN", "warning", page.path,
            f"Visible word count is low ({page.word_count} words).",
            "Add substantive content or demote to noindex."
        ))

    headings = re.findall(r"<h[2-6][^>]*>(.*?)</h[2-6]>", page.content, re.IGNORECASE | re.DOTALL)
    clean_headings = [re.sub(r"<[^>]+>", "", h).strip() for h in headings if re.sub(r"<[^>]+>", "", h).strip()]
    if page.word_count >= 300 and len(clean_headings) == 0:
        findings.append(Finding(
            "ARTICLE_NO_SECTION_HEADINGS", "warning", page.path,
            "Long article has no section headings after H1.",
            "Add H2/H3 sections to improve structure."
        ))

    for ch in clean_headings:
        if re.search(r"\b(TODO|FIXME|PLACEHOLDER|SECTION)\b", ch, re.IGNORECASE):
            findings.append(Finding(
                "ARTICLE_PLACEHOLDER_HEADING", "critical", page.path,
                f"Heading appears to be a placeholder: {ch!r}",
                "Replace placeholder heading with descriptive text."
            ))

    # Placeholder text outside intentional weak/example contexts
    weak_context_terms = [
        "weak output", "bad example", "poor example", "why this is weak",
        "why it fails", "why this fails", "anti-pattern", "example of",
        "sample output", "incorrect example", "do not use",
    ]
    text_no_code = text_outside_code_blocks(page.content)
    for pattern in PLACEHOLDER_PATTERNS:
        match = pattern.search(text_no_code)
        if match:
            # Grab surrounding context (200 chars) to decide if it's an example
            start = max(0, match.start() - 100)
            end = min(len(text_no_code), match.end() + 100)
            context = text_no_code[start:end].lower()
            if any(term in context for term in weak_context_terms):
                continue
            findings.append(Finding(
                "ARTICLE_PLACEHOLDER_TEXT", "critical", page.path,
                f"Indexable page contains placeholder text matching {pattern.pattern}.",
                "Remove placeholder text before publishing."
            ))
            break

    # Internal links
    if page.word_count >= 200 and not page.internal_links:
        findings.append(Finding(
            "ARTICLE_NO_INTERNAL_LINKS", "warning", page.path,
            "Substantial article has no internal links.",
            "Add at least one contextual internal link."
        ))

    return findings


def check_indexable_collection(page: Page) -> list[Finding]:
    findings: list[Finding] = []
    if not page.title:
        findings.append(Finding(
            "COLLECTION_TITLE_MISSING", "critical", page.path,
            "Indexable collection page has no <title>.",
            "Add a title."
        ))
    if not page.description:
        findings.append(Finding(
            "COLLECTION_META_DESCRIPTION_MISSING", "critical", page.path,
            "Indexable collection page has no meta description.",
            "Add a meta description."
        ))
    h1_count = len(page.h1_texts)
    if h1_count == 0:
        findings.append(Finding(
            "COLLECTION_H1_MISSING", "critical", page.path,
            "Indexable collection page has no <h1>.",
            "Add a single <h1>."
        ))
    elif h1_count > 1:
        findings.append(Finding(
            "COLLECTION_H1_DUPLICATE", "warning", page.path,
            f"Collection page has {h1_count} <h1> elements.",
            "Use a single <h1> for collection pages."
        ))
    if not page.canonical:
        findings.append(Finding(
            "COLLECTION_CANONICAL_MISSING", "critical", page.path,
            "Indexable collection page has no canonical URL.",
            "Add a canonical URL."
        ))
    if page.is_noindex:
        findings.append(Finding(
            "COLLECTION_UNEXPECTED_NOINDEX", "critical", page.path,
            "Page classified as indexable collection but has robots noindex.",
            "Resolve robots directive or classification."
        ))
    if page.word_count < 30 and not re.search(r'<(ul|ol|div)[^>]*class=["\'][^"\']*(list|grid|cards|items)', page.content, re.IGNORECASE):
        findings.append(Finding(
            "COLLECTION_CONTENT_EMPTY", "warning", page.path,
            "Collection page appears to have very little content and no visible list/grid.",
            "Add collection items or a visible list."
        ))
    return findings


def check_private_and_localhost(page: Page) -> list[Finding]:
    findings: list[Finding] = []

    url_values = collect_url_values(page)
    url_text = " ".join(url_values).lower()

    # 1) Real file-system / local leaks outside code/pre blocks or in URL values.
    # Documentation pages legitimately mention patterns like /Users/ or .env.local
    # inside <code> examples; we only flag them when they appear as real content or URLs.
    text_no_code = text_outside_code_blocks(page.content).lower()
    combined_text = f"{text_no_code} {url_text}"
    for pattern in PRIVATE_PATH_PATTERNS:
        if pattern.lower() in combined_text:
            findings.append(Finding(
                "PRIVATE_PATH_LEAK", "critical", page.path,
                f"Page contains private path or token pattern outside code blocks or in a URL: {pattern!r}",
                "Remove private paths from public output."
            ))
            break

    # 2) Localhost must only appear in actual URL values, not in explanatory text.
    for pattern in LOCALHOST_PATTERNS:
        if pattern in url_text:
            findings.append(Finding(
                "LOCALHOST_URL", "critical", page.path,
                f"URL value contains localhost reference: {pattern!r}",
                "Replace localhost with the production origin."
            ))
            break

    # 3) Unrendered template tokens outside code/pre blocks only.
    if "{{" in text_no_code or "{%" in text_no_code:
        findings.append(Finding(
            "BROKEN_TEMPLATE_TOKEN", "critical", page.path,
            "Visible text outside code blocks contains unrendered Liquid/Jinja template tokens.",
            "Fix template rendering so tokens do not appear in HTML."
        ))
    return findings


def check_noindex_page(page: Page, page_type: str) -> list[Finding]:
    findings: list[Finding] = []
    # Noindex pages should not leak private/localhost data or have broken tokens
    findings.extend(check_private_and_localhost(page))

    # Check for accidental indexable structured data on noindex pages
    rich_indexable_types = {"Article", "TechArticle", "NewsArticle", "BlogPosting", "Product", "Event", "Course", "Dataset"}
    if any(t in rich_indexable_types for t in page.jsonld_types):
        findings.append(Finding(
            "NOINDEX_RICH_STRUCTURED_DATA", "warning", page.path,
            f"Noindex page emits rich structured data types: {page.jsonld_types}.",
            "Consider using WebPage or omitting structured data on noindex pages."
        ))

    if page.canonical and "localhost" in page.canonical:
        findings.append(Finding(
            "NOINDEX_CANONICAL_LOCALHOST", "critical", page.path,
            f"Noindex page canonical points to localhost: {page.canonical!r}",
            "Use the production origin."
        ))

    # Broken template tokens in metadata are critical regardless of indexability
    for value, name in [(page.title, "title"), (page.description, "description"), (page.canonical, "canonical")]:
        if "{{" in value or "{%" in value:
            findings.append(Finding(
                "METADATA_TEMPLATE_TOKEN", "critical", page.path,
                f"{name} contains unrendered template tokens: {value!r}",
                "Fix template rendering."
            ))

    return findings


def check_page(page: Page, page_type: str) -> list[Finding]:
    findings: list[Finding] = []

    if page_type in {"indexable_article", "indexable_atlas_verified", "indexable_skill_hub"}:
        findings.extend(check_indexable_article(page, page_type))
    elif page_type in {"indexable_collection", "indexable_dataset_detail", "indexable_service_or_profile"}:
        findings.extend(check_indexable_collection(page))
    elif page_type in {"noindex_review_candidate", "noindex_research_or_draft", "utility_page"}:
        findings.extend(check_noindex_page(page, page_type))

    # Cross-cutting checks for all pages
    findings.extend(check_private_and_localhost(page))

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-dir", default="_site", help="Built site root")
    parser.add_argument("--fail-on-critical", action="store_true", help="Exit non-zero on critical findings")
    parser.add_argument(
        "--warning-budget",
        type=int,
        default=None,
        help="Fail when warning findings exceed this count.",
    )
    parser.add_argument("--json", action="store_true", help="Output findings as JSON")
    args = parser.parse_args()

    site_dir = Path(args.site_dir)
    if not site_dir.is_dir():
        print(f"Missing directory: {site_dir}. Build the site before running.")
        return 1

    html_files = sorted(site_dir.rglob("*.html"))
    all_findings: list[Finding] = []
    stats = {"pages": len(html_files), "critical": 0, "warning": 0, "info": 0}

    for html_path in html_files:
        page = parse_page(html_path, site_dir)
        page_type = classify_page(page)
        findings = check_page(page, page_type)
        for f in findings:
            stats[f.severity] = stats.get(f.severity, 0) + 1
        all_findings.extend(findings)

    if args.json:
        output = [
            {
                "rule": f.rule,
                "severity": f.severity,
                "path": f.path,
                "message": f.message,
                "fix": f.fix,
            }
            for f in all_findings
        ]
        print(json.dumps({"stats": stats, "findings": output}, indent=2))
    else:
        if all_findings:
            print(f"Page quality check found {len(all_findings)} issue(s) across {stats['pages']} pages:")
            print(f"  critical: {stats.get('critical', 0)}")
            print(f"  warning: {stats.get('warning', 0)}")
            print(f"  info: {stats.get('info', 0)}")
            print()
            for finding in all_findings:
                print(finding)
                print()
        else:
            print(f"Page quality check passed for {stats['pages']} HTML files.")

    warnings_exceed_budget = (
        args.warning_budget is not None
        and stats.get("warning", 0) > args.warning_budget
    )
    if warnings_exceed_budget:
        print(
            f"Page quality warning budget exceeded: "
            f"{stats.get('warning', 0)} warning(s) > budget {args.warning_budget}.",
            file=sys.stderr,
        )

    if args.fail_on_critical and stats.get("critical", 0) > 0:
        return 2
    if warnings_exceed_budget:
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
