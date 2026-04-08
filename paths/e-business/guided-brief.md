# Guided Build: Stakeholder Status Report Generator

Build a Python CLI tool (stdlib only) that reads a project status JSON file and generates a professional markdown status report — the kind you'd send to your executive sponsor or steering committee every week. Executive summary, workstream status table, risks and mitigations, asks from stakeholders, and upcoming milestones.

**You do not need to write Python to do this path.** You prompt Claude to write the code. Your job is to bring business judgment: what should the report contain, how should risks be framed, what does "done" look like for a stakeholder update. Claude handles the implementation.

**Time estimate:** 28 minutes

---

## Step 1: Set Up + Externalize (3 min)

Create your project directory and initialize Claude Code:

```bash
mkdir status-report-generator && cd status-report-generator
claude /init
```

When Claude generates `CLAUDE.md`, add project context by pressing `#` in Claude to attach notes:

- This tool generates stakeholder status reports in markdown from a project status JSON file
- Python 3 stdlib only — no external dependencies
- Output goes to `./output/` directory
- Every risk must have a mitigation, every workstream must have an owner
- Run `python3 -m unittest discover -s tests` after every code change. Never skip.

Also copy the sample data into your directory:

```bash
cp ../../paths/e-business/sample-data/project-status.json .
```

(Adjust the path depending on where you cloned the repo.)

This gives Claude the constraints it needs to stay on track.

> **Pillar 3 in action:** You just externalized your project conventions. Claude loads this every session.

---

## Step 2: Plan First (4 min)

Enter **Plan Mode** (`Shift+Tab` until `plan mode` shows in the input bar, or type `/plan`), then give Claude this prompt:

> Build a status report generator CLI that:
>
> - Reads a project status JSON file (see project-status.json in this directory for the schema)
> - Generates a markdown report with these sections: Header, Overall Status, Executive Summary, Workstream Status Table, Risks & Mitigations, Asks, Upcoming Milestones
> - The executive summary should be auto-generated prose — under 200 words, active voice, no hedging language
> - Workstreams rendered as a markdown table with owner, status, progress, and notes
> - Risks sorted by impact × likelihood (highest first)
> - Asks listed with owner and due date
> - Milestones filtered to the next 30 days
> - Saves the report to ./output/status-report.md
>
> Also plan a verify.sh shell script that checks: every section is present, every workstream has an owner, every risk has a mitigation, executive summary is under 200 words, and overall_status is one of (on_track, at_risk, blocked).
>
> Plan the module structure, function breakdown, and test approach. Don't write any code yet.

Review Claude's plan. Does the executive summary generator use the actual workstream data? Are the section functions independent so you can test each one? Does the verify script cover everything in the CLAUDE.md rule? Adjust before moving on.

> **Pillar 2 in action:** You planned before coding. The plan identifies the section breakdown and verification approach before a single line is written.

---

## Step 3: Build + Verify (12 min)

Exit Plan Mode (`Shift+Tab` until `plan mode` disappears). Tell Claude to implement the plan.

Key points to watch for during the build:

- **Parsing**: `json.load()` with explicit schema validation — fail loudly on missing required fields
- **Section functions**: One per report section (`render_header`, `render_summary`, `render_workstreams`, etc.) so they're individually testable
- **Summary generator**: Must produce prose that reflects the actual data — not a templated "Project is progressing well" — read the workstream statuses and risks, and reflect them honestly
- **Templating**: Python f-strings only — no Jinja2 or string.Template abuse
- **Tests**: After each section renderer is built, Claude should write a test that verifies output contains the expected elements (section header, table columns, required fields)
- **verify.sh**: Shell script that greps the output, counts sections, and exits 0/1

Example test prompt after the workstream renderer is done:

> Write a unittest test that verifies render_workstreams() output includes a markdown table header row, a row for every workstream in the input, and the word "Owner" in the column headers.

Run tests after each section:

```bash
python3 -m unittest discover -s tests -v
```

Then run the verify script against a generated report:

```bash
python3 report.py --input project-status.json --output output/status-report.md
./verify.sh output/status-report.md
```

> **Pillar 4 in action:** Tests verify each section renderer's output. The verify.sh script catches business-rule violations (missing mitigations, weasel words, overlong summaries). When either fails, Claude self-corrects before moving on. This is the same rule-plus-check pattern you saw in the warmup.

---

## Step 4: Iterate + Verify (5 min)

Ask Claude to add these enhancements:

- An `--audience` flag with two values: `executive` (one-page, summary only, no tables) and `team` (full detail, current default)
- A `--compare` flag that takes a second JSON file (previous report data) and produces a "changes since last report" section highlighting status changes, new risks, and closed asks
- A CSV export of the workstream table: `--csv output/workstreams.csv` for stakeholders who want to paste into a deck

Example prompt:

> Add three features. First, an --audience flag with values "executive" and "team" — executive is one page, summary only, no tables; team is the current full output. Second, a --compare flag that takes a previous project-status.json and produces a "Changes Since Last Report" section. Third, a --csv output option that also writes the workstream table to a CSV file. Write tests for each new feature. Run verify.sh on every generated output.

> **Pillar 4 in action (again):** Every new feature goes through the same verification. The CLAUDE.md rule makes this automatic — you don't have to remind Claude to run the checks.

---

## Step 5: Create a Skill (2 min)

Create a reusable skill that encodes your report voice conventions:

> Create a skill at `.claude/skills/report-voice/SKILL.md` that enforces these tone rules for any status report:
> - Active voice only — no "may", "could", "perhaps", "we're hoping to"
> - Every status claim backed by a metric or named owner
> - Executive summary in active voice, under 200 words
> - Risks stated plainly with concrete impact — no hedging
> - Asks phrased as requests, not suggestions
> - No jargon — a non-technical executive must understand every sentence

Once created, you can invoke it from any project that writes reports.

---

## Check Your Context

Run `/context` to see how much of your context window is used. If you are above **65%**, run `/compact` before moving on to the independent build.

> **Pillar 1 in action:** The context window is finite. Monitor it. One feature per session. Quality degrades as it fills.

---

## What's Next

- **Independent challenge:** Open [independent-brief.md](independent-brief.md) for a Weekly Report Comparator you can build on your own.
- **Skill reference:** See [`skills-examples/report-voice/SKILL.md`](../../skills-examples/report-voice/SKILL.md) in the repo root for an example of a tone/voice skill for business reports.
