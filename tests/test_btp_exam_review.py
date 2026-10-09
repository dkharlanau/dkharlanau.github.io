"""Whole-guide source regressions; no claim about SAP licences or live deployment."""
from pathlib import Path
from html import unescape
import importlib.util
import json
import re
import shutil
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('btp_architecture_helpers', Path(__file__).with_name('test_btp_architect_review.py'))
helpers = importlib.util.module_from_spec(spec); spec.loader.exec_module(helpers)
NEW = set('''exam-readiness mandatory-capabilities design-gates production-quality
commercial-checks integration-paths interface-change token-boundaries ai-runtime-path
reliability-design lab-artifacts oral-defense mobile offline service-map recipes'''.split())

class BtpExamReviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text=helpers.expanded_source()
        cls.parsed=helpers.helpers.Markup(); cls.parsed.feed(cls.text)
    def test_legacy_and_new_topics(self):
        self.assertFalse((helpers.LEGACY|NEW)-set(self.parsed.ids))
    def test_full_guide_links(self):
        self.assertFalse(set(self.parsed.anchors)-set(self.parsed.ids))
    def test_no_unreviewed_publication_promotion(self):
        front=(ROOT/'atlas/sap/sap-btp.md').read_text().split('---',2)[1]
        for expected in ['status: needs_verification','verified: false','robots: noindex,follow','sitemap: false']:
            self.assertIn(expected,front)
    def test_glossary_terms_are_unique_and_count_matches(self):
        glossary=(ROOT/'_includes/btp-handbook/glossary.html').read_text()
        labels=[unescape(re.sub('<[^>]+>','',x)) for x in re.findall(r'<dt>(.*?)</dt>',glossary)]
        self.assertEqual(140,len(labels)); self.assertEqual(len(labels),len(set(labels)))
        self.assertEqual(labels,sorted(labels,key=str.lower))
        self.assertIn('140 terms, explained and contrasted',self.text)
    def test_existing_lab_curl_bodies(self):
        lab=(ROOT/'_includes/btp-handbook/lab.html').read_text()
        bodies=re.findall(r"-d '(\{[\s\S]*?\})'",lab)
        self.assertTrue(bodies)
        for body in bodies:self.assertIsInstance(json.loads(unescape(body)),dict)
    def test_download_target_and_reference_anchors(self):
        self.assertIn('/assets/downloads/btp-recovery-drill.mjs',self.text)
        self.assertTrue((ROOT/'assets/downloads/btp-recovery-drill.mjs').is_file())
        for href in re.findall(r'href="([^"]+)"',self.text):
            if href.startswith('#ref-'):self.assertIn(href[1:],self.parsed.ids)
    def test_simulation_and_sizing_boundaries(self):
        self.assertIn('not an SAP API or a distributed database test',self.text)
        self.assertIn('not SAP service guarantees',self.text)
        self.assertIn('not an SAP price quote',self.text)
        self.assertIn('not an official topic weighting',self.text)
    def test_recovery_drill(self):
        node=shutil.which('node')
        if not node:self.skipTest('Node is not installed; the drill is a separate check.')
        version=subprocess.check_output([node,'-p','process.versions.node'],text=True).strip()
        if int(version.split('.')[0])<22:self.skipTest('Review uses Node 22 or later.')
        result=subprocess.run([node,str(ROOT/'assets/downloads/btp-recovery-drill.mjs')],
            check=True,capture_output=True,text=True,timeout=20)
        self.assertIn('# pass 11',result.stdout);self.assertIn('# fail 0',result.stdout)

if __name__=='__main__':unittest.main()
