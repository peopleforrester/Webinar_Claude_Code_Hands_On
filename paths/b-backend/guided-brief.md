# Guided Build: Reservation Validation API

Build a REST API that validates theme park reservation requests. The API enforces business rules (date ranges, party size limits, park validation) and returns clear error messages. You will build this entirely with stdlib — no frameworks, no databases, no package installs.

**Time estimate:** 28 minutes

---

## Step 1: Set Up + Externalize (3 min)

Create a fresh project directory and initialize Claude Code context:

```bash
mkdir reservation-api && cd reservation-api
claude /init
```

When Claude generates `CLAUDE.md`, press **#** (the context mention key) to add project context. Include these points:

- This is a **[Node.js / Python]** REST API (pick one and stick with it)
- No external database — use in-memory data structures
- No external packages — stdlib only
- All endpoints must have input validation and proper error responses
- Run tests after every change. Never skip.

Claude will update `CLAUDE.md` with these constraints. Confirm the file looks right before moving on.

> **Pillar 3 in action:** You just externalized your project conventions. Claude loads this every session.

---

## Step 2: Plan First (4 min)

Enter **Plan Mode** (use `Shift+Tab` to cycle to Plan Mode, or type `/plan`). Give Claude the full specification:

> Build a reservation validation API with these endpoints:
>
> - **POST /reservations** — Create a reservation (validate: date, party size 1-20, park name)
> - **GET /reservations** — List all reservations (filter by date, park)
> - **GET /reservations/:id** — Get one reservation
> - **DELETE /reservations/:id** — Cancel a reservation
>
> Business rules:
> - No reservations more than 60 days out
> - No reservations in the past
> - Max 3 active reservations per guest email
> - Park must be one of: Magic Kingdom, EPCOT, Hollywood Studios, Animal Kingdom
>
> Plan the project structure, data models, validation logic, and error response format. Don't write any code yet.

Review the plan Claude produces. Look for:
- A clear file/folder layout
- A data model for reservations (id, guestEmail, park, date, partySize, status)
- A validation module separate from routing
- A consistent error format
- A test strategy

Ask questions or request changes while still in Plan Mode. This is free — no code is written until you leave.

> **Note:** See `sample-data/sample-reservations.json` in this directory for example requests (both valid and invalid) that demonstrate the business rules.

> **Pillar 2 in action:** You planned before coding. The plan identifies dependencies and order of operations before a single line is written.

---

## Step 3: Build + Verify (12 min)

Exit Plan Mode (use `Shift+Tab` to cycle back to Default). Tell Claude:

> Implement the plan. Start with the data model, then routes, then validation, then tests. After writing each file, run the tests and fix any failures before moving on.

Watch Claude work through the build. Key things to observe:
- Claude reads `CLAUDE.md` constraints before writing code
- Tests run after each file and failures are fixed inline
- Validation logic enforces every business rule
- Error responses follow the format from the plan

> **Pillar 4 in action:** Claude runs tests after each change because of the rule you externalized. When a test fails, Claude self-corrects.

Test the API yourself once Claude finishes:

```bash
# Start the server (in one terminal)
python main.py   # or: node index.js

# In another terminal, create a reservation
curl -X POST http://localhost:3000/reservations \
  -H "Content-Type: application/json" \
  -d '{"guestEmail":"guest@example.com","park":"EPCOT","date":"2026-04-20","partySize":4}'

# List reservations
curl http://localhost:3000/reservations

# Try an invalid request (party size too large)
curl -X POST http://localhost:3000/reservations \
  -H "Content-Type: application/json" \
  -d '{"guestEmail":"guest@example.com","park":"EPCOT","date":"2026-04-20","partySize":25}'
```

---

## Step 4: Iterate + Verify (5 min)

Add three enhancements. Give Claude this prompt:

> Add these features:
> 1. **Rate limiting:** Max 10 requests per minute per IP. Use an in-memory counter. Return 429 when exceeded.
> 2. **Health endpoint:** GET /health returns JSON with server uptime (seconds) and total reservation count.
> 3. **Request logging middleware:** Log every request with method, path, response status code, and duration in ms.

Watch how Claude layers new functionality onto the existing codebase. Note that it updates tests for the new features.

---

## Step 5: Create a Skill (2 min)

Tell Claude:

> Create a Claude Code skill at `.claude/skills/api-scaffold/SKILL.md` that captures our API conventions: the input validation pattern, the error response format, the test structure, and the middleware order.

This skill becomes reusable context for future API work. Review what Claude generates — it should codify the patterns from this build, not just copy code.

---

## Check Your Context

Run `/context` to see how much of your context window is used. If you are above **65%**, run `/compact` before moving on to the independent build.

> **Pillar 1 in action:** The context window is finite. Monitor it. One feature per session. Quality degrades as it fills.

---

## What's Next

- **Independent challenge:** Open [independent-brief.md](independent-brief.md) for a Guest Dining Preferences Microservice you can build on your own.
- **Skill reference:** See [skills-examples/api-scaffold/SKILL.md](../../skills-examples/api-scaffold/SKILL.md) in the repo root for an example of a well-structured API scaffold skill.
