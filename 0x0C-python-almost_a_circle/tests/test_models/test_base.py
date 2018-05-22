#!/usr/bin/python3
import unittest
"""unittest"""
from models.base import Base
"""Base class"""
from models.rectangle import Rectangle
"""Rectangle class"""
from models.square import Square
"""Square class"""
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

    def test_fromJsonString(self):
        list_input = [{'id': 89, 'width': 10, 'height': 4},
                      {'id': 7, 'width': 1, 'height': 7}]  # list dict
        json_list_input = Rectangle.to_json_string(list_input)  # str list dict
        list_output = Rectangle.from_json_string(json_list_input)  # list dict
        self.assertTrue(list_input == list_output)

    def test_create(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_loadFromFile(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertTrue(type(list_rectangles_output) == list)
        for rect in list_rectangles_input:
            self.assertTrue(isinstance(rect, Rectangle))
        for rect in list_rectangles_output:
            self.assertTrue(isinstance(rect, Rectangle))
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertTrue(type(list_squares_output) == list)
        for sqr in list_squares_input:
            self.assertTrue(isinstance(sqr, Square))
        for sqr in list_squares_output:
            self.assertTrue(isinstance(sqr, Square))
