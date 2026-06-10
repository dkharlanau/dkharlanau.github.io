---
layout: default
title: "Quality Rules — What Makes a Skill Hub Page Good or Bad"
description: "Quality criteria for Skill Hub pages. Good page criteria, weak page warning signs, anti-generic writing rules, public-safety rules, agent-readiness rules, artifact-readiness rules, and link quality rules."
permalink: /skill-hub/quality-rules/
last_modified_at: 2026-06-09
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li aria-current="page">Quality Rules</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Foundation</p>
  <h1>Quality Rules</h1>
  <p class="lead">What makes a Skill Hub page good or bad. Use these rules when creating, reviewing, or editing skill pages.</p>

  <section>
    <h2>Good page criteria</h2>
    <p>A good Skill Hub page must satisfy all of these:</p>
    <ul>
      <li><strong>Actionable:</strong> A reader can follow the working method and produce output tomorrow.</li>
      <li><strong>Situation-specific:</strong> It names real work situations, not abstract topics.</li>
      <li><strong>Question-driven:</strong> It provides specific diagnostic questions, not generic prompts.</li>
      <li><strong>Rule-based:</strong> It includes "If X, then Y" decision rules.</li>
      <li><strong>Template-equipped:</strong> It includes at least one copy-paste-ready template.</li>
      <li><strong>Agent-ready:</strong> It has an Agent Instructions section with explicit do's and don'ts.</li>
      <li><strong>Honest:</strong> It states limitations and verification status.</li>
      <li><strong>Linked:</strong> It connects to related skills and Atlas pages with valid local links.</li>
      <li><strong>Mistake-aware:</strong> It lists common mistakes with consequences.</li>
      <li><strong>Quality-checked:</strong> It includes a verifiable quality checklist for its own output.</li>
    </ul>
  </section>

  <section>
    <h2>Weak page warning signs</h2>
    <p>These are signals that a page needs rewriting:</p>
    <ul>
      <li>The page starts with a definition of the concept.</li>
      <li>The "When to use" section has only one vague bullet like "when data quality is important."</li>
      <li>The working method has fewer than 5 steps or the steps are not sequential.</li>
      <li>There are no decision rules.</li>
      <li>The template is missing or is just a heading with no structure.</li>
      <li>The agent instructions are missing or say "use your best judgment."</li>
      <li>The page reads like a textbook chapter or a blog post.</li>
      <li>The page contains motivational language like "unlock the power of data."</li>
      <li>The page claims to be "comprehensive" or "complete."</li>
      <li>All examples are generic ("a company," "a system") instead of specific ("SAP S/4 sales order creation," "MDG business partner workflow").</li>
    </ul>
  </section>

  <section>
    <h2>Anti-generic writing rules</h2>
    <p>These rules prevent the most common quality failure: generic framework summaries.</p>
    <table>
      <thead>
        <tr>
          <th>Do not write</th>
          <th>Write instead</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>"Data governance is important because..."</td>
          <td>"If ownership is unclear, produce an ownership matrix before proposing automation."</td>
        </tr>
        <tr>
          <td>"Event-driven architecture provides loose coupling..."</td>
          <td>"Decide whether an event should exist, who owns it, what its contract is, and how failures are monitored."</td>
        </tr>
        <tr>
          <td>"Requirements elicitation is the process of..."</td>
          <td>"Turn vague stakeholder complaints into requirements, assumptions, risks, and acceptance criteria."</td>
        </tr>
        <tr>
          <td>"Stakeholder analysis helps identify key people..."</td>
          <td>"Map who has decision rights, who has information, who will resist, and who is missing from the room."</td>
        </tr>
        <tr>
          <td>"A root cause is the fundamental reason..."</td>
          <td>"Separate symptom, root cause, and prevention gap. If you only fix the symptom, the defect recurs."</td>
        </tr>
        <tr>
          <td>"Master data management ensures consistency..."</td>
          <td>"Decide which system creates the record, which system can change it, and how duplicates are detected."</td>
        </tr>
      </tbody>
    </table>
  </section>

  <section>
    <h2>Public-safety rules</h2>
    <p>Every Skill Hub page must be safe to publish:</p>
    <ul>
      <li><strong>No private material:</strong> Do not publish client names, internal project notes, proprietary code, or private correspondence.</li>
      <li><strong>No private paths:</strong> Do not reference internal file paths, server names, or network locations.</li>
      <li><strong>No copyrighted text:</strong> Do not copy passages from DAMA-DMBOK, BABOK, TOGAF, or other copyrighted frameworks. Paraphrase in your own words.</li>
      <li><strong>No fake authority:</strong> Do not claim official framework certification, endorsement, or authority.</li>
      <li><strong>No fake citations:</strong> Do not invent sources, page numbers, or edition references.</li>
      <li><strong>No vendor bias:</strong> Do not promote one vendor as the only solution unless the skill explicitly covers that vendor's product.</li>
      <li><strong>No invented data:</strong> Do not make up statistics, survey results, or case study details.</li>
    </ul>
  </section>

  <section>
    <h2>Agent-readiness rules</h2>
    <p>Every skill page must be usable by an AI agent:</p>
    <ul>
      <li>The <strong>Agent Instructions</strong> section is mandatory.</li>
      <li>Agent instructions must specify what context to gather before applying the skill.</li>
      <li>Agent instructions must tell the agent what artifacts to produce.</li>
      <li>Agent instructions must list things to avoid (generic language, fake certainty, skipping steps).</li>
      <li>Agent instructions must explain how to handle missing information.</li>
      <li>The working method must be sequential and unambiguous. An agent should not need to guess the order.</li>
      <li>Decision rules must be explicit. "Use judgment" is not a decision rule.</li>
      <li>Templates must be copy-paste ready with clear fill-in-the-blank fields.</li>
    </ul>
  </section>

  <section>
    <h2>Artifact-readiness rules</h2>
    <p>Every skill must produce usable artifacts:</p>
    <ul>
      <li>At least one template must be included directly on the skill page.</li>
      <li>Templates must have a clear artifact name and ID convention.</li>
      <li>Templates must include all fields needed for the artifact to be useful.</li>
      <li>Templates must distinguish between required and optional fields.</li>
      <li>Deliverables must be named and described, not just listed as nouns.</li>
      <li>Quality checklists must be verifiable yes/no items.</li>
    </ul>
  </section>

  <section>
    <h2>Link quality rules</h2>
    <p>Links must be valid and purposeful:</p>
    <ul>
      <li>All local links must resolve to existing pages. Do not invent links.</li>
      <li>Do not create broken links. Verify before committing.</li>
      <li>Do not over-link. Two to five related skills is enough.</li>
      <li>Only link to Atlas pages that add real diagnostic or conceptual value.</li>
      <li>External links must have a clear purpose and be verifiable.</li>
      <li>Do not link to every page in the same group. Link to the most relevant ones.</li>
    </ul>
  </section>

  <section>
    <h2>Review checklist for new skill pages</h2>
    <p>Before a skill page is accepted:</p>
    <ul>
      <li>[ ] Page follows the <a href="/skill-hub/skill-page-template/">Skill Page Template</a> structure.</li>
      <li>[ ] Page passes all good page criteria above.</li>
      <li>[ ] Page has no weak page warning signs.</li>
      <li>[ ] Page follows anti-generic writing rules.</li>
      <li>[ ] Page passes public-safety rules.</li>
      <li>[ ] Page passes agent-readiness rules.</li>
      <li>[ ] Page passes artifact-readiness rules.</li>
      <li>[ ] All local links are valid.</li>
      <li>[ ] No private material is exposed.</li>
      <li>[ ] No copyrighted text is copied.</li>
      <li>[ ] Verification status and limitations are stated.</li>
    </ul>
  </section>
</article>
