#!/usr/bin/python3
import unittest
"""unittest"""
from models.base import Base
"""base class"""


class TestBase(unittest.TestCase):
    """class TestBase"""
    def test_id(self):
        b1 = Base()
        self.assertIsNotNone(id(b1))

    def test_init(self):
        b2 = Base()
        self.assertIsInstance(b2, Base)

    def test_numObj(self):
        b3 = Base()
        self.assertEqual(b3.id, 3)
