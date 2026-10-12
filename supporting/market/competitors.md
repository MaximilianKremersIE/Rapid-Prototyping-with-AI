---
name: competitors
description: Sourced comparison of the housing options an international student in Madrid can use today (portals, mid-term booking platforms, student residences, IE University's own housing services, general AI assistants) and what it means for what we build first
sources: [../../evidence-log/opportunity.md, ../../evidence-log/assumptions.md, ../../evidence-log/personas/ai-persona-01.md, ../verification.md, web research accessed 2026-10-12]
aliases: [competitor table, competitive landscape, market baseline]
---

# Competitors

What a student moving to Madrid can use today instead of us. Feeds the [riskiest assumption](../../evidence-log/assumptions.md#riskiest-assumption) and the Area 3 assumption "we can defend a position in a crowded AI-assistant market" ([assumptions.md](../../evidence-log/assumptions.md#area-3-vendor--market-viability)).

## How to read this

- **Market evidence only.** These are features each company states on its own site, opened on the dates in [Sources](#sources). They show what exists, not what our users choose or would pay for.
- **Not evidence about our product.** Competitor features do not show that our aggregation, verification or differentiation would work or be valued. Those assumptions stay untested until [Card 1](../../evidence-log/experiment-card.md#card-1-supply-audit), [Card 2](../../evidence-log/experiment-card.md#card-2-concierge-pilot) and the [verification A/B test](../verification.md) run. The "main weakness" column is **our interpretation** for persona 01 ([Deadline Panic Settler](../../evidence-log/personas/ai-persona-01.md)), not a sourced fact.
- **Verification is not a guarantee.** We separate three things: who the platform checks (landlord identity, bank account), whether anyone checks the property itself, and what payment protection the student gets (rent held until move-in). See [verification.md](../verification.md) for our own levels.
- **unconfirmed** = we could not open a page that states it. Search-engine snippets are not counted as evidence.
- Listing counts are what the site displayed for Madrid when we opened it (12 October 2026). They change daily and overlap between sites (the same flat can be on several).

## Competitor table

| Option | Who it serves | Madrid coverage | Verification (what exactly) | English | Student filters | Who pays | Main weakness for our user (our interpretation) |
|---|---|---|---|---|---|---|---|
| **Idealista** | Buyers and renters of all kinds; rooms via Online Room Booking [S1] | Describes itself as the leading property marketplace in Spain, Portugal and Italy [S2]. Madrid listing count: unconfirmed (site blocked automated access) | **Room booking only:** first month's rent held until 48 h after move-in; payment system rejects fraudulent transactions [S1]. Idealista says platforms cannot check landlord-supplied data such as large-holder status or previous rent [S3]. Listing or landlord checks for normal ads: unconfirmed | English news site exists [S1]; English search interface: unconfirmed | Room listings; "Online Booking with Insurance" filter [S1]. Campus-distance filter: unconfirmed | **Room booking:** tenant pays 15% of one month's rent, min €75, max €200, once [S1]. Other ads: unconfirmed | The one site persona 01 students used, and they still panic-settled (REPORTED, [persona 01](../../evidence-log/personas/ai-persona-01.md)). Since March 2026 it also runs a natural-language search app inside ChatGPT [S2], so "AI search over listings" is no longer new |
| **Fotocasa** | Buyers and renters; private and professional advertisers [S4] | 8,526 rental homes in Madrid city [S5] | Rental ads are moderated before going live (1–48 h) [S4]. What the moderation checks: unconfirmed. No property visit or payment protection found | Yes, English interface [S5] | District, type, price, bedrooms, rental type; room-rental pages [S5]. No student or campus filter seen. Has an "AI Search" button; what it does: unconfirmed [S5] | Private advertisers list free; pay for highlighting, a second ad of the same type (€19.95) or hiding the address (€9.95) [S4]. Tenant fees: none seen (unconfirmed) | Another general portal: more listings to scroll, no remote-booking protection found |
| **Habitaclia** | Buyers and renters | 7,659 rental homes in Madrid city [S6] | unconfirmed | No English version found (/en/ returned "page not found") [S7] | Price, size, bedrooms, bathrooms [S6]. No student filter seen | unconfirmed | Spanish-only interface found. Gabriel and Camille, who speak no Spanish, met more friction than the others (REPORTED, [assumptions.md](../../evidence-log/assumptions.md#area-2-technical--product-capability)) |
| **Badi** | People renting rooms in shared flats; Badi Plus managed homes [S8][S9] | Madrid among its Spanish cities [S8]. Listing count: unconfirmed | "Trusted user" = lister whose bank account details Badi confirmed (blue label) [S10]; phone verification exists [S11]; users can report listings [S10]. No property check found | Yes (English and Spanish) [S8] | Move-in date; stay length (1–5, 6–11, 12+ months); couples; pets [S8]. No campus filter seen | Publishing is free [S8]. For listings by individuals or professionals, rent, deposit and contract are agreed directly with the lister; **Badi does not process those payments** [S9]. Badi Plus is booked and paid on Badi [S9]. Paid seeker features (Badi Gold, Fast-Track) are named in the FAQ; prices unconfirmed [S8] | No payment protection on most listings; Badi advises visiting in person or by video call before paying anything [S9], which a student abroad can only partly do |
| **Spotahome** | Renters booking mid- to long-term homes fully online [S12] | 10,190 listings in Madrid [S13] | "Checked" properties: Spotahome's verification team ensures the property matches the listing; Trust and Safety team verifies each landlord [S12]. **Not every listing carries the "Checked" badge** [S13]. First month's rent sent to the landlord 48 h after move-in; 24 h to report a mismatch; deposit protection only on listings with a "Deposit protected" badge [S12] | Yes, plus 5 other languages [S12] | Availability dates, property type, budget, group search [S13] | Tenant pays a one-time booking fee that varies by property type, shown at checkout [S14]; landlord admin fees possible [S15] | Fee on top of rent; covers only landlords who list on Spotahome |
| **HousingAnywhere** | Students, professionals, temporary stays [S16] | 9,340 listings in Madrid; 175+ cities; 400+ university partners [S17] | Landlords: email, ID and selfie checks, KYC [S16]; landlords and bank accounts verified with Stripe; AI scam detection [S18]. Property itself: no inspection claimed. Rent held until 48 h after move-in; refund if the place is very different from the listing [S18] | Yes; multilingual support [S16] | Private room, shared room, studio, student accommodation; move-in and move-out dates [S17] | Tenant pays a Tenant Protection fee of 25–40% of the first month's rent (min €175) outside the Netherlands, plus 2.5% on payments made through the platform [S19] | Highest stated tenant fee in this set; covers only its own landlords |
| **Uniplaces** | Students, Erasmus, interns, young professionals [S20] | Madrid listings shown on home page [S21]. Count: unconfirmed | Open platform: any landlord can publish once email is verified. Optional levels: Verified Landlord (phone, email, government photo ID and at least one hosted guest), Visited (staff or photographer visited the property), Exclusive [S22]. Rent held until 24 h after move-in [S23] | Yes; multilingual team [S23] | Rent, bedroom features, location, accommodation type; student-residence category [S23][S20] | Tenant pays a one-time, non-refundable service fee that varies per booking [S24]; landlords list free and pay commission on bookings [S20]. Offers a prepaid-accommodation certificate for visas [S23] | Beyond email, verification is optional, so a listing may carry no check at all. Lists Universidad Carlos III among partners [S23], so it already works with a Madrid university |
| **Student residence operators** (Resa, Livensa Living, Yugo, Nodis) | Degree, master's and Erasmus students [S25] | Own buildings only: Yugo 7 residences in Madrid [S26]; Nodis 2 (Arturo Soria, Vicálvaro) [S27]; Resa has Madrid halls [S28]; Livensa lists Madrid among 10 Spanish cities [S25]. Purpose-built beds equal 7.8% of on-site students in Madrid [S29] | The operator is the landlord, so there is no third-party listing to verify | Yes (English sites) [S25][S26][S27][S28] | Not applicable (own rooms only) | Student pays rent to the operator. Prices not compared here | Limited beds; IE says residences fill up quickly [S30]. Only an option if the student wants a residence |
| **IE University housing services** | IE students [S30] | Recommends Beyond Campus (platform founded by IE MBA alumni, with recommended residences and curated flats); also links Idealista, Fotocasa, Enalquiler and the students' Slack "roommates-wanted" channel [S30]. Beyond Campus inventory size: unconfirmed | Per IE: the Beyond Campus team visits every apartment and checks that prices fit the market; contracts in English, 24/7 service [S30]. **Stated by IE, not checked by us.** Beyond Campus's own site gave no detail [S31] | IE page in English [S30]; Beyond Campus site rendered in Spanish only for us [S31] | "Near your campus" section [S31] | unconfirmed | IE's own advice is to visit a flat in person before signing or paying [S30], which conflicts with signing before arrival. Curated, so likely a small share of the market (size unconfirmed) |
| **General AI assistants** (ChatGPT and similar) | Anyone | No inventory of their own. ChatGPT searches the web with links to sources [S32]; the idealista app inside ChatGPT searches idealista listings in plain language [S2] | None stated: no availability check, landlord check or payment protection in the sources read | Yes | Any criteria typed in plain language [S2] | Free and paid plans [S32] | Can search and summarise, but can't confirm a flat is real or available, or contact the landlord for the student. Our interpretation: "AI search" alone is not a differentiator |

## What the table shows

1. **Payment protection already exists, but only inside each platform.** Spotahome, HousingAnywhere, Uniplaces and idealista's room booking all hold the first month's rent until after move-in [S1][S12][S18][S23]. The student pays a fee for it (15% capped at €200 on idealista rooms; 25–40% of a month's rent on HousingAnywhere) and it covers only that platform's listings.
2. **Property checks are partial and optional.** Only Spotahome ("Checked") and Uniplaces ("Visited") claim someone checks the property, and both show it as a badge that not every listing has [S13][S22]. Landlord identity checks are more common (HousingAnywhere, Spotahome, Uniplaces, Badi bank details).
3. **Cross-source aggregation was not identified among the researched offerings.** This finding is limited to the ten options compared here; we did not survey the whole market. Each option researched shows its own inventory, and IE points students to five separate channels [S30]. It is not proof that aggregation helps students: whether combining sources surfaces more matching listings is what [Card 1](../../evidence-log/experiment-card.md#card-1-supply-audit) tests.
4. **Conversational search is now table stakes.** Idealista's ChatGPT app (March 2026) already lets a student describe what they want in plain English and get matching idealista listings [S2].

## Gaps

- TODO (team): open Idealista in a normal browser and record its English interface, Madrid rental count and any listing checks. Its site blocked our automated access.
- TODO (team): ask Beyond Campus (help@beyondcampus.es) how many Madrid flats and residences it lists, what a visit checks, and who pays.
- TODO (team): log one real booking flow per platform (fee shown at checkout for a €700 room) in the [supply audit](../research/supply-audit-template.csv) so fees can be compared on the same brief.

## Sources

Accessed dates are the dates we opened each page (UTC). Where a page did not load, the claim is marked unconfirmed in the table.

| # | Source | Accessed |
|---|---|---|
| S1 | idealista/news, "idealista launches online room booking", 3 Dec 2025: https://www.idealista.com/en/news/property-for-rent-in-spain/2025/12/03/873976-idealista-launches-online-room-booking | 2026-10-12 |
| S2 | idealista/news, "idealista launches its app on ChatGPT", 13 Mar 2026: https://www.idealista.com/en/news/property-for-sale-in-spain/2026/03/13/887103-idealista-launches-its-app-on-chatgpt | 2026-10-12 |
| S3 | idealista/news, "Los anuncios de viviendas en alquiler tendrán que incluir nuevos datos desde octubre", 8 Oct 2026: https://www.idealista.com/news/inmobiliario/vivienda/2026/10/08/917982-los-anuncios-de-alquiler-tendran-que-incluir-nuevos-datos-desde-octubre | 2026-10-12 |
| S4 | Fotocasa, "Publica tu piso en Fotocasa": https://www.fotocasa.es/es/publicar-anuncio/ | 2026-10-12 |
| S5 | Fotocasa, rentals in Madrid city (English): https://www.fotocasa.es/en/rental/homes/madrid-capital/all-zones/l | 2026-10-12 |
| S6 | Habitaclia, rentals in Madrid city: https://www.habitaclia.com/alquiler/viviendas/madrid-provincia/madrid-capital/s | 2026-10-12 |
| S7 | Habitaclia, English path: https://www.habitaclia.com/en/ | 2026-10-12 |
| S8 | Badi home page: https://badi.com/en/ | 2026-10-12 |
| S9 | Badi Help, "How renting a room with Badi works": https://badiapp.zendesk.com/hc/en-gb/articles/12134624797084-How-renting-a-room-with-Badi-works | 2026-10-12 |
| S10 | Badi, Trust and safety: https://badi.com/trust-and-safety | 2026-10-12 |
| S11 | Badi Help, Marketplace: https://badiapp.zendesk.com/hc/en-gb/categories/11510816644380-Marketplace | 2026-10-12 |
| S12 | Spotahome, How it works: https://www.spotahome.com/how-it-works | 2026-10-12 |
| S13 | Spotahome, Madrid search: https://www.spotahome.com/s/madrid | 2026-10-12 |
| S14 | Spotahome Help, "What is the Spotahome booking fee?": https://spotahome.zohodesk.com/portal/en/kb/articles/booking-fee | 2026-10-12 |
| S15 | Spotahome Help, "What is the total amount I will have to pay?": https://spotahome.zohodesk.com/portal/en/kb/articles/total-amount-to-pay | 2026-10-12 |
| S16 | HousingAnywhere, How it works: https://housinganywhere.com/renting | 2026-10-12 |
| S17 | HousingAnywhere home page: https://housinganywhere.com/ | 2026-10-12 |
| S18 | HousingAnywhere, Tenant Protection: https://housinganywhere.com/secure-payments | 2026-10-12 |
| S19 | HousingAnywhere, Pricing for tenants: https://housinganywhere.com/pricing/tenants | 2026-10-12 |
| S20 | Uniplaces Help Center: https://www.uniplaces.com/help/ | 2026-10-12 |
| S21 | Uniplaces home page: https://www.uniplaces.com/ | 2026-10-12 |
| S22 | Uniplaces Help, "What are the Uniplaces landlord verification levels?": https://www.uniplaces.com/help/landlords/trust-verification/what-are-the-uniplaces-landlord-verification-levels/ | 2026-10-12 |
| S23 | Uniplaces, How it works: https://www.uniplaces.com/how-it-works | 2026-10-12 |
| S24 | Uniplaces Help, "What is the Uniplaces service fee?": https://www.uniplaces.com/help/tenants/what-is-the-uniplaces-service-fee/ | 2026-10-12 |
| S25 | Livensa Living home page: https://www.livensaliving.com/en-gb/ | 2026-10-12 |
| S26 | Yugo, Madrid: https://yugo.com/en-gb/global/spain/madrid | 2026-10-12 |
| S27 | Nodis home page: https://nodis.es/en/ | 2026-10-12 |
| S28 | Resa, Madrid residences: https://resa.es/en/residences/madrid/ | 2026-10-12 |
| S29 | Savills Research, "Student Housing in Spain" (Spotlight, 2024), p. 6: https://pdf.euro.savills.co.uk/spain/nat-eng-2024/spotligh-pbsa-2024--eng.pdf | 2026-10-12 |
| S30 | IE University, Living in Madrid: https://www.ie.edu/student-services/living-in-madrid/ | 2026-10-12 |
| S31 | Beyond Campus home page: https://www.beyondcampus.es/ | 2026-10-12 |
| S32 | OpenAI Help Center, "Searching the web with ChatGPT": https://help.openai.com/en/articles/9237897-chatgpt-search | 2026-10-12 |

> **So what**
> Verification and rent-held-until-move-in already exist, but each platform applies them only to its own listings, charges the student for them, and shows property checks as an optional badge, and conversational search over idealista is already free inside ChatGPT. So we should start not with a chat search or our own escrow but with cross-source discovery and a dated "checked" status for listings no platform protects, and only if [Card 1](../../evidence-log/experiment-card.md#card-1-supply-audit) shows those listings matter. This table does not show that our version would work; that stays untested.
> Linked assumptions: [riskiest assumption (discovery value)](../../evidence-log/assumptions.md#riskiest-assumption) and "we can defend a position in a crowded AI-assistant market" ([Area 3](../../evidence-log/assumptions.md#area-3-vendor--market-viability)).
