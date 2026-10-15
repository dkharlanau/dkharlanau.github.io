"""Focused handbook regressions, not product-fact or production-readiness checks."""
from pathlib import Path
from html.parser import HTMLParser
import collections
import json
import re
import shutil
import subprocess
import tempfile
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
LEGACY = set('''big-picture architect-roles ea-value frameworks toolchain rba rsa trace
platform-scope accounts design-choices procurement-case btp-guidance btp-methods
btp-design-evidence build-clean-core build-tools build-runtimes build-experience
build-integration-strategy build-integration-suite build-events-agents build-operations
context-why context-language context-data-products context-products context-bdc
context-knowledge-models context-case govern-purpose govern-toolchain govern-failure
foundation-overview foundation-identity foundation-connectivity-data foundation-operations
method-extension method-data-analytics method-integration method-joined-case
client-explanation interview next sources'''.split())

class Markup(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.anchors, self.headings = [], [], []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a: self.ids.append(a['id'])
        if tag == 'a' and a.get('href', '').startswith('#'):
            self.anchors.append(a['href'][1:])
        if tag in ('h1','h2','h3','h4','h5','h6'):
            self.headings.append(int(tag[1]))

def rendered_source():
    source = (ROOT / 'atlas/sap/sap-btp.md').read_text(encoding='utf-8')
    def expand(match):
        name = match.group(1)
        return (ROOT / '_includes/btp-handbook' / name).read_text(encoding='utf-8')
    return re.sub(r'{% include btp-handbook/([a-z-]+\.html) %}', expand, source)

class BtpHandbookTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = rendered_source()
        cls.markup = Markup()
        cls.markup.feed(cls.source)
    def test_unique_ids_and_resolvable_anchors(self):
        duplicate = [key for key,count in collections.Counter(self.markup.ids).items() if count > 1]
        self.assertEqual([], duplicate)
        # A Liquid-generated service reference is resolved when Jekyll renders the page.
        static_anchors = {value for value in self.markup.anchors if "{{" not in value}
        self.assertEqual(set(), static_anchors - set(self.markup.ids))
        services = json.loads((ROOT / '_data/btp_services.json').read_text(encoding='utf-8'))
        for group in services:
            self.assertIn(group['reference'], self.markup.ids)
    def test_existing_deep_links_survive(self):
        self.assertEqual(set(), LEGACY - set(self.markup.ids))
    def test_single_title_and_heading_order(self):
        self.assertEqual(1, self.markup.headings.count(1))
        for left,right in zip(self.markup.headings,self.markup.headings[1:]):
            self.assertLessEqual(right,left+1)
    def test_sixteen_readable_architecture_decision_trees(self):
        # The current handbook uses readable text decision trees rather than retired SVGs.
        trees = [int(value) for value in re.findall(r'Tree\s+(\d+)', self.source)]
        self.assertEqual(list(range(1, 17)), sorted(set(trees)))
        self.assertGreaterEqual(self.source.count('<pre class="btp-tree"'), 16)
        self.assertIn('aria-label="Architecture decision or request flow"', self.source)
    def test_glossary_and_lab_are_present(self):
        self.assertGreaterEqual(self.source.count('class="btp-term"'),100)
        self.assertIn('id="development-lab"',self.source)
        self.assertIn('btp-recovery-drill.mjs',self.source)
        self.assertTrue((ROOT/'assets/downloads/btp-recovery-drill.mjs').is_file())
        self.assertIn('It is a simulation, not an SAP API',self.source)
    def test_example_curl_json_is_valid(self):
        lab=(ROOT/'_includes/btp-handbook/lab.html').read_text(encoding='utf-8')
        bodies=re.findall(r"-d '(\{[\s\S]*?\})'",lab)
        self.assertTrue(bodies)
        for body in bodies: self.assertIsInstance(json.loads(body),dict)
    def test_local_policy_scaffold(self):
        node=shutil.which('node')
        if not node: self.skipTest('Node is not installed; policy test is separate.')
        version=subprocess.check_output([node,'-p','process.versions.node'],text=True).strip()
        if int(version.split('.')[0])<22: self.skipTest('Policy lab requires Node >=22.')
        with tempfile.TemporaryDirectory(prefix='btp-handbook-') as temp:
            target=Path(temp)/'lab'
            scaffold=ROOT/'assets/downloads/btp-review-lab.mjs'
            subprocess.run([node,str(scaffold),str(target)],check=True,capture_output=True,text=True,timeout=20)
            result=subprocess.run([node,'--test','test/policy.test.cjs'],cwd=target,check=True,capture_output=True,text=True,timeout=20)
            self.assertIn('# pass 17',result.stdout)
            self.assertIn('# fail 0',result.stdout)

if __name__ == '__main__':
    unittest.main()
