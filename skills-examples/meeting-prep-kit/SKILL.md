---
name: meeting-prep-kit
description: Transform a raw meeting transcript into a stakeholder-ready prep kit — executive summary, decisions log, action items CSV, follow-up email, and topic-by-topic timeline with sentiment. Use when the user has a meeting transcript file and needs artifacts for attendees, stakeholders who missed the meeting, or downstream execution.
---

# Meeting Prep Kit

Convert a raw meeting transcript into a set of stakeholder-ready artifacts. **You are the tool.** There is no Python script, no parser, no extraction library. Read the transcript yourself. Reason about it yourself. Write the files yourself. This is exactly the kind of judgment work that models are better at than regex.

## Inputs

- One meeting transcript file in markdown or plain text. Speaker attribution is usually `**Speaker:** text` or `Speaker: text`. Timestamps and scene directions may be interleaved (`*[Dana joins — 14 min in]*`).
- Optional: a second transcript from a prior meeting for change-tracking.

## Outputs

Write all five files to `./output/`. Create the directory if it does not exist.

### 1. `output/summary.md` — Executive recap

For the person who missed the meeting. Under 300 words total.

Structure:
- **One-sentence purpose** — what the meeting was for.
- **Top 3 takeaways** — the three things a missed attendee needs to know to not be lost tomorrow. Each is one sentence.
- **Tone** — one sentence on meeting sentiment: collaborative, tense, rushed, avoidant, efficient, etc. Name it factually, not emotionally.
- **Key pivot** — one sentence on any moment where a position flipped or a topic changed direction. Omit if nothing pivoted.

### 2. `output/decisions.md` — Decisions with rationale

Every concrete decision made in the meeting. Format per decision:

```markdown
## Decision: {short title}

- **What:** {the decision, one sentence}
- **Why:** {rationale stated in the meeting, or "Not stated in transcript"}
- **Owner:** {person accountable for carrying it out}
- **Effective date:** {when it takes effect, or "Immediate"}
```

Do not invent rationale. If the transcript does not give a reason, write `Not stated in transcript` — flagging the gap is more valuable than filling it.

### 3. `output/action-items.csv` — Commitments, auditable

CSV with exact header row:

```
owner,action,due_date,status,source_quote
```

- One row per commitment. A commitment is any task with a named owner and either an explicit or implicit deadline.
- `due_date` is ISO format `YYYY-MM-DD`. If no date was given, write `TBD`.
- `status` is always `open` at creation.
- `source_quote` is a short verbatim snippet from the transcript proving the commitment exists. This is the audit trail — if the owner pushes back later ("I didn't agree to that"), this column is the receipt. Keep it under ~120 characters, quoted with double quotes, escape any internal quotes.

Example row:
```
Marcus Johnson,Send updated data migration schedule to team,2026-04-10,open,"I'll send it Friday the 10th."
```

### 4. `output/followup-email.md` — Draft email to all attendees

Structure:

```markdown
Subject: {Meeting title} — recap, decisions, and next steps

{One-paragraph recap, 3-5 sentences, active voice}

## Decisions
- {bullet per decision with owner}

## Action items
- {bullet per action, format: Owner — action — by DATE}

## Open questions
- {bullet per unresolved item with next-check}

Thanks,
[Your name]
```

The email is a draft, not a send. The attendee will edit it. Your job is to make the draft 95% ready so they only tweak tone.

### 5. `output/timeline.md` — Topic-by-topic with sentiment

Chronological walk through the meeting, one section per topic. This is where the model earns its keep — it's not extraction, it's interpretation.

Format per topic:

```markdown
## {topic title}

- **Raised by:** {person}
- **What happened:** {2-3 sentences on how the discussion went}
- **Resolution:** {decision, deferral, or park}
- **Sentiment:** {one phrase — quick agreement / tense debate / reluctant acceptance / avoidance / efficient dispatch / etc.}
- **Position shifts:** {anyone who changed their stated position during the topic, or "None"}
```

Order topics as they appeared in the meeting, not by importance. Include parked items and tangents — the timeline is the complete picture.

## Voice rules (applies to all five files)

- **Active voice only.** No weasel words: `may`, `might`, `could`, `perhaps`, `possibly`, `we discussed`, `it was mentioned`, `there was talk of`, `consideration was given`, `moving forward`.
- **Preserve verbatim:** names, titles, dollar amounts, dates, deadlines. Do not round, approximate, rename, or abbreviate.
- **Attribute to the committer, not the requester.** "Sarah asked Alex to pull two engineers onto auth" becomes "Alex to pull two engineers onto auth by Monday."
- **Sentiment is factual, not emotional.** "Alex and Priya disagreed on v1 vs v2, resolved in favor of v1" — not "tense standoff."
- **No invented content.** If the transcript does not support a claim, do not include it. When forced to note a gap, say so explicitly (`Not stated in transcript`, `Unassigned — needs to be assigned`, `TBD`).

## Process

1. Read the transcript in full before writing anything. Do not stream output as you read.
2. Build a mental list of: every decision, every commitment, every unresolved question, every parked item, every tangent, every position shift.
3. Draft the five files in the order listed above (summary → decisions → actions → email → timeline).
4. Run `./verify.sh` if it exists in the project root. If any check fails, fix and re-verify before reporting done.
5. Report to the user: list the five files created and call out anything you flagged as incomplete (unassigned owners, missing rationale, TBD dates, parked items).

## Done looks like

- All five files exist in `./output/`.
- `verify.sh` (if present) passes.
- Every action item has an owner and a date (or explicit `TBD`).
- Every decision has a rationale (or explicit `Not stated in transcript`).
- No weasel words anywhere in the output.
- The `source_quote` column in `action-items.csv` makes every commitment auditable.
- `timeline.md` covers every topic raised, including parked items and tangents.

## Do not

- Do not invent action items, decisions, or quotes that were not in the transcript.
- Do not attribute actions to people who did not verbally agree to them.
- Do not summarize by paraphrasing into vague corporate prose ("the team aligned on a path forward").
- Do not skip the verify step when `verify.sh` is present.
- Do not write Python, JavaScript, or any other code to do the extraction. You do it. The whole point is that the model is the tool.
- Do not write to paths outside `./output/`.
