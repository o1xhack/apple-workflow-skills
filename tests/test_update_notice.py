import importlib.util
from pathlib import Path
import unittest

path = Path(__file__).resolve().parents[1] / 'skills/apple-workflow-skills/scripts/check_update.py'
spec = importlib.util.spec_from_file_location('update_notice', path)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def release(tag='v0.3.0'):
    return {'tag_name': tag, 'draft': False, 'prerelease': False, 'assets': [
        {'name': 'apple-workflow-skills.zip', 'state': 'uploaded',
         'browser_download_url': f'{m.REPOSITORY}/releases/download/{tag}/apple-workflow-skills.zip'}]}


class UpdateNoticeTest(unittest.TestCase):
    def test_notice_cache_and_dedup(self):
        result, cache = m.check('0.2.0', {}, 100, lambda: release())
        self.assertEqual(result['status'], 'update_available')
        def forbidden():
            self.fail('Fresh cache must not access network')
        self.assertEqual(m.check('0.2.0', cache, 101, forbidden)[0]['status'], 'cached')
        self.assertEqual(m.check('0.2.0', cache, 100 + m.INTERVAL, lambda: release())[0]['status'], 'already_notified')
        self.assertEqual(m.check('0.2.0', cache, 101, lambda: release(), force=True)[0]['status'], 'update_available')
        self.assertEqual(m.check('0.2.0', cache, 100 + m.INTERVAL, lambda: release('v0.4.0'))[0]['status'], 'update_available')

    def test_numeric_versions_and_installed_upgrade(self):
        self.assertEqual(m.check('0.9.0', {}, 100, lambda: release('v0.10.0'))[0]['status'], 'update_available')
        for tag in ['v0.1.0', 'v0.2.0']:
            self.assertEqual(m.check('0.2.0', {}, 100, lambda: release(tag))[0]['status'], 'up_to_date')
        self.assertEqual(m.installed_version(), '0.2.0')

    def test_untrusted_metadata_is_not_a_notice(self):
        bad = [None, {}, release('v0.3.0-beta'), release('v0.3.0;echo unsafe')]
        draft = release(); draft['draft'] = True; bad.append(draft)
        pre = release(); pre['prerelease'] = True; bad.append(pre)
        missing = release(); missing['assets'] = []; bad.append(missing)
        url = release(); url['assets'][0]['browser_download_url'] = 'https://example.com/asset.zip'; bad.append(url)
        for data in bad:
            self.assertEqual(m.check('0.2.0', {}, 100, lambda: data)[0]['status'], 'unavailable')

    def test_failure_is_cached_and_not_up_to_date(self):
        def fail():
            raise OSError('offline')
        result, cache = m.check('0.2.0', {}, 100, fail)
        self.assertEqual(result['status'], 'unavailable')
        self.assertEqual(m.check('0.2.0', cache, 101, fail)[0]['status'], 'cached')
        self.assertEqual(m.check('0.2.0', cache, 101, fail, force=True)[0]['status'], 'unavailable')
        self.assertEqual(m.check('0.3.0', cache, 101, lambda: release('v0.4.0'))[0]['status'], 'update_available')


if __name__ == '__main__':
    unittest.main()
