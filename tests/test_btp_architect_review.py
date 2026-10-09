"""Architecture regression guards for the decision-led guide and existing recovery lab."""
from pathlib import Path
import collections
import importlib.util
import re
import shutil
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('btp_content_helpers', Path(__file__).with_name('test_btp_decisions.py'))
helpers = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helpers)
LEGACY = set('''big-picture architect-roles ea-value frameworks toolchain rba rsa trace
platform-scope accounts design-choices procurement-case btp-guidance btp-methods
btp-design-evidence build-clean-core build-tools build-runtimes build-experience
build-integration-strategy build-integration-suite build-events-agents build-operations
context-why context-language context-data-products context-products context-bdc
context-knowledge-models context-case govern-purpose govern-toolchain govern-failure
foundation-overview foundation-identity foundation-connectivity-data foundation-operations
method-extension method-data-analytics method-integration method-joined-case
client-explanation interview next sources'''.split())

def expanded_source():
    # The glossary is retained verbatim, not replaced by a fixture in these regressions.
    source = (ROOT/'atlas/sap/sap-btp.md').read_text(encoding='utf-8')
    def include(match):
        if match[1] == 'service-map.html': return helpers.render_catalogue()
        return (ROOT/'_includes/btp-handbook'/match[1]).read_text(encoding='utf-8')
    return re.sub(r'{% include btp-handbook/([a-z-]+\.html) %}', include, source)

class ArchitectReviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = expanded_source()
        cls.markup = helpers.Markup(); cls.markup.feed(cls.source)
    def test_chapters_and_old_entry_points(self):
        self.assertEqual(18,self.source.count('class="research-canvas__inventory signavio-reader__section"'))
        self.assertFalse(LEGACY-set(self.markup.ids))
    def test_anchors_and_heading_hierarchy(self):
        self.assertFalse([x for x,n in collections.Counter(self.markup.ids).items() if n>1])
        self.assertFalse(set(self.markup.anchors)-set(self.markup.ids))
        self.assertEqual(1,self.markup.headings.count(1))
        for a,b in zip(self.markup.headings,self.markup.headings[1:]): self.assertLessEqual(b,a+1)
    def test_certification_scope_is_not_a_readiness_claim(self):
        self.assertIn('sap-certified-solution-architect-sap-business-ai-platform',self.source)
        self.assertIn('C_BAIPA',self.source)
        self.assertNotIn('code <strong>P_BTPA</strong>',self.source)
        self.assertIn('not an official topic weighting',self.source)
        self.assertIn('passing-score predictor',self.source)
    def test_publication_state_is_not_promoted(self):
        for expected in ['status: needs_verification','verified: false','robots: noindex,follow','sitemap: false']:
            self.assertIn(expected,self.source)
    def test_review_topics_and_recovery_contract_remain(self):
        for ident in ['exam-brief','decision-workbench','minimum-solution','request-paths','license-gates','quality-contract','contract-exercise']:
            self.assertIn(ident,self.markup.ids)
        for text in ['SAP_COM_0008','ETag','If-Match','configuration backups','RACI']:
            self.assertIn(text.lower(),self.source.lower())
    def test_sixteen_readable_decision_trees(self):
        self.assertEqual(list(range(1,17)),[int(x) for x in re.findall(r'<h3[^>]*>Tree (\d+) ',self.source)])
        self.assertEqual(18,self.source.count('class="btp-tree" tabindex="0"'))
        self.assertIn('Cloud Foundry',self.source); self.assertIn('DefiningRequests',self.source)
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
