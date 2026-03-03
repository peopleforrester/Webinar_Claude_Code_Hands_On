# Guided Build: Operations Log Analyzer

Build a Python tool (stdlib only) that parses structured log data from theme park operations, identifies patterns (peak hours, common errors, slow operations), and generates a clean Markdown report. No external libraries required -- everything runs on Python's standard library.

**Time estimate:** 20 minutes

---

## Step 1: Set Up (2 min)

Create your project directory and initialize Claude Code:

```bash
mkdir log-analyzer && cd log-analyzer
claude /init
```

When Claude generates `CLAUDE.md`, add project context by pressing `#` in Claude to attach notes:

- This is a Python log analysis tool. No external dependencies (stdlib only).
- Input: JSON log files. Output: Markdown report.
- Handle malformed entries gracefully -- log warnings, don't crash.

---

## Step 2: Plan First (3 min)

Enter **Plan Mode** (press `Shift+Tab` twice), then give Claude this prompt:

> I'm building a log analyzer for park operations.
>
> **Input format:** JSON log files with entries containing: `timestamp`, `operation`, `duration_ms`, `status`, `location`.
>
> **Sample data:** Generate 500 log entries across 7 days, 4 locations, 10 operation types.
>
> **Analysis:**
> - Peak hours by location
> - Slowest operations (P50, P95, P99 latency)
> - Error rate by operation type
> - Anomaly detection (operations >3 standard deviations from mean)
>
> **Output:** Markdown report with ASCII tables and summary stats.
>
> Plan the data model, analysis pipeline, and report structure. Don't write any code yet.

You can use `sample-data/operations-logs.json` in this directory as seed data or as a reference for the log entry format.

Review the plan. Ask questions. Adjust before writing a single line of code.

---

## Step 3: Build (10 min)

Exit Plan Mode (press `Shift+Tab`). Build in this order:

1. **Sample data generator** -- so you have something to analyze immediately
2. **Log parser** with error handling -- malformed entries get warned and skipped
3. **Analysis functions** -- build one at a time, test each before moving on
4. **Report generator** -- Markdown output with ASCII tables

Let Claude build each piece, then verify the output before moving to the next.

Run tests after each component:

```bash
python -m pytest tests/ -v
```

---

## Step 4: Iterate (3 min)

Ask Claude to add these enhancements:

- A `--compare` flag that accepts two date ranges and shows the difference between them
- A **"Top 5 Issues"** section in the report that ranks issues by frequency x severity
- Export the report to both `.md` and `.csv` (the CSV contains raw numbers for downstream use)

Example prompt:

> Add a --compare flag that accepts two date ranges and shows a comparison. Add a "Top 5 Issues" section ranking by frequency times severity. Also export both .md and .csv output formats.

---

## Step 5: Create a Skill (2 min)

Create a reusable skill that encodes your report conventions:

```bash
mkdir -p .claude/skills/data-report
```

Ask Claude to create `.claude/skills/data-report/SKILL.md` with these conventions:

> Create a skill at `.claude/skills/data-report/SKILL.md` that enforces these report standards:
> - Always include a data quality summary at the top of every report
> - Use ASCII tables for all tabular output
> - Include methodology notes explaining how metrics are calculated
> - Flag statistical significance where applicable

---

## Check Your Context

Run `/context` to see how much of your context window is used. If you are above **65%**, demonstrate `/compact` before moving on to the independent build. This is a key workflow habit -- managing context keeps Claude effective on longer tasks.

---

## What's Next

- **Independent challenge:** Open [independent-brief.md](independent-brief.md) for a Guest Flow Simulator you can build on your own.
- **Skill reference:** See [skills-examples/data-report/SKILL.md](../../skills-examples/data-report/SKILL.md) in the repo root for an example of the data report skill.
