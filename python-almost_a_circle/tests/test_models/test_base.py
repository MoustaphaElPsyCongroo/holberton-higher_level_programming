#!/usr/bin/python3
"Unit tests for Base class"
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    "Unit tests suite for Base class"

    def test_id(self):
        "Test of Base for automatically assigning an ID"
        b = Base(5)
        self.assertEqual(b.id, 5)


if __name__ == "__main__":
    unittest.main()
