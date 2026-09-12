from pathlib import Path
import yaml
from scripts.audit_learning_materials import inventory

ROOT = Path(__file__).resolve().parents[1]

def test_case_routes_and_explicit_skills_resolve():
    report = inventory()
    by_route = {row['route']: row for row in report['items']}
    cases = yaml.safe_load((ROOT / '_data/learning_cases.yml').read_text())
    seen = set()
    for case in cases:
        assert len(case['stages']) == 4
        assert 'Synthetic' in case['scope']
        assert len(case['review']) >= 3
        assert case['transfer']
        for route in case['routes']:
            assert route in by_route, route
            assert route not in seen, f'Two cases compete for {route}'
            seen.add(route)
    rows = {row['route']: row for row in report['items']}
    assert 'sales-atp' in rows['/labs/enterprise-context/atp/']['practice_skills']
    assert 'ai-evaluation' in rows['/labs/ai-ready/evals-reliability/']['practice_skills']
    assert rows['/labs/ai-ready/evals-reliability/']['verified'] is False

def test_worked_case_quantities_match_the_reasoning():
    cases = {c['id']: c for c in yaml.safe_load((ROOT / '_data/learning_cases.yml').read_text())}
    values = lambda key: [int(s['value']) for s in cases[key]['stages']]
    source, outbound, delivered, correct = values('replication-gaps')
    assert source - outbound == 2
    assert outbound == delivered
    assert delivered - correct == 2
    total, completed, accepted, usable = values('ai-usable-output')
    assert total >= completed >= accepted >= usable
    assert usable / total == .32
    all_incidents, process, data, interface = values('repeat-demand')
    assert process + data + interface == all_incidents
    on_hand, in_scope, remaining, requested = values('promise-boundary')
    assert on_hand - in_scope == 20
    assert in_scope - remaining == 50
    assert requested - remaining == 10
