# Independent Challenge: Multi-Meeting Changelog

## The Brief

You have two transcripts from the same weekly project meeting, one week apart. Generate a **changelog** that shows what changed between them: which decisions held, which flipped, which action items slipped, which risks escalated, which people shifted position. This is the document you send to an exec who wants "just tell me what changed since last week."

## Requirements

- **Input:** Two meeting transcripts in markdown (`meeting-transcript-w1.md` and `meeting-transcript-w2.md`). For this challenge, create a second transcript yourself — either by editing the sample from the guided build (change a few decisions, add a new risk, slip a couple of action items) or by writing a fresh one from scratch.
- **Output:** A single `output/changelog.md` that covers:
  - **Decisions that held** — carried through from week 1 to week 2 unchanged
  - **Decisions that flipped** — made in w1, overturned or modified in w2, with the rationale for the flip
  - **Action items closed** — committed in w1, reported done in w2
  - **Action items slipped** — committed in w1, not yet done in w2, with new due date if one was given
  - **New action items** — first appeared in w2
  - **Risks escalated** — present in both but flagged as more severe in w2
  - **Risks resolved** — present in w1, no longer a concern in w2
  - **New risks** — first appeared in w2
  - **People who shifted position** — anyone whose stated stance on a topic changed between the two meetings
- **Bonus 1:** `output/exec-summary.md` — a 150-word version of the changelog for a busy VP
- **Bonus 2:** `output/attention.md` — a list of items that *should* have changed but didn't (e.g., a slipping action item that nobody commented on, a risk that was raised and then quietly ignored)

## Workflow Reminders

1. **Check context first** — if you're above 65% context usage, run `/compact` or `/clear` before starting.
2. **Start in Plan Mode** — cross-transcript comparison is exactly the kind of reasoning that benefits from a plan. Have Claude plan the comparison approach before generating anything.
3. **Externalize your plan** — create a `PLAN.md` listing what you're comparing and what counts as a "change" vs a "restatement."
4. **Reuse the verify.sh pattern** — extend your verification script to also check the changelog sections exist and that every flip has a stated reason.
5. **You have ~7 minutes of session time** — you will not finish. Focus on the workflow (plan, generate, verify, iterate). Take it home to complete.

## Hints (if stuck)

1. **Start with a side-by-side diff.** Before generating the changelog, ask Claude: "Read both transcripts and list every decision, action item, and risk from each, in parallel columns. Don't interpret yet — just extract." Then build the changelog from the comparison.

2. **Use `ultrathink` for the position-shift analysis.** Detecting when someone changed their stance is the hardest part. Use `ultrathink` in that specific prompt: "ultrathink — compare what Alex said about the auth refactor scope in w1 vs w2. Did his position change? Quote the specific lines that show the shift, if any."

3. **The "attention" bonus is where judgment shows up most.** Most changelogs only list what changed. A *good* changelog also flags what should have changed but didn't — a slipping action item nobody commented on is more dangerous than one everyone's watching. Prompt Claude explicitly: "Find anything that was raised as a risk or concern in w1 that is absent from w2 entirely. Those are items that got quietly dropped — flag them."

4. **Do not write Python.** Same rule as the guided build. The tool is Claude. Your verification script is bash. The comparison is reasoning, not code.

5. **Iterate tone.** The first draft of the changelog will probably read like a ledger. Ask Claude to rewrite it "as if you're the project manager briefing the CEO in three minutes — what's the narrative of the week?" That shift from ledger to narrative is the difference between a changelog that gets skimmed and one that drives decisions.
