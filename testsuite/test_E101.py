"""moved from testsuite files due to 3.12 making this a TokenError"""
import unittest
import sys

from testsuite.support import errors_from_src


class E101Test(unittest.TestCase):
    def test_E101(self):
        errors = errors_from_src(
            'if True:\n'
            '\tprint(1)  # tabs\n'
            '        print(2)  # spaces\n'
        )
        if sys.version_info >= (3, 12):
            self.assertEqual(errors, ['W191:2:1', 'E901:3:28'])
        else:
            self.assertEqual(errors, ['W191:2:1', 'E101:3:1'])