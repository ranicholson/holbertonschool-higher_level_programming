#!/usr/bin/python3

"""Unittest for the Rectangle class"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class RectangleTest(unittest.TestCase):
    """Tests for Rectangle class"""

    def test_rec_norm(self):
        """Testing under nomrmal parameters"""
        self.assertIsInstance((Rectangle(1, 1)), Base)

    def test_nosize(self):
        """Test wit no arguments"""
        with self.assertRaises(TypeError):
            Rectangle()
