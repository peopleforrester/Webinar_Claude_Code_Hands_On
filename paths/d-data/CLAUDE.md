# Operations Log Analyzer

## Build & Test
- Language: Python 3 (stdlib only)
- Run: `python analyzer.py --input logs.json --output report.md`
- Test: `python3 -m unittest discover -s tests`
- Generate sample data: `python generate_data.py`

## Conventions
- No external dependencies — stdlib only (no pandas, numpy, matplotlib)
- Use `json` module for parsing, `statistics` module for calculations
- Handle malformed log entries gracefully: log a warning, skip the entry, continue
- All analysis functions take a list of log entries and return a dict
- Output format: Markdown with ASCII tables (use string formatting, not tabulate)
- Include data quality summary at the top of every report

## Log Entry Schema
```json
{
  "timestamp": "2026-03-15T08:12:33Z",
  "operation": "gate_scan",
  "duration_ms": 145,
  "status": "success",
  "location": "Magic Kingdom"
}
```

## Analysis Pipeline
1. Parse -> 2. Validate -> 3. Analyze -> 4. Report

## Don't
- Don't install any packages (no `pip install`)
- Don't use pandas, numpy, or matplotlib
- Don't make network requests
- Don't use hardcoded absolute paths
- Don't crash on malformed input — warn and skip
