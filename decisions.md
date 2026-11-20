# Decisions

## 2026-11-20 · No E2E command for the heavy gate

Issue #10 asked for an `E2E command:` line in AGENTS.md wherever the repo has
end-to-end, browser or integration tests against real services. It has none.
The tracked files are Markdown docs, JSON sample data, skill examples and the
starter `.claude/settings.json`. The only code is `tests/test_repo_content.py`,
a stdlib content-integrity suite that needs no network, service or data outside
the clone. AGENTS.md's own conventions rule out network requests and any
external runtime for testing.

Decision: AGENTS.md declares no `E2E command:` line and says why, and the heavy
gate runs the light Test command. This follows the standing rule in
peopleforrester/hecaton#103: a repo with no real-service tests gets no E2E
line, with the reason recorded here. `TestGateCommands` in
`tests/test_repo_content.py` fails if an `E2E command:` line is added without
this entry being revisited.

Revisit this if the repo gains tests that need a browser, a network service or
data outside the clone. Declare their command then, and update the test.

## 2026-11-20 · No conference material here

Issue #6 relayed a notice from peopleforrester/conference-knowledge: that repo
is now the source of truth for conferences, CFPs, submissions, attendance,
organizer contacts, the speaking record and event travel. Any copy held
elsewhere is to be listed in an `agent-task` issue there and replaced with a
pointer.

A sweep of every tracked file found none. The repo is the companion to a
hands-on Claude Code workshop for one corporate client. Its only event facts
are that workshop's own delivery history: `instructor/live-card.md`'s title
(2026-04-09, 12:00 ET) and PROJECT_STATE.md's "Workshop delivered" line
(2026-04-09 and again in May). That is a client training, not a conference.
conference-knowledge also chose not to track it: its decisions.md entry of
2026-10-24 ("question 303") retired the record of this client's 2026-04-08
talk on Michael's word, because it is not in use. So no issue was filed there,
since it would ask that repo to track something Michael already dropped. The
dates stay here as workshop history. Other dates in the repo are sample data
(park reservations, operations logs, a fictional meeting transcript), and
"Skyward Summit" is a fictional park, not an event.

The optional AGENTS.md "Where things live" pointer was not added. AGENTS.md is
the attendee-facing CLAUDE.md teaching example (CLAUDE.md links to it), and a
public workshop repo has no use for a link to a private conference repo.

Revisit this if the repo starts holding conference material, such as a CFP
draft for this workshop or travel for a delivery at an event. Read and change
that information in conference-knowledge, by filing an `agent-task` issue there.
