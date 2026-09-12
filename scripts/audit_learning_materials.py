#!/usr/bin/env python3
"""Inventory learning surfaces using the shared page model; never change review status."""
import json
import re
import sys
from pathlib import Path
import yaml
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.lib.content_model import discover_pages, make_page, parse_frontmatter

ROOT = Path(__file__).resolve().parents[1]
AREAS = {'atlas', 'labs', 'skill-hub', 'scenarios', 'blog', 'notes', 'research', 'triz', 'frameworks', 'ddd', 'reusable-data-procedures'}

def inventory(root=ROOT):
    pages, errors = discover_pages(root)
    known = {p.relative_path for p in pages}
    for area in sorted(AREAS):
        for path in sorted((root / area).rglob('*.html')):
            if path.relative_to(root).as_posix() in known:
                continue
            fm, body, error = parse_frontmatter(path)
            if error:
                errors.append({'path': path.relative_to(root).as_posix(), 'error': error})
            if fm.get('layout'):
                pages.append(make_page(root, path, fm, body))
    roadmap = yaml.safe_load((root / '_data/career/roadmap.yml').read_text())
    bank = yaml.safe_load((root / '_data/career/question_bank.yml').read_text())
    cases = yaml.safe_load((root / '_data/learning_cases.yml').read_text())
    bank_ids = {g['skill_id'] for g in bank['skills']}
    rows = []
    for page in sorted(pages, key=lambda p: p.relative_path):
        if page.collection not in AREAS or not page.permalink:
            continue
        skills = [s['id'] for s in roadmap['skills'] if s['id'] in bank_ids and (
            s['id'] in (page.frontmatter.get('career_skills') or []) or
            any(x['href'] == page.permalink for x in s.get('sources', [])))]
        attached_cases = [c['id'] for c in cases if page.permalink in c['routes']]
        body = page.body
        signals = {
            'visual_in_source': bool(re.search(r'<(?:figure|svg|canvas|img)\b|!\[|```mermaid|class=[\"\'][^\"\']*(?:diagram|flow|graph)|include [^%]*(?:diagram|graph|map)', body)),
            'comparison_in_source': bool(re.search(r'<table\b|\|\s*:?-{3,}', body)),
            'practice_in_source': bool(re.search(r'interview|self.check|exercise|assessment|practice|drill', body, re.I)),
            'source_links': bool(page.frontmatter.get('source_links') or re.search(r'https://(?:help\.sap\.com|learning\.sap\.com|www\.sap\.com|docs\.|learn\.microsoft\.com)', body)),
        }
        gaps = []
        if not signals['visual_in_source'] and not attached_cases:
            gaps.append('Check whether a topic-specific diagram or comparison would clarify the explanation.')
        if not skills and not signals['practice_in_source']:
            gaps.append('Review a concrete recall question and an answer rubric for this topic.')
        if not signals['source_links']:
            gaps.append('Review source attribution manually; this scanner only recognises selected source patterns.')
        rows.append({'source': page.relative_path, 'route': page.permalink, 'title': page.title,
                     'status': page.status, 'verified': page.verified, 'signals': signals,
                     'practice_skills': skills, 'worked_cases': attached_cases, 'editorial_review': gaps})
    return {'scope': 'Source-based structural inventory, not a factual or editorial quality certification.',
            'page_count': len(rows), 'pages_with_linked_practice': sum(bool(r['practice_skills']) for r in rows),
            'pages_with_worked_case': sum(bool(r['worked_cases']) for r in rows),
            'parse_error_count': sum(e['path'].split('/')[0] in AREAS for e in errors), 'items': rows}

if __name__ == '__main__':
    result = inventory()
    out = ROOT / 'reports/learning-materials-inventory.json'
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'items'}, indent=2))
