# Q2 Portal Redesign — Planning Meeting Transcript

**Date:** 2026-04-07
**Duration:** 47 minutes
**Location:** Conference room 4B (hybrid — 3 dialed in)
**Attendees:**
- Sarah Chen (VP Product, facilitator)
- Alex Kim (Engineering Lead)
- Priya Patel (Design Lead)
- Marcus Johnson (Data Engineering)
- Linh Tran (User Research)
- Jordan Reyes (QA Lead)
- Dana Okafor (joined at 14 min, apologized, was in another meeting)

---

**Sarah:** Okay, thanks everyone. We're tight, 47 minutes on the clock, so let's move. Alex, engineering capacity first.

**Alex:** Yeah, so, through end of Q2 I've got six engineers, but two of them are still finishing the auth refactor and that's running about two weeks behind. Realistically I can put four engineers on new roadmap work until mid-May, maybe later depending on how auth lands.

**Sarah:** Mid-May is tight for the portal redesign timeline.

**Alex:** I know. I know.

**Priya:** Sarah, before we go further — can we actually decide on the design system version? Because I can't finalize mocks without knowing v1 or v2, and last meeting we kind of waved at it.

**Sarah:** I thought we decided v1 last meeting.

**Priya:** We said "probably v1." Nobody actually committed.

**Marcus:** Yeah, and it matters for data too. V2 has the new telemetry hooks. Different wiring.

**Sarah:** Okay. Let's decide now. Alex, from an engineering lens?

**Alex:** V1. Full stop. V2 won't be ready in time, and migrating mid-project is a death march. I'm not willing to own the risk.

**Sarah:** Priya, you good with v1?

**Priya:** V1's fine. I can work with it. I just needed the call.

**Sarah:** Done — design system v1 for all Q2 portal work. Marcus, does that unblock the data layer?

**Marcus:** Yeah, v1's actually simpler. I can have the telemetry spec done by, uh, let me think — probably Thursday next week.

**Sarah:** Thursday the 16th?

**Marcus:** Yeah.

**Sarah:** Give yourself buffer. Let's say Friday the 17th.

**Marcus:** Friday the 17th, works.

**Sarah:** Linh, user research. Where are we?

**Linh:** Honestly? Blocked. I've been trying to get the user testing incentive budget approved since March 20 and finance hasn't moved. I can't recruit external participants without the budget. Twelve thousand dollars, it's not a huge ask, but it's stuck.

**Sarah:** Three weeks on a $12K line item is ridiculous. I'll take this one. I'll escalate to VP Finance today. Linh, send me the exact ask — dollar amount, participant count, timeline — by end of day so I've got the numbers.

**Linh:** Yeah, I'll have it to you by five.

**Sarah:** Thanks. In the meantime, can we dogfood internally as a fallback signal?

**Linh:** I mean, yeah. It's not as good as external users but it would surface the obvious usability issues. I could set up internal sessions next week if the external stays blocked.

**Sarah:** Plan B. If finance doesn't approve by — let's say Monday the 13th — we pivot to internal dogfood. Linh, you own that decision call on Monday.

**Linh:** Monday April 13, got it.

**Jordan:** Quick question. Does the QA timeline change if we go dogfood?

**Linh:** Probably. We'd run them parallel instead of sequential.

**Jordan:** Either way I'll need to rework the test plan. Linh, can I get the final call by Tuesday so I can adjust?

**Linh:** Tuesday April 14. Yes.

*[Dana joins — 14 min in]*

**Dana:** Sorry, sorry, I was in the staff standup. What'd I miss?

**Sarah:** Quick recap — we decided design system v1, we're pulling the incentive budget escalation myself today, and user testing pivots to dogfood if finance is silent by Monday the 13th. We're about to do auth. Catch up after, I don't want to re-litigate.

**Dana:** Got it.

**Sarah:** Alex, auth refactor. Bottom line?

**Alex:** Bottom line is we're two weeks behind. Security review expanded scope — they want session token rotation plus new audit logging, neither of which was in the original plan. I don't think we can pull it back without either slipping launch or putting more bodies on it.

**Sarah:** How many more bodies?

**Alex:** Two engineers, full time, for ten days.

**Sarah:** What's the cost to the other workstreams?

**Alex:** Data migration slips about a week. Frontend rebuild is untouched, different team.

**Marcus:** Week slip on data migration is fine. Dry-run's scheduled for April 15, I can push to April 22.

**Sarah:** Alex, do it — pull two engineers onto auth starting Monday. Marcus, update the data migration schedule, push the dry-run to April 22, send the new timeline to the team by end of week.

**Marcus:** I'll send it Friday the 10th.

**Sarah:** And Alex — I need the security scope thing resolved. Is the expanded auth scope a hard launch requirement or can it be deferred to post-launch hardening? Because if security can live with post-launch, we save a week.

**Alex:** I'll ask them. But I need them to give me a written answer, not a verbal "we'll see."

**Sarah:** Fair. Put a date on it. When do you need the answer by?

**Alex:** Friday the 10th at the latest, otherwise I'm assuming it's in scope and planning accordingly.

**Sarah:** Security team, written answer by Friday April 10. I'll follow up with the security lead separately.

**Priya:** Sarah — one more flag. Brand team is reviewing the design system on Thursday the 9th. If they push back on the color palette, that could cost us another few days.

**Sarah:** Likelihood?

**Priya:** Low. I pre-reviewed with them last week. But I want it flagged.

**Sarah:** Noted as a risk, not a blocker. Don't plan around it.

**Dana:** Sarah, on the auth delay — have we talked about whether we slip the May 5 launch?

**Sarah:** That's the elephant. Alex, honest take?

**Alex:** 50/50. If auth lands with the extra bodies, if finance unblocks user testing by Monday, if integration testing doesn't surface anything horrible — we hit May 5. Any one of those goes sideways, we slip a week.

**Sarah:** I'm not making that call in this room. I'm taking it to the exec team Thursday. Staff meeting. I want the data in front of them, not my opinion.

**Dana:** Fair.

**Sarah:** Jordan, QA. Anything else?

**Jordan:** My lead is on PTO next week, so I'm solo on test planning. Not a blocker, just slower. Also — kind of unrelated — has anyone thought about the load test environment? Because last time we tried to run load tests in staging, it wasn't sized right.

**Sarah:** Let's table the load test thing, I don't want to open a new topic. Write it up and send it to me separately and I'll figure out where it fits.

**Jordan:** Okay.

**Priya:** One more — did we ever decide who's writing the launch comms? Marketing's been asking.

**Sarah:** No, we didn't. I don't want to assign that now either — it's going to depend on the launch date decision. Park it.

**Priya:** Park it, got it.

**Sarah:** Okay, I think we're good. Let me recap.

**Sarah:** Decisions: design system v1 for Q2 portal. Pull two engineers onto auth for ten days starting Monday. Data migration dry-run slips to April 22. User testing pivots to internal dogfood if finance is silent by Monday April 13.

**Sarah:** Actions: Linh sends me the finance ask by end of day today. I escalate to VP Finance today. Marcus sends updated data migration schedule Friday April 10, and telemetry spec Friday April 17. Alex gets written security scope answer by Friday April 10. Linh makes the dogfood call Monday April 13. Jordan reworks test plan after Linh's call, final version by Tuesday April 14. I take the launch slip question to the exec staff meeting Thursday April 9.

**Sarah:** Parked: load test environment sizing (Jordan to write up). Launch comms owner (pending launch date decision).

**Sarah:** Open question: do we slip May 5 launch? Exec staff Thursday.

**Sarah:** Anyone catch anything I missed?

**Alex:** No, I think that's it.

**Priya:** Nope.

**Dana:** Nothing from me.

**Sarah:** Good. Thanks everyone.

*[Meeting ended 2:47 PM]*
