# Operational Knowledge Capture — Detailed Method

## The Immediate-Capture Method

The core of this skill is documenting operational knowledge while it is fresh, in a form that the next person can actually use. Memory decays fast; capture within 24 hours of resolution.

### Step 1: Immediate Capture Timing

Schedule 15 minutes after every non-trivial incident to document. Do not wait for a formal request or a quiet afternoon.

Capture triggers:
- Resolution took more than 30 minutes to find
- Same symptom has occurred twice
- Fix involves a workaround for a known limitation
- Fix requires access to a restricted system
- Fix involves a custom program or enhancement

### Step 2: Situation Recording

Document what was happening:
- Which system, client, module
- Which process, which users
- Which time window
- Urgency and business impact

Example: "Production SAP S/4, client 100, SD module, sales order creation process, 14:00–16:00, 20 users blocked, revenue impact estimated at $2,000/hour."

### Step 3: Resolution Step Recording

Document step by step:
- Transaction codes
- Program names
- Table names
- Configuration paths
- Exact values entered

Assume the reader has moderate SAP knowledge but no context about this specific landscape.

Bad: "We fixed the IDoc."
Good: "Run BD87 for IDoc number 12345. Check status 51. Open WE19, copy the IDoc, modify segment E1EDKA1 field PARVW to 'WE'. Post the modified IDoc. Verify in WE02 that status changes to 53."

### Step 4: Causal Explanation Recording

Explain why the fix worked. This is the difference between a runbook and a cheat sheet.

Bad: "We ran program Z_CUSTOMER_FIX and it worked."
Good: "Program Z_CUSTOMER_FIX updates the customer credit segment table KNKK when the credit management area is missing. The missing credit segment was causing the credit check to bypass, which allowed orders to be created without credit validation. The program inserts the missing KNKK record with default values and triggers a re-evaluation of the credit limit."

### Step 5: Failed Attempt Recording

Document what was tried that did not work:
- Wrong paths
- False assumptions
- Dead ends
- Near misses

This prevents the next person from repeating the same two hours of dead ends.

Example: "We initially tried running program Z_CUSTOMER_FIX with parameter P_DATE = yesterday, but this only updates records created after that date. The affected customers were created last week, so the parameter had to be set to last Monday."

### Step 6: Preconditions and Limitations

Define when this knowledge applies:
- System version
- Client
- Module
- Data state
- Specific error message pattern

Define what it does not cover:
- Different error messages
- Different system versions
- Different modules
- Edge cases where the fix fails

### Step 7: Verification Method

Define how the next person confirms the procedure is still valid:
- Which transaction to check
- Which report to run
- Which value to verify
- How often to re-verify

### Step 8: Owner and Review Date

Name the person who maintains this knowledge. Set a review date:
- 3 months for volatile areas (frequent patches, active development)
- 6 months for stable areas
- Patch release date if the knowledge is a workaround for a known bug

### Step 9: Discoverability

Store the note where people look for help:
- Ticket system (link in resolved ticket)
- Wiki or knowledge base
- Runbook repository
- Shared drive with search indexing

Tag with:
- Symptom keywords
- Error message text
- Transaction codes
- Program names

### Step 10: Related Knowledge Linking

Connect to:
- Other capture notes
- Runbooks
- Atlas pages
- Ticket histories
- Related incidents

Build a network, not isolated documents.

## Common Knowledge Capture Pitfalls

1. **Documenting only the solution, not the context.** The next person applies the fix to the wrong situation.
2. **Writing knowledge in private notes or local files.** When the author leaves, the knowledge leaves.
3. **Not documenting failed attempts.** The next person repeats the same dead ends.
4. **Generalizing from one incident without verification.** The note claims to apply to all clients but only works in one.
5. **Never reviewing or retiring old knowledge.** A procedure that worked in ECC 6.0 fails in S/4HANA.
