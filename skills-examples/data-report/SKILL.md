---
name: data-report
description: Generates data analysis reports with quality summaries, ASCII tables, and methodology notes. Use when creating data analysis output or reports.
---
When generating a data report:

## Data Quality Summary
- Always start the report with a data quality section
- Include: total records, records processed, records skipped (with reasons)
- Report date range covered and any gaps detected
- Note any data anomalies found during parsing

## ASCII Tables
- Use fixed-width ASCII tables for all tabular data
- Right-align numeric columns, left-align text columns
- Include column headers with a separator line (dashes)
- Keep tables under 100 characters wide for terminal readability
- Example format:
```
| Location          | Count | Avg (ms) | P95 (ms) |
|-------------------|-------|----------|----------|
| Magic Kingdom     |   142 |    234.5 |    890.2 |
| EPCOT             |    98 |    198.3 |    756.1 |
```

## Methodology Notes
- Include a brief methodology section explaining how metrics were calculated
- Define any statistical terms used (P50, P95, P99, standard deviation)
- State assumptions (e.g., "outliers defined as values >3 standard deviations from mean")
- Note any limitations of the analysis

## Statistical Significance
- Flag when sample sizes are too small for reliable conclusions (< 30 observations)
- Use appropriate language: "suggests" vs "demonstrates" based on confidence
- Include confidence intervals or ranges where applicable
- Never present a single metric without context (always include count and spread)

## Report Structure
1. Title and date range
2. Data quality summary
3. Key findings (3-5 bullet points)
4. Detailed analysis sections with tables
5. Methodology notes
6. Appendix (raw counts, definitions) if needed
