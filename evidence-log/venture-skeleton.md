---
name: venture-skeleton
description: Venture Skeleton v0.1 for the housing discovery platform; one or two lines per element (customer to stop criteria), each linked to its evidence file and labelled with its evidence status; no test has run yet
sources: [opportunity.md, jtbd.md, assumptions.md, experiment-card.md, ERRC.md, goals.md, recruitment.md, personas/ai-persona-01.md, personas/ai-persona-02.md, personas/ai-persona-03.md, ../supporting/market/market-sizing.md, ../supporting/market/competitors.md, ../supporting/value-curve/README.md, ../supporting/verification.md, ../supporting/research/legal-review-brief.md, ../prototype/README.md, https://ie-pad-finder.lovable.app/ accessed 2026-10-13]
aliases: [venture skeleton, venture canvas, one-page venture summary]
---

# Venture Skeleton

**Version:** v0.1, 2026-10-13 (Europe/Madrid)

No course Venture Skeleton prompt is in [downloads/](../downloads/), so this uses the section list the team set. Every element is a hypothesis unless its label says otherwise. **No experiment has run yet.** Labels: REPORTED, SUPPORTED, HYPOTHESIS, UNTESTED, as defined in [assumptions.md](assumptions.md#evidence-status-labels). [opportunity.md](opportunity.md) is the current Opportunity; [opportunity-v02.md](opportunity-v02.md) is proposed and its additions are not confirmed team decisions.

Hypothetical launch press release for this skeleton: [press-release.md](../supporting/press-release.md).

1. **Customer.** International students moving to Madrid to study at IE, renting there for the first time. Primary: [persona 01 Deadline Panic Settler](personas/ai-persona-01.md) (€600–900/month, basic-to-functional Spanish, starts late). Supply side: [persona 03 Small Landlord or Agency](personas/ai-persona-03.md). Status: REPORTED for persona 01 (5 students, source verification pending, [recruitment.md](recruitment.md#source-check)); HYPOTHESIS for persona 03. TODO (team): confirm the persona picks.

2. **Problem.** Listings are spread across sources that each show part of the market, and every step is manual, so near the deadline students give up their criteria and sign whatever responds ([opportunity.md](opportunity.md#pain-point)). Status: REPORTED (all 5 persona-01 students gave up their neighbourhood). Whether the bottleneck is scarce supply or slow search is HYPOTHESIS, tested by [Card 1](experiment-card.md#card-1-supply-audit).

3. **Job to be done.** Secure housing that matches their criteria and arrive at university already settled, rather than starting the year anxious and still searching ([jtbd.md](jtbd.md)). Status: working hypothesis; not yet checked across the 15 interviews.

4. **Value proposition.** A short list of places from several sources that meet every must-have, each with a dated check status, early enough to sign before arrival ([opportunity.md](opportunity.md#business-idea-early-stage), [ERRC.md](ERRC.md#value-innovation-hypothesis)). Status: HYPOTHESIS.

5. **Solution.** [Prototype v0](https://ie-pad-finder.lovable.app/) (Lovable; [prototype/README.md](../prototype/README.md)). Opened 2026-10-13 (Europe/Madrid), it **demonstrates** a 7-step profile (arrival date, budget, home type, lifestyle, commute), a shortlist page, a filterable map, 14 neighbourhood profiles, commute times to IE Tower and a per-home check status, all on 24 homes the site labels "illustrative sample data, not live market data". **Proposed, not demonstrated:** live or cross-source listings, real checks ([verification.md](../supporting/verification.md)), landlord contact, a sign-by date. Status: UNTESTED with users. TODO (team): individual listing pages returned "Page not found" when opened on 2026-10-13; fix, and export `prototype-v0.pdf`.

6. **ERRC moves.** Eliminate tenant-paid fees (proposed, awaiting team agreement and legal review question 4); Reduce the listings a student must review; Raise listing and landlord checks across sources; Create an arrival-dated search across several sources ([ERRC.md](ERRC.md#errc-grid), [value curve](../supporting/value-curve/README.md)). Status: plausible hypotheses; the sign-by date is unsupported novelty.

7. **Market (range).** Sourced: 1,731 new foreign-nationality bachelor's students a year at IE, both campuses (2024-25). Provisional scenarios: ~1,300–1,370 on the Madrid campus. Master's intake and the **annual number needing a private rental in Madrid are unresolved**, so we quote no market size ([market-sizing.md](../supporting/market/market-sizing.md)). TODO (team): intake by campus from IE Admissions; private-renter share from the [student survey](../supporting/research/student-survey.md).

8. **Competitors and alternatives.** Strongest current alternative: Idealista searched alone, with agents and social networks as workarounds (REPORTED). Booking platforms (Spotahome, HousingAnywhere, Uniplaces) offer landlord checks and rent held until move-in, but charge the student and cover only their own listings; idealista already runs plain-language search inside ChatGPT. Cross-source search was not identified among the ten options researched ([competitors.md](../supporting/market/competitors.md#what-the-table-shows), accessed 2026-10-12). Market evidence only, not evidence that students would switch.

9. **Channels.** Not decided. Mentioned in the repo: student ambassadors (UNTESTED, [assumptions.md](assumptions.md#area-1-trust--user-adoption)); IE student services, exchange office and student groups as pilot recruitment channels ([recruitment.md](recruitment.md#how-we-will-recruit-next)). TODO (team): choose launch channels.

10. **Revenue model.** TODO (team): decide. Options named so far: subscription, one-time fee, premium features, partnerships ([goals.md](goals.md#longer-term-business-goals-team-intent)); ads, data ([assumptions.md](assumptions.md#area-3-vendor--market-viability)); landlord- or university-paid ([legal-review-brief.md](../supporting/research/legal-review-brief.md#questions), question 4). The ERRC no-student-fee proposal conflicts with the assumption that students will pay a small fee; neither is a team decision. Status: UNTESTED.

11. **Key assumptions and riskiest hypothesis.** Riskiest: consolidated discovery surfaces materially more matching, available listings than a student finds alone (mostly on Idealista), early enough to sign before arrival. Blocking roadblocks: legal operability and landlords responding ([assumptions.md](assumptions.md#riskiest-assumption)). Status: HYPOTHESIS; legal UNTESTED.

12. **Evidence so far.** 15 student interviews, 6 described in persona documents and none yet traced to notes or transcripts ([recruitment.md](recruitment.md#interview-index)); sourced desk research on competitors and market size (accessed 2026-10-12); prototype v0 built. **Not yet run:** Cards 1–3 (no results, thresholds not agreed), prototype user testing, verification A/B test, landlord interviews, legal review, revenue validation.

13. **Next experiment.** [Card 1: Supply audit](experiment-card.md#card-1-supply-audit): 3–5 student briefs searched across all sources for 2 weeks, 20 enquiries per source. Metric: share of unique, matching, confirmed-available listings not on Idealista. Legal review runs in parallel; then [Card 2](experiment-card.md#card-2-concierge-pilot) and [Card 3](experiment-card.md#card-3-landlord-response-test). TODO (team): agree thresholds, dates and owners before starting.

14. **What would make us narrow, pivot or stop.** From the experiment cards; all thresholds are proposals awaiting team agreement.
    - **Card 1:** ≥30% persevere; 15% to <30% narrow (lead with speed and checks); <15% pivot (earlier start, faster contact, checks, trade-off help). Bands apply only if at least half of matching listings have confirmed availability; otherwise inconclusive.
    - **Card 2:** ≥60% of 5–10 pilot students sign a place meeting all must-haves ≥21 days before arrival: persevere. Below 60% with ≥3 options: narrow to contact and checks. Below 60% with mostly <3 options: stop the discovery-led offer.
    - **Card 3:** ≥50% of enquiries answered within 48 hours: persevere with direct outreach; 25% to <50% narrow; <25% pivot to partnerships or landlord-submitted listings.
    - **Legal review:** no decision rule set. TODO (team): agree what changes if listing access or the fee model is ruled out.
