# Stakeholder Status Report Generator

## Build & Test
- Language: Python 3 (stdlib only)
- Run: `python3 report.py --input project-status.json --output output/status-report.md`
- Test: `python3 -m unittest discover -s tests`
- Verify: `./verify.sh output/status-report.md` (runs automatically per the rule below)

## Conventions
- No external dependencies — stdlib only (no Jinja2, no pandas, no markdown libraries)
- Use Python `json` module for parsing, f-strings for templating
- CLI arguments via `argparse`
- Output goes to `./output/` directory (create if missing)
- Each section is a separate function: `render_header()`, `render_summary()`, `render_workstreams()`, `render_risks()`, `render_asks()`, `render_milestones()`
- Validate input JSON against the schema before generating — fail loudly with a specific error if a required field is missing
- Status values normalized to: `on_track`, `at_risk`, `blocked`, `complete`

## Report Structure
1. **Header** — Project name, report date, reporting period, executive sponsor
2. **Overall Status** — Single line with status indicator (on track / at risk / blocked)
3. **Executive Summary** — Auto-generated prose paragraph, under 200 words
4. **Workstream Status Table** — Markdown table with owner, status, progress %, notes
5. **Risks & Mitigations** — Ordered by impact × likelihood, every risk has a mitigation
6. **Asks** — What we need from stakeholders, with owners and due dates
7. **Upcoming Milestones** — Next 30 days, with dates and status

## Input JSON Schema
See `sample-data/project-status.json` for the canonical example. Required top-level fields:
`project`, `report_date`, `reporting_period`, `executive_sponsor`, `overall_status`, `workstreams`, `risks`, `asks`, `milestones`.

## Verification Rule
- After any change to a generated report, run `./verify.sh <report-path>` and confirm it passes before responding.
- `verify.sh` checks: all required sections present, every workstream has an owner, every risk has a mitigation, executive summary under 200 words, overall status is one of the allowed values.
- Run `python3 -m unittest discover -s tests` after any code change. Never skip.

## Don't
- Don't install any packages (no `pip install`)
- Don't use markdown libraries, templating engines, or data frames
- Don't make network requests
- Don't use hardcoded absolute paths
- Don't crash on missing optional fields — warn and continue, but fail on missing required fields
- Don't use weasel words in generated report prose ("may", "could", "perhaps") — active voice only
