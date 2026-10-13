---
name: presentation-outline
description: Group Project I presentation outline, one slide per row from customer outcome to next experiment, each linked to its source file and labelled as existing evidence, proposed strategy or planned test; no test results exist yet; checklist for sources, links and a backup PDF
sources: [press-release.md, ../evidence-log/venture-skeleton.md, ../evidence-log/opportunity.md, ../evidence-log/jtbd.md, ../evidence-log/recruitment.md, ../evidence-log/personas/ai-persona-01.md, market/competitors.md, market/market-sizing.md, value-curve/README.md, ../evidence-log/ERRC.md, ../prototype/README.md, ../evidence-log/assumptions.md, ../evidence-log/experiment-card.md, ../evidence-log/goals.md, ../evidence-log/ai-usage-log.md]
aliases: [presentation, slide outline, pitch outline]
---

# Presentation Outline

One row per slide, in order. Every claim on a slide must come from the linked file, with its evidence label.

**Type** says what kind of content each slide shows:

- **Evidence:** what we have now. Desk research (sourced web pages) and interviews (REPORTED, not yet traced to notes) are named separately.
- **Strategy:** what we propose. Not tested.
- **Planned test:** what we will run. No experiment has run yet.

| # | Slide | Key message | Type | Source |
|---|---|---|---|---|
| 1 | Customer outcome | "New international students at IE arrive in Madrid already settled." Show as a **hypothetical launch press release** (September 2027): nothing has launched and the quote is illustrative, not a real student | Strategy | [press-release.md](press-release.md) |
| 2 | Problem and job | Listings are spread across sources and every step is manual, so near the deadline students give up their criteria. Job: secure a matching place and arrive settled. NIE, guarantor and deposit: possible extra pain, HYPOTHESIS | Evidence (interviews, REPORTED) | [opportunity.md](../evidence-log/opportunity.md#pain-point), [jtbd.md](../evidence-log/jtbd.md), [persona 01](../evidence-log/personas/ai-persona-01.md) |
| 3 | Evidence | **Market (desk research):** checks and rent-held-until-move-in exist, but only on each platform's own listings and paid by the student; chat search over idealista is already in ChatGPT. 1,731 new international bachelor's students a year at IE; private-renter count unresolved. **Interviews:** 15 held; 6 described in personas; none traced to notes yet | Evidence (desk research; interviews REPORTED) | [competitors.md "So what"](market/competitors.md), [market-sizing.md "So what"](market/market-sizing.md), [recruitment.md](../evidence-log/recruitment.md#interview-index) |
| 4 | Value curve + ERRC | Competitors lead on checks, payment holding and English; the gap is cross-source discovery and arrival-date planning. Moves: eliminate tenant fees, reduce listings to review, raise checks across sources, create an arrival-dated search. Our curve is target levels, not features | Strategy (competitor scores: desk research) | [value curve](value-curve/README.md), [ERRC.md](../evidence-log/ERRC.md#errc-grid) |
| 5 | Prototype | Prototype v0: 7-step profile, shortlist, map, neighbourhoods, commute times. Runs on 24 **sample** homes, not real or verified listings. Not tested with users | Strategy (built, untested) | [prototype/README.md](../prototype/README.md), [venture-skeleton.md](../evidence-log/venture-skeleton.md) element 5, [goals.md](../evidence-log/goals.md#current-status) |
| 6 | Highest-risk hypothesis + test result | Hypothesis: consolidated discovery surfaces materially more matching, available listings than a student finds alone (mostly on Idealista). Test: Card 1 supply audit. **Result: TODO (team): Card 1 has not run.** Show "not yet run", not a number | Planned test | [assumptions.md](../evidence-log/assumptions.md#riskiest-assumption), [Card 1](../evidence-log/experiment-card.md#card-1-supply-audit) |
| 7 | What did real evidence change? | **From desk research:** the unsourced ~9,570 market figure was replaced by 1,731 (sourced); we start with cross-source discovery and dated checks, not chat search or our own escrow; the ERRC targets platform fees, not agent fees, since the Housing Law appears to put agency fees on landlords (pending legal review). **From checking our own evidence:** "market scarcity, not search inefficiency" was relabelled HYPOTHESIS because no interview backs it. **From user tests:** TODO (team): none run yet | Evidence (desk research and source check only) | [market-sizing.md](market/market-sizing.md), [competitors.md](market/competitors.md), [ERRC.md](../evidence-log/ERRC.md#changes-to-the-starting-proposal), [ERRC.md evidence boundaries](../evidence-log/ERRC.md#evidence-boundaries), [ai-usage-log.md](../evidence-log/ai-usage-log.md) |
| 8 | What could still make us narrow, pivot or stop? | Card 1 below 30% non-Idealista: narrow; below 15%: pivot. Card 2 below 60% signing ≥21 days before arrival: narrow or stop. Card 3 below 50% replies in 48 h: narrow; below 25%: pivot. Legal review could rule out source access or the fee model. All thresholds are proposals awaiting team agreement | Planned test | [venture-skeleton.md](../evidence-log/venture-skeleton.md) element 14, [experiment-card.md](../evidence-log/experiment-card.md) |
| 9 | Next experiment | Card 1: 3–5 student briefs searched across all sources for 2 weeks, 20 enquiries per source. Legal review in parallel. TODO (team): thresholds, dates and owners agreed first | Planned test | [Card 1](../evidence-log/experiment-card.md#card-1-supply-audit), [goals.md](../evidence-log/goals.md#current-sprint-goal) |

## Before presenting

TODO (team): update slides 6 and 7 if any experiment or prototype test has run by then. Use only results recorded in [experiment-card.md](../evidence-log/experiment-card.md).

## Checklist

- [ ] **Sources openable:** every file in the Source column opens for the audience (repo access or an exported copy), and the slide's claim matches it
- [ ] **Links work:** every link in the deck opens, including the [live prototype](https://ie-pad-finder.lovable.app/). TODO (team): listing pages show "Page not found" ([goals.md](../evidence-log/goals.md#current-status)); fix or avoid them in the demo
- [ ] **Prototype PDF:** `prototype/prototype-v0.pdf` exported and committed, in case the live site fails
- [ ] **Backup copy:** deck exported to PDF and saved in `supporting/` and on a USB drive or shared drive
- [ ] **Labels kept:** hypothetical, sample data, HYPOTHESIS and "not yet run" labels appear on the slides, not only in these files
- [ ] **AI use disclosed:** final slide or appendix links [ai-usage-log.md](../evidence-log/ai-usage-log.md)
