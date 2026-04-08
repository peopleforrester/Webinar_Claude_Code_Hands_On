# Warmup Exercises — Feel the Difference

Four rapid exercises before the main build. Each one demonstrates a pattern you'll use throughout the workshop — no coding background required.

**Important:** You stay inside one Claude session for all four exercises. No exiting, no restarting, no switching directories. Start it once, finish all four, then move on to your build path.

Open a terminal and start a session:

```bash
mkdir -p ~/workshop-warmup && cd ~/workshop-warmup
claude
```

Leave that session running until Exercise 4 is done.

---

## Exercise 1: Effort Levels (3 min)

Claude has a reasoning dial. You control it.

**Step 1:** Set effort to low:

```
/effort low
```

Then paste this prompt:

```
Write a short retrospective document for a 1-hour hands-on workshop.
Cover what went well, what didn't, and what to change next time.
```

**Step 2:** Now set effort to high and paste the **exact same prompt**:

```
/effort high
```

**Step 3:** Compare the two responses in your chat window. At low effort, you get a bare bullet list — correct but minimal. At high effort, Claude thinks harder and produces structured sections, nuanced observations, and specific suggestions.

No files were written. The contrast is purely in the generated text.

The default is **medium**. You control the dial. For max reasoning on a single turn, type `ultrathink` inside your prompt.

Set yourself back to medium before moving on:

```
/effort medium
```

---

## Exercise 2: Plan Mode (3 min)

Same session, same directory. We need a baseline file for Claude to work on, so ask it to create one:

```
Create a file retro.md in the current directory with these four sections
and two or three bullet points in each: "## What Went Well",
"## What Didn't", "## Action Items", "## Metrics". Treat it as a
retrospective for a 1-hour hands-on Claude Code workshop.
```

Claude writes `retro.md`. That's your baseline.

**Step 1 — Without Plan Mode**, ask Claude:

```
Rewrite retro.md: add an executive summary at the top, fill in the
Action Items with realistic owners and deadlines, populate the Metrics
section with sensible numbers, and tighten the language everywhere.
Do not remove or rename any of the existing section headers.
```

Watch for about 30 seconds. You don't have to wait for Claude to finish — the point is to see Claude diving in without a plan. Interrupt with `Esc` once you've seen enough.

**Step 2 — With Plan Mode**, press `Shift+Tab` until you see `plan mode` in the input bar (or type `/plan`). Ask the exact same thing again:

```
Rewrite retro.md: add an executive summary at the top, fill in the
Action Items with realistic owners and deadlines, populate the Metrics
section with sensible numbers, and tighten the language everywhere.
Do not remove or rename any of the existing section headers.
```

Read the plan Claude produces. It should list what it found in the file, the order it intends to make changes, and any assumptions.

Press `Shift+Tab` again until `plan mode` disappears from the input bar, then:

```
Implement the plan you just described.
```

Compare. Without planning, Claude dives in and may miss pieces or order things badly. With Plan Mode, it reads the file first, reasons about order, then executes a coordinated pass.

---

## Exercise 3: Externalize (3 min)

Still in the same session. We're going to write three things to disk that will outlive the conversation: a CLAUDE.md, a verification script, and a skill.

**Step 1:** Bootstrap a CLAUDE.md:

```
/init
```

Claude will read the current directory and generate a starter `CLAUDE.md`.

**Step 2:** Ask Claude to create a verification script. The CLAUDE.md rule in Step 3 is going to point at it, so this comes first:

```
Create a shell script check.sh in the current directory. It should
grep retro.md for these required sections: "## What Went Well",
"## What Didn't", "## Action Items", "## Metrics". Print "OK" if all
four are present. For each missing section, print "FAIL: missing
<section name>" on its own line and exit non-zero. Make the script
executable.
```

Claude writes `check.sh` and makes it executable. Run it once yourself from bash mode by typing `!./check.sh` in the prompt — you should see `OK`.

**Step 3:** Add a persistent rule using the `#` memory shortcut. Type `#` as the **first character of a brand-new prompt** (not pasted into the middle of another message), then this text:

```
# After any change to retro.md, always run ./check.sh and confirm it passes before responding.
```

Claude will ask which CLAUDE.md to save it to — choose the **project-level** one.

That rule is now in a file. It survives `/compact`, `/clear`, and session resets. The conversation is temporary. The file is permanent.

**Step 4:** Create a skill. Skills live in their own named subdirectory under `.claude/skills/` — a bare `SKILL.md` directly in `.claude/skills/` will not be loaded. Ask Claude to do the directory and the file in one shot:

```
Create a skill file at .claude/skills/explain-doc/SKILL.md. It must
start with YAML front matter between --- fences, with two fields:
  name: explain-doc
  description: Summarizes a document by identifying the thesis, key decisions, and open questions
After the closing ---, add markdown instructions: identify the main
thesis in one sentence, list up to three key decisions the document
makes, flag any unanswered questions, and suggest one concrete
improvement.
```

Claude creates the directory and writes the file.

> **Note on skills:** Skills are scanned once at session start. There is no hot-reload in this build — the skill you just created will be available the next time you launch `claude`, not in this current session. That's fine for the workshop; we wrote it to *demonstrate* externalization, not to use it right now.

---

## Exercise 4: Verify (1 min)

Still in the same session. You now have `retro.md`, `check.sh`, and a CLAUDE.md rule telling Claude to run the check after any change to `retro.md`.

Ask Claude:

```
Reorganize retro.md: move "Action Items" to the top of the document,
and rename the "What Didn't" section to "Pain Points".
```

Watch what happens. Because of the CLAUDE.md rule, Claude runs `./check.sh` after the edit. The check **fails** — renaming `## What Didn't` to `## Pain Points` made `check.sh` report a missing section. Claude sees the failure in the script's output and self-corrects: it will either rename the section back, update `check.sh` to match, or ask you which you meant.

**The key insight:** Advisory instructions (CLAUDE.md rules) work about 80% of the time. Deterministic verification (scripts, linters, hooks) works 100% — and when it fails, Claude can *see* the failure in the output and fix it.

---

*You just touched every pillar: you controlled reasoning depth (Exercise 1), planned before building (Exercise 2), externalized rules and skills to files (Exercise 3), and watched Claude verify and self-correct against a deterministic check (Exercise 4). Next up: pick a build path and apply these patterns on a real project.*
