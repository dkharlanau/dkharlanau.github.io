#!/usr/bin/env python3
"""Create the complete, print-first SAP Lead Leadership Toolkit from the site page.

Every substantive section is rendered from the live source file in document order.
There is no independent case or method summary to go stale.
"""
from __future__ import annotations
import argparse
import html
import re
import unicodedata
from pathlib import Path
from bs4 import BeautifulSoup, Tag
from weasyprint import HTML

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DEFAULT = ROOT / 'labs/assessment/leadership-toolkit/index.md'
OUTPUT_DEFAULT = ROOT / 'assets/downloads/sap-lead-leadership-toolkit-print.pdf'

STYLE = r'''
@page {
  size: A4; margin: 21mm 19mm 19mm;
  @top-left { content: 'DK / PERSONAL SAP & AI LAB'; font: 700 7.1pt 'Lato', sans-serif;
    color: #586675; letter-spacing: .08em; padding-bottom: 4mm; border-bottom: .45pt solid #d8e0e7; }
  @top-right { content: string(chapter, first); font: 500 7.1pt 'Lato', sans-serif;
    color: #586675; padding-bottom: 4mm; border-bottom: .45pt solid #d8e0e7; }
  @bottom-left { content: 'LEADERSHIP TOOLKIT  /  2026'; font: 500 7.1pt 'Lato', sans-serif;
    color: #697785; padding-top: 3.5mm; border-top: .45pt solid #d8e0e7; }
  @bottom-right { content: counter(page, decimal-leading-zero); font: 700 8pt 'Lato', sans-serif;
    color: #22354a; padding-top: 3.5mm; border-top: .45pt solid #d8e0e7; }
}
@page:first { @top-left {content: none} @top-right {content: none}
  @bottom-left {content: none} @bottom-right {content: none} }
:root {--ink:#1e2b37; --soft:#52606e; --muted:#73808b; --line:#d8e0e6;
  --blue:#2057a5; --pale:#f3f7fb; --paper:#fff; }
html { font-family:'Lato',sans-serif; font-size:10.3pt; line-height:1.56; color:var(--ink); }
body { margin:0; background:#fff; }
*,*::before,*::after { box-sizing:border-box; }
p {margin:0 0 3.7mm; orphans:3; widows:3; hyphens:none; }
h1,h2,h3 {font-family:'Noto Serif',serif; line-height:1.24; font-weight:600;
  margin:0; break-after:avoid; text-wrap:pretty; }
h1 {font-size:45pt; letter-spacing:-.045em; }
h2 {font-size:20.4pt; margin-bottom:5mm; letter-spacing:-.023em; }
h3 {font-size:12.2pt; margin:8.5mm 0 3mm; }
a {color:var(--blue); text-decoration:none; }
a[href] {cursor:pointer;}
.cover { min-height:245mm; break-after:page; position:relative; }
.cover::before {content:'';height:2mm;background:var(--blue);position:absolute;top:0;left:0;right:0;}
.cover-head {padding-top:14mm;display:flex;justify-content:space-between;
  font:700 8.5pt 'Lato',sans-serif;letter-spacing:.15em;color:var(--blue);}
.cover-title {margin-top:44mm;}
.cover-title h1 {margin:0;max-width:149mm;}
.cover-deck {font:400 15.2pt/1.52 'Noto Serif',serif;color:var(--soft);
  margin-top:11mm; max-width:146mm;}
.cover-standfirst {margin-top:26mm; padding:7mm 0 0;border-top:.7pt solid var(--line);
  max-width:151mm;font-size:11.1pt;line-height:1.66;color:var(--soft);}
.cover-footer {margin-top:28mm;}
.cover-footer .name {font:700 10pt 'Lato',sans-serif;letter-spacing:.02em;}
.cover-footer .independent {font-size:8.5pt;color:var(--soft);margin-top:1.5mm;}
.signature {font:italic 13pt 'Noto Serif',serif;color:var(--blue);margin-bottom:3mm;}
.edition {font-weight:700;color:var(--blue);font-size:8pt;letter-spacing:.12em;text-transform:uppercase;}
.contents {break-after:page;}
.toc-lede {font:400 10.25pt/1.48 'Noto Serif',serif;color:var(--soft);margin-bottom:5mm;max-width:145mm;}
.toc-section {font:700 7.8pt 'Lato',sans-serif;letter-spacing:.15em;text-transform:uppercase;
  color:var(--blue);padding:2mm 0 .5mm;break-after:avoid;}
.toc-entry { display:block; padding:.7mm 0; border-bottom:.4pt solid var(--line);
  font-size:9.65pt; line-height:1.25; position:relative; color:var(--ink);
  break-inside:avoid; padding-right:12mm; }
.toc-entry::after {content:target-counter(attr(href),page);position:absolute;right:0;
  top:.7mm;font-weight:700;color:var(--blue);}
.toc-entry.small {font-size:8.55pt;padding-left:5.5mm;color:var(--soft);padding-top:.6mm;padding-bottom:.6mm;}
.toc-entry.small::after {top:.6mm;}
.chapter {margin-bottom:12mm;}
.chapter.major {break-before:page;}
.chapter.case {break-before:page;}
.chapter-title {string-set:chapter content(text);}
.headline-kicker {font:700 7.6pt 'Lato',sans-serif;color:var(--blue);
  letter-spacing:.13em;text-transform:uppercase;margin:0 0 4mm;}
.chapter-intro {font-size:10.6pt;line-height:1.62;color:var(--soft);
  max-width:148mm;margin-bottom:6mm;}
.hero-preface {break-after:page;}
.hero-preface h2 {font-size:26pt;line-height:1.19;max-width:150mm;}
.hero-preface .lead {font:400 12.2pt/1.66 'Noto Serif',serif;color:#455565;margin:7mm 0 9mm;}
.hero-preface .motto {font:italic 12.8pt/1.6 'Noto Serif',serif;color:var(--blue);
  border-top:.7pt solid var(--line);margin-top:10mm;padding-top:8mm;}
.signal-grid {display:table;width:100%;margin:9mm 0 5mm;border-top:.65pt solid var(--line);border-bottom:.65pt solid var(--line);}
.signal {display:table-cell;width:33.3%;padding:5mm 3mm 5mm 0;}
.signal strong {display:block;font:600 19.5pt 'Noto Serif',serif;color:var(--ink);}
.signal span {font-size:8.6pt;color:var(--soft);}
.boundary { border-left:2pt solid var(--blue); padding:4mm 0 3mm 6mm;
  margin:8mm 0; background:#fff; break-inside:avoid; }
.boundary p {font-size:10.3pt;line-height:1.6;}
.boundary p:last-child {margin-bottom:0;}
.pull-rule {font:600 10pt 'Lato',sans-serif;color:var(--blue);
  border-top:.75pt solid var(--line);padding-top:4mm;margin:5mm 0 10mm;}
.routes {margin:4mm 0 9mm;}
.route {display:table;width:100%;padding:3.2mm 0;border-bottom:.5pt solid var(--line);break-inside:avoid;}
.route-no {display:table-cell;vertical-align:top;width:10mm;color:var(--blue);
  font:700 8.5pt 'Lato',sans-serif;}
.route-title {display:table-cell;vertical-align:top;width:42mm;font-weight:700;}
.route-desc {display:table-cell;vertical-align:top;color:var(--soft);font-size:9.65pt;line-height:1.52;}
.data-table {width:100%;border-collapse:collapse;margin:5mm 0 7mm;table-layout:fixed;
  font-size:9.1pt;line-height:1.44;}
.data-table thead {display:table-header-group;}
.data-table tr {break-inside:avoid;}
.data-table th,.data-table td {vertical-align:top;padding:3mm 2.5mm;
  border-bottom:.5pt solid var(--line);overflow-wrap:break-word;}
.data-table thead th {font:700 8.65pt/1.4 'Lato',sans-serif;
  color:var(--ink);text-align:left;background:var(--pale);
  border-top:.8pt solid var(--blue);}
.data-table tbody tr:nth-child(2n) {background:#fbfcfe;}
.data-table tbody th {font-weight:700;text-align:left;}
.data-table:not(.raci-table) thead th:first-child {width:26%;}
.data-table.raci-table thead th {font-size:7.95pt;text-align:center;padding:2.4mm 1.2mm;}
.data-table.raci-table thead th:first-child {text-align:left;width:34%;}
.data-table.raci-table thead th:not(:first-child) {width:13.2%;}
.data-table.raci-table tbody th {font-size:8.75pt;}
.data-table.raci-table td {font-weight:700;text-align:center;font-size:9.1pt;}
.data-table.method-table thead th:nth-child(1) {width:22%;}
.data-table.method-table thead th:nth-child(2) {width:29%;}
.data-table.method-table thead th:nth-child(3) {width:49%;}
.data-table.three-col thead th:nth-child(1) {width:25%;}
.data-table.three-col thead th:nth-child(2) {width:33%;}
.data-table.three-col thead th:nth-child(3) {width:42%;}
.table-context {font-size:8.9pt;color:var(--muted);margin-top:-3mm;margin-bottom:8mm;}
.cell-key {font-size:7.45pt;font-weight:700;letter-spacing:.05em;text-transform:uppercase;
  color:var(--blue);display:block;margin-bottom:1.25mm;}
.cell-detail + .cell-detail {margin-top:2.5mm;}
.body-subhead {font:600 12.2pt 'Noto Serif',serif;margin:7mm 0 3.5mm;break-after:avoid;}
.flow-steps {margin:6mm 0 11mm;}
.flow-step {display:table;width:100%;padding:4.2mm 0;border-bottom:.5pt solid var(--line);
  break-inside:avoid;}
.flow-number {display:table-cell;width:13mm;vertical-align:top;font:700 9pt 'Lato',sans-serif;color:var(--blue);}
.flow-body {display:table-cell;vertical-align:top;}
.flow-body b {display:block;font-weight:700;margin-bottom:1mm;}
.flow-body p {color:var(--soft);font-size:9.75pt;margin:0;}
.practise-meta {font:700 8.1pt 'Lato',sans-serif;color:var(--blue);
  text-transform:uppercase;letter-spacing:.08em;margin:6mm 0 2.5mm;}
.practice-question {font:600 11.7pt/1.57 'Noto Serif',serif;margin:0 0 7mm;}
.challenge {padding:4.8mm 5.5mm;margin:7mm 0 9mm;background:var(--pale);
  border-left:2pt solid var(--blue);break-inside:avoid;}
.challenge p {margin:0;font:400 10.4pt/1.6 'Noto Serif',serif;}
.case .chapter-intro {font-size:10.55pt;color:var(--ink);}
.case-response {border-top:1pt solid var(--blue);padding-top:6mm;margin-top:9mm;}
.case-response h3 {font-size:11.6pt;margin:0 0 4mm;}
.case-response p {font-size:10.3pt;line-height:1.62;}
.review {padding:4mm 0 0;margin:7mm 0 0;border-top:.5pt solid var(--line);}
.review p {font-size:9.7pt;}
.case .variant {margin-top:5.5mm;color:#435262;}
.reference-table {font-size:8.8pt;}
.reference-table a {word-break:break-all;font-size:8.3pt;}
.author-rule {margin-top:6mm; border-top:.65pt solid var(--line);padding-top:6mm;}
.author-name {font:600 20pt 'Noto Serif',serif;margin:0 0 2mm;}
.author-role {font:700 10pt 'Lato',sans-serif;color:var(--blue);margin:0 0 8mm;}
.author-note {font:400 11pt/1.67 'Noto Serif',serif;max-width:153mm;}
.author-links {border-top:.55pt solid var(--line);border-bottom:.55pt solid var(--line);
  margin:8mm 0;padding:5mm 0;line-height:1.95;font-size:9.65pt;}
.author-disclosure {font-size:9pt;color:var(--soft);line-height:1.55;}
.small{font-size:8.9pt;color:var(--soft);}
ol {padding-left:7mm;margin:4mm 0 7mm;}
ol li {margin-bottom:2.5mm;}
/* Limit accidental page breaks without forcing long sections into oversized gaps. */
h2 + p, h3 + p {break-before:avoid;}
.section-overview {margin-bottom:8mm;}
@media print {a {color:var(--blue)}}
'''

METHOD_IDS = ['decisions','raci','conflict','feedback','delegation','motivation','planning',
              'reporting','meetings','self','learning']


def text(node: Tag | None) -> str:
    return ' '.join(node.get_text(' ',strip=True).split()) if node else ''

def escape(value: str) -> str:
    return html.escape(str(value),quote=True)


def leaf_text(node: Tag) -> str:
    """Read copy but ignore decorative Material icons and display-only action labels."""
    clone = BeautifulSoup(str(node),'html.parser')
    for icon in clone.select('.material-symbols-outlined,i.material-symbols-outlined,svg'):
        icon.decompose()
    return text(clone)


def linked_text(node: Tag | None) -> str:
    if not node: return ''
    return leaf_text(node)


def heading(slug: str, title: str, eyebrow: str='', desc: str='', major: bool=False,
            extra_class: str='') -> str:
    classnames='chapter'+ (' major' if major else '') + (' '+extra_class if extra_class else '')
    return (f'<section class="{classnames}" id="{escape(slug)}">'
            f'<header class="chapter-header">'
            f'<p class="headline-kicker">{escape(eyebrow)}</p>'
            f'<h2 class="chapter-title">{escape(title)}</h2>'
            f'{"<p class=\"chapter-intro\">"+escape(desc)+"</p>" if desc else ""}'
            f'</header>')


def convert_table(table: Tag, context: str='') -> str:
    raw=[]
    for tr in table.find_all('tr'):
        raw.append([leaf_text(c) for c in tr.find_all(['th','td'],recursive=False)])
    if len(raw)<2: raise ValueError('Missing meaningful table rows')
    oldheads=raw[0]
    raci = ('business owner' in ' '.join(oldheads).lower() and len(oldheads)>=6)
    ref = 'reference' in context or ('source' in oldheads[0].lower())
    method = (len(oldheads)>=4 and not raci and not ref)
    if raci:
        headers=[oldheads[0]]+[{'Business owner':'Business','Integration Lead':'Integration','Release Manager':'Release'}.get(h,h) for h in oldheads[1:]]
        kind='raci-table'
        body=raw[1:]
    elif method:
        headers=[oldheads[0],oldheads[1],oldheads[2]+' / '+oldheads[3]]
        kind='method-table'
        body=[]
        for row in raw[1:]:
            if len(row)!=4:raise ValueError('Expected four cells in method comparison')
            body.append([row[0],row[1],
                '<div class="cell-detail"><span class="cell-key">'+escape(oldheads[2])+'</span>'+escape(row[2])+'</div>'+
                '<div class="cell-detail"><span class="cell-key">'+escape(oldheads[3])+'</span>'+escape(row[3])+'</div>'])
    else:
        headers=oldheads
        kind='reference-table' if ref else 'three-col' if len(headers)==3 else ''
        body=raw[1:]
    out=[f'<table class="data-table {kind}"><thead><tr>']
    out.extend(f'<th>{escape(x)}</th>' for x in headers)
    out.append('</tr></thead><tbody>')
    for ridx,r in enumerate(body):
        out.append('<tr>')
        for i,c in enumerate(r):
            tag='th' if i==0 else 'td'
            if method and i==2:
                out.append(f'<{tag}>{c}</{tag}>')
            elif ref and i==len(r)-1:
                # Provide a real clickable and printable source domain, not icon text.
                trs=table.find_all('tr')
                links=trs[ridx+1].find_all('a') if ridx+1<len(trs) else []
                if links:
                    href=links[0].get('href','')
                    display=re.sub(r'^https?://(www\.)?','',href).split('/')[0]
                    out.append(f'<{tag}><a href="{escape(href)}">{escape(display)}</a></{tag}>')
                else:out.append(f'<{tag}>{escape(c)}</{tag}>')
            else:
                out.append(f'<{tag}>{escape(c)}</{tag}>')
        out.append('</tr>')
    out.append('</tbody></table>')
    if raci:
        out.append('<p class="table-context">Business = Business owner; Integration = Integration Lead; Release = Release Manager. '
                   'A = Accountable; R = Responsible; C = Consulted; I = Informed.</p>')
    return ''.join(out)


def render_direct(node: Tag, context: str='') -> str:
    """Convert everything semantically, including hidden web answers, without summarising."""
    classes=set(node.get('class') or [])
    if node.name in ('h3','h4'):
        return f'<h3 class="body-subhead">{escape(leaf_text(node))}</h3>'
    if node.name=='p':
        value=leaf_text(node)
        # Self-referential PDF-download call is website chrome, not teaching content.
        if ('download' in value.lower() and 'pdf' in value.lower()) or value.startswith('Print edition:'):
            return ''
        return f'<p>{escape(value)}</p>'
    if node.name in ('ol','ul'):
        return '<ol>'+''.join(f'<li>{escape(leaf_text(li))}</li>' for li in node.find_all('li',recursive=False))+'</ol>'
    if node.name=='table':return convert_table(node,context)
    if 'research-route-list' in classes:
        vals=['<div class="routes">']
        for link in node.find_all('a',recursive=False):
            v=lambda cls:linked_text(link.find(class_=cls))
            vals.append('<div class="route"><span class="route-no">'+escape(link.find('span').get_text(strip=True) if link.find('span') else '')+
                '</span><b class="route-title">'+escape(linked_text(link.find('strong')))+
                '</b><span class="route-desc">'+escape(linked_text(link.find('small')))+ '</span></div>')
        vals.append('</div>')
        return ''.join(vals)
    if node.name=='details':
        body=node.select_one('.page-faq__answer')
        title=leaf_text(node.find('summary'))
        return ('<div class="case-response"><h3>Sample answer and review prompts</h3>'+
          (''.join(render_direct(c,context) for c in body.find_all(recursive=False) if isinstance(c,Tag)) if body else '')+
          '</div>')
    if 'research-canvas__signal' in classes:return ''
    if 'page-faq__list' in classes:
        return ''.join(render_direct(d,context) for d in node.find_all('details',recursive=False))
    if 'table-scroll' in classes or 'assessment-practice-table' in classes:
        tbl=node.find('table');return convert_table(tbl,context) if tbl else ''
    if node.name in ('div','section','article'):
        return ''.join(render_direct(c,context) for c in node.find_all(recursive=False) if isinstance(c,Tag))
    return ''


def render_chapter(sec: Tag, index: int, major=False) -> str:
    slug=sec.get('id') or f'content-{index}'
    header=sec.find('header',recursive=False)
    eyebrow=header.find(class_='research-canvas__eyebrow') if header else None
    title=header.find('h2') if header else None
    title_text=leaf_text(title) if title else ('Working notes' if not sec.find('h2') else leaf_text(sec.find('h2')))
    intro=''
    if header:
        plist=[leaf_text(p) for p in header.find_all('p',recursive=False) if p is not eyebrow]
        intro=' '.join(plist)
    casetype=slug.startswith('case-')
    extra='case' if casetype else ''
    head=heading(slug,title_text,leaf_text(eyebrow) if eyebrow else '',intro,major,extra)
    blocks=[]
    for child in sec.find_all(recursive=False):
        if not isinstance(child,Tag) or child is header:continue
        blocks.append(render_direct(child,slug))
    if casetype:
        # Stronger reading hierarchy but keep each source paragraph verbatim.
        joined=''.join(blocks)
        joined=joined.replace('<p>The situation.','<p class="practise-meta">THE SITUATION</p><p>')
        joined=joined.replace('<p>Your 90-second question.','<p class="practise-meta">YOUR 90-SECOND QUESTION</p><p class="practice-question">')
        joined=joined.replace('<p>Assessor&#x27;s challenge.','<p class="practise-meta">ASSESSOR CHALLENGE</p><div class="challenge"><p>')
        joined=joined.replace('</p><div class="case-response">','</p><div class="case-response">')
        # Fix challenge wrapper where present without duplicating source text.
        if '<div class="challenge"><p>' in joined:
            ix=joined.index('<div class="challenge"><p>')
            ix2=joined.find('</p>',ix)
            joined=joined[:ix2+4]+'</div>'+joined[ix2+4:]
        joined=joined.replace('<p>Example B2 answer.','<p class="practise-meta">EXAMPLE B2 ANSWER</p><p>')
        joined=joined.replace('<p>Review.','<p class="practise-meta">REVIEW</p><p>')
        joined=joined.replace('<p>Change one condition.','<p class="practise-meta">CHANGE ONE CONDITION</p><p class="variant">')
        blocks=[joined]
    return head+''.join(blocks)+'</section>'


def cover(soup: BeautifulSoup, method_count: int, case_count: int) -> str:
    hero=soup.select_one('.research-canvas__hero')
    hero_h=hero.find('h1') if hero else None
    lead=hero.select_one('.research-canvas__hero-copy > p:not(.research-canvas__eyebrow)') if hero else None
    tagline=hero.select_one('.research-canvas__signal em') if hero else None
    signals=[]
    if hero:
        for line in hero.select('.research-canvas__signal-line'):
            key=leaf_text(line.find('strong'))
            val=leaf_text(line.find('small'))
            if key and val:signals.append((key,val))
    signal_html='<div class="signal-grid">'+''.join(f'<div class="signal"><strong>{escape(k)}</strong><span>{escape(v)}</span></div>' for k,v in signals)+'</div>' if signals else ''
    result=f'''<section class="cover" id="cover"><div class="cover-head"><span>DK / FIELD NOTES</span><span>01 — SAP LEAD SERIES</span></div>
    <div class="cover-title"><p class="edition">Leadership & delivery / 2026 edition</p>
    <h1>Leadership<br>Toolkit</h1><p class="cover-deck">Lead the work.<br>Do not manage the theatre.</p></div>
    <p class="cover-standfirst">{escape(leaf_text(lead))}</p>
    {signal_html}<div class="cover-footer"><p class="signature">{escape(leaf_text(tagline))}</p>
    <p class="edition">Methods &nbsp; / &nbsp; Cases &nbsp; / &nbsp; RACI & DACI</p>
    <p class="name">Dzmitryi Kharlanau</p>
    <p class="independent">Personal SAP & AI Lab / Independent educational material</p></div></section>'''
    if not hero_h:raise ValueError('Hero missing in source')
    return result


def chapter_map(soup:BeautifulSoup) -> list[tuple[str,str,str]]:
    """Automatic TOC from headings that actually exist in the source."""
    entries=[]
    for index,sec in enumerate(soup.select('.research-canvas > section')):
        name=(sec.get('id') or f'content-{index+1}')
        if 'research-canvas__boundary' in (sec.get('class') or []): continue
        hdr=sec.find('header',recursive=False)
        title=hdr.find('h2') if hdr else sec.find('h2')
        if not title:continue
        entries.append((name,leaf_text(title),'case' if name.startswith('case-') else 'chapter'))
    return entries


def toc(entries: list[tuple[str,str,str]]) -> str:
    pieces=['<section class="contents" id="contents"><p class="headline-kicker">Reader navigation</p>',
            '<h2>Contents</h2><p class="toc-lede">A complete printed counterpart of the online Leadership Toolkit. '
            'Theory, responsibility matrices, practical cases, model answers and references appear in source order.</p>']
    part=''
    for slug,title,kind in entries:
        if slug=='how-to-practice':new='Introduction'
        elif slug in ('field-kit','decisions'):new='Methods & ownership'
        elif slug=='raci':new='RACI / DACI'
        elif slug=='practice-stories':new='Practise the situations'
        elif kind=='case':new='Ten assessment cases'
        elif slug=='learning':new='Learn from failure'
        else:new=''
        if new and new!=part:
            pieces.append('<div class="toc-section">'+escape(new)+'</div>');part=new
        pieces.append(f'<a class="toc-entry{(" small" if kind=="case" else "")}" href="#{escape(slug)}">{escape(title)}</a>')
    pieces.append('<a class="toc-entry" href="#about-author">About the author</a></section>')
    return ''.join(pieces)


def pressure_section(sec:Tag) -> str:
    title=sec.find('h2')
    items=sec.select('ol li')
    out=heading('pressure-model',leaf_text(title),'Pressure model')
    out+='<div class="flow-steps">'
    for li in items:
        number=li.find('span')
        strong=li.find('strong')
        p=li.find('p')
        out+=('<div class="flow-step"><div class="flow-number">'+escape(leaf_text(number))+
              '</div><div class="flow-body"><b>'+escape(leaf_text(strong))+'</b><p>'+escape(leaf_text(p))+'</p></div></div>')
    return out+'</div></section>'


def boundary(sec:Tag) -> str:
    return '<div class="boundary">'+''.join('<p>'+escape(leaf_text(p))+'</p>' for p in sec.find_all('p',recursive=False))+'</div>'


def render_author() -> str:
    return '''<section class="chapter major" id="about-author">
    <p class="headline-kicker">Notes on authorship</p><h2 class="chapter-title">About the author</h2>
    <div class="author-rule"><p class="author-name">Dzmitryi Kharlanau</p>
    <p class="author-role">Senior SAP Consultant at EPAM Systems</p>
    <p class="author-note">Dzmitryi works across SAP SD, MM, end-to-end logistics, master data, integrations and enterprise operations. His personal technical lab explores practical SAP engineering, reliable delivery, AI tools and methods for making complicated work easier to understand and manage.</p>
    <p class="author-note">This guide is part of that personal knowledge base. It connects clear leadership practices with the situations that SAP consultants face when responsibilities, technical evidence and business deadlines meet.</p>
    <div class="author-links"><a href="https://dkharlanau.github.io/">dkharlanau.github.io</a><br>
    <a href="https://github.com/dkharlanau">github.com/dkharlanau</a><br>
    <a href="https://www.linkedin.com/in/dkharlanau/">linkedin.com/in/dkharlanau</a></div>
    <p class="author-disclosure">Independent, non-commercial educational material. It is not an official publication of EPAM Systems or SAP and does not represent either organisation. The scenarios are fictional; SAP behaviour and approval boundaries must be verified in the relevant landscape.</p>
    <p class="small">Source: dkharlanau.github.io/labs/assessment/leadership-toolkit/</p></div></section>'''


def render_source(source:Path) -> tuple[str,dict]:
    raw=source.read_text(encoding='utf8').split('---',2)[-1]
    soup=BeautifulSoup(raw,'html.parser')
    canvas=soup.select_one('div.research-canvas')
    if not canvas:raise ValueError('The expected research-canvas is missing')
    entries=chapter_map(soup)
    sections=canvas.find_all('section',recursive=False)
    case_count=sum(1 for s in sections if (s.get('id') or '').startswith('case-'))
    method_count=sum(len(section.find_all('tr'))-1 for section in sections
         if section.get('id') in METHOD_IDS and section.find('table'))
    if case_count!=10 or method_count<40:raise ValueError(f'Source content unexpectedly changed: cases={case_count}, methods={method_count}')
    parts=['<!doctype html><html lang="en"><head><meta charset="utf-8"><title>SAP Lead Leadership Toolkit — Complete Print Edition</title><style>',STYLE,'</style></head><body>']
    parts.append(cover(soup,method_count,case_count))
    parts.append(toc(entries))
    # Preserve all source sections in source order. Do not create an independent content list.
    n=0
    for section in sections:
        n+=1
        cls=set(section.get('class') or [])
        if 'research-canvas__boundary' in cls:
            parts.append(boundary(section));continue
        if 'research-canvas__method' in cls:
            parts.append(pressure_section(section));continue
        major=(section.get('id') in ('decisions','practice-stories'))
        parts.append(render_chapter(section,n,major=major))
    parts.append(render_author())
    parts.append('</body></html>')
    summary={'cases':case_count,'methods':method_count,'sections':len(sections),
        'tables':sum(len(s.find_all('table')) for s in sections),
        'source_paragraphs':sum(len(s.find_all('p')) for s in sections),
        'toc_entries':len(entries)+1}
    return ''.join(parts),summary



def assert_content_parity(source:Path, generated_html:str) -> dict:
    """Guard against accidentally omitting a substantive paragraph or table cell."""
    raw=source.read_text(encoding='utf8').split('---',2)[-1]
    root=BeautifulSoup(raw,'html.parser').select_one('div.research-canvas')
    rendered=BeautifulSoup(generated_html,'html.parser')
    if not root: raise ValueError('Cannot verify parity without source content')
    def canonical(s:str) -> str:
        return ''.join(ch for ch in unicodedata.normalize('NFKC',s).casefold() if ch.isalnum())
    haystack=canonical(rendered.get_text(' ',strip=True))
    checked=0
    missing=[]
    for block in root.select('section p,section td,section th,section small'):
        value=leaf_text(block)
        if ('download' in value.casefold() and 'pdf' in value.casefold()) or value.startswith('Print edition:'):
            continue
        for prefix in ('The situation.','Your 90-second question.',"Assessor's challenge.",
                       'Example B2 answer.','Review.','Change one condition.'):
            if value.startswith(prefix):
                value=value[len(prefix):].strip()
                break
        target=canonical(value)
        if len(target)<38: continue
        checked+=1
        if target not in haystack: missing.append(value[:110])
    if missing:
        raise ValueError(f'PDF would omit {len(missing)} of {checked} substantive source fragments. Examples: '+str(missing[:5]))
    return {'verified_fragments':checked,'omissions':0}


def main() -> None:
    parser=argparse.ArgumentParser(description='Build an unabridged, editorial A4 PDF from the Leadership Toolkit source.')
    parser.add_argument('--source',type=Path,default=SOURCE_DEFAULT)
    parser.add_argument('--output',type=Path,default=OUTPUT_DEFAULT)
    parser.add_argument('--html-preview',type=Path,default=None)
    args=parser.parse_args()
    html_source,summary=render_source(args.source)
    summary.update(assert_content_parity(args.source,html_source))
    if args.html_preview:
        args.html_preview.parent.mkdir(parents=True,exist_ok=True)
        args.html_preview.write_text(html_source,encoding='utf8')
    args.output.parent.mkdir(parents=True,exist_ok=True)
    HTML(string=html_source,base_url=str(args.source.parent)).write_pdf(str(args.output))
    if args.output.stat().st_size<30000:raise RuntimeError('PDF output is unexpectedly small')
    print(f'Complete leadership PDF created: {args.output} ({args.output.stat().st_size} bytes). {summary}')

if __name__=='__main__':main()
