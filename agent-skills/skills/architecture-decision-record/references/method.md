# Architecture Decision Record — Detailed Method

## The Neutral-Question Method

The core of this skill is documenting a decision with full context, honest evaluation, and clear consequences. The most common failure is framing the question to favor one answer.

### Step 1: Decision Question Formulation

Write one sentence that captures exactly what must be decided. The question must be neutral:

Bad: "Why should we use asynchronous events instead of synchronous APIs?"
Good: "How should customer master data be distributed to downstream systems?"

Test for neutrality:
- Does the question assume a preferred answer? If yes, rewrite.
- Would someone who prefers a different answer accept this question as fair? If no, rewrite.

### Step 2: Context Documentation

Explain the situation that forces this decision now. Include:
- **Business drivers:** what changed that makes this decision necessary
- **Constraints:** budget, timeline, regulatory, skill availability
- **Deadlines:** when the decision must be made
- **Dependencies:** other decisions or projects that affect this one

Do not omit constraints that favor one option. Constraints are facts, not bias.

### Step 3: Evaluation Criteria Definition

List 3–5 criteria that will be used to compare options. Common criteria:
- Cost (CAPEX and OPEX)
- Time to implement
- Risk (technical, operational, business)
- Maintainability
- Scalability
- Compliance
- Team skill fit

Weight criteria if the team agrees on relative importance. Document the weighting rationale.

### Step 4: Option Description

Describe each option at a consistent level of detail. Include:
- **At least two viable options**
- A "do nothing" or status quo option where relevant
- Description of what the option entails
- Pros, cons, and risks for each option

Be honest about drawbacks of the option you prefer. If you cannot list a con, you have not thought hard enough.

### Step 5: Option Evaluation

Evaluate each option against each criterion. Use a matrix:

| Criterion | Option A | Option B | Option C |
|-----------|----------|----------|----------|
| Cost | High | Medium | Low |
| Time | 6 months | 3 months | 1 month |
| Risk | Low | Medium | High |

Document the reasoning, not just the rating.

### Step 6: Decision Recording

State which option is chosen and why. Cite:
- The criteria that tipped the balance
- The specific trade-offs that were accepted
- Any constraints that eliminated other options

### Step 7: Consequence Documentation

List both positive and negative consequences:
- **Positive:** what we gain, enable, or improve
- **Negative:** technical debt, new dependencies, skill gaps, capability loss

Do not omit negative consequences. They are the most valuable part of the ADR for future teams.

### Step 8: Reversibility Assessment

Rate the decision:
- **Easily reversible:** can be changed within days with minimal cost
- **Moderately reversible:** can be changed within months with moderate cost
- **Irreversible:** would require major rework, data migration, or contract termination

Describe what would be required to reverse the decision. Include data migration, contract terms, skill retraining, and integration rework.

### Step 9: Ownership and Review Date

Name the person or role accountable for this decision. Set a review date based on:
- Volatility of the context: 6 months for fast-changing environments, 1 year for stable ones
- Reversibility: irreversible decisions need more frequent review
- Dependency on other decisions: review when dependencies change

### Step 10: Related Decision Linking

Reference other ADRs that this decision depends on or affects. Update the status of superseded ADRs.

## Common ADR Pitfalls

1. **Recording only the chosen option.** Future teams revisit the same question because they do not know why alternatives were discarded.
2. **Framing the question to favor one answer.** The ADR becomes rationalization, not documentation.
3. **Omitting negative consequences.** The team is surprised by technical debt or operational burden that was known but not communicated.
4. **Writing ADRs for trivial decisions.** The decision log becomes noise; important decisions are lost.
5. **Never revisiting decisions.** An ADR accepted three years ago under different constraints continues to constrain the architecture.
