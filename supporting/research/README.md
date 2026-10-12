---
name: research-tools
description: Index of the research tools used by the experiment cards; supply-audit log, student survey, landlord interview guide, legal review brief
sources: [../../evidence-log/experiment-card.md, ../../evidence-log/assumptions.md, ../../evidence-log/recruitment.md]
aliases: [research tools, test materials]
---

# Research tools

Each tool belongs to a test in [experiment-card.md](../../evidence-log/experiment-card.md) or an assumption in [assumptions.md](../../evidence-log/assumptions.md).

| Tool | Used by | What it is |
|---|---|---|
| [supply-audit-template.csv](supply-audit-template.csv) | [Card 1: Supply audit](../../evidence-log/experiment-card.md#card-1-supply-audit), [Card 3](../../evidence-log/experiment-card.md#card-3-landlord-response-test) | One row per matching listing per source. The two rows with brief ID `EXAMPLE-B1` are made-up examples of the format; delete them before logging real data |
| [student-survey.md](student-survey.md) | [Card 2: Concierge pilot](../../evidence-log/experiment-card.md#card-2-concierge-pilot) | Screening, intake and post-signing questions for students |
| [landlord-interview-guide.md](landlord-interview-guide.md) | [Card 3: Landlord response test](../../evidence-log/experiment-card.md#card-3-landlord-response-test) | Interview guide for landlords and agents |
| [legal-review-brief.md](legal-review-brief.md) | [Blocking roadblock 1: legal operability](../../evidence-log/assumptions.md#blocking-roadblocks) | One-page brief for an IE Law professor |

## CSV columns

| Column | Format |
|---|---|
| brief_id | Brief ID from Card 1 (B1–B5) |
| property_id | Same ID for every row that is the same property on different sources; used to count unique listings |
| source | Site or channel where the listing was found |
| listing_url | Full URL |
| area | Neighbourhood |
| price_eur_month | Monthly rent in € |
| size_m2 | Size in m² (room or whole flat; note which in the area or source cell if unclear) |
| date_found | YYYY-MM-DD |
| on_idealista_y_n | Y if the property is on Idealista (photos, address or price match); use the same value on every row with that property_id |
| contacted_y_n | Y if we sent an enquiry |
| replied_y_n | Y if a reply arrived; blank if not contacted |
| reply_time_hours | Hours from enquiry to first reply; blank if no reply |
| still_available_y_n | Y/N from the reply; blank if no reply (counts as unknown availability in Card 1) |
