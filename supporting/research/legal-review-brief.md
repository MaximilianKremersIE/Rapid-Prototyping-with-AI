---
name: legal-review-brief
description: One-page brief asking an IE Law professor to review GDPR lawful basis, listing access (scraping vs APIs vs partnerships), messaging on a student's behalf, Ley 12/2023 fees and liability for "verified" listings
sources: [../../evidence-log/assumptions.md, ../verification.md, ../../evidence-log/opportunity.md]
aliases: [legal brief, legal review]
---

# Legal review brief

**For:** TODO (team): name of the IE Law professor
**From:** TODO (team): team names, IE University, Rapid Prototyping with AI
**Asked by:** TODO (team): date sent. **Answer needed by:** TODO (team): date

Answers resolve blocking roadblock 1 in [assumptions.md](../../evidence-log/assumptions.md#blocking-roadblocks). We are asking expert questions: a short written view on what is allowed and what we must design around, not a formal opinion. Nothing in this brief is a legal conclusion.

## What we are building

An AI housing-discovery service for international students moving to Madrid. It gathers rental listings from several sources, checks that listings and landlords are real ([verification levels](../verification.md#verification-levels)), and helps students contact landlords before they arrive. Early tests are run by hand by students.

## Questions

1. **GDPR lawful basis.** We would process (a) students' data (budget, dates, nationality, messages) and (b) landlords' data in listings and in verification (name, phone, ID, Land Registry extract). Which lawful basis under GDPR Article 6(1) fits each? If landlord data comes from listing sites rather than the landlord, what must we tell them (Article 14), and is legitimate interest realistic?
2. **Listing access: scraping vs APIs vs partnerships.** Can we copy listing data from portals (Idealista, Fotocasa, Badi and others) without permission? How do the database maker's right (Database Directive, Article 7) and each site's terms of use apply? Is a meta-search that shows other sites' results riskier than linking out? What changes if we use official feeds, APIs or partnership agreements?
3. **Messaging on a student's behalf.** Can we send enquiries to landlords for a student, or must the student send them? What consent and disclosure do we need? Does this differ for our hand-run tests?
4. **Ley 12/2023 and fees.** We understand that since the Housing Law the landlord pays property-management and contract-formalisation costs (Article 20.1 LAU). Is that right, and can we charge students for search, verification or concierge services, or would that count as a fee the tenant may not be charged? What model is safe: free for students, landlord-paid, or university-paid?
5. **Liability for "verified".** If a listing we marked "verified" turns out to be a scam, what is our exposure? Is wording like "checked on [date]" with a clear list of what was checked enough? What must the terms say?
6. **Anything else** that would stop us operating, such as registration requirements for property intermediaries in Madrid.

## Pointers for you to check

These are open questions, not conclusions. We are not lawyers; please confirm or correct each one against the primary law.

**How we found these sources:** all were found through a web search on 2026-10-12. Our environment could not open the pages themselves, so we saw only search-result summaries. TODO (team): open each link, check it says what is summarised here, and record the date you accessed it.

### Official sources

| Question | What we want checked | Source | Found | Opened |
|---|---|---|---|---|
| 4 | Does Ley 12/2023, final provision 1, section 2, amend Article 20.1 LAU so that property-management and contract-formalisation costs fall on the landlord? Spain's consumer authority appears to say charging tenants these fees is illegal | [Ministerio de Derechos Sociales, Consumo y Agenda 2030, press release](https://www.dsca.gob.es/es/comunicacion/notas-prensa/consumo-advierte-inmobiliarias-es-ilegal-cobrar-comision-gestion-personas) | 2026-10-12 (search) | TODO (team) |
| 2 | Does Article 7 give a database maker the right to stop extraction or re-use of a substantial part of its contents, and does it cover listing portals? | [Directive 96/9/EC, Chapter III (UK government archive copy)](https://www.legislation.gov.uk/eudr/1996/9/chapter/III) | 2026-10-12 (search) | TODO (team) |

Primary texts we could not reach and would like you to rely on: [Ley 12/2023 on BOE](https://www.boe.es/buscar/act.php?id=BOE-A-2023-12203), [GDPR on EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj), [Directive 96/9/EC on EUR-Lex](https://eur-lex.europa.eu/eli/dir/1996/9/oj). TODO (team): open these and record the date accessed.

### Secondary commentary

| Question | What we want checked | Source | Found | Opened |
|---|---|---|---|---|
| 4 | Same point on Ley 12/2023 and Article 20.1 LAU | [Primera Lectura, Boletín Mercantil 25/05/2023](https://www.primeralecturaediciones.com/Boletines/2023/05/25/Mercantil/BsM_20230525.pdf) | 2026-10-12 (search) | TODO (team) |
| 1 | Is legitimate interest the realistic GDPR basis for scraping, subject to a necessity and balancing test, and do Article 14 notice duties apply? (Law-firm summary of EDPB guidance) | [Pinsent Masons, Out-Law](https://www.pinsentmasons.com/out-law/news/eu-guidance-helps-clarify-ai-web-scraping-requirements) | 2026-10-12 (search) | TODO (team) |
| 2 | Does CJEU *Innoweb* (C-202/12) mean a meta-search engine that re-uses a site's database can infringe the database right? | [EU Law Radar summary](https://eulawradar.com/case-c-20212-innoweb-search-engines-copying-insubstantial-parts-of-a-website/) | 2026-10-12 (search) | TODO (team) |
| 2 | Is the Danish first-instance decision *BoligPortal v ReData* (2025), reported as finding that scraping a rental-listings database infringed the database right, relevant in Spain? | [BDK Advokati summary](https://bdkadvokati.com/boligportal-v-redata-danish-court-finds-data-scraping-infringes-database-rights) | 2026-10-12 (search) | TODO (team) |

## How we will use the answer

Each answer becomes a design constraint in [assumptions.md](../../evidence-log/assumptions.md) and decides how Cards 1–3 in [experiment-card.md](../../evidence-log/experiment-card.md) send enquiries and store data.
