#!/usr/bin/python3
import unittest
"""unittest"""
from models.base import Base
"""Base class"""
from models.rectangle import Rectangle
"""Rectangle class"""
import json
"""JavaScript Object Notation"""


class TestBase(unittest.TestCase):
    """class TestBase"""
    def test_id(self):
        b1 = Base()
        self.assertIsNotNone(id(b1))

    def test_init(self):
        b2 = Base()
        self.assertIsInstance(b2, Base)

    def test_numObj(self):
        Base._Base__nb_objects = 0
        b3 = Base()
        self.assertEqual(b3.id, 1)

    def test_toJsonString(self):
        r1 = Rectangle(10, 7, 2, 8)
        a_dict = r1.to_dictionary()  # dict
        json_string = json.dumps([a_dict])  # str of list dict
        json_listdict = r1.to_json_string([a_dict])  # str of list dict
        self.assertTrue(json_string == json_listdict)

    def test_saveToFile(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        a_dict = [r1.to_dictionary(), r2.to_dictionary()]  # list dict
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            list_dict = json.loads(file.read())  # list dict
        self.assertTrue(a_dict == list_dict)
