from pathlib import Path
import re


def read(path):
    return Path(path).read_text(encoding="utf-8")


def write(path, text):
    Path(path).write_text(text, encoding="utf-8")


def replace_once(text, old, new, path):
    if old not in text:
        raise SystemExit(f"Missing marker in {path}: {old[:100]}")
    return text.replace(old, new, 1)


def replace_section(text, heading, next_heading, body, path):
    pattern = re.escape(heading) + r".*?(?=" + re.escape(next_heading) + r")"
    replacement = heading + "\n" + body.rstrip() + "\n\n"
    updated, count = re.subn(pattern, replacement, text, count=1, flags=re.S)
    if count != 1:
        raise SystemExit(f"Could not replace {heading} in {path}")
    return updated


# Permanent author-voice contract.
path = "_data/labs/enterprise_context/manifest.yml"
text = read(path)
old = '''  - id: independent_synthesis
    label: "Independent synthesis"
    description: "Vendor sources verify facts; public explanations, comparisons, models, and examples are written independently for this site."
'''
new = old + '''  - id: author_reasoning
    label: "Teach the reasoning"
    description: "Public content should show how I frame the problem, what I check, where I draw boundaries, and why I prefer one decision over another."
'''
text = replace_once(text, old, new, path)
old = '''    - "Do not bulk scrape or build a local copy of vendor web content."
  origin_labels:
'''
new = '''    - "Do not bulk scrape or build a local copy of vendor web content."
  author_voice_rules:
    - "Use first person for genuine professional methods, preferences, and reasoning, not for invented project history."
    - "Do not fabricate clients, incidents, outcomes, project details, metrics, savings, or personal experience."
    - "Prefer a reasoning path over a product catalogue: problem, evidence, boundary, trade-off, decision, and next check."
    - "Surface failure modes and operational consequences where they materially change the architecture decision."
    - "Mark fictional cases as synthetic; do not disguise a synthetic example as a real delivery story."
    - "Avoid generic consultant language when a concrete diagnostic question or decision rule can teach more."
  origin_labels:
'''
text = replace_once(text, old, new, path)
write(path, text)

path = "_data/labs/enterprise_context/schema.yml"
text = read(path)
old = '''    - "Do not bulk scrape or mirror vendor websites."

node_types:
'''
new = '''    - "Do not bulk scrape or mirror vendor websites."
    - "Use first person only for supportable professional methods and judgments; never invent projects, clients, outcomes, or metrics."
    - "Prefer reasoning that exposes evidence checks, trade-offs, failure modes, and the next decision over catalogue-style prose."
    - "Synthetic examples must remain visibly synthetic and must not be presented as personal delivery history."

node_types:
'''
text = replace_once(text, old, new, path)
write(path, text)

path = "legal/research-attribution.md"
text = read(path)
marker = '''This separation is intentional. A vendor statement and an architect's judgment are not the same thing.

## SAP names and trademarks
'''
insert = '''This separation is intentional. A vendor statement and an architect's judgment are not the same thing.

## Voice and authenticity

I write in the first person when I am describing a professional method, a diagnostic habit, an architecture preference, or a lesson that can be explained without exposing confidential work. The purpose is to teach the reasoning, not to make the page sound more personal for its own sake.

I do not invent client stories, project outcomes, savings figures, incident details, or experience that is not mine. When an example is fictional, it is marked as synthetic or illustrative. When I say that I would check something first, that is a working heuristic and not a claim that every SAP landscape behaves the same way.

A useful page should normally reveal more than the conclusion. It should show the business problem, the evidence I would ask for, the boundary or trade-off I care about, the failure mode I am trying to avoid, and the next decision. That is the part of professional knowledge worth preserving.

## SAP names and trademarks
'''
text = replace_once(text, marker, insert, path)
write(path, text)

# Profile voice.
path = "about.md"
text = read(path)
text = replace_once(
    text,
    '''    <p>SAP consultant at <a href="https://www.epam.com" target="_blank" rel="noopener noreferrer">EPAM Systems</a>, previously at abat. The work connects SAP operations, transformation, and AI readiness through process evidence, technical diagnosis, ownership, and a delivery sequence that remains useful after handover.</p>''',
    '''    <p>SAP consultant at <a href="https://www.epam.com" target="_blank" rel="noopener noreferrer">EPAM Systems</a>, previously at abat. I work where SAP operations, transformation, and AI readiness meet: process evidence, technical diagnosis, ownership, and delivery decisions that still make sense after handover.</p>''',
    path,
)
text = replace_once(
    text,
    '''      <p>The work sits where a business process crosses SAP configuration, master data, custom logic, interfaces, and the support model. A blocked order, failed replication, or delayed invoice is rarely a single-module problem. The useful question is which decision, dependency, or control broke—and what evidence separates a local workaround from a durable fix.</p>
      <p>It suits work where teams need a functional lead who can define the failure with application, ABAP, integration, data, and operations colleagues.</p>''',
    '''      <p>My work usually sits where a business process crosses SAP configuration, master data, custom logic, interfaces, and the support model. A blocked order, failed replication, or delayed invoice is rarely a useful "single-module" problem. I start by asking which decision, dependency, or control failed, then look for the evidence that separates a local workaround from a durable fix.</p>
      <p>This is the kind of work where I can frame the functional problem and keep the same evidence chain understandable to application, ABAP, integration, data, and operations colleagues.</p>''',
    path,
)
text = text.replace("<h2>How SAP problems are approached</h2>", "<h2>How I approach SAP problems</h2>", 1)
text = replace_once(
    text,
    '''    <div class="prose"><p>Avoid fixes that only improve the appearance of control: green SLAs while the same incidents recur, dashboards without an accountable recovery path, AI pilots without a usable knowledge layer, or “clean core” work that moves unowned complexity elsewhere. The result should be a bounded change with an owner, evidence, and a recovery path.</p></div>''',
    '''    <div class="prose"><p>I avoid fixes that only improve the appearance of control: green SLAs while the same incidents recur, dashboards without an accountable recovery path, AI pilots without a usable knowledge layer, or clean-core work that merely moves unowned complexity elsewhere. I want the result to be a bounded change with an owner, evidence, and a recovery path.</p></div>''',
    path,
)
write(path, text)

# Integration architecture article: repair migrated metadata and expose the author's decision model.
path = "_blog/centralized-or-federated-sap-integration-architecture-how-to-divide.md"
text = read(path)
text = re.sub(
    r"^description: .*$",
    'description: "A practical operating model for deciding which SAP integration responsibilities belong centrally and which should stay with business domains."',
    text,
    count=1,
    flags=re.M,
)
if "last_modified_at:" not in text.split("---", 2)[1]:
    text = text.replace("date: 2026-07-17\n", "date: 2026-07-17\nlast_modified_at: 2026-08-14\n", 1)
anchor = "A global company introduces one central integration platform.\n"
intro = '''### My starting position

I do not treat centralized and federated integration as opposite architecture styles. My default is to centralize the control plane and federate the business meaning. Security baselines, runtime standards, observability, deployment controls, and reusable technical patterns benefit from central ownership. The meaning of a customer event, a pricing rule, a procurement exception, or a reconciliation outcome belongs with the domain that can defend that meaning.

That distinction matters because a central platform team can own excellent tooling and still become a bottleneck if it is also expected to own every business decision. The reverse is equally dangerous: domain autonomy without common controls produces local speed and enterprise-level archaeology.

''' + anchor
text = replace_once(text, anchor, intro, path)
old = '''SAP currently presents Integration Suite as a unified platform for connecting applications, processes, data, APIs, events, partners and AI agents across SAP and third-party environments. The platform includes centralized governance, monitoring and security while supporting cloud, on-premises and hybrid landscapes.

Centralized platform capability does not require centralized ownership of every business decision.'''
new = '''A capable integration platform can centralize runtime controls, monitoring, security, and reusable technical patterns. I still keep a separate question on the table: who owns the business meaning of the contract and who can decide that a technically successful exchange is also a completed business outcome?

Centralized platform capability does not require centralized ownership of every business decision.'''
text = replace_once(text, old, new, path)
write(path, text)

# Integration service page.
path = "services/sap-integration-architecture.md"
text = read(path)
text = replace_once(
    text,
    '''      <p>The service helps teams choose where integration logic should live, how APIs and events should be versioned, and how much platform lock-in is acceptable. The core principle is simple: keep legal and transactional truth in S/4HANA, and make edge services replaceable through explicit contracts.</p>''',
    '''      <p>I start integration design with ownership, not protocol. I want to know which system owns the business fact, which systems are allowed to derive or copy it, where transformation logic is maintained, and how the process proves completion after a handoff. Only then do I choose the API, event, IDoc, file, or middleware pattern. My bias is to keep authoritative transactional decisions close to the system that owns them and make edge services replaceable through explicit contracts.</p>''',
    path,
)
text = replace_once(
    text,
    '''      <p>The goal is not to prescribe APIs or events as a universal replacement for files, IDocs, or middleware. A stable landscape may retain several patterns if their ownership, contracts, observability, and recovery rules are clear. The costly state is an accidental mix in which every new use case adds another unowned integration path.</p>''',
    '''      <p>I do not treat APIs or events as a maturity badge. A stable landscape can legitimately keep several integration patterns when ownership, contracts, observability, and recovery are explicit. The expensive state is not "old technology" by itself; it is an accidental mix where nobody can explain who owns the contract, how failure is reconciled, or what a safe change looks like.</p>''',
    path,
)
write(path, text)

# AI incident triage article.
path = "_blog/how-to-automate-sap-incident-triage-without-building-an-unreliable-ai.md"
text = read(path)
if "last_modified_at:" not in text.split("---", 2)[1]:
    text = text.replace("date: 2026-07-17\n", "date: 2026-07-17\nlast_modified_at: 2026-08-14\n", 1)
anchor = "A user reports that delivery processing has stopped.\n"
intro = '''### My default boundary

I automate evidence collection aggressively and automate irreversible action conservatively. For incident triage, that means letting automation enrich the ticket, correlate signals, retrieve verified knowledge, and propose ownership while keeping uncertainty visible. I do not give an AI component recovery authority merely because it can produce a plausible diagnosis.

''' + anchor
text = replace_once(text, anchor, intro, path)
write(path, text)

# Procurement scenario: remove false precision, correct posting-vs-payment-block mechanics, and teach the diagnostic path.
path = "scenarios/invoice-verification-three-way-match-delays.md"
text = read(path)
text = re.sub(
    r"^description: .*$",
    'description: "A working diagnostic scenario for delayed or blocked supplier invoices: trace the variance, PO and GR evidence, tolerance logic, and ownership before changing configuration."',
    text,
    count=1,
    flags=re.M,
)
text = text.replace("last_reviewed: 2026-06-09", "last_reviewed: 2026-08-14", 1)

text = replace_section(text, "    <h2>Business pain</h2>", "    <h2>Process context</h2>", '''    <p>A blocked supplier invoice is easy to reduce to an Accounts Payable problem, but the cause often sits earlier in procure-to-pay. A price changed, a receipt is incomplete, the invoice references a different quantity or unit, a tolerance was exceeded, or the inbound data does not match the purchasing document. The operational cost comes from the investigation loop: AP, procurement, receiving, master data, integration, and the supplier each see a different part of the same exception.</p>''', path)
text = replace_section(text, "    <h2>Process context</h2>", "    <h2>Typical symptoms</h2>", '''    <p>In Logistics Invoice Verification, SAP can compare invoice values with purchasing and goods-receipt reference data and evaluate configured tolerances. A variance does not automatically mean that the invoice cannot be posted. Depending on the condition and configuration, the document may be posted but blocked for payment until the blocking reason is reviewed and released. I therefore separate three questions: was the invoice captured, why is payment blocked, and is the underlying variance still valid?</p>
    <p>That distinction changes the investigation. "Invoice failed" is too vague. I want the exact document state, the variance or blocking reason, the PO and receipt history, and the ownership of the business decision needed to resolve it.</p>''', path)
text = replace_section(text, "    <h2>Typical symptoms</h2>", "    <h2>SAP touchpoints</h2>", '''    <ul>
      <li>A queue of invoices waiting for release or clarification rather than a clean flow into payment.</li>
      <li>Recurring price, quantity, timing, or reference-data differences for the same suppliers or purchasing patterns.</li>
      <li>Repeated manual comparison of the purchase order, goods receipt, and invoice before an owner can decide what is valid.</li>
      <li>Supplier escalations or lost payment predictability even though the technical invoice document exists.</li>
      <li>GR/IR reconciliation noise that points to timing or quantity differences elsewhere in the process.</li>
    </ul>''', path)
text = replace_section(text, "    <h2>SAP touchpoints</h2>", "    <h2>Master data / configuration / integration touchpoints</h2>", '''    <ul>
      <li><strong>Invoice document and blocking reason</strong>: establish whether the issue is entry, posting, payment block, or release.</li>
      <li><strong>Purchase order history</strong>: compare ordered, received, and invoiced quantities and values at the relevant item level.</li>
      <li><strong>Goods receipt</strong>: confirm timing, quantity, reversals, and whether the invoice references the expected receipt context.</li>
      <li><strong>Tolerance configuration</strong>: check which variance is evaluated and whether the configured limit reflects the intended business control.</li>
      <li><strong>Release of blocked invoices</strong>: determine whether the blocking reason is still valid before releasing it.</li>
    </ul>''', path)
text = replace_section(text, "    <h2>Master data / configuration / integration touchpoints</h2>", "    <h2>Cost drivers</h2>", '''    <ul>
      <li><strong>Supplier / Business Partner context</strong>: payment, tax, and organizational data can influence processing but should be checked only when the symptom points there.</li>
      <li><strong>Material, purchasing info, and order units</strong>: stale commercial data or inconsistent units can create repeatable differences.</li>
      <li><strong>Purchase-order changes</strong>: quantity or price changes after operational execution can create legitimate reconciliation questions.</li>
      <li><strong>Tax and country-specific rules</strong>: treat these as a separate control domain rather than guessing from an invoice message.</li>
      <li><strong>Inbound invoice integration</strong>: for EDI, IDoc, API, or network scenarios, compare the source payload with what SAP actually received before changing configuration.</li>
    </ul>''', path)
text = replace_section(text, "    <h2>Cost drivers</h2>", "    <h2>Root cause patterns</h2>", '''    <ul>
      <li><strong>Investigation handoffs</strong>: each unresolved variance can bounce between AP, procurement, receiving, integration, and the supplier.</li>
      <li><strong>Payment uncertainty</strong>: a posted but blocked invoice can still miss the intended payment window or cash-discount opportunity.</li>
      <li><strong>Supplier friction</strong>: recurring exceptions consume time on both sides and make status difficult to explain.</li>
      <li><strong>Close and reconciliation effort</strong>: unresolved receipt and invoice differences increase the work needed to understand open balances.</li>
      <li><strong>Bad configuration changes</strong>: loosening a tolerance to reduce ticket volume can remove a valid control instead of fixing the source of the variance.</li>
    </ul>''', path)
text = replace_section(text, "    <h2>Diagnostic workflow</h2>", "    <h2>Solution patterns</h2>", '''    <p>My first-pass diagnostic is deliberately narrow:</p>
    <ol>
      <li><strong>Name the document state</strong>: distinguish entry/posting problems from a payment block or release problem.</li>
      <li><strong>Name the variance</strong>: price, quantity, timing, reference data, tax, or another explicit blocking condition.</li>
      <li><strong>Compare the evidence</strong>: line up the PO item, relevant goods receipt history, invoice values, units, and later document changes.</li>
      <li><strong>Check the control</strong>: identify the tolerance or business rule that produced the block and whether it is behaving as intended.</li>
      <li><strong>Check integration only when relevant</strong>: if the invoice arrived electronically, compare the source payload, mapped values, and SAP document rather than assuming middleware is the cause.</li>
      <li><strong>Assign the decision</strong>: decide whether the next action belongs to AP, procurement, receiving, master data, integration, tax, or a process owner.</li>
      <li><strong>Release only after the reason is understood</strong>: restoring payment flow is not the same as removing the cause of recurrence.</li>
    </ol>''', path)
text = replace_section(text, "    <h2>Solution patterns</h2>", "    <h2>AI / automation / workflow opportunity</h2>", '''    <ul>
      <li><strong>Fix recurring source differences</strong>: correct purchasing data, units, receipt discipline, or inbound mappings when the same variance repeats.</li>
      <li><strong>Tune controls with evidence</strong>: change tolerances only after comparing the intended control with real variance patterns and business risk.</li>
      <li><strong>Make ownership explicit</strong>: route each blocking reason to the team that can make the required business decision, not merely the team that can open the transaction.</li>
      <li><strong>Separate release from prevention</strong>: a safe release process restores flow; a separate root-cause backlog prevents recurrence.</li>
      <li><strong>Add reconciliation signals</strong>: track repeated blocks by reason, supplier, purchasing pattern, and process owner instead of measuring ticket closure alone.</li>
    </ul>''', path)
text = replace_section(text, "    <h2>AI / automation / workflow opportunity</h2>", "    <h2>Related Atlas pages</h2>", '''    <p>AI can help summarize the evidence pack, cluster recurring blocking reasons, and suggest which diagnostic branch to open next. I would keep the actual release decision deterministic and accountable. The useful AI output is not "release this invoice"; it is "here is the variance, here is the supporting document trail, here is what is still unknown, and here is the owner who can decide."</p>''', path)
text = replace_section(text, "    <h2>Public references</h2>", "    <h2>Verification status and limitations</h2>", '''    <ul>
      <li><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/7870b6531de6b64ce10000000a174cb4.html">SAP Help: Blocking Invoices</a> - primary reference for invoice blocking and payment-block behavior.</li>
      <li><a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/af9ef57f504840d2b81be8667206d485/8770b6531de6b64ce10000000a174cb4.html">SAP Help: Setting Tolerances</a> - primary reference for configured tolerance behavior.</li>
      <li><a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/ed84b70c199d4470ae2e5ccb93b2e45b/74497657a11a0522e10000000a44147b.html">SAP Help: Release Blocked Invoices</a> - primary reference for review and release of blocked invoices.</li>
    </ul>''', path)
text = replace_once(
    text,
    '''    <p>This scenario is a structured working hypothesis based on operational patterns observed in SAP AMS support. Specific cost figures, transaction behavior, and configuration details vary by SAP release, industry solution, and custom enhancement. Validate in your own landscape and official SAP documentation before acting on diagnostic recommendations.</p>''',
    '''    <p>This is a structured working scenario built from common support and process-diagnostic patterns. The blocking, tolerance, and release mechanics above were rechecked against public SAP Help on 2026-08-14, while landscape-specific configuration, tax behavior, integrations, extensions, and ownership remain customer-specific. Treat the diagnostic sequence as a professional heuristic, not as a substitute for checking the actual document state and release-specific SAP documentation.</p>''',
    path,
)
write(path, text)
