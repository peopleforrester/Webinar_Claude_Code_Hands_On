# Guided Build: Reservation Validation API

Build a REST API that validates Disney theme park reservation requests. The API enforces business rules (date ranges, party size limits, park validation) and returns clear error messages. You will build this entirely with stdlib -- no frameworks, no databases, no package installs.

**Time estimate:** 20 minutes

---

## Step 1: Set Up (2 min)

Create a fresh project directory and initialize Claude Code context:

```bash
mkdir reservation-api && cd reservation-api
claude /init
```

When Claude generates `CLAUDE.md`, press **#** (the context mention key) to add project context. Include these points:

- This is a **[Node.js / Python]** REST API (pick one and stick with it)
- No external database -- use in-memory data structures
- No external packages -- stdlib only
- All endpoints must have input validation and proper error responses
- Include tests for every endpoint

Claude will update `CLAUDE.md` with these constraints. Confirm the file looks right before moving on.

---

## Step 2: Plan First (3 min)

Enter **Plan Mode** by pressing `Shift+Tab` twice (or type `plan` at the prompt). Give Claude the full specification:

> Build a reservation validation API with these endpoints:
>
> - **POST /reservations** -- Create a reservation (validate: date, party size 1-20, park name)
> - **GET /reservations** -- List all reservations (filter by date, park)
> - **GET /reservations/:id** -- Get one reservation
> - **DELETE /reservations/:id** -- Cancel a reservation
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

Ask questions or request changes while still in Plan Mode. This is free -- no code is written until you leave.

---

## Step 3: Build (10 min)

Exit Plan Mode (press `Shift+Tab` twice or type `code`). Tell Claude:

> Implement the plan. Start with the data model, then routes, then validation, then tests. After writing each file, run the tests and fix any failures before moving on.

Watch Claude work through the build. Key things to observe:
- Claude reads `CLAUDE.md` constraints before writing code
- Tests run after each file and failures are fixed inline
- Validation logic enforces every business rule
- Error responses follow the format from the plan

Test the API yourself once Claude finishes:

```bash
# Start the server (in one terminal)
python main.py   # or: node index.js

# In another terminal, create a reservation
curl -X POST http://localhost:3000/reservations \
  -H "Content-Type: application/json" \
  -d '{"guestEmail":"guest@example.com","park":"EPCOT","date":"2026-03-15","partySize":4}'

# List reservations
curl http://localhost:3000/reservations

# Try an invalid request (party size too large)
curl -X POST http://localhost:3000/reservations \
  -H "Content-Type: application/json" \
  -d '{"guestEmail":"guest@example.com","park":"EPCOT","date":"2026-03-15","partySize":25}'
```

---

## Step 4: Iterate (3 min)

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

This skill becomes reusable context for future API work. Review what Claude generates -- it should codify the patterns from this build, not just copy code.

---

## What's Next

- **Independent challenge:** Open [independent-brief.md](independent-brief.md) for a self-directed microservice build using the workflow you just practiced.
- **Skill reference:** See [skills-examples/api-scaffold/SKILL.md](../../skills-examples/api-scaffold/SKILL.md) for an example of a well-structured API scaffold skill.
