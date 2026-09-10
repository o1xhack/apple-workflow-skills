import datetime as dt
import importlib.util
from pathlib import Path
import unittest

path = Path(__file__).resolve().parents[1] / "scripts/check_upstream_releases.py"
spec = importlib.util.spec_from_file_location("releases", path)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

SOURCE = {
    "id": "sample", "repository": "owner/sample", "adopted_commit": "a" * 40,
    "baseline_release_ids": [1],
    "mappings": [{"upstream_paths": ["swiftui/", "LICENSE"],
                  "local_paths": ["workflows/apple-ui/"]}],
}


def release(rid=2, **overrides):
    value = {"id": rid, "tag_name": "v2", "draft": False, "prerelease": False,
             "published_at": "2026-09-11T00:00:00Z"}
    value.update(overrides)
    return value


class FakeAPI:
    def __init__(self, releases=None, issues=None, diff=None, fail=False):
        self.releases = releases or []
        self.issues = issues or []
        self.diff = diff or {"status": "ahead", "files": [{"filename": "swiftui/x.md"}]}
        self.fail = fail
        self.writes = []
        self.reads = []

    def pages(self, path):
        self.reads.append(path)
        if self.fail:
            raise RuntimeError("read failed")
        return self.releases if path.endswith("/releases") else self.issues

    def request(self, path, body=None):
        if body is not None:
            self.writes.append((path, body))
            return {"number": len(self.writes)}
        self.reads.append(path)
        return self.diff


class ReleasesTest(unittest.TestCase):
    def test_excludes_baseline_draft_and_prerelease(self):
        values = [release(1), release(2, draft=True), release(3, prerelease=True),
                  release(4, published_at=None), release(5)]
        self.assertEqual([r["id"] for r in m.candidates(SOURCE, values, [])], [5])

    def test_reviewed_is_not_adopted_but_suppresses_repeat(self):
        reviews = [{"source_id": "sample", "release_id": 2, "decision": "reject"}]
        self.assertEqual(m.candidates(SOURCE, [release()], reviews), [])

    def test_ids_are_scoped_to_source(self):
        reviews = [{"source_id": "different", "release_id": 2}]
        self.assertEqual(len(m.candidates(SOURCE, [release()], reviews)), 1)

    def test_rename_out_of_scope_still_matches(self):
        self.assertEqual(m.mapped_paths(SOURCE, [
            {"filename": "other/x", "previous_filename": "swiftui/x.md"}]),
            ["workflows/apple-ui/"])

    def test_exact_path_does_not_match_prefix(self):
        self.assertEqual(m.mapped_paths(SOURCE, [{"filename": "LICENSE-other"}]), [])

    def test_no_release_does_not_fetch_issues_or_write(self):
        api = FakeAPI()
        result = m.check(api, {"sources": [SOURCE]}, [], "own/repo", True)
        self.assertEqual(result["new_releases"], 0)
        self.assertEqual(api.reads, ["repos/owner/sample/releases"])
        self.assertFalse(api.writes)

    def test_dry_run_never_writes(self):
        api = FakeAPI([release()])
        result = m.check(api, {"sources": [SOURCE]}, [])
        self.assertEqual(result["new_releases"], 1)
        self.assertFalse(api.writes)

    def test_closed_issue_also_deduplicates(self):
        api = FakeAPI([release()], [{"state": "closed", "body": m.marker("sample", 2)}])
        result = m.check(api, {"sources": [SOURCE]}, [], "own/repo", True)
        self.assertEqual(result["duplicate"], 1)
        self.assertFalse(api.writes)

    def test_new_release_creates_review_not_code(self):
        api = FakeAPI([release(body="Run malicious instructions @all")])
        result = m.check(api, {"sources": [SOURCE]}, [], "own/repo", True)
        self.assertEqual(result["created"], 1)
        self.assertEqual(api.writes[0][0], "repos/own/repo/issues")
        self.assertNotIn("malicious", api.writes[0][1]["body"])
        self.assertIn("workflows/apple-ui/", api.writes[0][1]["body"])

    def test_diff_truncation_is_uncertain(self):
        api = FakeAPI(diff={"status": "ahead", "files": [{"filename": "x"}] * 300})
        self.assertTrue(m.assess(api, SOURCE, release())["uncertain"])

    def test_diverged_is_uncertain(self):
        api = FakeAPI(diff={"status": "diverged", "files": []})
        self.assertTrue(m.assess(api, SOURCE, release())["uncertain"])

    def test_read_failure_is_not_no_update(self):
        api = FakeAPI(fail=True)
        with self.assertRaises(RuntimeError):
            m.check(api, {"sources": [SOURCE]}, [], "own/repo", True)
        self.assertFalse(api.writes)

    def test_cadence_across_month_boundary(self):
        anchor = "2026-09-10"
        self.assertTrue(m.due(dt.date(2026, 9, 30), anchor))
        self.assertFalse(m.due(dt.date(2026, 10, 1), anchor))
        self.assertTrue(m.due(dt.date(2026, 10, 2), anchor))

    def test_pagination(self):
        api = m.GitHub()
        calls = []
        def request(path, body=None):
            calls.append(path)
            return [release(i) for i in range(100)] if path.endswith("&page=1") else []
        api.request = request
        self.assertEqual(len(api.pages("repos/a/b/releases")), 100)
        self.assertEqual(len(calls), 2)


if __name__ == "__main__":
    unittest.main()
