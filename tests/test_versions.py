import unittest
from s2protocol import versions as _versions

class VersionsTestCase(unittest.TestCase):
    def test_latest(self):
        p = _versions.latest()
        self.assertIsNotNone(p)

    def test_specific(self):
        p = _versions.build(58400)
        self.assertIsNotNone(p)

    def test_missing(self):
        self.assertRaises(ImportError, lambda: _versions.build(42))


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(VersionsTestCase)
