---
name: ERRC
description: Eliminate-Reduce-Raise-Create grid for the housing discovery platform against Idealista, agents and social networks; four proposed moves with evidence status, and one falsifiable value-innovation hypothesis tested by the concierge pilot (Card 2)
sources: [opportunity.md, jtbd.md, assumptions.md, experiment-card.md, personas/ai-persona-01.md, ../supporting/market/competitors.md, ../supporting/verification.md, ../supporting/research/legal-review-brief.md, ../supporting/value-curve/README.md, ../downloads/ai-prompt-ERRC.md]
aliases: [ERRC grid, four actions framework, value innovation hypothesis, blue ocean]
---

# Eliminate-Reduce-Raise-Create Grid

**Status:** Value innovation hypothesis requiring evidence. Every move below is a proposed capability, not an existing or validated feature. TODO (team): review each row against the evidence, then record the date the team confirmed the grid.

**Target user:** International students moving to Madrid for university, first-time renters there; primary persona [01 Deadline Panic Settler](personas/ai-persona-01.md) (€600–900/month, basic-to-functional Spanish, starts late).

**Job to Be Done:** Secure housing that matches their criteria and arrive at university already settled, rather than starting the year anxious and still searching ([jtbd.md](jtbd.md)).

**Strongest current alternative:** Idealista, searched alone, with agents and social networks (upperclassmen, student channels) as workarounds.

**Evidence basis for the baseline:** Idealista is the solution hired in the JTBD and the only site all 5 persona-01 students used, on an upperclassman's advice (REPORTED; source verification pending, see [recruitment.md](recruitment.md#source-check)). Agents ("expensive") and social networks ("most effective but not universally accessible") are reported in [opportunity.md](opportunity.md#situation--problem) without interview traces. Competitor features come from company sites ([competitors.md](../supporting/market/competitors.md)): market evidence of what exists, not of what students choose.

## Alternatives compared

| Category | Alternative | What it gives the student | Basis | Gap for the job |
|---|---|---|---|---|
| Direct competitor | Idealista; other portals (Fotocasa, Habitaclia, Badi) | Large listing feeds; idealista room booking holds first rent until move-in | [competitors.md](../supporting/market/competitors.md#competitor-table) (sourced) | One source each; checks on normal ads unconfirmed; persona-01 students still panic-settled (REPORTED) |
| Direct competitor | Booking platforms (Spotahome, HousingAnywhere, Uniplaces) | Landlord checks, rent held until move-in, English | [competitors.md](../supporting/market/competitors.md#competitor-table) (sourced) | Tenant fee; protection covers only their own landlords |
| Indirect substitute | Student residences; IE housing services (Beyond Campus); AI assistants | Own beds; curated flats; plain-language search | [competitors.md](../supporting/market/competitors.md#competitor-table) (sourced) | Limited beds; small curated stock (size unconfirmed); AI can't confirm a flat is real or available |
| Manual workaround | Agents; social networks (upperclassmen, IE Slack "roommates-wanted") | Personal help; trusted tips | [opportunity.md](opportunity.md#situation--problem) (REPORTED, no trace); Slack channel per [competitors.md](../supporting/market/competitors.md) | Agents: cost reported, offer unsourced. Networks: not everyone has one |
| Doing nothing | Arrive still searching, or sign whatever responds | A roof, late | [opportunity.md](opportunity.md#pain-point), [persona 01](personas/ai-persona-01.md#evidence-boundary) (REPORTED) | Gives up criteria; anxious start |

Scores per factor: [value curve](../supporting/value-curve/README.md).

## ERRC Grid

Evidence status uses the course scale (evidence-supported, plausible hypothesis, unsupported novelty) with the repo labels (REPORTED, SUPPORTED, HYPOTHESIS, UNTESTED) for the underlying claims.

| Action | Strategic move | Assumption challenged | Cost effect | Buyer value effect | Evidence status | What must be verified |
|---|---|---|---|---|---|---|
| **Eliminate** | **Tenant-paid fees to search, book or be matched.** Proposed, awaiting team agreement: students would pay nothing to find, check and contact listings. Subject to the legal review. Not a revenue-model decision | Booking platforms charge the student for protection: 15% of a month (max €200) on idealista room booking, 25–40% of the first month on HousingAnywhere, a variable fee on Spotahome and Uniplaces ([competitors.md](../supporting/market/competitors.md#what-the-table-shows)) | Lower for the student. **Moves to us:** revenue must come from landlords, agencies or the university, none tested. **Conflicts with** the open assumption that students will pay a small fee ([assumptions.md](assumptions.md#area-1-trust--user-adoption)) and with goal 2, prove willingness to pay ([goals.md](goals.md#longer-term-business-goals-team-intent)) | Removes a cost on top of rent and the "worth paying when Idealista is free?" anxiety | Plausible hypothesis. Competitor fees: evidence-supported. Fee as a barrier: REPORTED ([jtbd.md](jtbd.md), Anxiety). Legal fit: UNTESTED. Revenue without student fees: UNTESTED | [Legal review](../supporting/research/legal-review-brief.md#questions) question 4; what landlords pay today ([landlord guide](../supporting/research/landlord-interview-guide.md) Q9); team decision on the revenue model and on this conflict (TODO (team)) |
| **Reduce** | **Listings a student must review.** From scrolling a whole portal feed to a short list that meets every must-have, with each property shown once across sources. | Portals compete on volume: more listings is better | Less student time. Matching and de-duplication effort for us (by hand in Card 2; cost per student unknown) | Matches the Pull: a quick overview of only relevant options, without endless scrolling | Plausible hypothesis. Need: REPORTED ([jtbd.md](jtbd.md), Pull). **Possible contradiction:** persona 01 says the bottleneck is market scarcity, not search inefficiency. That is a persona-synthesis conclusion, not a traced finding (HYPOTHESIS; see [Evidence boundaries](#evidence-boundaries)). If true, a short list may be too short. Luca's "6–7 matching options" is HYPOTHESIS (one student) | Matching listings per brief vs Idealista alone ([Card 1](experiment-card.md#card-1-supply-audit)); matching options per student and criteria given up ([Card 2](experiment-card.md#card-2-concierge-pilot)) |
| **Raise** | **Listing and landlord checks across sources.** A dated check status (verification Levels 1–2: available; landlord identity and photos match the flat) on listings from any source, not only one platform's own landlords. | Checks are a platform feature for its own listings, often an optional badge (Spotahome "Checked", Uniplaces "Visited"); on Idealista's normal ads they are unconfirmed | Higher for us: staff time per Level 2 check, processing landlord personal data (GDPR), liability for the word "checked" | Lets a student commit remotely before arrival. Today: João met a scam; Mariana and Valentina signed from photos and couldn't verify anything | Plausible hypothesis. Need: REPORTED ([verification.md](../supporting/verification.md#why-verification-belongs-in-the-core-product)). Effect on behaviour: HYPOTHESIS | Verification A/B test (contact rate, time to decision); minutes per check in Card 2; at least half of 10 landlords agree to Level 2 ([verification.md](../supporting/verification.md#assumptions-to-validate)); legal questions 1 and 5 |
| **Create** | **An arrival-dated search.** One shortlist drawn from several listing sources (those the legal review allows), organised around a sign-by date counted back from the student's arrival. | Each platform shows only its own inventory and treats timing as a move-in filter; IE itself points students to five separate channels | Lower for the student: one place instead of several. Higher for us: source access (APIs or partnerships; scraping pending legal question 2), de-duplication, reminders | Tackles starting late: persona-01 students underestimate the search and start 4–6 weeks before arrival (REPORTED) | Cross-source search: plausible hypothesis (not identified among the ten offerings researched; market evidence only). Sign-by date: unsupported novelty (no evidence students act on it) | ≥30% of confirmed matching listings off Idealista ([Card 1](experiment-card.md#card-1-supply-audit), proposed threshold); legal question 2; whether a sign-by date moves the search start earlier (no card yet, TODO (team)) |

### Changes to the starting proposal

- **Endless scrolling moved from Eliminate to Reduce.** Eliminate means zero; a student still reviews a short list.
- **Tenant-paid agent fees replaced by tenant-paid platform fees.** Since Ley 12/2023, agency management fees appear to be the landlord's cost already (pending [legal review](../supporting/research/legal-review-brief.md#questions), question 4), so removing them would not set us apart. The fees students still visibly pay are platform booking fees.
- **Number of platforms moved into Create.** One place for several sources is the new mechanism, so it has one home.
- **Landlord response speed taken out of Raise.** We don't control it, and the only signal contradicts it (Luca: 10 messages, 2 replies; REPORTED, one interview). It stays a blocking roadblock tested by [Card 3](experiment-card.md#card-3-landlord-response-test); if Card 3 passes, the team can add it here.
- **"Every verified listing" dropped.** Coverage depends on which sources the legal review allows and how many landlords agree to checks.

## Value innovation hypothesis

The combined pattern drops the tenant fee and the volume race that booking platforms and portals compete on, and puts the effort into checks that travel across sources and a search planned around the arrival date. Idealista's curve stays high on volume; Spotahome and HousingAnywhere stay high on protection and English but charge the student and cover only their own landlords ([value curve](../supporting/value-curve/README.md)).

**Falsifiable statement** (tested by [Card 2: Concierge pilot](experiment-card.md#card-2-concierge-pilot)):

> If international IE students searching for a Madrid rental get a hand-run service that searches several sources for them, checks listings to verification Level 2 and contacts landlords, then at least **60%** of a concierge pilot group of **5–10 students** will sign a place that meets **all their must-have criteria at least 21 days before arrival**.

| Field | Value |
|---|---|
| Metric | Share of pilot students who sign a place meeting all must-have criteria ≥21 days before arrival (%) |
| Threshold | ≥60%. Proposed threshold carried from Card 2, not derived from interview evidence. TODO (team): agree before the pilot starts, with the date agreed |
| Sample | 5–10 international IE students searching now, screened per [recruitment.md](recruitment.md#screening-criteria) |
| Decision date | TODO (team): Card 2 end date |
| Baseline | Students find housing about 2 weeks before classes ([opportunity.md](opportunity.md#situation--problem)); all 5 persona-01 students gave up their neighbourhood ([persona 01](personas/ai-persona-01.md#evidence-boundary)). Both REPORTED, source verification pending |
| Falsified if | Below 60%. Card 2's decision rule then says narrow (students had ≥3 options but signed late) or stop the discovery-led offer (most had <3 options) |
| Cost side | Team minutes per student, recorded in Card 2 |

**Not tested by Card 2:** the €0 student fee (Eliminate; proposed, awaiting team agreement) and the sign-by date (Create). TODO (team): decide whether to make the pilot free to students and add a sign-by date to the intake, without changing Card 2's metric or threshold.

This remains a hypothesis, not a validated blue ocean or confirmed business model.

## Critical outstanding validation points

1. **Discovery value:** do enough matching, available listings exist outside Idealista? ([Card 1](experiment-card.md#card-1-supply-audit)). If not, Reduce and Create lose their basis.
2. **Legal fit:** can we access other sources (question 2) and run with no student fee (question 4)? ([legal-review-brief.md](../supporting/research/legal-review-brief.md))
3. **Who pays:** a revenue model that works without student fees. TODO (team).
4. **Checks change behaviour and scale:** verification A/B test and minutes per check ([verification.md](../supporting/verification.md#assumptions-to-validate)).
5. **Landlords reply:** [Card 3](experiment-card.md#card-3-landlord-response-test). Without replies, a short checked list doesn't become a lease.

## Evidence boundaries

- **Real evidence:** competitor fees, checks and listing counts (company sites, accessed 2026-10-12). Student pains (scams, signing from photos, scrolling, starting late, giving up criteria) are REPORTED in persona documents, not yet traced to transcripts.
- **Team or AI inference:** every move, cost effect and target level; this wording was written with AI help and must be checked against the original interviews, sources and real students. Persona content is a thinking aid, not evidence.
- **"Market scarcity, not search inefficiency":** treated here as HYPOTHESIS, not SUPPORTED. Its only source is the persona synthesis in [persona-hypothesis-01.md](personas/drafts/persona-hypothesis-01.md#evidence-boundary) (sources: "chat"), repeated in [ai-persona-01.md](personas/ai-persona-01.md#evidence-boundary) and [assumptions.md](assumptions.md#area-3-vendor--market-viability), now also labelled HYPOTHESIS there. No quote or interview notes back it ([recruitment.md](recruitment.md#source-check): no interview traced). The 5 students searched only Idealista, so their experience cannot separate scarcity from search inefficiency; [Card 1](experiment-card.md#card-1-supply-audit) can. TODO (team): trace it to transcripts; the draft [persona-hypothesis-01.md](personas/drafts/persona-hypothesis-01.md#evidence-boundary) still records the original SUPPORTED label as the persona author wrote it.
- **Contradictions and gaps:** landlord replies are weak (REPORTED, one interview); agents' offer is unsourced; no landlord, legal or revenue evidence yet.
- Jobs to Be Done unchanged after market and ERRC review. No jtbd-v02.md required.
- Proposed successor to the Opportunity: [opportunity-v02.md](opportunity-v02.md), awaiting team confirmation.
