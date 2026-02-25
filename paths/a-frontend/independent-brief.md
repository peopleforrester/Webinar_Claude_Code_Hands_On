# Independent Challenge: Park Wait Times Display Board

## Brief

Build a **Park Wait Times** display board — a single-page dashboard that shows current ride wait times across the park.

## Requirements

- Shows **ride names**, **current wait times** (in minutes), and **status** (Open / Closed / Maintenance)
- **Color-coded by wait time:**
  - Green: less than 15 minutes
  - Yellow: 15 to 45 minutes
  - Red: more than 45 minutes
- **Auto-sorts by shortest wait** by default
- Has a **search/filter input** to find rides by name
- Sample data for **20 rides** embedded in JavaScript
- **Single HTML file**, no external dependencies

## Workflow Reminders

1. **Check context first** — if above 65%, run `/compact` or `/clear` before starting
2. **Start in Plan Mode** — review this brief, have Claude plan the approach before writing code
3. **Externalize** — create a `PLAN.md` with your task breakdown before coding
4. **You won't finish in 7 minutes** — and that's fine. The goal is to practice the workflow, not complete the project. Take it home and keep building.

## Hints (if stuck)

1. Start in Plan Mode and let Claude break down the work
2. Ask Claude to create the data model first — define what a "ride" looks like
3. Use CSS Grid for the card layout
4. Use CSS custom properties for the status colors so theming is easy to change
