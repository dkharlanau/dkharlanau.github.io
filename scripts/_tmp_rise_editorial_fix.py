from pathlib import Path

p = Path('_blog/do-you-actually-need-rise-with-sap-what-it-is-what-it-includes-and.md')
t = p.read_text(encoding='utf-8')
old = 'description: "Its data centre is expensive. The SAP landscape contains years of custom code. Experienced Basis specialists are becoming difficult to replace."'
new = 'description: "A practical decision framework for evaluating RISE with SAP: transformation intent, operating model, architecture, commercial boundaries, and exit considerations."'
t = t.replace(old, new, 1)
if 'last_modified_at:' not in t.split('---', 2)[1]:
    t = t.replace('date: 2026-07-17\n', 'date: 2026-07-17\nlast_modified_at: 2026-08-14\n', 1)
anchor = 'A company is still running SAP ECC.\n'
if '### My decision test\n' not in t:
    intro = '''### My decision test

I would not start a RISE with SAP discussion with a hosting comparison. I would start with the operating problem the company is trying to solve: lifecycle risk, infrastructure ownership, transformation capacity, clean-core discipline, access to cloud innovation, or some combination of these. If the problem is not explicit, the commercial package becomes the architecture by accident.

For me, the useful question is not whether RISE is strategically "good" or "bad". It is whether the target operating model, application architecture, responsibilities, economics, and exit path make sense together for this landscape.

'''
    t = t.replace(anchor, intro + anchor, 1)
p.write_text(t, encoding='utf-8')
