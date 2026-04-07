# Warmup Exercises — Feel the Difference

Four rapid exercises before the main build. Each one demonstrates a pattern you'll use throughout the workshop.

---

## Exercise 1: Effort Levels (3 min)

Create a scratch directory and start a session:

```bash
mkdir ~/workshop-warmup && cd ~/workshop-warmup
claude
```

**Step 1:** Set effort to low:

```
/effort low
```

Then paste this prompt:

```
Write a Python function that validates a theme park reservation date.
Rules: no past dates, no more than 60 days out, no blackout dates
(Dec 24-25, Dec 31, Jul 4). Return a tuple of (bool, error_message).
```

**Step 2:** Now set effort to high and paste the **exact same prompt**:

```
/effort high
```

**Step 3:** Compare. At low effort, you get a bare function — correct but minimal. At high effort, Claude thinks harder — better edge case handling, docstrings, more thoughtful logic.

The default is **medium**. You control the dial. For max reasoning on a single turn, type `ultrathink` in your prompt.

```
/effort medium
```

---

## Exercise 2: Plan Mode (3 min)

**Important:** Use a fresh directory so the prior turn's output doesn't make this a no-op:

```bash
mkdir ~/workshop-warmup-plan && cd ~/workshop-warmup-plan
claude
```

Recreate the validator first (paste the Exercise 1 prompt again at default effort), so there's something to extend.

**Step 1:** Without Plan Mode, ask Claude:

```
Add error handling for malformed input, unit tests covering every
rule, and a CLI wrapper to the reservation validator. The CLI should
accept a date string as an argument and print whether it's valid.
```

Watch it for ~30 seconds — you don't have to wait for it to finish. The point is to see Claude diving in without a plan, not the final output. Interrupt with `Esc` once you've seen enough.

**Step 2:** Enter Plan Mode (`Shift+Tab` twice, or `/plan`). Ask:

```
Before making any changes, analyze what's here. What files exist?
What would need to change to add malformed-input handling, unit tests
covering every rule, and a CLI wrapper? What's the right order of
operations? What could go wrong?
```

Read the plan. Exit Plan Mode (`Shift+Tab` twice). Then:

```
Implement the plan you just described.
```

Compare. Without planning, Claude dives in and may miss dependencies. With Plan Mode, it reads first, thinks about order, then executes a coordinated plan.

---

## Exercise 3: Externalize (2 min)

This one is mechanical — no waiting on Claude to think. Move quickly.


**Step 1:** Bootstrap a CLAUDE.md:

```
/init
```

**Step 2:** Add a rule using `#`:

```
# Always run python -m pytest after every code change. Never skip tests.
```

That rule is now in a file. It survives `/compact`, `/clear`, and session resets. The conversation is temporary. The file is permanent.

**Step 3:** Create a skill. Skills live in their own named subdirectory under `.claude/skills/` — a bare `SKILL.md` directly in `.claude/skills/` will not be loaded.

```bash
mkdir -p .claude/skills/explain-code
```

Then ask Claude to create `.claude/skills/explain-code/SKILL.md`:

```
Create a skill file at .claude/skills/explain-code/SKILL.md with:
- name: explain-code
- description: Explains code with diagrams and analogies
- Instructions: start with an everyday analogy, draw an ASCII diagram,
  walk through step-by-step, highlight one common gotcha
```

Skills are discovered when a session starts. After creating a new skill, exit and restart `claude` so the registry picks it up. Anything you teach Claude in conversation gets compacted away. Anything you write to a file persists.

---

## Exercise 4: Verify (1 min)

Stay in the Exercise 2 directory (`~/workshop-warmup-plan`) — that's where the validator + tests live. Ask Claude:

```
Refactor the validator function to return a dataclass instead of a
tuple. Update the tests to match.
```

Watch what happens. Claude should run the tests after the change because of the rule you added to CLAUDE.md. When a test fails, Claude sees the failure and fixes it. When there are no tests, Claude guesses.

**The key insight:** Advisory instructions (CLAUDE.md) work about 80% of the time. Deterministic verification (tests, linters) works 100%.

---

*After these exercises, you'll choose a build path and apply all four patterns on a real project.*
