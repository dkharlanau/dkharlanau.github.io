#!/usr/bin/env python3
"""
Research Registry Validator for Skill Hub.

Checks:
- all source IDs are unique
- every source has required fields
- every source ID referenced in domain notes exists in registry
- every source ID referenced in synthesis files exists in registry
- no registry source has an empty URL
- no Tier 1 source is from a news/blog source type
- no src- reference is unresolved
"""

import os
import re
import sys

RESEARCH_DIR = os.path.dirname(os.path.abspath(__file__))
REGISTRY_PATH = os.path.join(RESEARCH_DIR, 'source-registry.yml')
DOMAINS_DIR = os.path.join(RESEARCH_DIR, 'domains')
SYNTHESIS_DIR = os.path.join(RESEARCH_DIR, 'synthesis')

REQUIRED_FIELDS = ['id', 'title', 'url', 'publisher', 'tier', 'type', 'topics', 'reliability_notes', 'citation_allowed']
TIER_1_ALLOWED_TYPES = ['official_docs', 'open_source_docs', 'research_report', 'standard']

def parse_registry():
    """Parse source-registry.yml manually."""
    with open(REGISTRY_PATH, 'r') as f:
        content = f.read()
    
    sources = []
    current = {}
    
    for line in content.split('\n'):
        if line.startswith('  - id:'):
            if current:
                sources.append(current)
            current = {'id': line.split(':', 1)[1].strip()}
        elif line.startswith('    ') and ':' in line and current is not None:
            key, val = line.strip().split(':', 1)
            key = key.strip()
            val = val.strip()
            if val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
            elif val.startswith('[') and val.endswith(']'):
                val = [v.strip() for v in val[1:-1].split(',')]
            elif val == 'yes':
                val = True
            elif val == 'no':
                val = False
            elif val.isdigit():
                val = int(val)
            current[key] = val
    
    if current:
        sources.append(current)
    
    return sources

def find_references(directory):
    """Find all src-XXX references in markdown files."""
    refs = set()
    for root, dirs, files in os.walk(directory):
        for f in files:
            if f.endswith('.md'):
                path = os.path.join(root, f)
                with open(path, 'r') as fh:
                    content = fh.read()
                refs.update(re.findall(r'src-\d+', content))
    return refs

def main():
    errors = []
    warnings = []
    
    # Parse registry
    sources = parse_registry()
    registry_ids = {s['id'] for s in sources}
    
    # Check uniqueness
    seen = set()
    for s in sources:
        if s['id'] in seen:
            errors.append(f"Duplicate source ID: {s['id']}")
        seen.add(s['id'])
    
    # Check required fields
    for s in sources:
        for field in REQUIRED_FIELDS:
            if field not in s or not s[field]:
                errors.append(f"{s['id']}: missing required field '{field}'")
    
    # Check empty URLs
    for s in sources:
        if 'url' in s and (not s['url'] or s['url'] == 'unknown'):
            errors.append(f"{s['id']}: empty or unknown URL")
    
    # Check Tier 1 source types
    for s in sources:
        if s.get('tier') == 1:
            src_type = s.get('type', '')
            if src_type not in TIER_1_ALLOWED_TYPES:
                warnings.append(f"{s['id']}: Tier 1 source has type '{src_type}' (allowed: {TIER_1_ALLOWED_TYPES})")
    
    # Check domain note references
    domain_refs = find_references(DOMAINS_DIR)
    for ref in sorted(domain_refs):
        if ref not in registry_ids:
            errors.append(f"Domain note references unresolved source: {ref}")
    
    # Check synthesis references
    synthesis_refs = find_references(SYNTHESIS_DIR)
    for ref in sorted(synthesis_refs):
        if ref not in registry_ids:
            errors.append(f"Synthesis references unresolved source: {ref}")
    
    # Also check README and RESEARCH_REPORT
    for fname in ['README.md', 'RESEARCH_REPORT.md']:
        path = os.path.join(RESEARCH_DIR, fname)
        if os.path.exists(path):
            with open(path, 'r') as f:
                content = f.read()
            refs = set(re.findall(r'src-\d+', content))
            for ref in sorted(refs):
                if ref not in registry_ids:
                    errors.append(f"{fname} references unresolved source: {ref}")
    
    # Report
    print("=" * 60)
    print("Skill Hub Research Registry Validation")
    print("=" * 60)
    print(f"Registry sources: {len(sources)}")
    print(f"Domain references: {len(domain_refs)}")
    print(f"Synthesis references: {len(synthesis_refs)}")
    print()
    
    if warnings:
        print(f"WARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f"  - {w}")
        print()
    
    if errors:
        print(f"ERRORS ({len(errors)}):")
        for e in errors:
            print(f"  - {e}")
        print()
        print("RESULT: FAILED")
        return 1
    else:
        print("RESULT: PASSED")
        return 0

if __name__ == '__main__':
    sys.exit(main())
