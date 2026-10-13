---
name: ai-usage-log
description: Log of every AI tool used on the project (Claude in Cowork, Claude Code, Codex, Lovable), with date, purpose, what the team accepted, what it changed or rejected, and the files affected; separates AI-proposed content from confirmed team decisions
sources: [team statement on Codex use 2026-10-13, git history and pull requests #1–#16 of MaximilianKremersIE/Rapid-Prototyping-with-AI (commit trailers name the Claude Code session), team task briefs for Claude Code, ../prototype/README.md, venture-skeleton.md]
aliases: [AI log, AI usage, AI disclosure]
---

# AI Usage Log

Dates are Europe/Madrid. Each row says how we know it happened:

| Basis | Meaning |
|---|---|
| Git | Commit or pull request in this repo shows it (date, author, `Co-Authored-By: Claude` and `Claude-Session` trailers) |
| Team brief | Stated in a team task brief or message to Claude Code; no other trace in the repo. TODO (team): confirm where marked |
| TODO (team) | Not recorded anywhere yet |

**Merged means accepted into the repo, not confirmed by the team.** Merged documentation is accepted repository content. It does not prove that every proposed strategy or assumption in it is a team decision: content labelled proposed, HYPOTHESIS or TODO (team) stays a proposal until a team member confirms it in the file. See [below](#accepted-repository-content-vs-confirmed-team-decisions).

## Log

| Date | Tool | Purpose | What we accepted | What we changed or rejected | Files affected | Basis |
|---|---|---|---|---|---|---|
| 2026-09-14 to 2026-09-22 | TODO (team) | First versions of opportunity, personas, goals, JTBD; these files cite "chat" as their source | Merged ([#1](https://github.com/MaximilianKremersIE/Rapid-Prototyping-with-AI/pull/1)–[#6](https://github.com/MaximilianKremersIE/Rapid-Prototyping-with-AI/pull/6)) | TODO (team) | opportunity.md, personas (now persona-hypothesis-01/02), goals.md, jtbd.md, prototype/README.md | TODO (team): say whether "chat" was an AI chat, which tool, and what it wrote |
| 2026-10-06 | Claude (Cowork per team brief; commit links session [01LTRAqp](https://claude.ai/code/session_01LTRAqpPbuazZe4r6V8bYJC)) | Review the repo; reframe the problem statements around arriving already settled | "Discovery" framing, merged 2026-10-08 ([#7](https://github.com/MaximilianKremersIE/Rapid-Prototyping-with-AI/pull/7), commit `7e317dc`, Itai) | TODO (team) | README.md, opportunity.md | Git |
| 2026-10-06 (team brief); committed 2026-10-12 | Claude (Cowork) | Write the verification proposal and the riskiest-assumption change | Discovery value as riskiest assumption; legal as a parallel roadblock ([#8](https://github.com/MaximilianKremersIE/Rapid-Prototyping-with-AI/pull/8), [#9](https://github.com/MaximilianKremersIE/Rapid-Prototyping-with-AI/pull/9), merged 2026-10-12) | Revenue-model change dropped. No such pull request exists on GitHub, so it was never opened | verification.md, riskiest-assumption.md (now assumptions.md), opportunity.md, goals.md | Team brief. Commits have no AI trailer; TODO (team): confirm the writing date and tool |
| 2026-10-12 | Claude (Cowork) | Map the Group Project I brief to the repo; write the Claude Code task prompts | The task list and folder structure used from #10 onwards | TODO (team) | None directly (prompts only) | Team brief |
| 2026-10-12 to 2026-10-13 | Codex (one chat) | GitHub setup guidance; review of Claude Code task summaries; suggested evidence and market-sizing corrections; retrieval of the seven original course helper prompts | Guidance and review only: Codex did not edit the repo. The team committed the seven prompts in [#11](https://github.com/MaximilianKremersIE/Rapid-Prototyping-with-AI/pull/11) (2026-10-13 00:22) | Suggested corrections were applied through later Claude Code sessions. TODO (team): name which commits they led to | downloads/ai-prompt-*.md (committed by the team); others indirectly via Claude Code | Team statement, 2026-10-13; commit for #11 |
| 2026-10-13 00:02 | Claude Code (session [015DPBWP](https://claude.ai/code/session_015DPBWPGDSh78EbMSnCx2p6)) | Move files into the course folder structure; split personas; merge assumptions; fix links; rewrite README | Merged ([#10](https://github.com/MaximilianKremersIE/Rapid-Prototyping-with-AI/pull/10)) | None recorded | README.md, downloads/README.md, evidence-log/*, prototype/README.md, supporting/verification.md | Git |
| 2026-10-13 00:39 | Claude Code (session [01CYmD76](https://claude.ai/code/session_01CYmD76M6B3oAd3LGfbiSWh)) | Assumptions in course format; experiment cards 1–3; recruitment index; research tools | Merged ([#12](https://github.com/MaximilianKremersIE/Rapid-Prototyping-with-AI/pull/12)). Thresholds stay proposals | Changed before merge: supply audit stays inconclusive below minimum coverage; unopened legal sources marked unverified (`52d400b`) | assumptions.md, experiment-card.md, recruitment.md, goals.md, opportunity.md, supporting/research/* | Git |
| 2026-10-13 01:00 | Claude Code (session [01VR79fc](https://claude.ai/code/session_01VR79fcrbFQBvdiRR1q6KdD)) | Refine persona hypotheses 01–02; add hypotheses 03–06 and selected personas 01–03 | Merged ([#13](https://github.com/MaximilianKremersIE/Rapid-Prototyping-with-AI/pull/13)). Persona picks await team confirmation | None recorded | personas/*, recruitment.md, README.md | Git |
| 2026-10-13 01:36 | Claude Code (session [01Vi78AS](https://claude.ai/code/session_01Vi78AS6vWLpJJrDbHxYTZ2)) | Web research: competitor table and market sizing, sources accessed 2026-10-12 | Merged ([#14](https://github.com/MaximilianKremersIE/Rapid-Prototyping-with-AI/pull/14)) | Rejected the unsourced ~9,570 student figure; replaced by 1,731 (sourced) | supporting/market/*, opportunity.md, assumptions.md, goals.md, README.md | Git |
| 2026-10-13 01:47 | Claude Code (session [017H4dm9](https://claude.ai/code/session_017H4dm9Kz1Kwob2NfadbDxx)) | ERRC grid, value curve, proposed opportunity-v02 | Merged ([#15](https://github.com/MaximilianKremersIE/Rapid-Prototyping-with-AI/pull/15)). ERRC moves and v02 additions await team confirmation | Changed before merge: "market scarcity, not search inefficiency" relabelled from SUPPORTED to HYPOTHESIS (`d8fd204`) | ERRC.md, opportunity-v02.md, experiment-card.md, assumptions.md, ai-persona-01.md, supporting/value-curve/* | Git |
| 2026-10-13 01:56 | Claude Code (session [01Q7JjG8](https://claude.ai/code/session_01Q7JjG8GJniVaVJZPjcJANA)) | Hypothetical press release; Venture Skeleton v0.1 | Merged ([#16](https://github.com/MaximilianKremersIE/Rapid-Prototyping-with-AI/pull/16)). Product name and link left TODO (team) | None recorded | supporting/press-release.md, venture-skeleton.md, README.md | Git |
| 2026-10-13 | Claude Code (session [01AYxwml](https://claude.ai/code/session_01AYxwmjLediqGN1arPE9f5H)) | This log; NIE, guarantor and deposit hypothesis; goals status; presentation outline | TODO (team): fill when the pull request is merged | TODO (team) | ai-usage-log.md, opportunity.md, opportunity-v02.md, goals.md, supporting/presentation-outline.md, README.md | Git once merged |
| TODO (team) | Lovable | Build prototype v0 ([live](https://ie-pad-finder.lovable.app/)) | Prototype v0 with 24 sample homes labelled "illustrative sample data, not live market data" | TODO (team) | [prototype/README.md](../prototype/README.md) | TODO (team): build dates and the prompts used |
| TODO (team) | TODO (team) | Any AI used for personas, interview guides, interview analysis or transcription | TODO (team) | TODO (team) | TODO (team) | TODO (team) |

## Accepted repository content vs confirmed team decisions

**Accepted repository content:** every file merged into `main` (pull requests #1–#16).

**Confirmed team decisions** (a team member made the change and the team brief states it was accepted):

- The problem is discovery, framed as arriving already settled ([#7](https://github.com/MaximilianKremersIE/Rapid-Prototyping-with-AI/pull/7), written by a team member with Claude)
- Riskiest assumption is discovery value; legal operability is a parallel blocking roadblock ([#9](https://github.com/MaximilianKremersIE/Rapid-Prototyping-with-AI/pull/9), committed by a team member)

**Accepted content still awaiting team confirmation** (AI-proposed; each is marked TODO (team) or proposed in its file):

- Experiment-card thresholds, dates and owners ([experiment-card.md](experiment-card.md))
- Critical assumptions per area ([assumptions.md](assumptions.md))
- Persona picks ([personas/](personas/)) and persona hypotheses 03–06
- ERRC moves, including no tenant fee, and the value-curve target levels ([ERRC.md](ERRC.md), [value curve](../supporting/value-curve/README.md))
- opportunity-v02 additions ([opportunity-v02.md](opportunity-v02.md))
- Replacing the ~9,570 figure with the sourced 1,731 and its provisional Madrid-campus scenarios ([market-sizing.md](../supporting/market/market-sizing.md))
- Press release wording ([press-release.md](../supporting/press-release.md))
- The NIE, guarantor and deposit pain point ([opportunity.md](opportunity.md#possible-pain-point-to-check-nie-guarantor-and-deposit))

## How we use AI

- AI output is a proposal until a team member confirms it in the file, with the date.
- Interview quotes, user feedback and test results come from people, never from AI. Persona content is a thinking aid, not evidence ([recruitment.md](recruitment.md#source-check)).
- Web research by AI carries a source link and an access date.
