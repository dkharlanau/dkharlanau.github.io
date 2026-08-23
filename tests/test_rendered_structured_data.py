import html
import json
import re
from pathlib import Path
from urllib.parse import urlparse

import pytest


REPO_ROOT = Path(__file__).resolve().parents[1]
SITE_DIR = REPO_ROOT / "_site"

SCRIPT_LD_RE = re.compile(
    r'<script\s+type=["\']application/ld\+json["\']\s*>(.*?)</script>',
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
SUMMARY_QUESTION_RE = re.compile(
    r'<summary\b[^>]*>(?:(?!</summary>).)*?<h2\b[^>]*>(.*?)</h2>(?:(?!</summary>).)*?</summary>',
    re.IGNORECASE | re.DOTALL,
)
TAG_RE = re.compile(r"<[^>]+>")

ALLOWED_NOINDEX_TYPES = {"DefinedTerm", "DefinedTermSet"}


def _require_site() -> Path:
    if not SITE_DIR.exists():
        pytest.skip("_site not built; this suite is rerun after the Jekyll build in CI")
    return SITE_DIR


def _html_files():
    site = _require_site()
    return sorted(site.rglob("*.html"))


def _jsonld_blocks(content: str, rel_path: Path):
    result = []
    for index, block in enumerate(SCRIPT_LD_RE.findall(content), start=1):
        try:
            result.append(json.loads(block))
        except json.JSONDecodeError as exc:
            pytest.fail(f"{rel_path}: invalid JSON-LD block {index}: {exc}")
    return result


def _collect_types(value, output=None):
    if output is None:
        output = set()
    if isinstance(value, dict):
        item_type = value.get("@type")
        if isinstance(item_type, str):
            output.add(item_type)
        elif isinstance(item_type, list):
            output.update(item for item in item_type if isinstance(item, str))
        for child in value.values():
            _collect_types(child, output)
    elif isinstance(value, list):
        for child in value:
            _collect_types(child, output)
    return output


def _top_level_nodes(value):
    if isinstance(value, dict) and isinstance(value.get("@graph"), list):
        return [item for item in value["@graph"] if isinstance(item, dict)]
    if isinstance(value, dict):
        return [value]
    if isinstance(value, list):
        return [item for item in value if isinstance(item, dict)]
    return []


def _plain_text(value: str) -> str:
    return " ".join(html.unescape(TAG_RE.sub(" ", value)).split())


def test_rendered_jsonld_is_valid_json():
    for html_path in _html_files():
        content = html_path.read_text(encoding="utf-8", errors="ignore")
        _jsonld_blocks(content, html_path.relative_to(SITE_DIR))


def test_no_rich_jsonld_on_noindex_pages():
    failures = []
    for html_path in _html_files():
        content = html_path.read_text(encoding="utf-8", errors="ignore")
        robots_match = ROBOTS_RE.search(content)
        robots = robots_match.group(1).lower() if robots_match else ""
        if "noindex" not in robots:
            continue
        blocks = _jsonld_blocks(content, html_path.relative_to(SITE_DIR))
        for block in blocks:
            types = _collect_types(block)
            if not types.issubset(ALLOWED_NOINDEX_TYPES):
                failures.append(
                    f"{html_path.relative_to(SITE_DIR)}: noindex page emits {sorted(types)}"
                )
                break
    assert not failures, "Rich JSON-LD found on noindex pages:\n" + "\n".join(failures[:50])


def test_no_deprecated_searchaction_schema():
    failures = []
    for html_path in _html_files():
        content = html_path.read_text(encoding="utf-8", errors="ignore")
        for block in _jsonld_blocks(content, html_path.relative_to(SITE_DIR)):
            if "SearchAction" in _collect_types(block):
                failures.append(str(html_path.relative_to(SITE_DIR)))
    assert not failures, "Deprecated SearchAction schema remains on: " + ", ".join(failures)


def test_no_conflicting_typed_top_level_ids():
    failures = []
    for html_path in _html_files():
        content = html_path.read_text(encoding="utf-8", errors="ignore")
        typed_ids = {}
        for block in _jsonld_blocks(content, html_path.relative_to(SITE_DIR)):
            for node in _top_level_nodes(block):
                item_id = node.get("@id")
                item_type = node.get("@type")
                if not isinstance(item_id, str) or not item_type:
                    continue
                typed_ids.setdefault(item_id, []).append(item_type)
        for item_id, types in typed_ids.items():
            if len(types) > 1:
                failures.append(
                    f"{html_path.relative_to(SITE_DIR)}: {item_id} declared with typed nodes {types}"
                )
    assert not failures, "Conflicting typed JSON-LD @id declarations:\n" + "\n".join(failures[:50])


def test_breadcrumbs_are_contiguous_and_end_at_canonical():
    failures = []
    for html_path in _html_files():
        content = html_path.read_text(encoding="utf-8", errors="ignore")
        canonical_match = CANONICAL_RE.search(content)
        canonical = html.unescape(canonical_match.group(1)).strip() if canonical_match else ""
        for block in _jsonld_blocks(content, html_path.relative_to(SITE_DIR)):
            for node in _top_level_nodes(block):
                if node.get("@type") != "BreadcrumbList":
                    continue
                items = node.get("itemListElement") or []
                positions = [item.get("position") for item in items if isinstance(item, dict)]
                if positions != list(range(1, len(items) + 1)):
                    failures.append(
                        f"{html_path.relative_to(SITE_DIR)}: breadcrumb positions {positions}"
                    )
                    continue
                item_urls = [
                    item.get("item")
                    for item in items
                    if isinstance(item, dict) and isinstance(item.get("item"), str)
                ]
                normalized_urls = [item_url.rstrip("/") for item_url in item_urls]
                if len(normalized_urls) != len(set(normalized_urls)):
                    failures.append(
                        f"{html_path.relative_to(SITE_DIR)}: breadcrumb contains duplicate URLs {item_urls}"
                    )
                malformed_urls = [
                    item_url for item_url in item_urls if "//" in urlparse(item_url).path
                ]
                if malformed_urls:
                    failures.append(
                        f"{html_path.relative_to(SITE_DIR)}: breadcrumb contains double-slash paths {malformed_urls}"
                    )
                if canonical and items:
                    terminal = items[-1].get("item") if isinstance(items[-1], dict) else None
                    if terminal != canonical:
                        failures.append(
                            f"{html_path.relative_to(SITE_DIR)}: breadcrumb ends at {terminal!r}, canonical is {canonical!r}"
                        )
    assert not failures, "Invalid breadcrumb chains:\n" + "\n".join(failures[:50])


def test_reviewed_scenario_emits_techarticle_and_product_breadcrumb():
    scenario_path = (
        SITE_DIR
        / "scenarios"
        / "ai-pilots-for-sap-support-fail-before-value"
        / "index.html"
    )
    if not scenario_path.exists():
        pytest.skip("Reviewed scenario not present in the current _site build")

    content = scenario_path.read_text(encoding="utf-8", errors="ignore")
    blocks = _jsonld_blocks(content, scenario_path.relative_to(SITE_DIR))
    articles = [
        block
        for block in blocks
        if isinstance(block, dict) and block.get("@type") == "TechArticle"
    ]
    breadcrumbs = [
        block for block in blocks if isinstance(block, dict) and block.get("@type") == "BreadcrumbList"
    ]

    assert len(articles) == 1
    assert articles[0]["articleSection"] == "Scenarios"
    assert len(breadcrumbs) == 1
    assert [item["name"] for item in breadcrumbs[0]["itemListElement"][:3]] == [
        "Home",
        "Knowledge",
        "Scenarios",
    ]


def test_faq_page_schema_matches_visible_questions():
    _require_site()
    faq_path = SITE_DIR / "faq" / "index.html"
    assert faq_path.exists(), "Built /faq/ page missing"
    content = faq_path.read_text(encoding="utf-8", errors="ignore")
    blocks = _jsonld_blocks(content, faq_path.relative_to(SITE_DIR))
    faq_blocks = [block for block in blocks if isinstance(block, dict) and block.get("@type") == "FAQPage"]
    assert len(faq_blocks) == 1, f"Expected one FAQPage block, found {len(faq_blocks)}"

    visible_questions = [_plain_text(item) for item in SUMMARY_QUESTION_RE.findall(content)]
    schema_questions = [
        item.get("name")
        for item in faq_blocks[0].get("mainEntity", [])
        if isinstance(item, dict) and item.get("@type") == "Question"
    ]

    assert len(visible_questions) == 10, f"Expected 10 visible FAQ questions, found {len(visible_questions)}"
    assert schema_questions == visible_questions
