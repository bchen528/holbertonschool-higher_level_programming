#!/usr/bin/python3
import unittest
"""unittest"""
from models.base import Base
"""Base class"""
from models.rectangle import Rectangle
"""Rectangle class"""
from models.square import Square
"""Square class"""
from io import StringIO
"""StringIO class"""
import sys
"""sys module"""
import json
"""JavaScript Object Notation"""


class TestSquare(unittest.TestCase):
    """class TestSquare"""
    def test_id(self):
        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertIsNotNone(id(s1))

    def test_init(self):
        Base._Base__nb_objects = 0
        s2 = Square(5)
        self.assertIsInstance(s2, Square)
        self.assertTrue(issubclass(type(s2), Rectangle))

    def test_numObj(self):
        Base._Base__nb_objects = 0
        s3 = Square(2, 2)
        s4 = Square(5, 5)
        self.assertEqual(s4.id, 2)

    def test_getterAndSetter(self):
        Base._Base__nb_objects = 0
        s5 = Square(5)
        self.assertEqual(s5.width, 5)
        self.assertEqual(s5.height, 5)
        s5 = Square(2, 2)
        self.assertEqual(s5.width, 2)
        self.assertEqual(s5.height, 2)
        self.assertEqual(s5.x, 2)
        s5 = Square(3, 1, 3)
        self.assertEqual(s5.width, 3)
        self.assertEqual(s5.height, 3)
        self.assertEqual(s5.x, 1)
        self.assertEqual(s5.y, 3)

    def test_area(self):
        Base._Base__nb_objects = 0
        s6 = Square(5)
        self.assertEqual(s6.area(), s6.width * s6.height)

    def test_errors(self):
        Base._Base__nb_objects = 0
        s = Square(5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.size = "10"
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = -10
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.x = "1"
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.x = -10
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.y = "10"
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(10, 3, -1)

    def test_display(self):
        Base._Base__nb_objects = 0
        s7 = Square(5)
        old_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        s7.display()
        sys.stdout = old_stdout
        result_string = result.getvalue()
        self.assertEqual(result_string, "#####\n#####\n#####\n#####\n#####\n")
        s8 = Square(2, 2)
        old_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        s8.display()
        sys.stdout = old_stdout
        result_string = result.getvalue()
        self.assertEqual(result_string, "  ##\n  ##\n")
        s9 = Square(3, 1, 3)
        old_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        s9.display()
        sys.stdout = old_stdout
        result_string = result.getvalue()
        self.assertEqual(result_string, "\n\n\n ###\n ###\n ###\n")

    def test_str(self):
        Base._Base__nb_objects = 0
        s8 = Square(5)
        s9 = Square(2, 2)
        s10 = Square(3, 1, 3)
        string1 = s8.__str__()
        string2 = s9.__str__()
        string3 = s10.__str__()
        self.assertEqual(string1, "[Square] ({:d}) 0/0 - 5".format(s8.id))
        self.assertEqual(string2, "[Square] ({:d}) 2/0 - 2".format(s9.id))
        self.assertEqual(string3, "[Square] ({:d}) 1/3 - 3".format(s10.id))

    def test_display_xy(self):
        Base._Base__nb_objects = 0
        s1 = Square(2, 3, 2)
        old_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        s1.display()
        sys.stdout = old_stdout
        result_string = result.getvalue()
        self.assertEqual(result_string, "\n\n   ##\n   ##\n")
        s2 = Square(3, 2, 1)
        old_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        s2.display()
        sys.stdout = old_stdout
        result_string = result.getvalue()
        self.assertEqual(result_string, "\n  ###\n  ###\n  ###\n")

    def test_update_args(self):
        Base._Base__nb_objects = 0
        s1 = Square(5)
        s1.update(10)
        string = s1.__str__()
        self.assertEqual(string, "[Square] (10) 0/0 - 5")
        s1.update(1, 2)
        string = s1.__str__()
        self.assertEqual(string, "[Square] (1) 0/0 - 2")
        s1.update(1, 2, 3)
        string = s1.__str__()
        self.assertEqual(string, "[Square] (1) 3/0 - 2")
        s1.update(1, 2, 3, 4)
        string = s1.__str__()
        self.assertEqual(string, "[Square] (1) 3/4 - 2")
        s1.update(x=12)
        string = s1.__str__()
        self.assertEqual(string, "[Square] (1) 12/4 - 2")
        s1.update(size=7, y=1)
        string = s1.__str__()
        self.assertEqual(string, "[Square] (1) 12/1 - 7")
        s1.update(size=7, id=89, y=1)
        string = s1.__str__()
        self.assertEqual(string, "[Square] (89) 12/1 - 7")

    def test_dictionary(self):
        Base._Base__nb_objects = 0
        s1 = Square(10, 2, 1, 1)
        a_dict = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        s1_dictionary = s1.to_dictionary()
        self.assertTrue(s1_dictionary == a_dict)
