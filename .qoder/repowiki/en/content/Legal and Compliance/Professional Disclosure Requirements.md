# Professional Disclosure Requirements

<cite>
**Referenced Files in This Document**   
- [professional-disclosure.md](file://legal/professional-disclosure.md)
- [resume.yml](file://_data/resume.yml)
- [responsible-ai.md](file://legal/responsible-ai.md)
- [credentials.html](file://_includes/sections/credentials.html)
- [home.yml](file://_data/home.yml)
</cite>

## Table of Contents
1. [Purpose of Professional Disclosure](#purpose-of-professional-disclosure)
2. [Core Disclosure Elements](#core-disclosure-elements)
3. [Credibility and Trust in Professional Services](#credibility-and-trust-in-professional-services)
4. [Disclosure Requirements by Engagement Type](#disclosure-requirements-by-engagement-type)
5. [Standard Disclosure Statement Templates](#standard-disclosure-statement-templates)
6. [Alignment with Industry Standards for SAP Consultants](#alignment-with-industry-standards-for-sap-consultants)
7. [AI-Assisted Content and Responsible AI Integration](#ai-assisted-content-and-responsible-ai-integration)

## Purpose of Professional Disclosure

Transparent disclosure of professional affiliations, certifications, employment history, and potential conflicts of interest is a foundational practice for maintaining integrity in consulting engagements. This disclosure ensures that clients, partners, and audiences can assess the context and potential influences behind recommendations, analyses, and public statements. By openly sharing employment relationships, certification status, and professional networks, consultants uphold accountability and enable informed decision-making by stakeholders.

The primary objectives of professional disclosure include:
- Establishing transparency about organizational affiliations that may influence project governance
- Clarifying the scope of independent versus corporate engagements
- Preventing conflicts of interest through upfront declaration
- Demonstrating compliance with ethical consulting standards
- Supporting auditability and traceability of professional claims

**Section sources**
- [professional-disclosure.md](file://legal/professional-disclosure.md#L1-L10)

## Core Disclosure Elements

The following elements must be disclosed in all professional contexts to ensure full transparency:

### Employment History
Current and recent employment relationships must be clearly stated, including employer name, role title, and engagement model. For engagements conducted through a corporate entity, the applicable governance frameworks must be identified.

**Section sources**
- [professional-disclosure.md](file://legal/professional-disclosure.md#L12-L18)
- [resume.yml](file://_data/resume.yml#L4-L440)

### Affiliations and Certifications
All active professional affiliations, community memberships, and certifications must be disclosed. This includes:
- Vendor-specific certifications (e.g., SAP credentials)
- Participation in technical working groups or architecture forums
- Membership in professional communities of practice

Certifications are dynamically tracked in the `resume.yml` file and displayed via the credentials section on the homepage, ensuring up-to-date representation of current qualifications.

**Section sources**
- [professional-disclosure.md](file://legal/professional-disclosure.md#L20-L25)
- [resume.yml](file://_data/resume.yml#L380-L420)
- [credentials.html](file://_includes/sections/credentials.html#L1-L25)

### Potential Conflicts of Interest
Any situation that could reasonably be perceived as a conflict between professional responsibilities and personal interests must be disclosed prior to engagement. This includes overlapping client engagements, financial incentives, or relationships that might influence objectivity.

**Section sources**
- [professional-disclosure.md](file://legal/professional-disclosure.md#L27-L31)

## Credibility and Trust in Professional Services

Professional disclosure directly supports credibility by enabling stakeholders to evaluate the background and potential biases of a consultant. When affiliations and qualifications are transparently shared, clients can:
- Validate expertise through verifiable certifications
- Understand the organizational context of service delivery
- Assess independence and objectivity in technology recommendations

The resume.yml file serves as the authoritative source for disclosed information, with machine-readable formats (YAML, JSON) provided in the `/ai/` directory to support automated verification and integration with AI systems. This structured approach ensures consistency across platforms and reduces the risk of misrepresentation.

Public display of credentials on the homepage—powered by `_data/home.yml` and rendered through `credentials.html`—further reinforces trust by providing immediate access to verified professional data.

**Section sources**
- [resume.yml](file://_data/resume.yml#L1-L440)
- [home.yml](file://_data/home.yml#L1-L55)
- [credentials.html](file://_includes/sections/credentials.html#L1-L25)

## Disclosure Requirements by Engagement Type

### Client Engagements
Prior to initiating any client engagement, the following must be disclosed:
- Current employment status and primary employer
- Any existing client relationships that could create overlap
- Technology recommendations that are governed by corporate frameworks
- Use of AI tools in analysis or documentation (linked to responsible-ai.md)

**Section sources**
- [professional-disclosure.md](file://legal/professional-disclosure.md#L12-L31)

### Public Speaking
When participating in conferences, webinars, or panel discussions, speakers must:
- State their current employer and role
- Disclose any sponsored content or vendor partnerships
- Indicate if opinions expressed are personal or represent organizational positions
- Reference the professional disclosure page for full transparency

**Section sources**
- [professional-disclosure.md](file://legal/professional-disclosure.md#L1-L35)

### Published Content
All articles, whitepapers, or technical documentation must include:
- Author affiliation and employment context
- Disclosure of AI-assisted content creation (when applicable)
- Links to the full professional disclosure and responsible AI statements
- Timestamps indicating when certifications or roles were current

**Section sources**
- [professional-disclosure.md](file://legal/professional-disclosure.md#L1-L35)
- [responsible-ai.md](file://legal/responsible-ai.md#L1-L31)

## Standard Disclosure Statement Templates

### General Professional Disclosure
"I am employed as a System Analyst and Senior SAP Order-to-Cash Consultant at EPAM Systems. Independent collaborations are scoped transparently to avoid conflicts with EPAM responsibilities. A full record of certifications and professional history is available at [Professional Disclosure](https://dkharlanau.github.io/legal/professional-disclosure/)."

### Speaking Engagement Disclosure
"I currently serve as a Senior SAP Consultant at EPAM Systems. The views expressed in this presentation are my own and do not necessarily reflect the views of EPAM Systems. My full professional background and disclosure statement can be found at [Professional Disclosure](https://dkharlanau.github.io/legal/professional-disclosure/)."

### AI-Assisted Content Disclosure
"This content was developed with assistance from AI tools for drafting and analysis. All technical recommendations have been reviewed and validated by me as a certified SAP consultant. AI usage follows the guidelines in my [Responsible AI Statement](https://dkharlanau.github.io/legal/responsible-ai/)."

**Section sources**
- [professional-disclosure.md](file://legal/professional-disclosure.md#L1-L35)
- [responsible-ai.md](file://legal/responsible-ai.md#L1-L31)

## Alignment with Industry Standards for SAP Consultants

This disclosure policy aligns with recognized best practices for SAP consultants and independent professionals, including:
- SAP Partner Code of Conduct requirements for transparency
- ISACA and IEEE guidelines for technology ethics
- PMI standards for conflict of interest management
- Open Group principles for vendor-neutral consulting

By maintaining a clean core approach to S/4HANA implementations and avoiding vendor lock-in, the disclosed methodology supports industry trends toward composable ERP and open integration. Certification tracking through SAP and third-party platforms ensures adherence to evolving technical standards.

The policy also reflects EPAM Systems' governance frameworks, which emphasize compliance, security, and ethical delivery in all client engagements.

**Section sources**
- [professional-disclosure.md](file://legal/professional-disclosure.md#L1-L35)
- [resume.yml](file://_data/resume.yml#L380-L420)

## AI-Assisted Content and Responsible AI Integration

When AI tools are used in content creation, automation, or analysis, this must be explicitly disclosed in accordance with the [Responsible AI Statement](file://legal/responsible-ai.md). Key requirements include:
- Human review and validation of all AI-generated outputs
- Documentation of data sources and prompt engineering practices
- Compliance with data minimization and security protocols
- Retention of accountability for final deliverables

The `/ai/` directory provides machine-readable versions of the resume (YAML, JSON) and LLM persona (LLM.txt) to enable transparent AI interactions while maintaining control over professional representation.

Linking disclosure practices to responsible-ai.md ensures consistency across digital platforms and reinforces the principle that AI serves as an assistive tool under human oversight.

**Section sources**
- [responsible-ai.md](file://legal/responsible-ai.md#L1-L31)
- [professional-disclosure.md](file://legal/professional-disclosure.md#L1-L35)
- [resume.yml](file://_data/resume.yml#L1-L440)