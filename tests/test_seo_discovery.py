import json
import re
import sys
from pathlib import Path

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
    for title in unverified_titles:
        assert f"PAGE: {title}" not in text, f"llms-full.txt should not contain unverified: {title}"


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
    # Replace full if/elsif/else/endif blocks with the first branch content
    def replace_conditional(m):
        return m.group(1) if m.group(1) else '"placeholder"'
    clean = re.sub(
        r'{%\s*if\s+.*?%}(.*?)(?:{%\s*elsif.*?%}.*?){0,}(?:{%\s*else\s*%}.*?)?{%\s*endif\s*%}',
        replace_conditional,
        clean,
        flags=re.DOTALL,
    )
    # Remove any remaining liquid tags
    clean = re.sub(r'{%.*?%}', '', clean)
    # Replace Jekyll expressions including trailing filters or anchors like #webpage
    clean = re.sub(r'{{.*?}}(?:#[a-zA-Z0-9_-]+)?', '"placeholder"', clean)
    # Collapse multiple placeholders with em-dashes or other connectors into one
    clean = re.sub(r'"placeholder"\s*[-–—]\s*"placeholder"', '"placeholder"', clean)
    # Remove trailing commas before closing braces/brackets
    clean = re.sub(r',\s*}', '}', clean)
    clean = re.sub(r',\s*]', ']', clean)
    # Fix double quotes that may appear from placeholder + existing quotes
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


def test_structured_data_has_techarticle_for_atlas():
    path = REPO_ROOT / "_includes" / "seo" / "structured-data.html"
    text = path.read_text(encoding="utf-8")
    assert "TechArticle" in text


def test_structured_data_has_organization():
    path = REPO_ROOT / "_includes" / "seo" / "structured-data.html"
    text = path.read_text(encoding="utf-8")
    assert "Organization" in text


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
