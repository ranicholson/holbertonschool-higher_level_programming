#!/usr/bin/python3

"""Unittest for the Square class"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class SquareTest(unittest.TestCase):
    """Tests for Square class"""

    def test_rec_norm(self):
        """Testing under nomrmal parameters"""
        self.assertIsInstance((Square(1, 1)), Base)

    def test_nosize(self):
        """Test with no arguments"""
        with self.assertRaises(TypeError):
            Square()
