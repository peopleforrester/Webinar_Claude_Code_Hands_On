# Independent Challenge: Weekly Report Comparator

## The Brief

Build a tool that takes a directory of weekly status report JSON files (one per week) and produces a rolling 4-week trend report showing how project health has changed over time. Generate a single markdown report that stakeholders can read to understand trajectory, not just snapshot.

## Requirements

- **Input:** A directory containing JSON files named `status-YYYY-WW.json` (one per reporting week), each matching the `project-status.json` schema from the guided build
- **Load the last 4 weeks** of data, sorted chronologically
- **Per-workstream trend:** For each workstream, show the status over time (sparkline of progress %, status changes, churn in owner)
- **Risk evolution:** New risks, resolved risks, risks that escalated in severity
- **Milestone tracking:** Which milestones slipped, which were hit, which are newly added
- **Overall health trend:** A single "trajectory" indicator — improving, flat, declining — with a one-sentence justification
- **Output:** A single markdown report (`output/trend-report.md`) and a CSV of per-workstream progress over time (`output/progress-history.csv`)
- **Bonus:** Generate a plain-text executive email version that's under 150 words and paste-ready

## Workflow Reminders

1. **Check context first** — if you're above 65% context usage, run `/compact` or `/clear` before starting
2. **Start in Plan Mode** — the multi-file comparison logic is where plans pay off. Have Claude plan the data model before writing code
3. **Externalize your plan** — create a `PLAN.md` with your task breakdown before coding begins
4. **Reuse your verify.sh pattern** — the same rule-plus-check discipline from the guided build. Every generated report must pass a check script
5. **You have about 7 minutes of session time for this** — you won't finish, and that's fine. Focus on practicing the workflow (plan, build, iterate). Take it home to finish the full implementation

## Hints (if stuck)

1. **Start with the data loader** — get "read all files in a directory matching a pattern, parse them, sort by date" working before any analysis. Verify it with a quick test.
2. **Use Python's `statistics` module** for trend calculations — `statistics.mean` and a simple linear slope on progress percentages is enough for a "trajectory" indicator
3. **ASCII sparklines** are easier than you think — map progress values to the characters `▁▂▃▄▅▆▇█` and concatenate. No libraries needed.
4. **Write the executive email version LAST.** Once you have the full report working, ask Claude: "Now generate a 150-word executive email version of this report that a busy VP could read in 30 seconds." Use `/effort high` for that turn — concision is harder than verbosity.
5. **The hardest part is the trajectory indicator.** Use `ultrathink` in your prompt when you get to it: "ultrathink — given these 4 weeks of data, is this project improving, flat, or declining? Back your conclusion with specific metric changes."
