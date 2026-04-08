---
name: report-voice
description: Enforces tone, voice, and structure rules for business status reports and executive communications. Use when writing stakeholder updates, status reports, or exec-facing summaries.
---
When writing a business status report or executive communication, apply these voice and structure rules. These are not suggestions — they are the difference between a report that gets read and one that gets skipped.

## Active Voice Only

- Replace "may", "could", "might", "perhaps", "we're hoping to" with direct statements
- Replace "there is a concern that X" with "X is a risk because..."
- Replace "it has been decided that" with "we decided that" — name the decider
- Replace "work is being done" with "<owner> is doing <work>"

Passive voice hides accountability. Active voice names owners. In a stakeholder report, accountability is the point.

## Every Claim Backed by Data or an Owner

- "The frontend rebuild is on track" → "The frontend rebuild is 72% complete; Alex Kim owns delivery by 2026-04-22"
- "We are making progress" → "We shipped 4 of 6 planned deliverables this period"
- "Things are going well" — delete this sentence; it says nothing

If you can't back a claim with a metric or a named owner, the claim doesn't belong in the report.

## Executive Summary Rules

- Under 200 words, always
- First sentence states overall status in plain English ("This project is at risk due to a two-week slip in the auth service refactor.")
- Second paragraph names the single most important risk and what's being done about it
- Third paragraph states what you need from the reader (the ask)
- No recap of the methodology, no throat-clearing, no "as you know"

A busy executive reads the first sentence, decides whether to keep reading, and skips to the asks. Write for that reader.

## Risks Stated Plainly

- Every risk has: a description, an impact, a likelihood, and a concrete mitigation
- Risks without mitigations are not risks — they are complaints. Either add a mitigation or remove the risk.
- Impact and likelihood use a fixed scale (low / medium / high) — do not invent new labels
- Order risks by impact × likelihood, highest first

## Asks Phrased as Requests, Not Suggestions

- "It would be helpful if" → "Please approve X by Y date"
- "Consideration should be given to" → "Decide whether to X or Y"
- Every ask has: who you need it from, what you need, and by when
- If you can't specify all three, it's not a real ask

## Forbidden Phrases

The following phrases add length without adding meaning. Delete them on sight:

- "As you know"
- "I wanted to reach out"
- "Just checking in"
- "Looping back"
- "Per our earlier discussion"
- "At this point in time" → "now"
- "In order to" → "to"
- "Due to the fact that" → "because"
- "At the end of the day"
- "Moving forward"

## Report Structure (in order)

1. **Header** — Project, period, executive sponsor, overall status
2. **Executive Summary** — Under 200 words, active voice, ends with the ask
3. **Workstream Status** — Table: name, owner, status, progress, notes
4. **Risks & Mitigations** — Ordered by impact × likelihood
5. **Asks** — What you need, from whom, by when
6. **Upcoming Milestones** — Next 30 days, with dates

Do not add sections beyond this list unless the report sponsor explicitly asks for them. Stakeholders read reports in the same order you wrote them; that order is where the information belongs.

## Before You Ship

Verify:
- [ ] Executive summary is under 200 words
- [ ] No weasel words (grep for: may, could, might, perhaps, hoping, working to)
- [ ] Every workstream has a named owner
- [ ] Every risk has a mitigation
- [ ] Every ask has a recipient, a need, and a date
- [ ] The first sentence of the summary states overall status plainly
- [ ] A stranger could read this report and understand the project's state in 60 seconds
