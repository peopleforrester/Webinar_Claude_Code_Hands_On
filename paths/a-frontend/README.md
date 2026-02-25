# Path A: Frontend — Guest Feedback Dashboard

## Overview

Build a single-page **Guest Feedback Dashboard** using plain HTML, CSS, and JavaScript. The dashboard displays guest feedback entries with filtering by category and a sentiment visualization. No frameworks, no build tools, no server — open `index.html` in a browser and it works.

**Best for:** Frontend developers, UI engineers, anyone comfortable with HTML/CSS/JS.

**Prerequisites:** Claude Code CLI installed and working. Nothing else.

---

## Guided Build (20 min)

### Step 1: Set Up (2 min)

Create your project directory and initialize Claude Code:

```bash
mkdir guest-feedback-dashboard && cd guest-feedback-dashboard
claude /init
```

When Claude generates `CLAUDE.md`, add project context by pressing `#` in Claude to attach notes:

- This is a standalone HTML/CSS/JS dashboard. No build tools, no npm.
- Must work by opening `index.html` directly in a browser.
- Use modern vanilla JS (ES6+). No external CDN dependencies.

### Step 2: Plan First (3 min)

Enter **Plan Mode** (press `Shift+Tab` twice), then give Claude this prompt:

> I'm building a guest feedback dashboard. Here are the requirements:
>
> - Display feedback entries with category, rating, and comment
> - Filter by category (Attractions, Dining, Service, Facilities)
> - Show a sentiment summary (positive/neutral/negative counts)
> - Include sample data embedded in the JS (at least 15 entries)
> - Plan the file structure, component layout, and data model
> - Don't write any code yet

Review the plan Claude produces. Approve it or ask for changes before moving on.

### Step 3: Build (10 min)

Exit Plan Mode. Tell Claude to implement the plan:

- Create all files
- Start with the data model and sample data (at least 15 entries)
- Then HTML structure, JS logic, CSS styling

> **Note:** You can copy the sample data from `sample-data/guest-feedback.json` in this directory as a starting point for your embedded data.

Open `index.html` in your browser to verify it works after Claude finishes.

### Step 4: Iterate (3 min)

Ask Claude to polish the dashboard with these enhancements:

- Add a **count badge** next to each filter button showing how many entries match
- Make the sentiment summary a **simple bar chart using CSS only** (no libraries)
- Add a **"sort by rating" toggle** button

### Step 5: Create a Skill (2 min)

Create a reusable skill that encodes your project conventions:

> Create a skill at `.claude/skills/ui-component/SKILL.md` that captures these conventions:
> vanilla JS only, no external dependencies, accessible HTML with proper ARIA labels,
> CSS custom properties for theming.

This skill can be reused in future projects to enforce the same standards.

---

## Check Your Context

Run `/context` to see how much of your context window is used. If you are above **65%**, demonstrate `/compact` before moving on to the independent build. This is a key workflow habit — managing context keeps Claude effective on longer tasks.

---

## Next Steps

- See **[independent-brief.md](independent-brief.md)** for the self-directed challenge (Park Wait Times Display Board).
- See [`skills-examples/ui-component/SKILL.md`](../../skills-examples/ui-component/SKILL.md) in the repo root for an example skill file for this path.
