import importlib.util
import json
from pathlib import Path
import re
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("validate", ROOT / "scripts/validate.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
ARCHIVE = Path("external-sources/apple/iphone-duo/2026-09-10")


class ExternalSourcesTest(unittest.TestCase):
    def test_reading_copies_preserve_all_unique_cues(self):
        folder = ROOT / ARCHIVE
        for video in json.loads((folder / "manifest.json").read_text())["videos"]:
            source = (folder / video["vtt"]).read_text()
            cues = re.findall(r"(\d\d:\d\d:\d\d\.\d+) --> ([^\n]+)\n(.*?)(?=\n\n|\Z)", source, re.S)
            unique = list(dict.fromkeys(cues))
            self.assertEqual(video["raw_cues"], len(cues))
            self.assertEqual(video["unique_cues"], len(unique))
            text = (folder / video["transcript"]).read_text()
            actual = re.findall(r"^## ([^\n]+)\n\n(.*?)(?=\n\n|\Z)", text, re.M | re.S)
            self.assertEqual(actual, [(start, body.replace("\n", " ")) for start, end, body in unique])

    def test_archive_detects_corruption_missing_text_and_media(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            shutil.copytree(ROOT / ARCHIVE, root / ARCHIVE)
            self.assertEqual(m.validate_archive(root), [])
            (root / ARCHIVE / "111461.md").write_text("truncated")
            (root / ARCHIVE / "111462.en.vtt").unlink()
            (root / ARCHIVE / "video.mp4").write_bytes(b"not video")
            errors = m.validate_archive(root)
            self.assertTrue(any("checksum mismatch" in e for e in errors))
            self.assertTrue(any("Missing or indirect" in e for e in errors))
            self.assertTrue(any("only its manifest" in e for e in errors))

    def test_reading_links_reject_unpinned_and_unrelated_hosts(self):
        pinned = "https://raw.githubusercontent.com/o1xhack/apple-workflow-skills/" + "a" * 40 + "/external-sources/apple/iphone-duo/2026-09-10/111466.md"
        self.assertTrue(m.allowed_reading_url(pinned))
        self.assertTrue(m.allowed_reading_url("https://developer.apple.com/iphone-duo/"))
        for url in [pinned.replace("a" * 40, "main"), pinned.replace("o1xhack", "other"),
                    "http://developer.apple.com/iphone-duo/", "https://developer.apple.com.example.com/iphone-duo/",
                    "https://developer.apple.com@evil.example/iphone-duo/", "file:///tmp/source.md"]:
            self.assertFalse(m.allowed_reading_url(url), url)


if __name__ == "__main__":
    unittest.main()
