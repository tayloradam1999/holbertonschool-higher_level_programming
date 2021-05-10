#!/usr/bin/python3

"""This module is a unittest for 'max_integer(list=[]):'"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """This class runs tests for our function"""
    def test_BegEnd(self):
        """Tests max int on the beginning and end"""
        self.assertEqual(max_integer([10, 2, 4, 5]), 10)
        self.assertEqual(max_integer([2, 4, 5, 10]), 10)

    def test_Inc(self):
        """Tests for raising errors"""
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([-10, -10, 10, 10]), 10)
        self.assertEqual(max_integer([10, 10, 10, 10]), 10)
        self.assertEqual(max_integer([1, 2, 2, 2]), 2)
        self.assertRaises(TypeError, max_integer("max_integer"))
        self.assertRaises(TypeError, max_integer((500, 5000)))
        self.assertRaises(TypeError, max_integer([1.2, 1.3, 1.4, 1.5]))
        self.assertRaises(TypeError, max_integer([1.2]))

    def test_Mid(self):
        """Tests for max int in the middle of a list"""
        self.assertEqual(max_integer([1, 2, 5, 4, 3]), 5)
        self.assertEqual(max_integer([1, 3, 2, 1]), 3)
