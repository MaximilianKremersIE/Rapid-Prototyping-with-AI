---
name: opportunity-v02
description: Proposed successor to opportunity.md after the ERRC exercise; current Opportunity wording kept unchanged, with proposed additions (alternatives in four categories, strongest current alternative, competitive factors, value innovation hypothesis, evidence gaps) awaiting team confirmation
sources: [opportunity.md, ERRC.md, jtbd.md, assumptions.md, experiment-card.md, ../supporting/market/competitors.md, ../supporting/value-curve/README.md, ../downloads/ai-prompt-ERRC.md]
aliases: [opportunity v02, opportunity after ERRC]
---

**Status:** Proposed successor to [opportunity.md](opportunity.md), which stays the current version until the team confirms this one. The sections from "Target User" to "Open Validation Gaps" are copied unchanged from opportunity.md. Everything under [Proposed additions from the ERRC exercise](#proposed-additions-from-the-errc-exercise) was proposed with AI help and is **awaiting team confirmation**. TODO (team): confirm, edit or reject each addition, record the date, then replace opportunity.md with this file.


## Target User

International students relocating to new cities for university study, often for the first time, with no prior experience navigating real estate websites, local rental systems, or housing searches. Primary initial market: IE University Madrid. Sourced: **1,731 new foreign-nationality bachelor's students a year** at IE across both campuses (Ministry of Universities, 2024-25). Provisional scenario: ~1,300–1,370 of them on the Madrid campus. Master's intake is unresolved. **The number of international students needing a private rental in Madrid each year is unresolved** ([market-sizing.md](../supporting/market/market-sizing.md)). This replaces the previous unsourced figure of ~9,570. TODO (team): get new intake by campus from IE Admissions and the private-renter share from the student survey.

## Situation & Problem

International students spend months searching across fragmented housing platforms (Idealista dominant) with low visibility into available options. They face:
- Non-responsive landlords and agencies
- Language barriers and unfamiliar foreign websites
- No access to alternative platforms
- Isolation from other students' collective intelligence
- Only finding housing 2 weeks before classes begin

Current workarounds: pay agents (expensive), grind a single platform alone (draining), leverage existing social networks (most effective but not universally accessible).

## Pain Point

The problem is **discovery**, and the process around it is arduous rather than simple. Listings are spread across Idealista, Fotocasa, Badi, Spotahome, HousingAnywhere, agency sites and private groups, and each shows only part of the market. Students don't know most of these exist, can't search them efficiently in a foreign language, and can't tell which listings are real, current or fairly priced. Every step (finding, filtering, contacting, verifying, applying) is manual and slow.

Because the process is so slow, the calendar beats them. With about one month to go before university starts, students who haven't secured a place give up their criteria and panic-settle for whatever responds (wrong neighbourhood, overpriced, poor condition) just to have something locked in.

## User Need

Students need a simple, straightforward way to see every available, verified option that matches their criteria in one place, and to move from discovery to a signed lease quickly, because the fragmented and arduous process is what stops them securing the right place before they arrive.

## Insight

The job is not "find an apartment"; it is **arrive at university already settled**. Settled means housing secured, verified and matching their criteria *before* arrival, so the first weeks go to university, not to searching. The one-month-before deadline is the forcing function; fragmented, arduous discovery is the friction that stops students meeting it. Under that time pressure, students abandon their criteria rather than keep searching. Making discovery simple moves the moment of decision earlier, and that early decision is what lets students arrive settled.

## How Might We

How might we make housing discovery simple and straightforward enough that international students secure a verified place matching their criteria before they arrive, so they start university already settled?

## Business Idea (Early Stage)

AI-powered housing discovery platform that consolidates available listings from Spanish rental sources into one simple search, **verifies** them, and helps students contact landlords and agencies quickly, in their language, with student-specific filters (campus proximity, budget, move-in date). Success is measured by whether students sign a place matching their criteria before arrival, not by how many listings they browse.

## Key Assumptions by Risk Area

All assumptions, grouped by risk area, with the riskiest-assumption ranking and test: [assumptions.md](assumptions.md).

## Riskiest Assumption

**Consolidated discovery surfaces materially more available listings that match a student's criteria than the student finds on their own (mostly Idealista), early enough to sign before arrival.** If most matching listings are already on Idealista, consolidation adds little and the value proposition collapses. Reasoning: [assumptions.md](assumptions.md#riskiest-assumption). Test plan: [experiment-card.md](experiment-card.md#card-1-supply-audit).

Legal operability (GDPR, Spanish data protection, terms for accessing listings, and the 2023 Housing Law on who pays agency fees) and landlords responding are **blocking roadblocks** that run in parallel. Legal is critical, but cheap to resolve and largely possible to design around ([legal-review-brief.md](../supporting/research/legal-review-brief.md)).

## Current Evidence Base

- 15 interviews with international students (mostly IE University) documenting pain points, current search behaviors, and workarounds
- No vendor/landlord feedback yet
- No user testing with prototype
- No legal/regulatory review
- Competitor research from official sources ([competitors.md](../supporting/market/competitors.md)); market sizing partly sourced, private-renter count unresolved ([market-sizing.md](../supporting/market/market-sizing.md))
- No revenue model validation

## Open Validation Gaps

**From JTBD Exercise:**
- Does the deadline-driven job pattern hold across the 15 interviews, or are there multiple distinct jobs?
- Do all students face the same one-month timeline, or does the deadline vary? (Some may start earlier; some may be last-minute arrivals.)
- Is the constraint primarily *time scarcity* or *discovery difficulty*, or both? (This changes solution direction.)
- What specifically needs to be "in place" for a student to feel settled beyond just housing? (Other factors: neighborhood familiarity, proximity to campus, housemate compatibility, etc.?)

**Ongoing:**
- How much will students actually pay for this service?
- Will landlords/agencies engage with AI outreach, or only direct human contact?
- What is the legal path forward under GDPR and Spanish data protection law?
- How differentiated can this be in a crowded AI assistant market?

## Proposed additions from the ERRC exercise

Awaiting team confirmation. Source for all of this section: [ERRC.md](ERRC.md) and the [value curve](../supporting/value-curve/README.md).

### Current alternatives

| Category | Alternative | Basis |
|---|---|---|
| Direct competitor | Idealista and other portals (Fotocasa, Habitaclia, Badi) | [competitors.md](../supporting/market/competitors.md#competitor-table): market evidence (company sites, accessed 2026-10-12) |
| Direct competitor | Booking platforms (Spotahome, HousingAnywhere, Uniplaces) | Same |
| Indirect substitute | Student residences; IE housing services (Beyond Campus); general AI assistants | Same |
| Manual workaround | Agents; social networks (upperclassmen, IE Slack "roommates-wanted" channel) | Agents and networks: REPORTED in Situation & Problem above, no interview trace. Agents' offer: unsourced. Slack channel: [competitors.md](../supporting/market/competitors.md) |
| Doing nothing | Arrive still searching, or sign whatever responds | REPORTED ([persona 01](personas/ai-persona-01.md#evidence-boundary)) |

Market research shows what exists, not what students choose.

### Strongest current alternative

**Idealista, searched alone**, with agents and social networks as workarounds. Basis: the solution hired in [jtbd.md](jtbd.md) and the only site all 5 persona-01 students used (REPORTED; source verification pending, see [recruitment.md](recruitment.md#source-check)).

### Competitive factors and market conventions

The factors options compete on, scored 0–5 in the [value curve](../supporting/value-curve/README.md#factors-and-scale): listings in one search, landlord checks, property checks, payment held until move-in, English access, student filters, tenant fee, cross-source discovery, arrival-date planning.

Conventions the market takes for granted (from [competitors.md](../supporting/market/competitors.md#what-the-table-shows)):

- Each option shows only its own inventory; cross-source search was not identified among the ten options researched.
- Checks and payment protection apply only to a platform's own listings, and property checks are an optional badge.
- The student pays for protection: up to €200 on idealista room booking, 25–40% of the first month's rent on HousingAnywhere.
- Plain-language search over idealista listings already exists inside ChatGPT.

### Value innovation hypothesis

Proposed moves ([ERRC grid](ERRC.md#errc-grid)): eliminate tenant-paid fees (proposed, awaiting team agreement and the legal review), reduce the listings a student must review, raise listing and landlord checks across sources, create an arrival-dated search across several sources.

Falsifiable statement, tested by [Card 2](experiment-card.md#card-2-concierge-pilot): at least 60% (proposed threshold) of a concierge pilot group of 5–10 students sign a place meeting all their must-have criteria at least 21 days before arrival. Decision date: TODO (team). This remains a hypothesis, not a validated strategy.

### Tensions with the current wording

Not resolved here; the wording above is unchanged. TODO (team): decide whether to revise.

- **User Need** says "every available, verified option ... in one place". Coverage depends on which sources the legal review allows and how many landlords agree to checks, so "every" may not be achievable.
- **Pain Point** says the problem is discovery. Persona 01 says the bottleneck is market scarcity, not search inefficiency. That claim comes only from persona synthesis (sources: "chat"), with no traced interview, so it is HYPOTHESIS, not SUPPORTED. [Card 1](experiment-card.md#card-1-supply-audit) tests it.
- **Business Idea** does not say who pays. The ERRC proposes no student fee, which conflicts with the open assumption that students will pay a small fee ([assumptions.md](assumptions.md#area-1-trust--user-adoption)) and with goal 2 in [goals.md](goals.md). No revenue model is decided.

### Open evidence gaps

- Matching, available listings outside Idealista ([Card 1](experiment-card.md#card-1-supply-audit))
- Legal answers on source access and student fees ([legal-review-brief.md](../supporting/research/legal-review-brief.md#questions), questions 2 and 4)
- A revenue model that works without student fees
- Whether checks change student behaviour, and what each check costs ([verification.md](../supporting/verification.md#assumptions-to-validate))
- Landlord replies ([Card 3](experiment-card.md#card-3-landlord-response-test))
- What agents offer; Idealista's count, English interface, filters and checks ([value curve gaps](../supporting/value-curve/README.md#gaps))
