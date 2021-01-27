#!/usr/bin/python3

"""Unittest for the Base class"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class BaseTest(unittest.TestCase):
    """Tests for the Base class"""

    def test_noid(self):
        """Test under normal parameters"""
        bas1 = Base()
        bas2 = Base()
        bas3 = Base()
        self.assertEqual(bas1.id, (bas2.id - 1))

    def test_idprov(self):
        """Test with id provided and id as None"""
        bas1 = Base(None)
        bas2 = Base(20)
        bas3 = Base()
        self.assertEqual(bas1.id, (bas3.id - 1))
        self.assertEqual(bas2.id, 20)

if __name__ == '__main__':
    unittest.main()
