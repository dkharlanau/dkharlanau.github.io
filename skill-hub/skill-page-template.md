---
layout: default
title: "Skill Page Template — Standard Structure for Skill Hub Pages"
description: "The standard template for all Skill Hub pages. Defines the required sections, their purpose, and quality criteria. Use this when creating or reviewing skill pages."
permalink: /skill-hub/skill-page-template/
last_modified_at: 2026-06-09
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li aria-current="page">Skill Page Template</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Foundation</p>
  <h1>Skill Page Template</h1>
  <p class="lead">The standard structure for every Skill Hub page. All skill pages must follow this template. Reviewers use this to judge completeness.</p>

  <section>
    <h2>Template structure</h2>
    <p>Every skill page must include the following sections in this order:</p>

    <h3>1. What this skill is for</h3>
    <p>Explain the practical job-to-be-done. One to three sentences. Avoid generic definitions. Focus on what the user will be able to do after applying this skill.</p>
    <p><strong>Good:</strong> "This skill helps identify why bad data exists, where it entered the lifecycle, what business process it affects, who owns the correction, and what prevention control is required."</p>
    <p><strong>Bad:</strong> "Data quality is important because organizations need accurate data."</p>

    <h3>2. When to use this skill</h3>
    <p>List real project situations where this skill is needed. Use bullet points. Each bullet should describe a recognizable work moment.</p>
    <p><strong>Good:</strong> "Use it when sales orders are blocked by incomplete customer data."</p>
    <p><strong>Bad:</strong> "Use it when data quality is a concern."</p>

    <h3>3. Real work situations</h3>
    <p>Use concrete examples from enterprise, SAP, data, integration, or operations work. Two to four examples. Include enough detail that a reader recognizes their own situation.</p>
    <p>Each example should include: the symptom, the system or process, the stakeholder, and the business consequence.</p>

    <h3>4. Inputs required</h3>
    <p>List documents, systems, logs, data samples, stakeholders, decisions, diagrams, tickets, or examples needed before the skill can be applied. Be specific. If an input is optional, label it optional.</p>

    <h3>5. Questions to ask</h3>
    <p>Provide strong diagnostic questions. Avoid generic consultant questions like "What are your pain points?" Instead, ask specific questions that reveal structure, ownership, and causality.</p>
    <p><strong>Good:</strong> "Which field is missing, and which business process fails when it is missing?"</p>
    <p><strong>Bad:</strong> "What data quality issues are you experiencing?"</p>

    <h3>6. Working method</h3>
    <p>Step-by-step workflow. Numbered list. Each step should be actionable. Make it usable tomorrow. A person with moderate domain knowledge should be able to follow the steps and produce output.</p>
    <p>Include substeps where needed. Label decision points clearly.</p>

    <h3>7. Decision rules</h3>
    <p>Include rules in the form: "If X, then Y." Or: "If condition A, do B. If condition C, do D instead."</p>
    <p>Decision rules are the core of a skill. They turn judgment into repeatable logic.</p>
    <p><strong>Examples:</strong></p>
    <ul>
      <li>If ownership is unclear, produce an ownership matrix before proposing automation.</li>
      <li>If data defects recur, fix upstream validation, not only existing records.</li>
      <li>If requirements are vague, separate need, assumption, rule, constraint, and acceptance criterion.</li>
      <li>If only a few records are affected and the rule is clear, correct records through the governed process.</li>
      <li>If many records are affected, prepare mass correction with validation and approval.</li>
    </ul>

    <h3>8. Deliverables</h3>
    <p>List artifacts the skill should produce. Name each artifact. Describe what it contains. Link to templates where available.</p>

    <h3>9. Templates</h3>
    <p>Include at least one compact reusable Markdown template directly in the page. The template should be copy-paste ready. Fill-in-the-blank format. Include example values in comments where helpful.</p>
    <p>Templates may also reference the <a href="/skill-hub/artifact-templates/">Artifact Templates</a> page for longer formats.</p>

    <h3>10. Quality checklist</h3>
    <p>Explain how to judge whether the output is good. Use a checklist format. Each item should be verifiable yes/no.</p>
    <p><strong>Good:</strong> "Every defect has a classified root cause type."</p>
    <p><strong>Bad:</strong> "The analysis is thorough."</p>

    <h3>11. Common mistakes</h3>
    <p>Explain practical mistakes people and agents make when using this skill. Be specific. Include the mistake and the consequence.</p>
    <p><strong>Good:</strong> "Mistake: treating the symptom as the root cause. Consequence: the defect recurs because the upstream validation was never fixed."</p>
    <p><strong>Bad:</strong> "Not following the process."</p>

    <h3>12. Agent instructions</h3>
    <p>This section is mandatory. It must tell an AI agent exactly how to use the skill.</p>
    <p>Include:</p>
    <ul>
      <li>What context the agent must gather before applying the skill.</li>
      <li>How to separate facts from assumptions.</li>
      <li>What artifacts to produce.</li>
      <li>What to avoid (generic language, fake certainty, skipping steps).</li>
      <li>How to handle missing information.</li>
      <li>How to link to Atlas diagnostics if applicable.</li>
    </ul>

    <h3>13. Related skills</h3>
    <p>Use valid local links only. Link to other Skill Hub pages that are commonly used together. Two to five links. Do not link every page to everything.</p>

    <h3>14. Related Atlas pages</h3>
    <p>Link to existing Atlas pages where useful. Do not invent links. Do not create broken links. Do not over-link. Two to five links. Only link when the Atlas page adds diagnostic or conceptual depth.</p>

    <h3>15. Verification status and limitations</h3>
    <p>Be honest. State that this is a public working interpretation, not official framework documentation. Note any known gaps, version dependencies, or areas where the skill is incomplete.</p>
  </section>

  <section>
    <h2>Front matter conventions</h2>
    <p>All skill pages use this front matter pattern:</p>
    <pre><code>---
layout: default
title: "&lt;Skill Name&gt;"
description: "&lt;One-line practical description&gt;"
permalink: /skill-hub/&lt;group&gt;/&lt;slug&gt;/
last_modified_at: YYYY-MM-DD
status: reviewed
verified: true
---</code></pre>
  </section>

  <section>
    <h2>Quality gate</h2>
    <p>A skill page is acceptable only if it helps a real person or AI agent perform a real task better. A page is not acceptable if it only explains a concept.</p>
    <p>Before marking a skill page complete, verify:</p>
    <ul>
      <li>Does it help someone do work?</li>
      <li>Does it include concrete situations?</li>
      <li>Does it include specific questions?</li>
      <li>Does it include a workflow?</li>
      <li>Does it include decision rules?</li>
      <li>Does it include a template?</li>
      <li>Does it include agent instructions?</li>
      <li>Does it avoid generic textbook language?</li>
      <li>Does it avoid fake official framework claims?</li>
      <li>Are all links valid?</li>
    </ul>
  </section>
</article>
