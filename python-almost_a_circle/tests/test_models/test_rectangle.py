#!/usr/bin/python3
"Unit tests for Rectangle class"
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    "Unit test suite for Rectangle class"

    def test_init(self):
        "test of Rectangle for width/height and default initialization"
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)


if __name__ == "__main__":
    unittest.main()
