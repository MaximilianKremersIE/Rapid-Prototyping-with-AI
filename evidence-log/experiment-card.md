---
name: experiment-card
description: Experiment cards for the three tests, in run order; supply audit (highest-risk hypothesis, discovery value), concierge pilot (arriving settled), landlord response test (blocking roadblock)
sources: [assumptions.md, goals.md, recruitment.md, ../supporting/verification.md, ../supporting/research/README.md, ../downloads/ai-prompt-experiment-card.md]
aliases: [experiment cards, smallest test, test plan]
---

# Experiment Cards

Each card follows the course's six fields (Hypothesis, Method, Metric, Threshold, Evidence strength, Decision rule) plus logistics, what counts as verifiable evidence, results and the decision.

**Before any card runs:** the team agrees the Threshold and Decision rule, writes the date agreed on the card, and does not change them after seeing data. **Every threshold below is a proposal.** None is derived from interview evidence; each needs team agreement before its test starts.

Decision vocabulary: **persevere** = continue; **narrow** or **pivot** = change (narrow keeps the idea but cuts scope; pivot changes the value proposition); **stop** = stop.

---

## Card 1: Supply audit

Tests the **highest-risk hypothesis** (discovery value). See [assumptions.md](assumptions.md#riskiest-assumption).

### Hypothesis
For realistic student briefs, at least 30% of unique matching listings with confirmed availability are found only on sources other than Idealista.

### Method
Technical spike, run by hand: a narrow proof of one question (does matching supply exist outside Idealista?) before building any aggregation. TODO (team): confirm with the course that this is the right experiment type.

1. Write 3–5 student briefs from the interviews, each linked to the interview it came from in [recruitment.md](recruitment.md#interview-index). Example shape: room or studio, €600–900/month, within 30 min of IE Tower / María de Molina, move-in 1 September.
2. For 2 weeks, search every source with each brief: Idealista, Fotocasa, Habitaclia, Badi, Spotahome, HousingAnywhere, Uniplaces, student residences, agency websites, Facebook/WhatsApp housing groups.
3. Log every matching listing in [supply-audit-template.csv](../supporting/research/supply-audit-template.csv), one row per listing per source. Give rows for the same property the same `property_id` (match by photos, address or price), and record whether the property also appears on Idealista.
4. Contact 20 listings per source and record whether they reply, how fast, and whether the listing is still available. TODO (team): agree an honest enquiry script (who we are and why we ask) and check it against the [legal review](../supporting/research/legal-review-brief.md) before sending.

### Metric
Share of unique, matching listings with confirmed availability that are **not** on Idealista, pooled across briefs (%):

- **Unique:** count each `property_id` once. If any copy of a property is on Idealista, the property counts as on Idealista.
- **Matching:** meets every must-have in the brief (price, area or travel time, type, move-in date).
- **Confirmed availability:** the landlord or agency replied that it is available for the brief's dates.
- **Unknown availability** (not contacted, or no reply): excluded from both numerator and denominator, and reported separately as a count and share of all unique matching listings.
- **Bias risk:** excluding non-responses can bias the result if reply rates differ between sources. For example, if Idealista landlords reply more often than Facebook-group landlords, non-Idealista listings are under-counted. Report confirmed-availability coverage per source next to the result, and read the metric with that in mind.

Metric = unique, matching, confirmed-available listings not on Idealista ÷ all unique, matching, confirmed-available listings.

Also reported: unique matching listings per brief vs Idealista alone, and reply rate and reply time per source.

### Threshold
Proposed threshold, carried over from the earlier assumptions work and not derived from interview evidence. TODO (team): agree before testing.

- **≥30%:** pass
- **15% to <30%:** partial pass
- **<15%:** fail

**Minimum coverage (proposal, requiring team agreement before testing):** the bands apply only if at least half of the unique matching listings have confirmed availability. Below that, the result is inconclusive.

**Extension rule (proposal, requiring team agreement before testing):** if coverage is below the minimum after 2 weeks, extend the audit by one week to contact the listings with unknown availability. No further extension.

Threshold agreed by the team on: TODO (team): date.

### Evidence strength
MEDIUM: real listings and real landlord replies, but the briefs are built from interviews and the searching is done by the team, not by students.

### Sample, dates, owner
- Sample: 3–5 briefs × all sources above; 20 enquiries per source
- Dates: TODO (team): start and end date (2 weeks)
- Owner: TODO (team)

### Verifiable evidence
- The filled CSV, committed as `supporting/research/supply-audit-YYYY-MM-DD.csv`
- A dated screenshot or archived copy of each listing (listings disappear)
- The briefs, each linked to its source interview
- Enquiry and reply log with timestamps (screenshots or exported messages, personal details removed)

### Decision rule
- If ≥30%: **continue (persevere)**. Aggregation is the core; verification is the trust layer. Run Card 2.
- If 15% to <30%: **change (narrow)**. Lead with speed and verification; aggregation becomes a supporting feature. Run Card 2 with that framing.
- If <15%: **change (pivot)**. Rework the value proposition around starting earlier, faster landlord contact, verification and trade-off help; re-examine the problem statement in [opportunity.md](opportunity.md) before running Card 2.
- The bands above are applied only if the minimum coverage is met, after the 2 weeks or after the one-week extension.
- If coverage is still below the minimum after the extension: the result is **inconclusive**. Do not apply the bands and do not record persevere, narrow or pivot. TODO (team): agree before testing what the team does next in this case (for example, repeat the audit with a different contact method, or run Card 2 without a discovery result) and record it here.

### Results
TODO (team): fill after the test runs.

**Decision: persevere / narrow / pivot / stop / inconclusive** — TODO (team): circle one after results. Inconclusive only if the minimum coverage was not met after the extension.

---

## Card 2: Concierge pilot

Tests the outcome we promise: **arriving already settled**. Runs after Card 1, unless Card 1 says pivot.

### Hypothesis
International students who receive a hand-run discovery and verification service sign a place that meets all their must-have criteria at least 21 days before arrival.

The 21-day line is a proposal for team agreement, not a figure from interview evidence. Context only: [opportunity.md](opportunity.md#situation--problem) says students find housing about 2 weeks before classes, and persona 01 says deadline pressure hits 1–2 weeks before arrival (both reported in existing persona and opportunity documents; source verification pending, see [recruitment.md](recruitment.md#source-check)).

### Method
Concierge: the team runs the full flow by hand for each pilot student (brief, multi-source search, verification to Level 2 per [verification.md](../supporting/verification.md#verification-levels), landlord contact, comparison), visibly as a service.

Intake and follow-up questions: [student-survey.md](../supporting/research/student-survey.md).

### Metric
Share of pilot students who sign a place meeting all must-have criteria ≥21 days before arrival (%). Also recorded per student: number of matching options they could choose from, whether they gave up a criterion, whether they signed remotely, confidence after signing (1–5), team minutes spent.

### Threshold
**Proposed threshold, requiring team agreement before testing.** It is not established by interview evidence.

The test passes if ≥60% of pilot students sign a place meeting all must-have criteria ≥21 days before arrival.

Threshold agreed by the team on: TODO (team): date.

### Evidence strength
HIGH for behaviour (real students signing real leases), but the sample is small (5–10), so the result shows direction, not a reliable rate.

### Sample, dates, owner
- Sample: 5–10 international students searching now (for example, exchange students arriving for the spring semester), screened with the criteria in [recruitment.md](recruitment.md#screening-criteria)
- Dates: TODO (team): recruitment window, pilot start and end
- Owner: TODO (team)
- Consent: TODO (team): written consent form covering what we do on the student's behalf and how their data is stored (depends on the legal review)

### Verifiable evidence
- Signed consent form per student (stored privately, referenced by pseudonym)
- Intake and post-signing survey responses (exported raw file)
- Per-student log: options shown, landlord contacts, verification steps, minutes spent
- Proof of signing date (student confirmation by message or email, contract details removed)

### Decision rule
- If ≥60%: **continue (persevere)**. Automate the steps that took the most team time first.
- If <60% and students had ≥3 matching options but still signed late: **change (narrow)**. The bottleneck is decision or landlord speed, not discovery; focus on contact and verification.
- If <60% and most students had <3 matching options: **stop** the discovery-led offer and return to the assumption map with this result.

### Results
TODO (team): fill after the test runs.

**Decision: persevere / narrow / pivot / stop** — TODO (team): circle one after results.

---

## Card 3: Landlord response test

Tests **blocking roadblock 2**: landlords respond to students who come through us. See [assumptions.md](assumptions.md#blocking-roadblocks).

### Hypothesis
Landlords and agencies reply within 48 hours to at least half of the enquiries sent through our flow (in Spanish, with a short student profile and clear dates and budget).

The 50% / 48-hour line is a proposal for team agreement, not a figure from interview evidence. Context only: Luca sent 10 messages and got 2 replies (reported in [persona 01](personas/drafts/persona-hypothesis-01.md#evidence-boundary); one interview; source verification pending).

### Method
Concierge: the team writes enquiries for real student briefs; the student sends them, or the team sends them with the student's consent (depends on the [legal review](../supporting/research/legal-review-brief.md)). Then interview 5 landlords or agents, including some who did not reply, with [landlord-interview-guide.md](../supporting/research/landlord-interview-guide.md).

TODO (team): decide whether to merge this with step 4 of Card 1 to save effort; if merged, keep the reply data for this card separate in the CSV.

### Metric
Share of enquiries that get a reply within 48 hours (%), by source and by private landlord vs agency.

### Threshold
**Proposed threshold, requiring team agreement before testing.** It is not established by interview evidence.

- **≥50%** of enquiries get a reply within 48 hours: pass
- **25% to <50%:** partial pass
- **<25%:** fail

Threshold agreed by the team on: TODO (team): date.

### Evidence strength
MEDIUM: real landlords replying to real enquiries, but we don't observe whether a lease follows (Card 2 covers that), and the baseline is a single interview.

### Sample, dates, owner
- Sample: TODO (team): number of enquiries (proposal: at least 40, at least 10 per source across 4+ sources) and 5 landlord interviews
- Dates: TODO (team)
- Owner: TODO (team)

### Verifiable evidence
- Enquiry log with send and reply timestamps (in the supply-audit CSV format, personal details removed)
- Screenshots or exports of enquiries and replies
- Landlord interview notes, one file per interview, referenced by pseudonym, with date and interviewer

### Decision rule
- If ≥50%: **continue (persevere)** with direct outreach as the contact model.
- If 25% to <50%: **change (narrow)**. Focus on the sources and landlord types that replied; start partnership conversations with agencies.
- If <25%: **change (pivot)** to a partnership or landlord-submitted model (landlords come to us) before scaling outreach.

### Results
TODO (team): fill after the test runs.

**Decision: persevere / narrow / pivot / stop** — TODO (team): circle one after results.
