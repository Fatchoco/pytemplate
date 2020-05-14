""" This is test basic01 docstring.
    This can be run via commandline with:
        python -m nose2
        python -m nose2 tests.test_basic01.TestBasic01.test_01b
        python -m unittest tests\test_basic01.py
        python -m unittest tests.test_basic01.TestBasic01.test_01b
"""
import unittest
import pytemplate.helpers


class TestBasic01(unittest.TestCase):

    def test_01a(self):
        self.assertEqual(1, 1)

    def test_01b(self):
        self.assertEqual(pytemplate.helpers.helperno01(), "Finish helperno01")


if __name__ == "__main__":
    unittest.main()
