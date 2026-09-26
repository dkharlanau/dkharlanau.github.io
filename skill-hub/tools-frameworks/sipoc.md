---
layout: default
title: "SIPOC — Process Boundary Map"
description: "How to use SIPOC to define suppliers, inputs, process, outputs, and customers before detailed process analysis."
permalink: /skill-hub/tools-frameworks/sipoc/
last_modified_at: 2026-09-26
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/skill-hub/">Skill Hub</a></li><li><a href="/skill-hub/tools-frameworks/">Tools &amp; Frameworks</a></li><li aria-current="page">SIPOC</li></ol></nav>
<article class="section note-detail atlas-page">
<p class="eyebrow">Process framing tool</p><h1>SIPOC</h1>
<p class="lead">Use SIPOC before detailed process modeling when the team cannot agree where the process starts, what enters it, what leaves it, or who consumes the result.</p>

<section><h2>The five views</h2>
<table class="study-table"><thead><tr><th>View</th><th>Question</th></tr></thead><tbody>
<tr><td>Supplier</td><td>Who or what provides the input?</td></tr>
<tr><td>Input</td><td>What must exist before the process can work?</td></tr>
<tr><td>Process</td><td>What are the 4–7 high-level steps?</td></tr>
<tr><td>Output</td><td>What result leaves the process?</td></tr>
<tr><td>Customer</td><td>Who or what uses the output?</td></tr>
</tbody></table>
</section>

<section><h2>Use it when</h2><ul>
<li>A process workshop starts with people arguing about scope.</li>
<li>A failure may come from an upstream input rather than the process itself.</li>
<li>A downstream team reports “bad output” but the producing team does not know the acceptance conditions.</li>
<li>You need a quick end-to-end frame before BPMN, value-stream analysis, or detailed requirements work.</li>
</ul></section>

<section><h2>How to run it</h2>
<ol>
<li>Name the process using a verb and object, such as “Create customer master”.</li>
<li>Define the trigger and end condition.</li>
<li>Write 4–7 high-level process steps.</li>
<li>List the outputs and the consumers of each output.</li>
<li>List the inputs required to produce those outputs.</li>
<li>Trace each input to its supplier.</li>
<li>Mark quality criteria, missing ownership, and uncertain assumptions.</li>
</ol></section>

<section><h2>SAP example</h2>
<p>For “Create Sales Order”, suppliers may include the customer, master-data team, pricing configuration, and ATP data sources. Inputs include customer PO, business partner data, material data, pricing conditions, and requested dates. Outputs include the sales order, confirmation, demand, and follow-on document readiness. Customers include sales users, warehouse planning, finance, and the external customer.</p>
</section>

<section><h2>Decision rules</h2><ul>
<li>If the team needs gateways, exceptions, or parallel flow, move from SIPOC to BPMN.</li>
<li>If an input has no clear supplier, you have found an ownership gap.</li>
<li>If an output has no customer or consuming purpose, challenge why it exists.</li>
<li>If the “Process” column contains more than about seven steps, the map is becoming a detailed process model.</li>
</ul></section>

<section><h2>Copyable template</h2>
<pre><code>| Supplier | Input | High-level process | Output | Customer |
|---|---|---|---|---|
| Customer | Purchase order | 1. Capture demand | Sales order | Sales |
| Master data team | BP / material data | 2. Validate data | Confirmation | Customer |
| Pricing owner | Conditions | 3. Price and check | Demand signal | Planning |</code></pre>
</section>

<section><h2>Pair it with</h2><ul>
<li><a href="/skill-hub/business-analysis/process-analysis-working-skill/">Process Analysis</a></li>
<li><a href="/skill-hub/tools-frameworks/bpmn/">BPMN</a></li>
<li><a href="/skill-hub/tools-frameworks/raci/">RACI</a></li>
</ul></section>

<section><h2>Verification status and limitations</h2><p>SIPOC is a high-level framing tool. It should not be treated as a substitute for detailed process logic, controls, business rules, or system behavior.</p></section>
</article>
