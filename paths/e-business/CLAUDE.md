# Meeting Prep Kit

A no-code workflow: Claude reads a raw meeting transcript and writes five stakeholder-ready artifacts to `./output/`. There is no Python, no JavaScript, no parser — Claude is the tool. The format and voice rules live in the `meeting-prep-kit` skill at `.claude/skills/meeting-prep-kit/SKILL.md`; a shell script verifies the output.

## Build & Test
- Language: none (Claude writes markdown and CSV directly)
- Input: a meeting transcript file in markdown or plain text
- Output: five files in `./output/` — `summary.md`, `decisions.md`, `action-items.csv`, `followup-email.md`, `timeline.md`
- Verify: `./verify.sh` runs automatically per the rule below

## Conventions
- Do not write any code (Python, JavaScript, etc.) to do the extraction. Claude reads the transcript and writes the artifacts directly. The point of this project is that the model is the tool.
- Output directory: `./output/` (create if missing).
- After generating or updating any output file, run `./verify.sh` and confirm it passes before responding.
- All format rules, voice rules, and done-criteria live in the skill — do not duplicate them here.

## Skill
The `meeting-prep-kit` skill at `.claude/skills/meeting-prep-kit/SKILL.md` is the single source of truth for output structure, voice rules, and verification criteria. Invoke it whenever you process a transcript.

## Don't
- Don't write Python, JavaScript, or any other code to do extraction.
- Don't install any packages.
- Don't make network requests.
- Don't write outside `./output/`.
- Don't skip the verify step.
