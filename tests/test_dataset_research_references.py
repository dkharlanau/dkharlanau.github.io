"""Research references must remain visible, attributable and safe to follow."""
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('dataset_pages', ROOT / 'bin/generate_dataset_pages.py')
generator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(generator)


def test_ce_references_match_data_and_preserve_source_boundary():
    for number in range(1, 5):
        source = ROOT / f'datasets/LLM-prompts/CE-0{number}.json'
        output = ROOT / f'datasets/view/LLM-prompts/CE-0{number}.md'
        data = json.loads(source.read_text())
        section = generator.research_references(source.read_text())
        assert section in output.read_text()
        assert data['research_basis']['source_note'] in section
        assert '<a href="https://' in section


def test_references_escape_text_deduplicate_and_reject_unsafe_urls():
    data = {'research_basis': {'source_note': '<review>', 'key_findings': [
        {'sources': ['https://example.org/a?x=1&y=2', 'https://example.org/a?x=1&y=2',
                     'javascript:alert(1)', 'https://user:password@example.org/', 'https://example.org/a\nb']}]}}
    result = generator.research_references(json.dumps(data))
    assert '&lt;review&gt;' in result
    assert result.count('<li>') == 1
    assert 'href="https://example.org/a?x=1&amp;y=2"' in result
    assert 'javascript:' not in result and 'password' not in result
