---
name: assumptions
description: All assumptions for the housing discovery platform by risk area, each with an evidence status; the highest-risk hypothesis (discovery value), the two blocking roadblocks (legal operability, landlords responding) and how they were ranked
sources: [chat, opportunity.md, recruitment.md, experiment-card.md, personas/drafts/persona-hypothesis-01.md, personas/drafts/persona-hypothesis-02.md, ../supporting/verification.md]
aliases: [assumptions, riskiest assumption, leap of faith]
---

# Assumptions

## Evidence status labels

| Label | Meaning |
|---|---|
| REPORTED | Reported in existing persona documents as something students said in interviews. Source verification pending: not yet traced to transcripts or notes (see [recruitment.md](recruitment.md#source-check)) |
| SUPPORTED | A pattern across several interviews, or a stated preference consistent with other reports. Still not observed behaviour |
| HYPOTHESIS | We believe it; only indirect or contradicting signals so far |
| UNTESTED | No evidence collected |

**No assumption below has been verified by a test yet.** The tests are in [experiment-card.md](experiment-card.md).

"Critical" marks the assumptions we test first in each area (high impact if false, weak evidence). TODO (team): confirm the critical selection; the course asks the team to choose at least two per area.

## Area 1: Trust & User Adoption

Will students actually trust and act on what the platform shows them?

- **Critical.** Must be true: students trust the platform and its listings enough to contact landlords through it.
  - Status: HYPOTHESIS. Valentina said verification "would have made me feel even better" (REPORTED, one student, stated preference only).
  - Evidence needed: verified listings get a higher contact rate and faster decisions than the same listings unverified, in a prototype A/B test ([verification.md](../supporting/verification.md#assumptions-to-validate)).
- **Critical.** Must be true: students trust the landlords and agencies we surface enough to sign remotely, before arrival.
  - Status: HYPOTHESIS. Today they don't: João met a scam; Mariana and Valentina signed from photos and couldn't verify anything (REPORTED).
  - Evidence needed: most concierge-pilot students sign remotely and rate confidence after signing above the interview baseline ([Card 2](experiment-card.md#card-2-concierge-pilot)).
- Must be true: students trust the AI to understand nuanced requirements (e.g. distance to a specific campus building or gym).
  - Status: UNTESTED.
- Must be true: students will pay a small fee for the service.
  - Status: HYPOTHESIS. One stated-preference signal (Valentina); the €600–900 budget group is likely price-sensitive. Tested after the highest-risk hypothesis is resolved.
- Must be true: student ambassadors have enough influence at the university to drive network effects.
  - Status: UNTESTED.

## Area 2: Technical & Product Capability

Can we deliver the service reliably?

- **Critical.** Must be true: the AI can access listing sources reliably (official feeds, APIs, partnerships or scraping).
  - Status: UNTESTED. Depends on the legal review (blocking roadblock 1).
  - Evidence needed: TODO (team): define a technical spike for the sources the supply audit shows matter most ([Card 1](experiment-card.md#card-1-supply-audit)).
- **Critical.** Must be true: the AI can contact agencies and landlords by email, or draft messages the student sends.
  - Status: UNTESTED. Messaging on a student's behalf is a legal question ([legal-review-brief.md](../supporting/research/legal-review-brief.md)).
  - Evidence needed: replies to AI-drafted messages arrive at least as often as the interview baseline ([Card 3](experiment-card.md#card-3-landlord-response-test)).
- Must be true: the platform works in real time.
  - Status: UNTESTED.
- Must be true: the platform supports English and Spanish.
  - Status: UNTESTED as a capability. The need is REPORTED: Gabriel and Camille (no Spanish) met more friction than the others.
- Must be true: it covers the city-specific websites relevant to target universities.
  - Status: UNTESTED. The supply audit lists the Madrid sources.
- Must be true: users can set guardrails on how far the agent can act.
  - Status: UNTESTED.

## Area 3: Vendor & Market Viability

Is there enough supply, landlord engagement and room in the market for a viable business?

- **Critical. Highest-risk hypothesis.** Must be true: consolidated discovery surfaces materially more available listings that match a student's criteria than the student finds on their own (mostly on Idealista), early enough to sign before arrival.
  - Status: HYPOTHESIS, with a contradicting signal: persona 01 records "market scarcity, not search inefficiency" as the bottleneck (SUPPORTED across 5 students).
  - Evidence needed: share of available matching listings that are not on Idealista, from a 2-week multi-source supply audit ([Card 1](experiment-card.md#card-1-supply-audit)).
- **Critical. Blocking roadblock 2.** Must be true: landlords and agencies respond to students who come through us as they would to any tenant.
  - Status: HYPOTHESIS, with a contradicting signal: Luca sent 10 messages and got 2 replies, one already rented (REPORTED, one interview).
  - Evidence needed: reply rate and reply time to enquiries sent through us, against that baseline ([Card 3](experiment-card.md#card-3-landlord-response-test)).
- **Critical. Blocking roadblock 1.** Must be true: no legal restriction (GDPR and Spanish data protection, terms for accessing listings, Ley 12/2023) stops the platform from working.
  - Status: UNTESTED. No legal review yet.
  - Evidence needed: a written review from an IE Law professor answering the questions in [legal-review-brief.md](../supporting/research/legal-review-brief.md).
- Must be true: landlords and agencies see visibility and client-connection benefits.
  - Status: UNTESTED. No vendor feedback yet; see [landlord-interview-guide.md](../supporting/research/landlord-interview-guide.md).
- Must be true: target universities have enough international students.
  - Status: HYPOTHESIS. The ~9,570 figure in [opportunity.md](opportunity.md#target-user) is **unverified**: no source is cited. TODO (team): replace it with sourced market sizing.
- Must be true: the revenue model is sustainable (subscription, ads, data, partnerships).
  - Status: UNTESTED.
- Must be true: we can defend a position in a crowded AI-assistant market.
  - Status: UNTESTED.

## Riskiest assumption

> **Consolidated discovery surfaces materially more available listings that match a student's criteria than the student finds on their own (mostly on Idealista), early enough for them to sign before arrival.**

Our problem statement says the problem is discovery: the market is fragmented and the process is arduous. This assumption is what that claim depends on. If almost everything a student needs is already on Idealista, putting listings in one place adds little, and the value proposition collapses into "Idealista with a nicer interface", which a general AI assistant can also offer.

## Blocking roadblocks

These are not the riskiest assumption, but each one stops launch if it fails. They run in parallel with the supply audit.

1. **Legal operability.** If we can't lawfully access listings, process landlord data or message on a student's behalf, the product must change shape. Cheap to answer: a short expert review.
2. **Landlords responding.** If landlords ignore enquiries that come through us, discovery never turns into a signed lease. Tested in [Card 3](experiment-card.md#card-3-landlord-response-test) and again in the concierge pilot.

## How it was chosen

Riskiest means **most important to the idea** combined with **least evidence**. The question is whether the idea dies if the assumption is false, and whether we already know the answer.

| Assumption | Kills the idea if false? | Evidence today | Status | Cost to test | Verdict |
|---|---|---|---|---|---|
| Consolidated discovery surfaces materially more matching, available listings | Yes: no reason to switch from Idealista | **None.** Personas suggest the opposite ("market scarcity, not search inefficiency") | HYPOTHESIS | Low (2-week supply audit) | **Highest-risk hypothesis** |
| Landlords and agencies respond to students coming through us | Yes: discovery doesn't turn into leases | Weak: 2 of 10 messages answered in one interview | HYPOTHESIS | Medium | **Blocking roadblock** |
| Students trust and act on a new platform | Partly: verification may solve it | Some interview quotes | HYPOTHESIS | Medium | Tested with [verification](../supporting/verification.md) |
| Someone pays | Yes, eventually | One stated preference | HYPOTHESIS | Medium | Test after the riskiest is resolved |
| Legal operability (GDPR, listing access, Housing Law) | Could force design changes | None yet | UNTESTED | **Low**: a 1-week legal review | **Blocking roadblock**, run in parallel |

### Why legal is not the riskiest assumption

Legal operability matters, but it isn't *uncertain* in the same way. Experts can answer it quickly, and the main risks can be designed around:

- Ask students for explicit consent
- Use official feeds, APIs or partnerships instead of scraping
- Have the AI draft messages that the student sends
- Charge the supply side instead of tenants (Ley 12/2023)

Spending a whole sprint on legal alone delays the question that decides whether the business exists at all.

## Tests

| Order | Test | Assumption | Card |
|---|---|---|---|
| 1 | Supply audit | Highest-risk hypothesis (discovery value) | [Card 1](experiment-card.md#card-1-supply-audit) |
| 2 | Concierge pilot | Arriving settled; students sign remotely | [Card 2](experiment-card.md#card-2-concierge-pilot) |
| 3 | Landlord response test | Blocking roadblock 2 | [Card 3](experiment-card.md#card-3-landlord-response-test) |
| Parallel | Legal review | Blocking roadblock 1 | [legal-review-brief.md](../supporting/research/legal-review-brief.md) |
