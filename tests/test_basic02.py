""" This is test basic02 docstring."""
import unittest
import pytemplate.subfolder_a.subhelper_a as a
import pytemplate.subfolder_b.subhelper_b as subhelper_b


class TestBasic02(unittest.TestCase):

    def test_sub_a_01(self):
        self.assertEqual(a.sub_a01('test'), "Finish sub_a01")

    def test_sub_b_01(self):
        self.assertEqual(subhelper_b.sub_b01(), "Finish sub_b01")


if __name__ == "__main__":
    unittest.main()
