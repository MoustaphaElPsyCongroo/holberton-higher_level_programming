#!/usr/bin/python3
"""Unit test for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_maxbeginning(self):
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_onenegative(self):
        self.assertEqual(max_integer([1, -5, 5, 3, 4]), 5)

    def test_onlynegative(self):
        self.assertEqual(max_integer([-5, -4, -3, -2, -1], -1))

    def test_onelem(self):
        self.assertEqual(max_integer([5]), 5)

    def test_sortedmax(self):
        self.assertEqual(max_integer([0, 1, 2]), 2)

    def test_unsortedmax(self):
        self.assertEqual(max_integer([3, 4, 1, 0]), 4)


if __name__ == '__main__':
    unittest.main()
