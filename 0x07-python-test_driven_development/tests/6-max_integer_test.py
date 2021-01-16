#!/usr/bin/python3

"""Unittest for max_integer(list=[])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class MaxIntegerTest(unittest.TestCase):
    """Call to test max_integer function
    """

    def test_max_at_the_end(self):
        """Tests with the max at the end list"""
        tlist = [0, 0, 1]
        self.assertEqual(max_integer(tlist), 1)

    def test_max_in_the_middle(self):
        """Test with the max in the middle of the list"""
        tlist = [0, 1, 0]
        self.assertEqual(max_integer(tlist), 1)

    def test_one_negative(self):
        """Test with negative number in list"""
        tlist = [0, 2, -1]
        self.assertEqual(max_integer(tlist), 2)

    def test_only_negative(self):
        """Test a list with only negative numbers"""
        tlist = [-1, -2, -3]
        self.assertEqual(max_integer(tlist), -1)

    def test_one_element(self):
        """Test if only one element exists in list"""
        tlist = [1]
        self.assertEqual(max_integer(tlist), 1)

    def test_empty_list(self):
        """Test for an empty list"""
        tlist = []
        self.assertEqual(max_integer(tlist), None)
