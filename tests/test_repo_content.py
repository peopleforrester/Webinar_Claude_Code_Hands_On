"""Content-integrity tests for the workshop repo (stdlib only).

The repo ships docs, sample data, skill examples and starter settings rather
than application code, so these tests check that what attendees copy and rely
on stays well-formed and consistent with the briefs.

Run: python3 -m unittest discover -s tests
"""

import datetime
import json
import os
import re
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Local-only paths from .gitignore that may exist on a maintainer's machine.
SKIP_DIRS = {
    ".git", ".claude", "docs", "transcripts", "claude-ai-context", ".claude-history",
    "node_modules", "output", "__pycache__",
    "tmp",  # scratch space for automated runs, never shipped
}
SKIP_FILES = {"ACTION_ITEMS.md", "CLAUDE.local.md"}

PATHS = ["a-frontend", "b-backend", "c-infrastructure", "d-data", "e-business"]
PARKS = {"Coral Kingdom", "Skyward Summit", "Harbor Gardens", "Meadow Haven"}

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")


def repo_files(suffix):
    found = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            if name.endswith(suffix) and name not in SKIP_FILES:
                found.append(os.path.join(dirpath, name))
    return sorted(found)


def load_json(*parts):
    with open(os.path.join(ROOT, *parts), encoding="utf-8") as f:
        return json.load(f)


def rel(path):
    return os.path.relpath(path, ROOT)


class TestJson(unittest.TestCase):
    def test_all_json_files_parse(self):
        files = repo_files(".json")
        self.assertTrue(files)
        for path in files:
            with self.subTest(file=rel(path)):
                with open(path, encoding="utf-8") as f:
                    json.load(f)


class TestStarterSettings(unittest.TestCase):
    def test_deny_rules_enforce_conventions(self):
        settings = load_json(".claude", "settings.json")
        deny = settings["permissions"]["deny"]
        self.assertIsInstance(deny, list)
        for rule in deny:
            self.assertIsInstance(rule, str)
        # CLAUDE.md conventions: no network requests, no package installs.
        for rule in ["Bash(curl *)", "Bash(wget *)", "Bash(pip *)",
                     "Bash(pip3 *)", "Bash(npm *)"]:
            self.assertIn(rule, deny)


class TestMarkdown(unittest.TestCase):
    def test_relative_links_resolve(self):
        broken = []
        for path in repo_files(".md"):
            with open(path, encoding="utf-8") as f:
                text = f.read()
            for target in LINK_RE.findall(text):
                if re.match(r"^[a-z]+:", target) or target.startswith("#"):
                    continue
                target = target.split("#", 1)[0]
                resolved = os.path.normpath(
                    os.path.join(os.path.dirname(path), target))
                if not os.path.exists(resolved):
                    broken.append(f"{rel(path)} -> {target}")
        self.assertEqual(broken, [])

    def test_claude_md_files_stay_under_200_lines(self):
        files = [p for p in repo_files(".md")
                 if os.path.basename(p) in ("CLAUDE.md", "AGENTS.md")]
        self.assertTrue(files)
        for path in files:
            with self.subTest(file=rel(path)):
                with open(path, encoding="utf-8") as f:
                    self.assertLess(len(f.readlines()), 200)

    def test_root_claude_md_points_at_agents_md(self):
        claude = os.path.join(ROOT, "CLAUDE.md")
        agents = os.path.join(ROOT, "AGENTS.md")
        self.assertTrue(os.path.isfile(agents))
        self.assertTrue(os.path.samefile(claude, agents))


class TestGateCommands(unittest.TestCase):
    def setUp(self):
        with open(os.path.join(ROOT, "AGENTS.md"), encoding="utf-8") as f:
            self.lines = f.read().splitlines()

    def test_agents_md_declares_one_test_command(self):
        declared = [l for l in self.lines if l.startswith("Test command: `")]
        self.assertEqual(len(declared), 1)

    def test_agents_md_declares_no_e2e_command(self):
        # decisions.md, 2026-11-20: the repo has no tests against real
        # services, so the heavy gate runs the Test command.
        declared = [l for l in self.lines if l.startswith("E2E command:")]
        self.assertEqual(declared, [])


class TestNoHardcodedRepoPaths(unittest.TestCase):
    # The maintainer's home "repos" tree gets restructured (issue #4); a path
    # into it from a rule, skill or script goes dead silently. The workshop
    # also forbids hardcoded absolute paths, so none may appear at all.
    REPO_PATH_RE = re.compile(
        r"(~|\$HOME|\$\{HOME\}|/home/[A-Za-z0-9_.-]+)/repos(?![A-Za-z0-9_-])")

    def test_pattern_catches_each_home_spelling(self):
        tail = "/" + "repos/mrf/second-brain"
        for home in ["~", "$HOME", "${HOME}", "/home/michael"]:
            with self.subTest(home=home):
                self.assertTrue(self.REPO_PATH_RE.search(home + tail))
        self.assertIsNone(self.REPO_PATH_RE.search("~/" + "repository"))
        self.assertIsNone(
            self.REPO_PATH_RE.search("https://api.github.com/" + "repos/x"))

    def test_no_file_references_a_path_under_home_repos(self):
        # .claude/settings.json is the only shipped file under .claude/.
        files = repo_files("") + [os.path.join(ROOT, ".claude", "settings.json")]
        hits = []
        for path in files:
            try:
                with open(path, encoding="utf-8") as f:
                    lines = f.readlines()
            except UnicodeDecodeError:
                continue
            for number, line in enumerate(lines, 1):
                match = self.REPO_PATH_RE.search(line)
                if match:
                    hits.append(f"{rel(path)}:{number}: {match.group(0)}")
        self.assertEqual(hits, [])


class TestPaths(unittest.TestCase):
    def test_each_path_has_its_core_docs(self):
        for name in PATHS:
            for doc in ["README.md", "CLAUDE.md", "guided-brief.md",
                        "independent-brief.md"]:
                with self.subTest(path=name, doc=doc):
                    self.assertTrue(os.path.isfile(
                        os.path.join(ROOT, "paths", name, doc)))


class TestSkillExamples(unittest.TestCase):
    def test_skills_have_frontmatter_matching_directory(self):
        base = os.path.join(ROOT, "skills-examples")
        skills = sorted(os.listdir(base))
        self.assertTrue(skills)
        for skill in skills:
            with self.subTest(skill=skill):
                with open(os.path.join(base, skill, "SKILL.md"),
                          encoding="utf-8") as f:
                    text = f.read()
                match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
                self.assertIsNotNone(match, "missing frontmatter")
                fields = dict(
                    line.split(":", 1) for line in match.group(1).splitlines()
                    if ":" in line)
                fields = {k.strip(): v.strip() for k, v in fields.items()}
                self.assertEqual(fields.get("name"), skill)
                self.assertTrue(fields.get("description"))
                self.assertTrue(text[match.end():].strip(), "empty body")


class TestGuestFeedbackSample(unittest.TestCase):
    def setUp(self):
        self.entries = load_json(
            "paths", "a-frontend", "sample-data", "guest-feedback.json")

    def test_has_at_least_15_entries_with_unique_ids(self):
        # guided-brief.md asks for at least 15 entries.
        self.assertGreaterEqual(len(self.entries), 15)
        ids = [e["id"] for e in self.entries]
        self.assertEqual(len(ids), len(set(ids)))

    def test_entries_match_dashboard_model(self):
        categories = {"Attractions", "Dining", "Service", "Facilities"}
        sentiments = {"positive", "neutral", "negative"}
        for e in self.entries:
            with self.subTest(id=e.get("id")):
                self.assertIn(e["category"], categories)
                self.assertIn(e["sentiment"], sentiments)
                self.assertIn(e["rating"], range(1, 6))
                self.assertTrue(e["comment"].strip())
                datetime.date.fromisoformat(e["date"])
        self.assertEqual({e["category"] for e in self.entries}, categories)
        self.assertEqual({e["sentiment"] for e in self.entries}, sentiments)


class TestReservationSample(unittest.TestCase):
    def setUp(self):
        self.requests = load_json(
            "paths", "b-backend", "sample-data", "sample-reservations.json")

    def test_has_valid_and_invalid_examples(self):
        notes = [r["_note"] for r in self.requests]
        for note in notes:
            self.assertRegex(note, r"^(Valid|INVALID)\b")
        self.assertTrue(any(n.startswith("Valid") for n in notes))
        self.assertTrue(any(n.startswith("INVALID") for n in notes))

    def test_examples_agree_with_date_independent_rules(self):
        # Date rules are relative to "today", so only park and party size
        # are checked here.
        for r in self.requests:
            with self.subTest(note=r["_note"], guest=r["guestEmail"]):
                self.assertIn("@", r["guestEmail"])
                datetime.date.fromisoformat(r["date"])
                park_ok = r["park"] in PARKS
                size_ok = 1 <= r["partySize"] <= 20
                note = r["_note"]
                if note.startswith("Valid"):
                    self.assertTrue(park_ok and size_ok)
                elif "party size" in note:
                    self.assertFalse(size_ok)
                elif "park" in note:
                    self.assertFalse(park_ok)

    def test_dates_follow_workshop_day_offsets(self):
        # The date rules depend on "today", so instead of reading the clock
        # this checks the file against the workshop day the README states:
        # each date is that day plus the offset in its note, the offsets
        # agree with the notes, and the README's delivery window is the one
        # the offsets allow (issue #9).
        with open(os.path.join(ROOT, "paths", "b-backend", "README.md"),
                  encoding="utf-8") as f:
            readme = f.read()
        day = re.search(r"\*\*Workshop day:\*\* (\d{4}-\d{2}-\d{2})", readme)
        window = re.search(r"\*\*Works as labelled for a workshop held:\*\* "
                           r"(\d{4}-\d{2}-\d{2}) through (\d{4}-\d{2}-\d{2})",
                           readme)
        self.assertIsNotNone(day, "README must state the workshop day")
        self.assertIsNotNone(window, "README must state the delivery window")
        workshop = datetime.date.fromisoformat(day.group(1))

        # Each bound is the latest/earliest workshop day, as an offset from
        # the stated one, at which every note still holds.
        earliest, latest = -10**6, 10**6
        for r in self.requests:
            note = r["_note"]
            with self.subTest(note=note, guest=r["guestEmail"]):
                m = re.search(r"\(workshop day ([+-]\d+)\)$", note)
                self.assertIsNotNone(m, "note must end with its offset")
                offset = int(m.group(1))
                date = datetime.date.fromisoformat(r["date"])
                self.assertEqual(
                    date, workshop + datetime.timedelta(days=offset))
                if "in the past" in note:
                    self.assertLess(offset, 0)
                    earliest = max(earliest, offset + 1)
                elif "60 days out" in note:
                    self.assertGreater(offset, 60)
                    latest = min(latest, offset - 61)
                else:
                    # Valid, or invalid for a date-independent reason:
                    # the date itself must pass "today through 60 days".
                    self.assertTrue(0 <= offset <= 60)
                    earliest = max(earliest, offset - 60)
                    latest = min(latest, offset)
        self.assertLessEqual(earliest, 0)
        self.assertGreaterEqual(latest, 0)
        self.assertEqual(
            (window.group(1), window.group(2)),
            ((workshop + datetime.timedelta(days=earliest)).isoformat(),
             (workshop + datetime.timedelta(days=latest)).isoformat()))

    def test_guided_brief_dates_valid_across_window(self):
        # The guided brief's curl examples create reservations, so their
        # dates must pass "today through 60 days" on every workshop day in
        # the README's window (issue #11). Every date in the brief, prose
        # included, must also be the workshop day plus the offset the README
        # gives for it, so re-dating by the README's note keeps them in step.
        base = os.path.join(ROOT, "paths", "b-backend")
        with open(os.path.join(base, "README.md"), encoding="utf-8") as f:
            readme = f.read()
        day = re.search(r"\*\*Workshop day:\*\* (\d{4}-\d{2}-\d{2})", readme)
        window = re.search(r"\*\*Works as labelled for a workshop held:\*\* "
                           r"(\d{4}-\d{2}-\d{2}) through (\d{4}-\d{2}-\d{2})",
                           readme)
        offset = re.search(r"guided-brief\.md\)[^.]*\(workshop day \+(\d+)\)",
                           readme)
        self.assertIsNotNone(day, "README must state the workshop day")
        self.assertIsNotNone(window, "README must state the delivery window")
        self.assertIsNotNone(offset, "README must state the brief's offset")
        expected = (datetime.date.fromisoformat(day.group(1))
                    + datetime.timedelta(days=int(offset.group(1))))
        first = datetime.date.fromisoformat(window.group(1))
        last = datetime.date.fromisoformat(window.group(2))
        with open(os.path.join(base, "guided-brief.md"), encoding="utf-8") as f:
            brief = f.read()
        self.assertRegex(brief, r'"date"\s*:\s*"\d{4}-\d{2}-\d{2}"',
                         "guided brief has no example dates")
        self.assertIn("plus %s days" % offset.group(1), brief)
        for d in re.findall(r"\d{4}-\d{2}-\d{2}", brief):
            with self.subTest(date=d):
                date = datetime.date.fromisoformat(d)
                self.assertEqual(date, expected)
                self.assertGreaterEqual(date, last)
                self.assertLessEqual(date, first + datetime.timedelta(days=60))


class TestOperationsLogSample(unittest.TestCase):
    def test_entries_match_log_format(self):
        logs = load_json(
            "paths", "d-data", "sample-data", "operations-logs.json")
        self.assertGreaterEqual(len(logs), 10)
        for e in logs:
            with self.subTest(entry=e):
                self.assertEqual(set(e), {"timestamp", "operation",
                                          "duration_ms", "status", "location"})
                datetime.datetime.fromisoformat(
                    e["timestamp"].replace("Z", "+00:00"))
                self.assertIsInstance(e["duration_ms"], int)
                self.assertGreaterEqual(e["duration_ms"], 0)
                self.assertIn(e["status"], {"success", "error", "timeout"})
                self.assertIn(e["location"], PARKS)

    def test_readme_states_actual_entry_count(self):
        logs = load_json(
            "paths", "d-data", "sample-data", "operations-logs.json")
        with open(os.path.join(ROOT, "paths", "d-data", "README.md"),
                  encoding="utf-8") as f:
            readme = f.read()
        m = re.search(r"\b(\d+) sample log entries\b", readme)
        self.assertIsNotNone(m, "Path D README no longer states a log count")
        self.assertEqual(int(m.group(1)), len(logs))


if __name__ == "__main__":
    unittest.main()
