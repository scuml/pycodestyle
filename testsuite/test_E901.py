"""moved from testsuite files due to 3.12 changing syntax errors"""
import unittest
import sys

from testsuite.support import errors_from_src


class E901Test(unittest.TestCase):
    def test_closing_brace(self):
        errors = errors_from_src('}\n')
        if sys.version_info < (3, 12):
            self.assertEqual(errors, ['E901:2:1'])
        else:
            self.assertEqual(errors, [])

    def test_unclosed_brace(self):
        src = '''\
if msg:
    errmsg = msg % progress.get(cr_dbname))

def lasting(self, duration=300):
    progress = self._progress.setdefault('foo', {}
'''
        errors = errors_from_src(src)
        if sys.version_info < (3, 12):
            expected = ['E122:4:1', 'E225:4:27', 'E251:5:13', 'E251:5:15']
        else:
            expected = ['E122:4:1', 'E225:4:27', 'E251:5:13', 'E251:5:15', 'E901:5:1']  # noqa: E501
        self.assertEqual(errors, expected)