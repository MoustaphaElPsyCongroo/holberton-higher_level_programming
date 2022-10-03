#!/usr/bin/python3
"Unit tests for Rectangle class"
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    "Unit test suite for Rectangle class"

    def test_init(self):
        "Test of Rectangle for width/height and default initialization"
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 5)

    def test_type(self):
        "Test of Rectangle for wrong attribute types"
        self.assertRaisesRegex(
            TypeError, "width must be an integer", Rectangle, "1", 2)
        self.assertRaisesRegex(
            TypeError, "height must be an integer", Rectangle, 1, "2")
        self.assertRaisesRegex(
            TypeError, "x must be an integer", Rectangle, 1, 2, "3")
        self.assertRaisesRegex(
            TypeError, "y must be an integer", Rectangle, 1, 2, 3, "4")

    def test_value(self):
        "Test of Rectangle for invalid values"
        self.assertRaisesRegex(
            ValueError, "width must be > 0", Rectangle, -1, 2)
        self.assertRaisesRegex(
            ValueError, "height must be > 0", Rectangle, 1, -2)
        self.assertRaisesRegex(
            ValueError, "width must be > 0", Rectangle, 0, 2)
        self.assertRaisesRegex(
            ValueError, "height must be > 0", Rectangle, 1, 0)
        self.assertRaisesRegex(
            ValueError, "x must be >= 0", Rectangle, 1, 2, -3)
        self.assertRaisesRegex(
            ValueError, "y must be >= 0", Rectangle, 1, 2, 3, -4)


if __name__ == "__main__":
    unittest.main()
