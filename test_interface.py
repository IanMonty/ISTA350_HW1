"""
Author: <your name>
Date: <the date>
Class: ISTA 350
Section Leader: <your section leader>

Description:
<summary of these tests>
"""

from binary import Binary2C
import unittest


class TestBinary2C(unittest.TestCase):
    def setUp(self):
        self.bin_0 = Binary2C("")
        self.bin_1 = Binary2C("01")
        self.bin_neg_1 = Binary2C("1")
        self.bin_5 = Binary2C("0101")
        self.bin_neg_5 = Binary2C("1011")
        self.bin_7 = Binary2C("00000000000000000111")
        self.bin_neg_7 = Binary2C("11111111111111111001")

    def test_init(self):
        self.assertEqual([0], self.bin_0.num_list)
        self.assertEqual([0, 1], self.bin_1.num_list)
        self.assertEqual([1, 0, 1, 1], self.bin_neg_5.num_list)
        self.assertEqual([1, 0, 0, 1], self.bin_neg_7.num_list)
        self.assertRaises(RuntimeError, Binary2C, "abc")
        self.assertRaises(RuntimeError, Binary2C, "010120101")

    def test_repr(self):
        self.assertEqual("0", repr(self.bin_0))
        self.assertEqual("01", repr(self.bin_1))
        self.assertEqual("1011", repr(self.bin_neg_5))
        self.assertEqual("1001", repr(self.bin_neg_7))

    # Complete the above tests and add in your own.
    # You need to have at least one test method
    #   for every method/function in the binary module.
    # Don't forget to add documentation.


if __name__ == "__main__":
    unittest.main()
