from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "check_indexing_policy", ROOT / "scripts" / "check_indexing_policy.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


def test_indexable_page_can_link_to_jsonl_static_asset(tmp_path: Path) -> None:
    site = tmp_path / "_site"
    page_dir = site / "labs" / "ai-ready"
    data_dir = page_dir / "data"
    data_dir.mkdir(parents=True)
    (data_dir / "eval-sample.jsonl").write_text('{"id":"case-1"}\n', encoding="utf-8")
    (page_dir / "index.html").write_text(
        '<html><head><meta name="robots" content="index,follow"></head>'
        '<body><a href="/labs/ai-ready/data/eval-sample.jsonl">Eval sample</a></body></html>',
        encoding="utf-8",
    )
    assert MODULE.check_built_html(site, tmp_path) == []
