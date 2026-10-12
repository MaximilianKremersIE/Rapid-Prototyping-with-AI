---
name: opportunity
description: Housing discovery platform helping international students arrive at university already settled; problem is fragmented, arduous discovery; 15 interviews conducted
sources: [chat]
aliases: [housing platform, student housing opportunity]
---

## Target User

International students relocating to new cities for university study, often for the first time, with no prior experience navigating real estate websites, local rental systems, or housing searches. Primary initial market: IE University Madrid, ~9,570 target students (approximately 10,000 new students + 1,000 3rd-year transfers, excluding ~13% already-local Spanish students). **Unverified:** these figures have no cited source. TODO (team): replace with sourced market sizing.

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
- No competitive landscape analysis
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
