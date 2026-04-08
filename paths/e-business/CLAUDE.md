# Meeting Prep Kit

## What this project is
A no-code workflow: Claude reads a raw meeting transcript and generates a set of stakeholder-ready artifacts. There is no Python, no JavaScript, no parser. Claude is the tool; a Skill file encodes the format and voice rules; a shell script verifies the output.

## Build & Test
- Language: none (Claude writes markdown and CSV directly)
- Input: a meeting transcript file in markdown or plain text
- Output: five files in `./output/` — `summary.md`, `decisions.md`, `action-items.csv`, `followup-email.md`, `timeline.md`
- Verify: `./verify.sh` (runs automatically per the rule below)

## Conventions
- Do not write any code (Python, JavaScript, etc.) to do the extraction. Claude reads the transcript and writes the artifacts directly. The point of this project is that the model is the tool.
- Output directory: `./output/` (create if missing)
- All five required files must exist after a successful run. Names are exact.
- Preserve names, dollar amounts, and dates verbatim from the transcript. No rounding, no approximation, no renaming.
- Active voice only. No weasel words: `may`, `might`, `could`, `perhaps`, `possibly`, `we discussed`, `it was mentioned`, `there was talk of`, `moving forward`.
- Attribute action items to the person who committed to them, not the person who requested them.
- Never invent content. If the transcript does not support a claim, either flag the gap (`Not stated in transcript`, `TBD`, `Unassigned`) or leave it out.

## Output Structure
1. **summary.md** — Under 300 words. One-sentence purpose, top 3 takeaways, one-sentence tone, one-sentence key pivot (if any).
2. **decisions.md** — Every concrete decision as `## Decision: {title}` with **What**, **Why**, **Owner**, **Effective date**.
3. **action-items.csv** — Header: `owner,action,due_date,status,source_quote`. Every commitment is one row. `due_date` ISO format or `TBD`. `source_quote` is a verbatim snippet from the transcript proving the commitment.
4. **followup-email.md** — Draft email with `Subject:` line, one-paragraph recap, `## Decisions`, `## Action items`, `## Open questions`, sign-off `[Your name]`.
5. **timeline.md** — Topic-by-topic walk through the meeting in order, each with `Raised by`, `What happened`, `Resolution`, `Sentiment`, `Position shifts`.

## Skill
The `meeting-prep-kit` skill at `.claude/skills/meeting-prep-kit/SKILL.md` encodes the full workflow. Invoke it whenever you process a transcript.

## Verification Rule
- After generating or updating any output file, run `./verify.sh` and confirm it passes before responding to the user.
- `verify.sh` checks: all five required files exist, `action-items.csv` has the correct header, every CSV row has a non-empty owner and a due_date (or `TBD`), `summary.md` is under 300 words, no weasel words appear in any output file.

## Don't
- Don't write Python, JavaScript, or any other code to do extraction.
- Don't install any packages.
- Don't make network requests.
- Don't invent action items, decisions, or quotes that aren't in the transcript.
- Don't write outside `./output/`.
- Don't skip the verify step.
- Don't use weasel words anywhere in the output.
