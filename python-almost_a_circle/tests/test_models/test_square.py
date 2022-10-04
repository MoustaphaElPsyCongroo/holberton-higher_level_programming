#!/usr/bin/python3
"Unit tests for Rectangle class"
import unittest
from unittest import mock
import io
from models.square import Square


class TestSquare(unittest.TestCase):
  """Testing Square"""
  def test_instance(self):
      """test input size correct standard """
      s = Square(5)
      self.assertEqual(s.size, 5)



  def test_area(self):
      """testing area"""

      s = Square(5)
      self.assertEqual(s.area(), 25)

  def test_display(self):
      """test display()"""

      s = Square(4)
      with mock.patch("sys.stdout", new=io.StringIO()) as mock_stdout:
        s.display()

      assert mock_stdout.getvalue() == "####\n####\n####\n####\n"


if __name__ == "__main__":
    unittest.main()
