---
name: verification
description: What "verified" means on the platform, how we verify listings and landlords, and how we'll test whether verification changes student behaviour
sources: [chat]
aliases: [listing verification, trust layer]
---

# Verification

**Status:** Proposal, not yet tested with users or landlords

## Why verification belongs in the core product

Students can't arrive settled if they can't trust what they sign. In the interviews, the friction isn't only *finding* listings. Once students find one, they can't tell whether it's real, current or fairly priced:

- Scam encounters (João)
- Signing based on photos alone with no way to check anything (Mariana, Valentina)
- Not knowing whether the price was fair (Camille)
- Valentina, the best-resourced student in the sample, still said a platform confirming "this listing is real, the photos are current" would have made her feel better

Discovery gets students to options faster. Verification lets them **commit** to one remotely, before arrival, without panic. General-purpose AI assistants can't verify a flat, so verification is also part of how we stand out.

## Verification levels

Each listing shows the highest level it has reached. Levels are cumulative.

| Level | Badge | What we check | How (first version) |
|---|---|---|---|
| 0 | Unverified | Nothing beyond the source listing | Shown, but clearly labelled |
| 1 | Available | Listing is live and still available for the student's dates | Message or call the landlord or agency within 24–48 h |
| 2 | Real | Landlord or agency identity matches the property; photos match the flat | Agency: registered business details. Private landlord: ID check plus a *nota simple* (Land Registry extract) showing the owner. Live video walk-through compared with the listing photos |
| 3 | Fair | Price is in line with comparable listings; no red-flag contract terms | Compare with similar listings in the same area; checklist review of the contract (deposit, duration, who pays fees) |
| 4 | Viewed | Someone physically visited | Student ambassador or team member visits and records a short video (paid add-on or partner landlords only) |

## Red flags we check for (scam signals)

Any of these blocks a listing from Level 2 and shows a warning:

- Asking for a deposit or "reservation fee" before any viewing (in person or live video)
- Landlord claims to be abroad and asks for payment via wire, Western Union or crypto
- Price far below comparable listings in the same area
- Refuses a live video call, or the video doesn't match the photos
- Contact only through WhatsApp, or pressure to move off-platform immediately
- Same photos appear on other listings at different addresses (reverse image search)
- Asks the tenant to pay agency fees (in Spain, since the 2023 Housing Law, agency management fees are the landlord's cost)

## How we deliver it (staged)

1. **Concierge (now):** the team verifies listings by hand for pilot students. We learn which checks matter and how long each takes.
2. **Landlord-submitted:** landlords and agencies upload documents and book a video verification slot in exchange for a "Verified" badge and better placement.
3. **Partly automated:** reverse image search, price comparison and red-flag detection run automatically; people handle Levels 2–4.

## What verification is not

- Not a guarantee or insurance. The interface says "checked on [date]", not "guaranteed".
- Not legal advice on the contract. The contract check is a checklist, and complex cases are referred to a lawyer or university housing services.

## Constraints to check

- **GDPR:** verifying private landlords means processing their personal data (ID, property ownership). We need a lawful basis, a retention policy, and an explanation of how this is handled. Include this in the legal review.
- **Liability:** what happens if a verified listing turns out to be a scam? Define wording and policy before launch.
- **Cost per verification:** Level 2+ takes staff time. Track minutes per check during the concierge phase.

## Assumptions to validate

| Assumption | Test | Signal that it holds |
|---|---|---|
| Students value verification enough to change behaviour | A/B test in the prototype: same listings with and without badges. Measure contact rate and time to decision | Verified listings get noticeably more contacts and faster decisions |
| Verification lets students sign before arrival without seeing the flat in person | Concierge pilot: share of pilot students who sign remotely, and how confident they feel afterwards | Most pilot students sign remotely and report feeling confident |
| Landlords and agencies will go through verification | Ask 10 landlords and agencies to complete Level 2 | At least half agree without being paid |
| Level 2 verification is cheap enough to scale | Time each check during the pilot | A sustainable cost per verified listing |
| Scams are common enough to matter | Count red-flag listings in a sample of 100 listings matching student criteria | A meaningful share is flagged |

## Metrics

- Share of shown listings at Level 2 or higher
- Time from first contact to verified
- Contact rate and signing rate: verified vs unverified listings
- Scams reported on verified listings (target: zero)
- Student confidence after signing (1–5), compared with the interview baseline
