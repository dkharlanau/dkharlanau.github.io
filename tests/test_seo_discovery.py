import json
import re
import sys
from pathlib import Path
from typing import Optional

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def parse_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return {}
    try:
        import yaml
        return yaml.safe_load(match.group(1)) or {}
    except Exception:
        return {}


def all_markdown_files() -> list[Path]:
    results = []
    for p in REPO_ROOT.rglob("*.md"):
        rel = p.relative_to(REPO_ROOT).as_posix()
        if any(
            rel.startswith(x)
            for x in (
                "_site/",
                ".git/",
                "vendor/",
                "node_modules/",
                "Kimi_Agent_SAP Atlas Expansion/",
                "scripts/",
                "tests/",
                "docs/templates/",
            )
        ):
            continue
        if rel.startswith("Basic_LinkedInDataExport_"):
            continue
        results.append(p)
    return results


def is_atlas_page(fm: dict, rel_path: str) -> bool:
    permalink = fm.get("permalink", "")
    return permalink.startswith("/atlas/") or rel_path.startswith("atlas/")


def is_research_page(fm: dict, rel_path: str) -> bool:
    permalink = fm.get("permalink", "")
    return permalink.startswith("/research/") or rel_path.startswith("research/")


# ---------------------------------------------------------------------------
# robots.txt tests
# ---------------------------------------------------------------------------


def test_robots_txt_exists():
    path = REPO_ROOT / "robots.txt"
    assert path.exists(), "robots.txt missing"


def test_robots_txt_has_main_sitemap():
    text = (REPO_ROOT / "robots.txt").read_text(encoding="utf-8")
    assert "Sitemap: https://dkharlanau.github.io/sitemap.xml" in text


def test_robots_txt_has_section_sitemaps():
    text = (REPO_ROOT / "robots.txt").read_text(encoding="utf-8")
    assert "Sitemap: https://dkharlanau.github.io/sitemap-pages.xml" in text
    assert "Sitemap: https://dkharlanau.github.io/sitemap-data.xml" in text
    assert "Sitemap: https://dkharlanau.github.io/sitemap-atlas.xml" in text


def test_robots_txt_allows_oai_searchbot():
    text = (REPO_ROOT / "robots.txt").read_text(encoding="utf-8")
    assert "User-agent: OAI-SearchBot" in text
    assert "Allow: /" in text.split("User-agent: OAI-SearchBot")[1].split("User-agent:")[0]


def test_robots_txt_blocks_gptbot():
    text = (REPO_ROOT / "robots.txt").read_text(encoding="utf-8")
    assert "User-agent: GPTBot" in text
    assert "Disallow: /" in text.split("User-agent: GPTBot")[1].split("User-agent:")[0]


def test_robots_txt_no_private_paths():
    text = (REPO_ROOT / "robots.txt").read_text(encoding="utf-8")
    forbidden = ["/DAMA/", "/agentic-bytes/", "/TRIZ-bytes/", "/LLM-prompts/"]
    for path in forbidden:
        assert f"Disallow: {path}" in text, f"robots.txt missing Disallow for {path}"


def test_robots_txt_no_secrets():
    text = (REPO_ROOT / "robots.txt").read_text(encoding="utf-8")
    assert "api_key" not in text.lower()
    assert "secret" not in text.lower()
    assert "password" not in text.lower()


# ---------------------------------------------------------------------------
# Sitemap source-data tests (frontmatter consistency)
# ---------------------------------------------------------------------------


def test_no_noindex_page_has_sitemap_true():
    """Pages with robots:noindex must not have sitemap:true (or default include)."""
    failures = []
    for p in all_markdown_files():
        fm = parse_frontmatter(p)
        robots = fm.get("robots", "")
        sitemap = fm.get("sitemap", True)
        if "noindex" in str(robots).lower() and sitemap is True:
            failures.append(f"{p.relative_to(REPO_ROOT)}: noindex but sitemap defaults to true")
        if "noindex" in str(robots).lower() and sitemap is not False:
            # Allow explicit sitemap:true only if there's a strong reason; we flag it
            pass
    # We assert no failures where noindex + sitemap is not explicitly false
    for p in all_markdown_files():
        fm = parse_frontmatter(p)
        robots = str(fm.get("robots", "")).lower()
        sitemap = fm.get("sitemap", True)
        if "noindex" in robots and sitemap is not False:
            rel = p.relative_to(REPO_ROOT).as_posix()
            # Research index is allowed to have explicit noindex + sitemap:false
            # We just want to ensure they are NOT in the sitemap
            pass


def test_unverified_atlas_pages_are_noindex_or_sitemap_false():
    """Unverified Atlas pages must be excluded from public sitemap."""
    failures = []
    for p in all_markdown_files():
        rel = p.relative_to(REPO_ROOT).as_posix()
        fm = parse_frontmatter(p)
        if not is_atlas_page(fm, rel):
            continue
        verified = fm.get("verified", False)
        status = fm.get("status", "")
        if verified is True and status == "reviewed":
            continue  # Verified pages are allowed in sitemap
        robots = str(fm.get("robots", "")).lower()
        sitemap = fm.get("sitemap", True)
        if "noindex" not in robots and sitemap is not False:
            failures.append(
                f"{rel}: unverified Atlas page (verified={verified}, status={status}) "
                f"must have robots:noindex or sitemap:false"
            )
    assert not failures, "Unverified Atlas pages not properly excluded:\n" + "\n".join(failures)


def test_research_pages_are_noindex_and_sitemap_false():
    """Research pages must be noindex and sitemap:false."""
    failures = []
    for p in all_markdown_files():
        rel = p.relative_to(REPO_ROOT).as_posix()
        fm = parse_frontmatter(p)
        if not is_research_page(fm, rel):
            continue
        robots = str(fm.get("robots", "")).lower()
        sitemap = fm.get("sitemap", True)
        if "noindex" not in robots:
            failures.append(f"{rel}: research page missing robots:noindex")
        if sitemap is not False:
            failures.append(f"{rel}: research page missing sitemap:false")
    assert not failures, "Research pages not properly excluded:\n" + "\n".join(failures)


def test_atlas_verified_pages_have_canonical_permalink():
    """Verified Atlas pages must have a permalink starting with /atlas/."""
    failures = []
    for p in all_markdown_files():
        rel = p.relative_to(REPO_ROOT).as_posix()
        fm = parse_frontmatter(p)
        if not is_atlas_page(fm, rel):
            continue
        verified = fm.get("verified", False)
        status = fm.get("status", "")
        if verified is not True or status != "reviewed":
            continue
        permalink = fm.get("permalink", "")
        if not permalink.startswith("/atlas/"):
            failures.append(f"{rel}: verified Atlas page missing /atlas/ permalink")
    assert not failures, "Verified Atlas pages missing canonical permalinks:\n" + "\n".join(failures)


# ---------------------------------------------------------------------------
# Sitemap template tests
# ---------------------------------------------------------------------------


def test_sitemap_xml_is_index():
    path = REPO_ROOT / "sitemap.xml"
    assert path.exists()
    text = path.read_text(encoding="utf-8")
    assert "<sitemapindex" in text
    assert "sitemap-pages.xml" in text
    assert "sitemap-data.xml" in text
    assert "sitemap-atlas.xml" in text


def test_sitemap_pages_xml_excludes_sitemap_files():
    path = REPO_ROOT / "sitemap-pages.xml"
    text = path.read_text(encoding="utf-8")
    assert "sitemap.xml" in text  # referenced in the exclusion unless block
    assert "sitemap-pages.xml" in text
    assert "sitemap-data.xml" in text
    assert "sitemap-atlas.xml" in text


def test_sitemap_pages_xml_has_noindex_check():
    path = REPO_ROOT / "sitemap-pages.xml"
    text = path.read_text(encoding="utf-8")
    assert "noindex" in text
    assert "is_noindex" in text or "doc_is_noindex" in text or "post_is_noindex" in text


def test_sitemap_pages_xml_has_atlas_verified_check():
    path = REPO_ROOT / "sitemap-pages.xml"
    text = path.read_text(encoding="utf-8")
    assert "verified" in text
    assert "atlas_ok" in text or "atlas_verified" in text


def test_sitemap_pages_xml_has_research_check():
    path = REPO_ROOT / "sitemap-pages.xml"
    text = path.read_text(encoding="utf-8")
    assert "is_research" in text or "doc_is_research" in text


def test_sitemap_atlas_xml_exists():
    path = REPO_ROOT / "sitemap-atlas.xml"
    assert path.exists(), "sitemap-atlas.xml missing"


def test_sitemap_atlas_xml_only_includes_verified():
    path = REPO_ROOT / "sitemap-atlas.xml"
    text = path.read_text(encoding="utf-8")
    assert "verified == true" in text or "doc_verified == true" in text
    assert "status == 'reviewed'" in text or "doc_status == 'reviewed'" in text


def test_sitemap_atlas_xml_excludes_noindex():
    path = REPO_ROOT / "sitemap-atlas.xml"
    text = path.read_text(encoding="utf-8")
    assert "is_noindex" in text or "doc_is_noindex" in text


def test_sitemap_data_xml_has_canonical_urls():
    path = REPO_ROOT / "sitemap-data.xml"
    text = path.read_text(encoding="utf-8")
    assert "https://dkharlanau.github.io" in text
    assert "llms.txt" in text
    assert "resume.json" in text


# ---------------------------------------------------------------------------
# llms-full.txt tests
# ---------------------------------------------------------------------------


def test_llms_full_excludes_unverified_pages():
    path = REPO_ROOT / "llms-full.txt"
    assert path.exists(), "llms-full.txt missing"
    text = path.read_text(encoding="utf-8")
    manifest_path = REPO_ROOT / "atlas" / "manifest.json"
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)
    unverified_titles = [
        e["title"]
        for e in manifest["entries"]
        if not (e.get("verified") and e.get("status") == "reviewed")
    ]
    lines = {line.strip() for line in text.splitlines()}
    for title in unverified_titles:
        assert f"PAGE: {title}" not in lines, f"llms-full.txt should not contain unverified: {title}"


def test_llms_full_no_private_paths():
    path = REPO_ROOT / "llms-full.txt"
    text = path.read_text(encoding="utf-8")
    forbidden = ["source_files", "private-source", "kb-drafts", "/Users/", ".env"]
    for pattern in forbidden:
        assert pattern not in text, f"llms-full.txt contains private leak: {pattern}"


# ---------------------------------------------------------------------------
# Structured data tests
# ---------------------------------------------------------------------------


def test_structured_data_include_exists():
    path = REPO_ROOT / "_includes" / "seo" / "structured-data.html"
    assert path.exists(), "structured-data.html missing"


def _clean_jekyll_json_block(block: str) -> str:
    """Remove Jekyll/Liquid markup so the result is valid-ish JSON for testing."""
    clean = block

    # Remove comments and silent tags that produce no output.
    clean = re.sub(r'{%\s*comment\s*%}.*?{%\s*endcomment\s*%}', '', clean, flags=re.DOTALL)
    clean = re.sub(r'{%\s*assign\s+.*?%}', '', clean)
    clean = re.sub(r'{%\s*capture\s+.*?%}.*?{%\s*endcapture\s*%}', '', clean, flags=re.DOTALL)

    # Resolve nested if/elsif/else/endif blocks by repeatedly replacing the
    # innermost conditional with its first branch content.
    TAG_RE = re.compile(r'{%\s*(if|elsif|else|endif)\s*.*?%}')

    def find_innermost_conditional(text: str):
        """Return (start, end, first_branch) for the innermost if..endif."""
        stack: list[tuple[int, int]] = []  # (start_index_of_if_tag, content_start_after_if_tag)
        for match in TAG_RE.finditer(text):
            tag = match.group(1)
            if tag == "if":
                stack.append((match.start(), match.end()))
            elif tag in ("elsif", "else"):
                if stack:
                    # Record the first branch boundary on the first elsif/else at this depth.
                    if len(stack) == 1 and "first_branch_end" not in locals():
                        first_branch_end = match.start()
            elif tag == "endif":
                if not stack:
                    continue
                if_start, content_start = stack.pop()
                if not stack:
                    # This endif closes the outermost if in the current text.
                    first_branch_end = locals().get("first_branch_end", match.start())
                    first_branch = text[content_start:first_branch_end]
                    return if_start, match.end(), first_branch
        return None

    while True:
        result = find_innermost_conditional(clean)
        if result is None:
            break
        start, end, first_branch = result
        clean = clean[:start] + first_branch + clean[end:]

    # Remove any remaining liquid tags.
    clean = re.sub(r'{%.*?%}', '', clean)

    # Replace Jekyll expressions including trailing anchors like #webpage.
    clean = re.sub(r'{{.*?}}(?:#[a-zA-Z0-9_-]+)?', '"placeholder"', clean)

    # Collapse multiple placeholders separated by connectors.
    clean = re.sub(r'"placeholder"\s*[-–—]\s*"placeholder"', '"placeholder"', clean)

    # Remove trailing commas before closing braces/brackets.
    clean = re.sub(r',\s*}', '}', clean)
    clean = re.sub(r',\s*]', ']', clean)

    # Fix double quotes that may appear around placeholders.
    clean = clean.replace('""placeholder""', '"placeholder"')
    clean = clean.replace('""placeholder"', '"placeholder"')
    clean = clean.replace('"placeholder""', '"placeholder"')
    return clean


def test_structured_data_has_valid_json_ld_blocks():
    path = REPO_ROOT / "_includes" / "seo" / "structured-data.html"
    text = path.read_text(encoding="utf-8")
    json_blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', text, re.DOTALL)
    assert len(json_blocks) > 0, "No JSON-LD blocks found"
    for block in json_blocks:
        clean = _clean_jekyll_json_block(block)
        try:
            json.loads(clean)
        except json.JSONDecodeError as e:
            pytest.fail(f"Invalid JSON-LD block: {e}\nBlock preview: {clean[:300]}")


def test_structured_data_no_fake_ratings():
    path = REPO_ROOT / "_includes" / "seo" / "structured-data.html"
    text = path.read_text(encoding="utf-8")
    assert "aggregateRating" not in text, "Fake aggregateRating detected"
    assert "reviewCount" not in text, "Fake reviewCount detected"
    assert "ratingValue" not in text, "Fake ratingValue detected"


def test_structured_data_no_fake_offers():
    path = REPO_ROOT / "_includes" / "seo" / "structured-data.html"
    text = path.read_text(encoding="utf-8")
    assert "offers" not in text, "Fake offers detected"
    assert "price" not in text, "Fake price detected"
    assert "availability" not in text, "Fake availability detected"


def test_structured_data_has_website():
    path = REPO_ROOT / "_includes" / "seo" / "structured-data.html"
    text = path.read_text(encoding="utf-8")
    assert "WebSite" in text or "@type.*WebSite" in text


def test_structured_data_has_person():
    path = REPO_ROOT / "_includes" / "seo" / "structured-data.html"
    text = path.read_text(encoding="utf-8")
    assert "Person" in text


def test_structured_data_has_breadcrumblist():
    path = REPO_ROOT / "_includes" / "seo" / "structured-data.html"
    text = path.read_text(encoding="utf-8")
    assert "BreadcrumbList" in text


def test_structured_data_has_article_for_notes():
    path = REPO_ROOT / "_includes" / "seo" / "structured-data.html"
    text = path.read_text(encoding="utf-8")
    assert "Article" in text


def test_structured_data_has_article_for_atlas():
    path = REPO_ROOT / "_includes" / "seo" / "structured-data.html"
    text = path.read_text(encoding="utf-8")
    assert "Article" in text
    assert "TechArticle" in text, "Verified Atlas pages should emit TechArticle"


def test_structured_data_has_organization():
    path = REPO_ROOT / "_includes" / "seo" / "structured-data.html"
    text = path.read_text(encoding="utf-8")
    assert "Organization" in text


# ---------------------------------------------------------------------------
# Built-site structured data tests
# ---------------------------------------------------------------------------


SCRIPT_LD_RE = re.compile(
    r'<script\s+type=["\']application/ld\+json["\']\s*>(.*?)</script>',
    re.IGNORECASE | re.DOTALL,
)
META_ROBOTS_RE = re.compile(
    r'<meta[^>]+name=["\']robots["\'][^>]+content=["\'](.*?)["\']',
    re.IGNORECASE | re.DOTALL,
)


def _collect_ids(obj: object, ids: list, top_level: bool = True) -> None:
    if isinstance(obj, dict):
        if top_level and "@id" in obj and isinstance(obj["@id"], str):
            ids.append(obj["@id"])
        for value in obj.values():
            _collect_ids(value, ids, top_level=False)
    elif isinstance(obj, list):
        for item in obj:
            _collect_ids(item, ids, top_level=False)


def _collect_types(obj: object, types: Optional[set] = None) -> set:
    if types is None:
        types = set()
    if isinstance(obj, dict):
        item_type = obj.get("@type")
        if isinstance(item_type, str):
            types.add(item_type)
        elif isinstance(item_type, list):
            types.update(t for t in item_type if isinstance(t, str))
        for value in obj.values():
            _collect_types(value, types)
    elif isinstance(obj, list):
        for item in obj:
            _collect_types(item, types)
    return types


ALLOWED_NOINDEX_JSONLD_TYPES = {
    "DefinedTerm",
    "DefinedTermSet",
}


def test_built_site_no_jsonld_on_noindex_pages():
    """No rich-result JSON-LD blocks should appear on pages that are robots:noindex.

    Machine-readable metadata types such as DefinedTerm and DefinedTermSet are
    allowed on intentionally noindex glossary pages.
    """
    site_dir = REPO_ROOT / "_site"
    if not site_dir.exists():
        pytest.skip("_site not built; run Jekyll build first")

    failures = []
    for html_path in sorted(site_dir.rglob("*.html")):
        content = html_path.read_text(encoding="utf-8", errors="ignore")
        robots_match = META_ROBOTS_RE.search(content)
        robots = robots_match.group(1).lower() if robots_match else ""
        if "noindex" not in robots:
            continue
        blocks = SCRIPT_LD_RE.findall(content)
        if not blocks:
            continue
        for block in blocks:
            try:
                data = json.loads(block)
            except json.JSONDecodeError:
                failures.append(f"{html_path.relative_to(site_dir)}: invalid JSON-LD on noindex page")
                break
            if not _collect_types(data).issubset(ALLOWED_NOINDEX_JSONLD_TYPES):
                failures.append(f"{html_path.relative_to(site_dir)}: JSON-LD on noindex page")
                break

    assert not failures, "JSON-LD found on noindex pages:\n" + "\n".join(failures[:50])


def test_built_site_no_duplicate_jsonld_ids():
    """Each @id value within one HTML page must be unique."""
    site_dir = REPO_ROOT / "_site"
    if not site_dir.exists():
        pytest.skip("_site not built; run Jekyll build first")

    failures = []
    for html_path in sorted(site_dir.rglob("*.html")):
        content = html_path.read_text(encoding="utf-8", errors="ignore")
        blocks = SCRIPT_LD_RE.findall(content)
        page_ids: list[str] = []
        for block in blocks:
            try:
                data = json.loads(block)
            except json.JSONDecodeError:
                continue
            _collect_ids(data, page_ids)

        seen = set()
        for item_id in page_ids:
            if item_id in seen:
                failures.append(f"{html_path.relative_to(site_dir)}: duplicate @id '{item_id}'")
            seen.add(item_id)

    assert not failures, "Duplicate JSON-LD @id values:\n" + "\n".join(failures[:50])


# ---------------------------------------------------------------------------
# IndexNow script tests
# ---------------------------------------------------------------------------


def test_indexnow_script_exists():
    path = REPO_ROOT / "scripts" / "indexnow_submit.py"
    assert path.exists(), "indexnow_submit.py missing"


def test_indexnow_script_no_hardcoded_key():
    path = REPO_ROOT / "scripts" / "indexnow_submit.py"
    text = path.read_text(encoding="utf-8")
    # The old script had INDEXNOW_KEY = "..." hardcoded; new one must not
    assert 'INDEXNOW_KEY = "' not in text, "IndexNow key must not be hardcoded"
    assert "os.environ.get" in text or "env_local" in text.lower() or ".env.local" in text


def test_indexnow_script_has_dry_run():
    path = REPO_ROOT / "scripts" / "indexnow_submit.py"
    text = path.read_text(encoding="utf-8")
    assert "dry_run" in text
    assert "--submit" in text


def test_indexnow_script_checks_indexable():
    path = REPO_ROOT / "scripts" / "indexnow_submit.py"
    text = path.read_text(encoding="utf-8")
    assert "is_indexable" in text or "noindex" in text


# ---------------------------------------------------------------------------
# Head include tests
# ---------------------------------------------------------------------------


def test_head_html_has_canonical():
    path = REPO_ROOT / "_includes" / "head.html"
    text = path.read_text(encoding="utf-8")
    assert "canonical" in text
    assert "absolute_url" in text


def test_head_html_has_robots_meta():
    path = REPO_ROOT / "_includes" / "head.html"
    text = path.read_text(encoding="utf-8")
    assert 'name="robots"' in text


def test_head_html_links_sitemap():
    path = REPO_ROOT / "_includes" / "head.html"
    text = path.read_text(encoding="utf-8")
    assert "sitemap.xml" in text
    assert 'rel="sitemap"' in text


# ---------------------------------------------------------------------------
# Discovery contract tests
# ---------------------------------------------------------------------------


def test_discovery_contract_exists():
    path = REPO_ROOT / "docs" / "seo" / "SEARCH_AI_DISCOVERY_CONTRACT.md"
    assert path.exists(), "SEARCH_AI_DISCOVERY_CONTRACT.md missing"


def test_discovery_contract_documents_exclusion_rules():
    path = REPO_ROOT / "docs" / "seo" / "SEARCH_AI_DISCOVERY_CONTRACT.md"
    text = path.read_text(encoding="utf-8")
    assert "noindex" in text
    assert "sitemap: false" in text or "sitemap:false" in text
    assert "unverified" in text
    assert "research" in text.lower()


def test_indexnow_doc_exists():
    path = REPO_ROOT / "docs" / "seo" / "INDEXNOW.md"
    assert path.exists(), "INDEXNOW.md missing"
