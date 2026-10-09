"""Focused review guards: source structure and the synthetic recovery contract only."""
from pathlib import Path
from html.parser import HTMLParser
import collections
import re
import shutil
import subprocess
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
class Markup(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids=[]; self.anchors=[]; self.headings=[]
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if 'id' in a: self.ids.append(a['id'])
        if tag=='a' and a.get('href','').startswith('#'): self.anchors.append(a['href'][1:])
        if re.fullmatch(r'h[1-6]',tag): self.headings.append(int(tag[1]))

def expanded_source():
    source=(ROOT/'atlas/sap/sap-btp.md').read_text(encoding='utf-8')
    return re.sub(r'{% include btp-handbook/([a-z-]+\.html) %}',
        lambda m:(ROOT/'_includes/btp-handbook'/m.group(1)).read_text(encoding='utf-8'),source)

class ArchitectReviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source=expanded_source(); cls.markup=Markup(); cls.markup.feed(cls.source)
    def test_twenty_one_chapters_and_old_entry_points(self):
        self.assertEqual(21,self.source.count('class="research-canvas__inventory signavio-reader__section"'))
        legacy='big-picture architect-roles ea-value frameworks toolchain rba rsa trace platform-scope accounts design-choices procurement-case btp-guidance btp-methods btp-design-evidence build-clean-core build-tools build-runtimes build-experience build-integration-strategy build-integration-suite build-events-agents build-operations context-why context-language context-data-products context-products context-bdc context-knowledge-models context-case govern-purpose govern-toolchain govern-failure foundation-overview foundation-identity foundation-connectivity-data foundation-operations method-extension method-data-analytics method-integration method-joined-case client-explanation interview next sources'
        self.assertFalse(set(legacy.split())-set(self.markup.ids))
    def test_anchors_and_heading_hierarchy(self):
        self.assertEqual([], [x for x,n in collections.Counter(self.markup.ids).items() if n>1])
        self.assertFalse(set(self.markup.anchors)-set(self.markup.ids))
        self.assertEqual(self.markup.headings.count(1),1)
        for a,b in zip(self.markup.headings,self.markup.headings[1:]): self.assertLessEqual(b,a+1)
    def test_correct_certification_target_and_no_readiness_claim(self):
        for name in ['exam-brief.html','practice.html','sources.html']:
            text=(ROOT/'_includes/btp-handbook'/name).read_text(encoding='utf-8')
            self.assertIn('C_BAIPA',text)
        # The canonical URL may be linked through the shared source register.
        self.assertIn('sap-certified-solution-architect-sap-business-ai-platform',self.source)
        self.assertNotIn('code <strong>P_BTPA</strong>',self.source)
        self.assertIn('not an official topic weighting',self.source)
        self.assertIn('passing-score predictor',self.source)
    def test_publication_state_is_not_promoted(self):
        for expected in ['status: needs_verification','verified: false','robots: noindex,follow','sitemap: false']:
            self.assertIn(expected,self.source)
    def test_required_review_topics_are_present(self):
        for ident in ['exam-brief','decision-workbench','minimum-solution','request-paths','license-gates','quality-contract','contract-exercise']:
            self.assertIn(ident,self.markup.ids)
        for text in ['SAP_COM_0008','ETag','If-Match','configuration backups','RACI']:
            self.assertIn(text.lower(),self.source.lower())
    def test_six_svg_diagrams_remain_parseable(self):
        diagrams=re.findall(r'<svg\b[\s\S]*?</svg>',self.source);self.assertEqual(6,len(diagrams))
        for diagram in diagrams:
            svg=ET.fromstring(diagram);self.assertEqual('img',svg.attrib.get('role'))
            self.assertIsNotNone(svg.find('{http://www.w3.org/2000/svg}title'))
            self.assertIsNotNone(svg.find('{http://www.w3.org/2000/svg}desc'))
    def test_glossary_is_preserved(self):
        self.assertEqual(140,self.source.count('class="btp-term"'))
    def test_recovery_simulation(self):
        node=shutil.which('node')
        if not node:self.skipTest('Node.js unavailable; no execution claim.')
        version=subprocess.check_output([node,'-p','process.versions.node'],text=True).strip()
        if int(version.split('.')[0])<22:self.skipTest('Exercise requires Node.js >=22.')
        test_file=ROOT/'assets/examples/btp-recovery-contract.test.mjs'
        output=subprocess.run([node,'--test',str(test_file)],check=True,capture_output=True,text=True,timeout=20).stdout
        self.assertIn('# pass 18',output);self.assertIn('# fail 0',output)

if __name__=='__main__':unittest.main()
