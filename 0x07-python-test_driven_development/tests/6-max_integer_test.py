#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test case for the max_integer_function

    """

    def test_typeErrors(self):
        self.assertRaises(TypeError, max_integer, None)
        self.assertRaises(TypeError, max_integer, 2)
        self.assertRaises(TypeError, max_integer, -2)
        self.assertRaises(TypeError, max_integer, 1 + 2j)
        self.assertRaises(TypeError, max_integer, ["2", 1j, 5])
        self.assertRaises(TypeError, max_integer, 2.2)
        self.assertRaises(TypeError, max_integer, )

    def test_normalResults(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 2, 8, 10, 5, 9]), 10)
        self.assertEqual(max_integer([1, 7, -38, 5, 33, -40, 8]), 33)
        self.assertEqual(max_integer([-20, -41, -3, -67, -18]), -3)
        self.assertEqual(max_integer([55, 8, 7, 19, 20]), 55)
        self.assertEqual(max_integer([-20, -41, -333, -67, -18]), -18)
        self.assertEqual(max_integer([4]), 4)
        self.assertEqual(max_integer([]), None)
