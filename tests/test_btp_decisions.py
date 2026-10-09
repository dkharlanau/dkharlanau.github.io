"""Decision-led content checks. No SAP tenant, licence or full-site build is exercised."""
from pathlib import Path
from html.parser import HTMLParser
from html import escape
import collections
import json
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
INCLUDES = ROOT / '_includes/btp-handbook'

class Markup(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.anchors, self.headings = [], [], []
        self.stack, self.errors = [], []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a: self.ids.append(a['id'])
        if tag == 'a' and a.get('href', '').startswith('#'): self.anchors.append(a['href'][1:])
        if re.fullmatch(r'h[1-6]', tag): self.headings.append(int(tag[1]))
        if tag not in {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}: self.stack.append(tag)
    def handle_endtag(self, tag):
        if tag in {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}: return
        if not self.stack or self.stack[-1] != tag: self.errors.append((tag, self.stack[-4:]))
        else: self.stack.pop()

def catalogue_data():
    return json.loads((ROOT/'_data/btp_services.json').read_text(encoding='utf-8'))

def render_catalogue():
    source = (INCLUDES/'service-map.html').read_text(encoding='utf-8')
    outer = re.search(r'{% for group in site.data.btp_services %}([\s\S]*?){% endfor %}\s*\n<p><strong>Before', source)
    if not outer: raise AssertionError('Catalogue outer loop not found')
    template = outer[1]
    inner = re.search(r'{% for item in group.items %}([\s\S]*?){% endfor %}', template)
    if not inner: raise AssertionError('Catalogue row loop not found')
    groups = []
    for group in catalogue_data():
        rows = []
        for item in group['items']:
            row = re.sub(r'{{ item\.([a-z]+) \| escape }}', lambda m: escape(str(item[m[1]]), quote=True), inner[1])
            rows.append(row)
        out = template.replace(inner[0], ''.join(rows))
        out = out.replace('{{ group.items.size }}', str(len(group['items'])))
        out = re.sub(r'{{ group\.([a-z]+) \| escape }}', lambda m: escape(str(group[m[1]]), quote=True), out)
        groups.append(out)
    block = re.search(r'{% for group in site.data.btp_services %}[\s\S]*?{% endfor %}\s*\n(?=<p><strong>Before)', source)[0]
    return source.replace(block, ''.join(groups)+'\n')

def expand_new_content():
    source = (ROOT/'atlas/sap/sap-btp.md').read_text(encoding='utf-8').split('---', 2)[2]
    def include(match):
        name = match[1]
        if name == 'service-map.html': return render_catalogue()
        if name == 'glossary.html':
            # Preserve the existing glossary in production; isolate new-content checks.
            return '<section id="glossary"><h2>Terminology reference</h2></section>'
        return (INCLUDES/name).read_text(encoding='utf-8')
    return re.sub(r'{% include btp-handbook/([a-z-]+\.html) %}', include, source)

class BtpDecisionContentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = expand_new_content()
        cls.parsed = Markup(); cls.parsed.feed(cls.text)
        cls.items = [item for group in catalogue_data() for item in group['items']]
    def test_balanced_markup(self):
        self.assertEqual([], self.parsed.errors)
        self.assertEqual([], self.parsed.stack)
    def test_new_links_and_unique_ids(self):
        self.assertFalse([x for x,n in collections.Counter(self.parsed.ids).items() if n > 1])
        self.assertFalse(set(self.parsed.anchors)-set(self.parsed.ids))
    def test_heading_order(self):
        self.assertEqual(1,self.parsed.headings.count(1))
        for previous,current in zip(self.parsed.headings,self.parsed.headings[1:]): self.assertLessEqual(current,previous+1)
    def test_sixteen_numbered_decisions(self):
        numbers = [int(x) for x in re.findall(r'<h3[^>]*>Tree (\d+) ',self.text)]
        self.assertEqual(list(range(1,17)),numbers)
        self.assertGreaterEqual(self.text.count('├─'),32)
        self.assertEqual(18,self.text.count('class="btp-tree"'))
    def test_catalogue_count_types_and_unique_ids(self):
        self.assertEqual(94,len(self.items))
        self.assertEqual(94,len({x['id'] for x in self.items}))
        self.assertEqual(12,len(catalogue_data()))
        self.assertEqual(40,sum(x['kind']=='Service' for x in self.items))
        self.assertEqual(3,sum(x['kind']=='Lifecycle' for x in self.items))
        self.assertEqual(94,self.text.count('class="btp-service-row"'))
    def test_catalogue_is_server_rendered(self):
        self.assertNotIn('{% for',render_catalogue())
        for item in self.items:
            for key in ['id','name','kind','use','boundary']: self.assertTrue(item[key].strip())
            self.assertIn('service-'+item['id'],self.parsed.ids)
    def test_pilots_and_minimum_stacks(self):
        self.assertEqual(8,self.text.count('btp-check btp-pilot'))
        for text in ['R — selected minimum','C — add when','O — not automatic']: self.assertIn(text,self.text)
        for name in ['pilot-bp','pilot-offline','pilot-events','pilot-approval','pilot-documents','pilot-rag','pilot-runtimes','pilot-cost']: self.assertIn(name,self.parsed.ids)
    def test_technical_boundaries(self):
        for text in ['DefiningRequests','OfflineEnabled','UnknownOutcome','SAP_COM_0008','If-Match','xs-security.json','mta.yaml','cds add kyma','configuration backups','premium-user','RACI']: self.assertIn(text,self.text)
        self.assertIn('not an SAP API or a distributed database test',self.text)
        self.assertIn('not an SAP price quote',self.text)
    def test_no_editorial_work_diary(self):
        for text in ['Human editorial review remains pending','Second review:','Original practice and selected current SAP documentation','previous handbook','reported score']:
            self.assertNotIn(text,self.text)
    def test_publication_state_preserved(self):
        front=(ROOT/'atlas/sap/sap-btp.md').read_text().split('---',2)[1]
        for text in ['status: needs_verification','verified: false','robots: noindex,follow','sitemap: false']: self.assertIn(text,front)
    def test_registered_table_and_native_disclosure_patterns(self):
        self.assertEqual(20,self.text.count('class="table-scroll study-table"'))
        self.assertIn('aria-live="polite"',self.text)
        self.assertIn('btp-service-tools" hidden',self.text)
        self.assertNotIn('onclick=',self.text)
    def test_reference_links_are_official(self):
        refs=(INCLUDES/'decision-references.html').read_text()
        from urllib.parse import urlparse
        for href in re.findall(r'href="(https:[^"]+)"',refs):
            host=urlparse(href).hostname
            self.assertTrue(host=='sap.com' or host.endswith('.sap.com') or host.endswith('.cloud.sap'),href)

if __name__=='__main__': unittest.main()
