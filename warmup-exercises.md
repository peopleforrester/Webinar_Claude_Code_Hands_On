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

## Exercise 2: Plan Mode (4 min)

**Exit your Exercise 1 session first** (`Ctrl+D` or `/exit`). Then start fresh in a new directory so leftover state from Exercise 1 doesn't make this a no-op:

```bash
mkdir ~/workshop-warmup-plan && cd ~/workshop-warmup-plan
```

Seed a minimal baseline with one paste so we can spend Exercise 2's time on the Plan Mode contrast, not on regenerating Exercise 1:

```bash
cat > validate.py <<'PY'
from datetime import date, timedelta

BLACKOUT = {(12, 24), (12, 25), (12, 31), (7, 4)}

def validate_date(d):
    today = date.today()
    if d < today:
        return False, "past date"
    if (d - today).days > 60:
        return False, "more than 60 days out"
    if (d.month, d.day) in BLACKOUT:
        return False, "blackout date"
    return True, ""
PY

cat > test_validate.py <<'PY'
import unittest
from datetime import date, timedelta
from validate import validate_date

class TestValidateDate(unittest.TestCase):
    def test_future_date_valid(self):
        ok, _ = validate_date(date.today() + timedelta(days=10))
        self.assertTrue(ok)

    def test_past_date_rejected(self):
        ok, _ = validate_date(date.today() - timedelta(days=1))
        self.assertFalse(ok)

if __name__ == "__main__":
    unittest.main()
PY

claude
```

**Step 1:** Without Plan Mode, ask Claude:

```
Add error handling for malformed input, more thorough unit tests
covering every rule, and a CLI wrapper to the reservation validator.
The CLI should accept a date string as an argument and print whether
it's valid.
```

Watch it for ~30 seconds — you don't have to wait for it to finish. The point is to see Claude diving in without a plan, not the final output. Interrupt with `Esc` once you've seen enough.

**Step 2:** Enter Plan Mode by pressing `Shift+Tab` until you see `plan mode` indicated in the input bar (or type `/plan`). Ask:

```
Before making any changes, analyze what's here. What files exist?
What would need to change to add malformed-input handling, more
thorough unit tests covering every rule, and a CLI wrapper? What's
the right order of operations? What could go wrong?
```

Read the plan. Press `Shift+Tab` again to leave Plan Mode (watch the input bar — when `plan mode` disappears, you're out). Then:

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

**Step 2:** Add a rule using the `#` memory shortcut. Type `#` as the **first character of a brand-new prompt** (not pasted into the middle of another message), then this text:

```
# Always run python -m pytest after every code change. Never skip tests.
```

Claude will ask which CLAUDE.md to save it to — choose the **project-level** one.

That rule is now in a file. It survives `/compact`, `/clear`, and session resets. The conversation is temporary. The file is permanent.

**Step 3:** Create a skill. Skills live in their own named subdirectory under `.claude/skills/` — a bare `SKILL.md` directly in `.claude/skills/` will not be loaded.

```bash
mkdir -p .claude/skills/explain-code
```

Then ask Claude to create `.claude/skills/explain-code/SKILL.md`:

```
Create a skill file at .claude/skills/explain-code/SKILL.md. It must
start with YAML front matter between --- fences, with two fields:
  name: explain-code
  description: Explains code with diagrams and analogies
After the closing ---, add markdown instructions: start with an
everyday analogy, draw an ASCII diagram, walk through step-by-step,
highlight one common gotcha.
```

Skills are discovered when a session starts. After creating a new skill, exit and restart `claude` so the registry picks it up. Anything you teach Claude in conversation gets compacted away. Anything you write to a file persists.

---

## Exercise 4: Verify (1 min)

Still in `~/workshop-warmup-plan` with a fresh `claude` session (you just restarted it at the end of Exercise 3 to load the skill). Confirm there's a test file on disk before continuing — `ls test_*.py` should show at least one. If not, paste Exercise 2's "Implement the plan" prompt again first.

Then ask Claude:

```
Refactor the validator function to return a dataclass instead of a
tuple. Update the tests to match.
```

Watch what happens. Claude should run the tests after the change because of the rule you added to CLAUDE.md. When a test fails, Claude sees the failure and fixes it. When there are no tests, Claude guesses.

**The key insight:** Advisory instructions (CLAUDE.md) work about 80% of the time. Deterministic verification (tests, linters) works 100%.

---

*After these exercises, you'll choose a build path and apply all four patterns on a real project.*
