# Independent Challenge: Guest Dining Preferences Microservice

You have **7 minutes**. The goal is to practice the Claude Code workflow, not to finish the entire service. Prioritize planning and iterating over completeness.

---

## Requirements

Build a microservice that stores guest dining preferences and recommends restaurants based on those preferences.

### Endpoints

| Method | Path | Description |
|--------|------|-------------|
| POST | /preferences | Store dietary restrictions and cuisine preferences for a guest |
| GET | /preferences/:guestId | Retrieve stored preferences for a guest |
| GET | /restaurants/recommend?guestId=X | Return mock restaurant suggestions matching the guest's preferences |

### Validation Rules
- At least one dietary restriction or cuisine preference is required when creating preferences
- `guestId` must be alphanumeric (letters and numbers only, no spaces or special characters)
- Return clear error messages for invalid input

### Data
- In-memory storage for guest preferences (no database)
- Pre-load 10 mock restaurants, each with `cuisineTags` (e.g., "American", "Japanese", "Mexican") and `dietaryOptions` (e.g., "vegetarian", "gluten-free", "nut-free")
- Recommendation logic: filter restaurants where tags overlap with the guest's stored preferences

### Tests
- Full test coverage for all three endpoints
- Test validation rules (missing preferences, invalid guestId)
- Test recommendation matching (guest with "vegetarian" preference gets restaurants with "vegetarian" in dietaryOptions)

---

## Workflow Reminders

1. **Check context first** -- if your context window is above 65%, run `/compact` or `/clear` before starting
2. **Start in Plan Mode** -- review this brief with Claude, have it plan the approach before writing code
3. **Externalize the plan** -- create a `PLAN.md` with your task breakdown before coding starts
4. **You won't finish in 7 minutes** -- that's fine. Practice the workflow (plan, build, test, iterate). Take the project home to complete it.

---

## Hints (If Stuck)

1. **Plan Mode first.** Design the matching algorithm before writing any code. How will you score or filter restaurants against preferences?
2. **Model restaurants as objects** with `cuisineTags` and `dietaryOptions` arrays. Example:
   ```json
   {
     "id": "r1",
     "name": "Coral Reef Restaurant",
     "cuisineTags": ["Seafood", "American"],
     "dietaryOptions": ["gluten-free", "vegetarian"]
   }
   ```
3. **Recommendation = filter.** A restaurant matches if any of its tags overlap with the guest's preferences. Start with a simple intersection check -- you can rank by overlap count later.
4. **Use `/effort high`** for the matching logic. Tell Claude to spend more time reasoning through edge cases (guest with no matching restaurants, guest not found, etc.).
