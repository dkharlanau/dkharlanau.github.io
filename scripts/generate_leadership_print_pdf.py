#!/usr/bin/env python3
"""Build an A4 print edition of the public SAP Lead Leadership Toolkit."""
from pathlib import Path
from html import escape
from bs4 import BeautifulSoup
from weasyprint import HTML
import argparse

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "labs/assessment/leadership-toolkit/index.md"
DEFAULT_OUTPUT = ROOT / "assets/downloads/sap-lead-leadership-toolkit-print.pdf"

CSS = """
@page {
  size:A4; margin:20mm 20mm 19mm;
  @top-left {content:"SAP LEAD  /  LEADERSHIP TOOLKIT"; font:700 7.8pt Lato; color:#59636d; border-bottom:.5pt solid #dae0e5; padding-bottom:4.5mm}
  @top-right {content:"PRINT EDITION"; font:400 7.6pt Lato; color:#75818b; border-bottom:.5pt solid #dae0e5; padding-bottom:4.5mm}
  @bottom-left {content:"PERSONAL SAP & AI LAB  /  FICTIONAL CASES";font:400 7.5pt Lato;color:#737d87;border-top:.5pt solid #dae0e5;padding-top:4mm}
  @bottom-right {content:counter(page);font:700 8.5pt Lato;color:#30383f;border-top:.5pt solid #dae0e5;padding-top:4mm}
}
@page:first {@top-left{content:none}@top-right{content:none}@bottom-left{content:none}@bottom-right{content:none}}
html {font-family:Lato,"Liberation Sans",sans-serif;color:#283039}
body {font-size:10.55pt;line-height:1.62;margin:0}
h1,h2,h3 {font-family:"Noto Serif","Liberation Serif",serif;line-height:1.24;break-after:avoid;margin:0}
h2{font-size:23pt;letter-spacing:-.02em;margin-bottom:7mm}
h3{font-size:15.5pt;margin:9mm 0 4mm}
p{margin:0 0 4mm;orphans:3;widows:3}
a{color:#215b95;text-decoration:none}
.kicker{font:700 8.4pt Lato;color:#215b95;text-transform:uppercase;letter-spacing:.13em;margin-bottom:5mm}
.lede{font-size:12pt;line-height:1.58;color:#56626d}
.muted{color:#586570;font-size:9.5pt}
.cover{break-after:page;min-height:235mm}
.cover .top{border-top:1.4pt solid #215b95;padding-top:20mm}
.cover h1{font-size:40pt;line-height:1.17;margin-top:27mm;margin-bottom:7mm}
.cover .subtitle{font:400 18pt/1.4 "Noto Serif",serif;color:#5b6873;margin-bottom:21mm}
.cover .summary{font-size:12.3pt;color:#4f5c67;border-top:.6pt solid #d6dce2;padding-top:9mm;max-width:145mm}
.cover .edition{font:700 9pt Lato;color:#215b95;margin-top:20mm}
.cover .by{font-size:9pt;color:#697581;margin-top:26mm}
.chapter{break-before:page}
.chapter-head{margin-bottom:9mm}
.chapter-head p{max-width:148mm}
.toc{break-after:page}
.toc .title{font:700 30pt "Noto Serif",serif;margin-bottom:9mm}
.toc h3{font-size:15pt;margin:7mm 0 4mm}
.toc-link{display:block;border-bottom:.45pt solid #dbe0e5;position:relative;padding:2.2mm 0;break-inside:avoid;font-size:10.1pt;color:#293039}
.toc-link::after{content:target-counter(attr(href),page);position:absolute;right:0;color:#215b95}
.toc-case{font-size:9.1pt;padding:1.4mm 0 1.4mm 6mm;color:#586570}
.eyebrow{font:700 8.4pt Lato;text-transform:uppercase;letter-spacing:.09em;color:#215b95;margin-bottom:4mm}
hr{border:0;border-top:.7pt solid #dce1e6;margin:8mm 0}
.rail{border-bottom:.45pt solid #dce1e6;padding:3mm 0;display:table;width:100%}
.rail b{display:table-cell;width:42mm;font-size:9.8pt}
.rail span{display:table-cell;font-size:9.7pt;color:#596570;line-height:1.5}
table{border-collapse:collapse;table-layout:fixed;width:100%;margin:4mm 0 7mm}
thead{display:table-header-group}
tr{break-inside:avoid}
th,td{vertical-align:top;border-bottom:.45pt solid #dce1e6;overflow-wrap:break-word}
thead th{background:#f4f6f8;color:#28323b;font:700 8.7pt/1.4 Lato;text-align:left;padding:3mm 2.7mm}
tbody th,tbody td{padding:3mm 2.7mm;font:400 9.1pt/1.45 Lato}
tbody th{font-weight:700;text-align:left}
tbody tr:nth-child(even){background:#fafbfc}
.methods-table thead th:nth-child(1){width:22%}
.methods-table thead th:nth-child(2){width:29%}
.methods-table thead th:nth-child(3){width:49%}
.roles-table thead th:nth-child(1){width:23%}
.roles-table thead th:nth-child(2){width:49%}
.roles-table thead th:nth-child(3){width:28%}
.contrast-table thead th:nth-child(1){width:24%}
.contrast-table thead th:nth-child(2){width:38%}
.contrast-table thead th:nth-child(3){width:38%}
.raci-table thead th{font-size:8.1pt;text-align:center;padding:3mm 1.6mm}
.raci-table thead th:first-child{text-align:left;width:36%}
.raci-table thead th:not(:first-child){width:12.8%}
.raci-table tbody th{font-size:8.6pt;line-height:1.4}
.raci-table tbody td{text-align:center;font:700 9.4pt Lato}
.raci-table tbody th,.raci-table tbody td{padding:2.7mm 1.6mm}
.method{margin-top:10mm}
.method>p{color:#596570;font-size:9.8pt}
.method h3{font-size:15pt;margin:0 0 4mm}
.case,.answer{break-before:page}
.case h2,.answer h2{font-size:24pt;margin-bottom:10mm}
.case p,.answer p{font-size:10.7pt;line-height:1.64}
.field{margin-top:7mm;break-inside:avoid}
.field-label{font:700 8.3pt Lato;letter-spacing:.09em;text-transform:uppercase;color:#215b95;margin-bottom:3mm}
.question{font:700 12pt/1.55 "Noto Serif",serif!important}
.notes{margin-top:10mm}
.note-line{height:9mm;border-bottom:.5pt solid #c7cfd6}
.answer-text{font-size:11pt!important;line-height:1.72!important}
.review{border-top:.6pt solid #dce1e6;margin-top:10mm;padding-top:7mm}
.small{font-size:8.9pt;color:#66727e}
.phrase{border-bottom:.45pt solid #dce1e6;padding:3mm 0;font-size:10pt}
.author-name{font:700 19pt "Noto Serif",serif;margin:10mm 0 4mm}
.links{border-top:.6pt solid #dce1e6;border-bottom:.6pt solid #dce1e6;padding:5mm 0;line-height:2.1;margin:9mm 0}
.notice{border-left:2pt solid #215b95;padding-left:5mm;color:#5b6670;margin:7mm 0;font-size:9.65pt}
"""

def t(node):
    return " ".join(node.get_text(" ",strip=True).split()) if node else ""
def e(x):
    return escape(str(x),quote=True)
def rows(table):
    return [[t(c) for c in tr.find_all(["th","td"],recursive=False)] for tr in table.find_all("tr")] if table else []
def table(head,data,css="methods-table"):
    out=['<table class="'+css+'"><thead><tr>']
    out += ["<th>"+e(x)+"</th>" for x in head]
    out.append("</tr></thead><tbody>")
    for r in data:
        out.append("<tr>")
        for i,x in enumerate(r):
            tag="th" if i==0 else "td"
            out.append("<"+tag+">"+e(x)+"</"+tag+">")
        out.append("</tr>")
    out.append("</tbody></table>")
    return "".join(out)
def read(source):
    raw=Path(source).read_text(encoding="utf8").split("---",2)[-1]
    soup=BeautifulSoup(raw,"html.parser")
    methods=[]
    for n,slug in enumerate(["decisions","conflict","feedback","delegation","motivation","planning","reporting","meetings","self","learning"],1):
        sec=soup.find("section",id=slug)
        if not sec:raise ValueError("Missing method: "+slug)
        hdr=sec.find("header")
        intro=next((t(p) for p in hdr.find_all("p",recursive=False) if len(t(p))>35),"")
        methods.append((n,slug,t(sec.find("h2")),intro,rows(sec.find("table"))[1:]))
    raci=soup.find("section",id="raci")
    if not raci:raise ValueError("Missing RACI")
    rr=[rows(x) for x in raci.find_all("table")]
    if len(rr)!=3:raise ValueError("RACI tables changed")
    cases=[]
    for n,sec in enumerate(soup.select('section[id^="case-"]'),1):
        ps=[t(p) for p in sec.find_all("p")]
        def get(prefix):
            found=[v[len(prefix):].strip() for v in ps if v.startswith(prefix)]
            if len(found)!=1:raise ValueError(prefix+" case "+str(n))
            return found[0]
        topic=t(sec.find("p",class_="research-canvas__eyebrow")).split(" / ",1)[-1]
        cases.append((n,sec["id"],topic,t(sec.find("h2")),get("The situation."),get("Your 90-second question."),get("Assessor's challenge."),get("Example B2 answer."),get("Review."),get("Change one condition.")))
    if len(cases)!=10 or len(rr[1])!=7:raise ValueError("Expected ten cases and six RACI deliverables")
    return methods,rr,cases

def render(methods,rr,cases):
    b=['<!doctype html><html lang="en"><meta charset="utf-8"><style>',CSS,'</style><body>']
    a=b.append
    a('<section class="cover"><div class="top"><p class="kicker">SAP Lead / The practice edition</p></div><h1>Leadership<br>Toolkit</h1><p class="subtitle">Decisions, people and delivery in SAP situations</p><p class="summary">A practical print-first guide to responsibility, conflict, delegation, delivery risk and clear decisions across SAP teams.</p><p class="edition">10 cases &nbsp; / &nbsp; RACI &amp; DACI &nbsp; / &nbsp; Methods &amp; B2 spoken answers</p><p class="by">Dzmitryi Kharlanau<br>Personal SAP &amp; AI Lab<br>October 2026</p></section>')
    a('<section class="toc" id="contents"><p class="kicker">Navigation / Print reference</p><p class="title">Contents</p><p class="lede">Start with ownership, then methods and the casebook. Model answers are at the end so you can practise without looking ahead.</p>')
    for k,v in [("how","How to use this guide"),("ownership","Part I  /  Responsibility and decision rights"),("raci","RACI in an SAP project"),("methods","Part II  /  Leadership methods"),("practice","Part III  /  Situation practice"),("models","Part IV  /  Model answers"),("rehearsal","Part V  /  Rehearsal and sources"),("about","About the author")]:
        a('<a class="toc-link" href="#'+k+'">'+e(v)+'</a>')
    a('<h3>Practice cases</h3>')
    for n,slug,topic,title,*_ in cases:
        a('<a class="toc-link toc-case" href="#'+e(slug)+'">'+f'{n:02}'+"  "+e(title)+'</a>')
    a('</section>')
    a('<section class="chapter" id="how"><div class="chapter-head"><p class="eyebrow">Start here</p><h2>How to use this guide</h2><p class="lede">Practise judgement, not management vocabulary. Choose a technique only if it changes the next action.</p></div>')
    for k,v in [("Read","Understand the difference between responsibility and decision authority."),("Speak","Answer one fictional situation aloud in about 90 seconds."),("Handle pressure","Reply to the challenge; then change a condition and reconsider."),("Review","Compare your answer against ownership, risks and proof.")]:
        a('<div class="rail"><b>'+e(k)+'</b><span>'+e(v)+'</span></div>')
    a('<h3>A Lead answer in five moves</h3>')
    a(table(["Move","Question","Useful evidence"],[("Outcome","What must the business protect?","Missed delivery, blocked order, financial control"),("Evidence","What do we know?","Document flow, test, interface trace"),("Authority","Who decides and who executes?","RACI, DACI or change record"),("Trade-off","Which choice fits the constraints?","Time, scope, risk and maintenance"),("Close","What confirms success?","Owner, date, criteria and evidence")]))
    a('<p class="small">All scenarios are fictional. SAP behaviour and approval authority vary by project and system.</p></section>')
    a('<section class="chapter" id="ownership"><div class="chapter-head"><p class="eyebrow">Part I / Ownership</p><h2>Responsibility and decision rights</h2><p class="lede">RACI defines work ownership. DACI defines who drives and approves one decision. Both may be needed, but they are not interchangeable.</p></div><h3>Four RACI roles</h3>')
    a(table(["Role","Meaning","Question to ask"],rr[0][1:],"roles-table"))
    a('<h3>RACI and DACI compared</h3>')
    a(table(rr[2][0],rr[2][1:],"contrast-table"))
    a('<div class="notice">Use one Accountable owner for each deliverable, and one authorised Approver for the decision.</div></section>')
    a('<section class="chapter" id="raci"><div class="chapter-head"><p class="eyebrow">Ownership / Worked example</p><h2>RACI in an SAP project</h2><p class="lede">An illustrative responsibility matrix for SAP Order-to-Cash testing and cutover.</p></div>')
    labels=["Deliverable","Business owner","SD Lead","Integration Lead","Test Lead","Release Manager"]
    a(table(labels,rr[1][1:],"raci-table"))
    a('<p class="small">R = Responsible  /  A = Accountable  /  C = Consulted  /  I = Informed</p>')
    a('<h3>Read the matrix</h3><p>For test data, the SD Lead prepares it and the Test Lead owns readiness. The business and Integration teams provide input. The Release Manager receives the status.</p>')
    a('<h3>Apply it in 15 minutes</h3>')
    for k,v in [("List deliverables","Start with five to ten important outcomes."),("Assign ownership","Exactly one A and at least one R for each row."),("Confirm evidence","Agree the criteria that prove the result."),("Escalate gaps","Escalate an unclear decision boundary, not a person.")]:
        a('<div class="rail"><b>'+e(k)+'</b><span>'+e(v)+'</span></div>')
    a('</section>')
    a('<section class="chapter" id="methods"><div class="chapter-head"><p class="eyebrow">Part II / Field reference</p><h2>Leadership methods</h2><p class="lede">Ten common situations. Use the lightest technique that creates a clear decision or better commitment.</p></div>')
    for n,slug,title,intro,methodrows in methods:
        a('<section class="method" id="method-'+f'{n:02}'+'"><p class="eyebrow">Method '+f'{n:02}'+' / '+e(slug)+'</p><h3>'+e(title)+'</h3><p>'+e(intro)+'</p>')
        data=[]
        for r in methodrows:
            last=r[2] if len(r)>2 else ""
            if len(r)>3:last+="  Example: "+r[3]
            data.append([r[0],r[1] if len(r)>1 else "",last])
        a(table(["Technique","Use it when","Practical move / SAP example"],data))
        a('</section>')
    a('</section>')
    a('<section class="chapter" id="practice"><div class="chapter-head"><p class="eyebrow">Part III / Casebook</p><h2>Situation practice</h2><p class="lede">Read one story, speak for 90 seconds, then respond to the assessor. Do not read the model answer before your attempt.</p></div>')
    for z in ["Identify the business result.","Separate facts from assumptions.","Compare possible decisions and the risk.","Name the owner and evidence of completion."]:a("<p>"+e(z)+"</p>")
    a('</section>')
    for n,slug,topic,title,story,question,challenge,answer,review,variant in cases:
        a('<section class="case" id="'+e(slug)+'"><p class="eyebrow">Case '+f'{n:02}'+'  /  '+e(topic)+'</p><h2>'+e(title)+'</h2>')
        for name,value,css in [("The situation",story,""),("Your 90-second answer",question,"question"),("Assessor pushback",challenge,""),("Changed condition",variant,"")]:
            a('<div class="field"><p class="field-label">'+name+'</p><p'+(' class="'+css+'"' if css else '')+'>'+e(value)+'</p></div>')
        a('<div class="notes"><p class="field-label">Your notes  /  Decision - Evidence - Owner</p><div class="note-line"></div><div class="note-line"></div><div class="note-line"></div></div><p class="small">Fictional scenario for assessment practice.</p></section>')
    a('<section class="chapter" id="models"><div class="chapter-head"><p class="eyebrow">Part IV / Review</p><h2>Model answers</h2><p class="lede">These are examples, not fixed scripts. A strong assessor will change one condition and ask whether your decision still works.</p></div><p>Compare your answer with the business outcome, evidence, options, risk, approval authority and next action.</p></section>')
    for n,slug,topic,title,story,question,challenge,answer,review,variant in cases:
        a('<section class="answer" id="answer-'+f'{n:02}'+'"><p class="eyebrow">Model answer '+f'{n:02}'+' / B2 speaking</p><h2>'+e(title)+'</h2><p class="field-label">One possible response</p><p class="answer-text">'+e(answer)+'</p><div class="review"><p class="field-label">What makes this answer strong</p><p>'+e(review)+'</p><p class="field-label">Practise the variation</p><p>'+e(variant)+'</p></div><p class="small">Now try the answer again without reading it.</p></section>')
    a('<section class="chapter" id="rehearsal"><div class="chapter-head"><p class="eyebrow">Part V / Memory sheet</p><h2>Last-page rehearsal</h2><p class="lede">Use these clear B2 sentences when you need a reliable way to start.</p></div>')
    for x in ["I would start by clarifying the business impact and the decision owner.","Before changing configuration, I would check the evidence.","The main trade-off here is delivery speed versus long-term risk.","Let us separate immediate recovery from root-cause investigation.","I would document the decision, its assumptions and the review point."]:
        a('<div class="phrase">'+e(x)+'</div>')
    a('<h3>Final self-check</h3><p>Outcome - Facts - Authority - Options - Owner - Evidence.</p><h3>Further reading</h3>')
    for label,url in [("Atlassian: RACI","https://www.atlassian.com/work-management/project-management/raci-chart"),("Atlassian: DACI","https://www.atlassian.com/team-playbook/plays/daci"),("Atlassian: Pre-mortem","https://www.atlassian.com/team-playbook/plays/pre-mortem"),("Center for Creative Leadership: SBI / SBII","https://www.ccl.org/articles/leading-effectively-articles/closing-the-gap-between-intent-vs-impact-sbii/"),("Harvard Program on Negotiation: BATNA","https://www.pon.harvard.edu/daily/batna/translate-your-batna-to-the-current-deal/")]:
        a('<p><a href="'+e(url)+'">'+e(label)+'</a></p>')
    a('</section>')
    a('<section class="chapter" id="about"><div class="chapter-head"><p class="eyebrow">Personal lab</p><h2>About the author</h2></div><p class="author-name">Dzmitryi Kharlanau</p><p><strong>Senior SAP Consultant at EPAM Systems</strong></p>')
    a('<p>Dzmitryi works across SAP logistics, Sales and Procurement, integration, master data and enterprise operations. His personal technical lab also explores practical AI and methods for managing complex business problems.</p>')
    a('<p>He maintains this site as an independent knowledge base for learning, experiments and reusable engineering practices. This guide helps SAP practitioners discuss decisions, coordinate work across teams and connect technical evidence with business outcomes.</p>')
    a('<div class="links"><a href="https://dkharlanau.github.io/">dkharlanau.github.io</a><br><a href="https://github.com/dkharlanau">github.com/dkharlanau</a><br><a href="https://www.linkedin.com/in/dkharlanau/">linkedin.com/in/dkharlanau</a></div>')
    a('<h3>Independence and use</h3><p class="small">This is personal, non-commercial study material, not an official EPAM Systems or SAP publication. All project scenarios are fictional, not actual client accounts. System-specific SAP rules and decision authority require verification.</p><p class="small">October 2026. Refer to the online Leadership Toolkit for updates.</p></section></body></html>')
    return "".join(b)

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--source",type=Path,default=DEFAULT_SOURCE)
    parser.add_argument("--output",type=Path,default=DEFAULT_OUTPUT)
    args=parser.parse_args()
    methods,rr,cases=read(args.source)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    HTML(string=render(methods,rr,cases),base_url=str(args.source.parent)).write_pdf(str(args.output))
    if args.output.stat().st_size<20000:raise RuntimeError("PDF appears incomplete")
    print(f"Created {args.output}: {args.output.stat().st_size} bytes; {len(cases)} cases")