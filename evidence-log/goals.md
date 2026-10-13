---
name: goals
description: Team and business goals for housing platform venture; current sprint goal is testing the riskiest assumption (discovery value), with legal review in parallel; status is prototype built, not yet tested
sources: [chat, assumptions.md, experiment-card.md, ../prototype/README.md, venture-skeleton.md]
aliases: [project goals, sprint goals]
---

## Current Sprint Goal

**Prove that consolidated discovery surfaces materially more available, matching listings than students find on their own.** This is the riskiest assumption (see [assumptions.md](assumptions.md)). If it fails, the value proposition fails, whatever the legal or revenue picture.

Tested by [Card 1: Supply audit](experiment-card.md#card-1-supply-audit), then [Card 2: Concierge pilot](experiment-card.md#card-2-concierge-pilot) and [Card 3: Landlord response test](experiment-card.md#card-3-landlord-response-test). No card has run; thresholds await team agreement.

**In parallel:** get a short written legal review (GDPR, terms for accessing listings, Ley 12/2023) to set design constraints. This is a blocking roadblock, not the sprint's main question.

## Longer-Term Business Goals (Team Intent)

1. **Validate the Job to Be Done** — Confirm that international students have a real, recurring need for consolidated housing search and that the emotional/psychological dimension is as significant as the operational one.

2. **Prove user willingness to pay** — Determine the sustainable revenue model (subscription tier, one-time fee, premium features, or partnerships).

3. **Validate vendor/landlord engagement** — Confirm that landlords and real estate agencies will respond to and benefit from AI outreach; determine if partnerships are necessary.

4. **Establish competitive defensibility** — Identify how to differentiate from ChatGPT, Claude, and other general-purpose AI assistants in a crowded market.

5. **Scale beyond IE Madrid** — Prove the model works for other universities and cities if successful at IE.

## Constraints & Assumptions Guiding the Work

- Discovery value is the riskiest assumption and is tested first; legal operability and landlords responding are blocking roadblocks, tested in parallel and designed around where possible
- International student housing search has annual cohort cycles; time-to-market matters for capturing each cohort
- The competitive landscape is crowded with AI assistants; differentiation must be clear
- Network effects (student ambassadors) may be necessary for growth, but this is unvalidated

## Current Status

**Prototype built, not yet tested** (checked 2026-10-13, Europe/Madrid).

- [Prototype v0](../prototype/README.md) is live on Lovable. Its 24 homes are labelled "illustrative sample data, not live market data" ([venture-skeleton.md](venture-skeleton.md), element 5). They are not real or verified listings, and no check status shown in the prototype has been carried out.
- No user has tested the prototype; no experiment card has run ([experiment-card.md](experiment-card.md): Cards 1–3, results TODO (team)).
- 15 interviews conducted with international students; none yet traced to notes or transcripts ([recruitment.md](recruitment.md#source-check))
- Legal/regulatory path still unclear
- No vendor outreach
- No revenue model validation
- Competitor research done from official sources ([competitors.md](../supporting/market/competitors.md)); market sizing partly sourced, with the number needing a private rental unresolved ([market-sizing.md](../supporting/market/market-sizing.md))

**Outstanding checks before any prototype test:**

- TODO (team): individual listing pages (`/listing/<id>`) show "Page not found". Reported in [venture-skeleton.md](venture-skeleton.md) and seen again on 2026-10-13 when `cha-01`, `mal-01` and `tet-03` were loaded directly. Fix in Lovable, then re-check.
- TODO (team): export `prototype/prototype-v0.pdf` (not in the repo yet; see [prototype/README.md](../prototype/README.md)).
