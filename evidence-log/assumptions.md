---
name: assumptions
description: All assumptions for the housing discovery platform by risk area, the riskiest assumption, how it was chosen, and the test that resolves it; legal operability reclassified as a must-check constraint
sources: [chat, opportunity.md, ../supporting/verification.md]
aliases: [assumptions, riskiest assumption, leap of faith]
---

# Assumptions

**Status:** Proposed. Replaces "legal operability" as the riskiest assumption.

## Assumptions by Risk Area

### Area 1: Trust & User Adoption
- Students trust the platform and its listings
- Students trust the agencies/landlords being surfaced
- Students trust the AI to understand nuanced requirements (e.g., proximity to specific campus buildings or gyms)
- Students are willing to pay a small fee for the service
- Student ambassadors have real influence within the university to drive network effects

**Evidence status:** Observations from 15 interviews; validation gaps remain on willingness to pay and ambassador influence

### Area 2: Technical & Product Capability
- AI can access real estate websites reliably (scraping or API access)
- AI can communicate with agencies/vendors directly via email
- Platform works in real-time
- Supports English and Spanish
- Covers city-specific websites relevant to target universities
- Users can set guardrails on how far the agent can reach

**Evidence status:** Unvalidated; requires prototype testing with real users

### Area 3: Vendor & Market Viability
- Landlords/agencies see visibility and client-connection benefits
- Landlords/agencies are willing to respond to AI outreach as they would to real customers
- Target universities have sufficient international student populations
- Revenue model is sustainable (subscription + potential ads + data + partnerships)
- Competitive defensibility exists in a crowded AI space
- **No legal restrictions (specifically data privacy laws) prevent the platform from functioning**

**Evidence status:** Requires vendor interviews, revenue modeling, competitive analysis, legal/regulatory research

## Riskiest assumption

> **Consolidated discovery surfaces materially more available listings that match a student's criteria than the student finds on their own (mostly on Idealista), early enough for them to sign before arrival.**

Our problem statement says the problem is discovery: the market is fragmented and the process is arduous. This assumption is what that claim depends on. If almost everything a student needs is already on Idealista, putting listings in one place adds little, and the value proposition collapses into "Idealista with a nicer interface", which a general AI assistant can also offer.

## How it was chosen

Riskiest means **most important to the idea** combined with **least evidence**. The question is whether the idea dies if the assumption is false, and whether we already know the answer.

| Assumption | Kills the idea if false? | Evidence today | Cost to test | Verdict |
|---|---|---|---|---|
| Consolidated discovery surfaces materially more matching, available listings | Yes: no reason to switch from Idealista | **None.** Personas even suggest the opposite ("market scarcity, not search inefficiency") | Low (2-week supply audit) | **Riskiest** |
| Landlords and agencies respond to students coming through us | Yes: discovery doesn't turn into leases | Weak: 2 of 10 messages answered in one interview | Medium | Second riskiest; tested in the concierge pilot |
| Students trust and act on a new platform | Partly: verification may solve it | Some interview quotes | Medium | Tested together with [verification](../supporting/verification.md) |
| Someone pays | Yes, eventually | None | Medium | Test after the riskiest is resolved |
| Legal operability (GDPR, listing access, Housing Law) | Could force design changes | None yet | **Low**: a 1-week legal review | **Must-check constraint**, run in parallel |

### Why legal is not the riskiest assumption
Legal operability matters, but it isn't *uncertain* in the same way. Experts can answer it quickly, and the main risks can be designed around:

- Ask students for explicit consent
- Use official feeds, APIs or partnerships instead of scraping
- Have the AI draft messages that the student sends
- Charge the supply side instead of tenants (Ley 12/2023)

Spending a whole sprint on legal alone delays the question that decides whether the business exists at all.

## The test: supply audit

**Goal:** find out whether discovery outside Idealista is real, and how big it is.

1. **Define 3–5 realistic student briefs** from the interviews. Example: room or studio, €600–900/month, within 30 min of IE Tower / María de Molina, move-in 1 September.
2. **Search every source for 2 weeks**, using each brief: Idealista, Fotocasa, Habitaclia, Badi, Spotahome, HousingAnywhere, Uniplaces, student residences, agency websites, and Facebook/WhatsApp housing groups.
3. **Log each matching listing** in a shared sheet: source, address or area, price, size, date found, and whether it also appears on Idealista (match by photos, address or price).
4. **Check availability** for a sample: contact 20 listings per source and record the reply rate and whether the listing was still available.
5. **Calculate:**
   - Unique matching listings per brief across all sources, compared with Idealista alone
   - Share of matching listings not on Idealista
   - Share of non-Idealista listings that are actually available
   - Reply rate and reply time for each source

### Decision thresholds (agree on these before running the test)

| Result | Meaning | Action |
|---|---|---|
| ≥30% of available matching listings are **not** on Idealista | Discovery value is real | Proceed: aggregation is the core, verification is the trust layer |
| 15–30% | Moderate discovery value | Proceed, but lead with speed and verification, with aggregation as a supporting feature |
| <15% | Little extra discovery value | Pivot the value proposition: start earlier, contact landlords faster, verify listings, help with trade-offs. Re-examine the problem statement |

These thresholds are a starting proposal. The team should agree on them before seeing the data.

## Follow-on test: concierge pilot

If the audit passes, run the full flow by hand for 5–10 students who are searching now (for example, exchange students arriving for the spring semester). Compare against the interview baseline:

- Days before arrival that they signed (baseline: about 2 weeks)
- How many matching options they could choose from (baseline: often one)
- Whether they got their first-choice neighbourhood or gave up a criterion
- Confidence after signing (1–5)

This tests the second-riskiest assumption (landlords respond) and the outcome we actually promise: **arriving already settled**.
