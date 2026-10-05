# Public workspace strategy

Last reviewed: 2026-10-05.

## Positioning

The site is the personal, non-commercial SAP and AI workspace of **Dzmitryi Kharlanau, Senior SAP Consultant at EPAM Systems**.

It is not an independent consulting business, agency, or commercial service channel. Employer and client work stays private. Public material is limited to reusable knowledge, practical engineering, learning material, open-source tools, synthetic examples, and source-backed research.

## English entry points only

The public site uses English entry points. Do not recreate localized home pages or duplicate the same positioning across language folders unless this is explicitly requested later.

## Four primary routes

The homepage should answer four questions.

| Route | User need | Canonical entry |
|---|---|---|
| Private boundary | What is intentionally not public? | `/legal/professional-disclosure/` |
| Knowledge Base | Where can I learn or find a durable explanation? | `/knowledge/` |
| Practical Setup | Where can I run or reproduce a difficult solution? | `/lab/` |
| Technology Watch | What changed in SAP, AI, integration, data, or engineering? | `/research/` |

Profile, Labs, Frameworks, and Machine remain important supporting surfaces. They are not commercial funnels.

## Private boundary

Never publish client names, project details, tickets, credentials, production data, proprietary system information, internal documents, or private corpus content.

Public examples should be generic, synthetic, or based on public sources. If a useful method came from professional experience, publish the reusable pattern without exposing private context.

## Knowledge Base

The Knowledge Base owns durable explanations and reusable diagnostic material. Use Atlas, Scenarios, Journal, Notes, and linked Labs instead of creating duplicate topic pages.

Learning and assessment material remains practice material. It must not be presented as an official SAP exam dump, hiring guarantee, or certification guarantee.

## Practical Setup

`/lab/` is the task-oriented Enterprise Engineering Toolkit. Prefer a runnable browser surface when possible, then a reproducible CLI path, then source code.

The practical layer includes Process as Code, Decision Tables as Code, Interface as Code, Mapping as Code, Reconciliation as Code, data relationship maps, transformation and cutover graphs, architecture composition, visual workbench patterns, and SAP agentic operations.

A practical setup demonstrates a method. It does not prove production adoption, customer approval, or universal runtime compatibility.

## Technology Watch

Use Research, Radar, and News to track fast-moving evidence. Separate current signals from durable guidance.

A technology watch item should answer:
1. What changed?
2. Why may it matter?
3. What evidence supports it?
4. What should be tested before adoption?
5. What remains uncertain?

Do not turn a vendor announcement into a recommendation without checking fit, controls, integration, cost, and operational impact.

## EPAM Systems employment

The profile, CV, machine identity, and homepage should clearly state the current professional context: **Senior SAP Consultant at EPAM Systems**.

The public site is personal. It must not imply that a page, tool, opinion, or example is an EPAM offer, EPAM deliverable, SAP statement, or client statement unless a page explicitly and validly says so.

## Legacy service URLs

Existing `/services/*` URLs are retained for link compatibility and technical reference. They must be `noindex`, show the non-commercial reference notice, and stay outside active navigation and AI routing.

Do not add pricing, booking, paid review, paid assessment, implementation offer, lead-generation copy, or independent contract terms. No checkout or payment flow belongs on this site.

Useful technical content from legacy pages may be migrated over time into Knowledge, Practical Lab, Labs, Frameworks, or Technology Watch.

## AI and machine-readable context

AI-facing files must carry the same positioning as the human site:

- `/ai/identity.json` owns the canonical public role and employment context.
- `/ai/resume.json` and `/ai/resume.yml` own the public CV record.
- `/ai/focus-map.json` owns the four-route model and private boundary.
- discovery routes should point to public knowledge, labs, practical tools, or research rather than commercial service pages.
- generated retrieval artifacts inherit publication state; noindex or unverified content must not be promoted as reviewed evidence.

## Success criteria

The change is complete when:

- the homepage leads with Private boundary, Knowledge Base, Practical Setup, and Technology Watch;
- EPAM Systems employment is clear on Home, About, CV, identity data, and resume data;
- active navigation has no commercial Services entry;
- homepage structured data does not describe an OfferCatalog or ProfessionalService;
- legacy service pages are noindex and visibly reference-only;
- AI discovery does not route users to a commercial offer;
- tests and Jekyll build pass;
- public links remain valid.
