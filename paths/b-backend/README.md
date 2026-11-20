# Path B: Backend — Reservation Validation API

## Overview

Build a REST API that validates theme park reservation requests. The API enforces business rules (date ranges, party size limits, park validation) and returns clear error messages. You will build this entirely with stdlib — no frameworks, no databases, no package installs.

**Best for:** Backend developers, API engineers, anyone who wants to see Claude Code drive a server-side build from plan to working tests.

**Prerequisites:** Python 3.11+ **or** Node.js 22 LTS+ installed, plus Claude Code CLI.

---

## What's in This Directory

| File | Purpose |
|------|---------|
| [guided-brief.md](guided-brief.md) | Step-by-step guided build (28 min, instructor-led) |
| [independent-brief.md](independent-brief.md) | Self-directed challenge: Guest Dining Preferences Microservice |
| [CLAUDE.md](CLAUDE.md) | Path-specific project conventions — copy into your build directory |
| [sample-data/sample-reservations.json](sample-data/sample-reservations.json) | 10 example reservation requests (valid and invalid) |

### Sample reservation dates

The date rules ("no reservations in the past", "no more than 60 days out") depend on the day you run the API, so the sample dates are written relative to a workshop day. Each `_note` ends with its offset, for example `(workshop day +25)`.

- **Workshop day:** 2026-12-01
- **Works as labelled for a workshop held:** 2026-11-07 through 2026-12-22

For a delivery outside that window, move every date in the file forward by the number of days between 2026-12-01 and the new workshop day, then update the two dates above. The offsets in the notes stay the same. Move the date in the [guided-brief.md](guided-brief.md) curl examples (workshop day +21) by the same number of days. Asking Claude to do this is a quick warm-up exercise.

## Quick Start

1. Read the [guided-brief.md](guided-brief.md) and follow along with the instructor
2. When done, try the [independent-brief.md](independent-brief.md) challenge on your own
3. See [`skills-examples/api-scaffold/SKILL.md`](../../skills-examples/api-scaffold/SKILL.md) for an example skill for this path
