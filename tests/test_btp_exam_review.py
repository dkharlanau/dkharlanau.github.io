"""Second-review checks. They do not validate SAP licensing or live deployment."""
from pathlib import Path
from html.parser import HTMLParser
from html import unescape
import collections
import json
import re
import shutil
import subprocess
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
NEW = set('''exam-readiness mandatory-capabilities design-gates production-quality
commercial-checks integration-paths interface-change token-boundaries ai-runtime-path
reliability-design lab-artifacts oral-defense'''.split())

class Markup(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.anchors, self.headings = [], [], []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'a' and attrs.get('href', '').startswith('#'):
            self.anchors.append(attrs['href'][1:])
        if re.fullmatch(r'h[1-6]', tag):
            self.headings.append(int(tag[1]))

def expand():
    source = (ROOT/'atlas/sap/sap-btp.md').read_text(encoding='utf-8')
    return re.sub(r'{% include btp-handbook/([a-z-]+\.html) %}',
        lambda m: (ROOT/'_includes/btp-handbook'/m[1]).read_text(encoding='utf-8'), source)

class BtpExamReviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = expand()
        cls.parsed = Markup()
        cls.parsed.feed(cls.text)
    def test_unique_ids_and_links(self):
        self.assertEqual([], [x for x,n in collections.Counter(self.parsed.ids).items() if n > 1])
        self.assertEqual(set(), set(self.parsed.anchors)-set(self.parsed.ids))
    def test_legacy_and_new_topics(self):
        self.assertEqual(set(), (LEGACY | NEW)-set(self.parsed.ids))
    def test_heading_hierarchy(self):
        self.assertEqual(1, self.parsed.headings.count(1))
        for a,b in zip(self.parsed.headings, self.parsed.headings[1:]):
            self.assertLessEqual(b,a+1)
    def test_six_accessible_svg_examples(self):
        diagrams = re.findall(r'<svg\b[\s\S]*?</svg>', self.text)
        self.assertEqual(6,len(diagrams))
        for text in diagrams:
            svg = ET.fromstring(text)
            self.assertEqual('img',svg.attrib.get('role'))
            self.assertTrue(svg.attrib.get('aria-labelledby'))
            self.assertIsNotNone(svg.find('{http://www.w3.org/2000/svg}title'))
            self.assertIsNotNone(svg.find('{http://www.w3.org/2000/svg}desc'))
    def test_certification_reference_and_boundaries(self):
        sources = (ROOT/'_includes/btp-handbook/sources.html').read_text()
        record = re.search(r'<div id="source-certification">[\s\S]*?</div>', sources)[0]
        self.assertIn('sap-certified-solution-architect-sap-business-ai-platform',record)
        self.assertIn('C_BAIPA',record)
        self.assertIn('previous handbook',record)
        self.assertIn('not a disclosed exam blueprint',self.text)
        self.assertIn('cannot inspect or confirm your booking',self.text)
    def test_no_unreviewed_publication_promotion(self):
        front=(ROOT/'atlas/sap/sap-btp.md').read_text().split('---',2)[1]
        for expected in ['status: needs_verification','verified: false','robots: noindex,follow','sitemap: false']:
            self.assertIn(expected,front)
    def test_glossary_terms_are_unique_and_count_matches(self):
        glossary=(ROOT/'_includes/btp-handbook/glossary.html').read_text()
        labels=[unescape(re.sub('<[^>]+>','',x)) for x in re.findall(r'<dt>(.*?)</dt>',glossary)]
        self.assertEqual(140,len(labels))
        self.assertEqual(len(labels),len(set(labels)))
        self.assertEqual(labels,sorted(labels,key=str.lower))
        self.assertIn('140 terms, explained and contrasted',self.text)
    def test_curl_bodies(self):
        lab=(ROOT/'_includes/btp-handbook/lab.html').read_text()
        bodies=re.findall(r"-d '(\{[\s\S]*?\})'",lab)
        self.assertTrue(bodies)
        for body in bodies:
            self.assertIsInstance(json.loads(unescape(body)),dict)
    def test_source_and_download_targets(self):
        for href in re.findall(r'href="([^"]+)"',self.text):
            if href.startswith('#source-'):
                self.assertIn(href[1:],self.parsed.ids)
        self.assertIn('/assets/downloads/btp-recovery-drill.mjs',self.text)
        self.assertTrue((ROOT/'assets/downloads/btp-recovery-drill.mjs').is_file())
    def test_evidence_does_not_claim_live_erp_validation(self):
        self.assertIn('have not been executed',self.text)
        self.assertIn('not an SAP API or a distributed database test',self.text)
        self.assertIn('not SAP service guarantees',self.text)
    def test_recovery_drill(self):
        node=shutil.which('node')
        if not node:
            self.skipTest('Node is not installed; the drill is a separate check.')
        version=subprocess.check_output([node,'-p','process.versions.node'],text=True).strip()
        if int(version.split('.')[0]) < 22:
            self.skipTest('Review uses Node 22 or later.')
        result=subprocess.run([node,str(ROOT/'assets/downloads/btp-recovery-drill.mjs')],
            check=True,capture_output=True,text=True,timeout=20)
        self.assertIn('# pass 11',result.stdout)
        self.assertIn('# fail 0',result.stdout)

if __name__ == '__main__':
    unittest.main()
