"""Shared public-content discovery and eligibility model.

This module deliberately contains policy primitives used by the quality
pipeline. It does not decide whether technical prose is correct; it reports
whether the repository has the metadata and publication signals needed to
review that question safely.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

import yaml


DEFAULT_BASE_URL = "https://dkharlanau.github.io"
FRONT_MATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*(?:\n|$)", re.DOTALL)


@dataclass
class ContentPage:
    source_path: Path
    permalink: str = ""
    canonical_url: str = ""
    collection: str = ""
    content_model: str = ""
    language: str = "en"
    title: str = ""
    description: str = ""
    author: str = ""
    date_published: str = ""
    date_modified: str = ""
    last_reviewed: str = ""
    status: str = ""
    verified: bool = False
    robots: str = ""
    sitemap_enabled: bool = True
    retrieval_eligible: bool = False
    expert_context_enabled: bool = False
    topics: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    service_url: str = ""
    evidence_urls: list[str] = field(default_factory=list)
    body: str = ""
    frontmatter: dict[str, Any] = field(default_factory=dict)

    @property
    def relative_path(self) -> str:
        return self.source_path.as_posix()

    @property
    def is_indexable(self) -> bool:
        return "noindex" not in self.robots.lower() and self.sitemap_enabled

    @property
    def fingerprint(self) -> str:
        return hashlib.sha1(self.relative_path.encode("utf-8")).hexdigest()[:12]


def parse_frontmatter(path: Path) -> tuple[dict[str, Any], str, str | None]:
    """Return (frontmatter, body, parse_error) for a Markdown file."""
    text = path.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---"):
        return {}, text, None
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return {}, text, "front matter starts with --- but has no closing delimiter"
    try:
        data = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError as exc:
        return {}, text[match.end():], str(exc)
    if not isinstance(data, dict):
        return {}, text[match.end():], "front matter root must be a mapping"
    return data, text[match.end():], None


def canonical_url(permalink: str, base_url: str = DEFAULT_BASE_URL) -> str:
    value = str(permalink or "").strip()
    if not value:
        return ""
    if value.startswith("http://") or value.startswith("https://"):
        return value
    return f"{base_url.rstrip('/')}/{value.strip('/')}/"


def normalize_language(value: Any) -> str:
    text = str(value or "en").strip().lower()
    return text or "en"


def _as_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, (list, tuple, set)):
        return [str(item).strip() for item in value if str(item).strip()]
    return [str(value).strip()] if str(value).strip() else []


def infer_collection(rel_path: str) -> str:
    parts = rel_path.split("/")
    if rel_path.startswith("_blog/"):
        return "blog"
    if rel_path.startswith("_notes/"):
        return "notes"
    if rel_path.startswith("_news/"):
        return "news"
    if rel_path.startswith("_radar/"):
        return "radar"
    return parts[0] if parts else "pages"


def infer_permalink(rel_path: str, fm: dict[str, Any]) -> str:
    """Mirror the repository's collection defaults when front matter omits one."""
    explicit = str(fm.get("permalink") or "").strip()
    if explicit:
        return explicit
    path = Path(rel_path)
    stem = path.stem
    if rel_path.startswith("_blog/"):
        return f"/blog/{stem}/"
    if rel_path.startswith("_notes/"):
        return f"/notes/{stem}/"
    if rel_path.startswith("_radar/"):
        return f"/radar/{stem}/"
    if rel_path.startswith("_news/"):
        return f"/news/{stem}/"
    if rel_path.startswith("_glossary/"):
        return f"/atlas/glossary/{stem}/"
    return ""


def infer_content_model(rel_path: str, fm: dict[str, Any]) -> tuple[str, bool]:
    explicit = str(fm.get("content_model") or "").strip()
    if explicit:
        return explicit, False
    path = rel_path.lower()
    if path.startswith("atlas/diagnostics/"):
        return "diagnostic", True
    if path.startswith(("services/",)):
        return "service", True
    if path.startswith(("scenarios/",)):
        return "scenario", True
    if path.startswith(("datasets/",)):
        return "dataset", True
    if path.startswith(("agent-tools/", "mcp/")):
        return "tool", True
    if "sap-architecture-course" in path or path.startswith("skill-hub/architecture/"):
        return "architecture", True
    if path.startswith(("research/", "_radar/")):
        return "research", True
    if path in {"about.md", "cv/index.html"} or path.startswith("ai/resume"):
        return "profile", True
    if path.startswith(("atlas/concepts/", "atlas/maps/", "atlas/sap/")):
        return "reference", True
    if path.startswith(("_blog/", "_notes/")):
        return "opinion", True
    if path.startswith(("atlas/", "skill-hub/")):
        return "technical_guide", True
    if path in {"index.md", "blog/index.md", "notes/index.md", "research/index.md", "skill-hub/index.md"}:
        return "landing_page", True
    return "technical_guide", True


def make_page(repo_root: Path, path: Path, fm: dict[str, Any], body: str, base_url: str = DEFAULT_BASE_URL) -> ContentPage:
    rel = path.relative_to(repo_root).as_posix()
    expert = fm.get("expert_context") or {}
    topics = _as_list(fm.get("topics")) + _as_list(fm.get("tags"))
    if isinstance(fm.get("search"), dict):
        topics += _as_list(fm["search"].get("topic_cluster"))
    content_model, inferred = infer_content_model(rel, fm)
    resolved_permalink = infer_permalink(rel, fm)
    return ContentPage(
        source_path=Path(rel),
        permalink=resolved_permalink,
        canonical_url=canonical_url(resolved_permalink, base_url),
        collection=infer_collection(rel),
        content_model=content_model,
        language=normalize_language(fm.get("lang") or fm.get("language") or fm.get("locale")),
        title=str(fm.get("title") or "").strip(),
        description=str(fm.get("description") or "").strip(),
        author=str(fm.get("author") or "").strip(),
        date_published=str(fm.get("date") or fm.get("published") or "").strip(),
        date_modified=str(fm.get("last_modified_at") or fm.get("updated") or "").strip(),
        last_reviewed=str(fm.get("last_reviewed") or "").strip(),
        status=str(fm.get("status") or "").strip(),
        verified=fm.get("verified") is True,
        robots=str(fm.get("robots") or ""),
        sitemap_enabled=fm.get("sitemap", True) is not False,
        retrieval_eligible=bool(resolved_permalink) and fm.get("verified") is True and fm.get("status") == "reviewed" and "noindex" not in str(fm.get("robots") or "").lower() and fm.get("sitemap", True) is not False,
        expert_context_enabled=expert.get("enabled") is True,
        topics=list(dict.fromkeys(topics)),
        tags=_as_list(fm.get("tags")),
        service_url=str(expert.get("service_url") or fm.get("service_url") or "").strip(),
        evidence_urls=_as_list(expert.get("evidence_urls") or fm.get("evidence_urls")),
        body=body,
        frontmatter=fm,
    )


def discover_pages(repo_root: Path, excluded_prefixes: Iterable[str] = ()) -> tuple[list[ContentPage], list[dict[str, Any]]]:
    excluded_values = tuple(str(item).strip() for item in excluded_prefixes)
    excluded = tuple(value.rstrip("/") + "/" for value in excluded_values if value and not value.endswith(".md"))
    excluded_files = {value.rstrip("/") for value in excluded_values if value.endswith(".md")}
    pages: list[ContentPage] = []
    parse_errors: list[dict[str, Any]] = []
    for path in sorted(repo_root.rglob("*.md")):
        rel = path.relative_to(repo_root).as_posix()
        if rel in excluded_files or any(rel.startswith(prefix) for prefix in excluded) or rel.startswith("."):
            continue
        fm, body, error = parse_frontmatter(path)
        if error:
            parse_errors.append({"path": rel, "error": error})
            continue
        if not fm:
            continue
        pages.append(make_page(repo_root, path, fm, body))
    return pages, parse_errors


def normalize_text(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    value = re.sub(r"\{%.*?%\}|\{\{.*?\}\}", " ", value, flags=re.DOTALL)
    value = re.sub(r"[^a-z0-9]+", " ", value.lower())
    return re.sub(r"\s+", " ", value).strip()


def word_count(value: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", normalize_text(value)))


def stable_fingerprint(rule_id: str, page: ContentPage, location: str = "") -> str:
    raw = f"{rule_id}|{page.permalink or page.relative_path}|{normalize_text(location)}"
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()[:16]
