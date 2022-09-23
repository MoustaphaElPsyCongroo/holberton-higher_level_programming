#!/usr/bin/python3
"""Unit test for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_sortedmax(self):
        self.assertEqual(max_integer([0, 1, 2]), 2)

    def test_unsortedmax(self):
        self.assertEqual(max_integer([3, 4, 1, 0]), 4)


if __name__ == '__main__':
    unittest.main()
