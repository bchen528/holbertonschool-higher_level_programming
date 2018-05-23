#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
import sys
import json
import pep8


class TestRectangle(unittest.TestCase):
    """class TestRectangle"""
    def test_id(self):
        """check id"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 2)
        self.assertIsNotNone(id(r1))

    def test_init(self):
        """check proper instances created"""
        Base._Base__nb_objects = 0
        r2 = Rectangle(2, 10)
        self.assertIsInstance(r2, Rectangle)

    def test_numObj(self):
        """check number of objects"""
        Base._Base__nb_objects = 0
        r3 = Rectangle(10, 2, 0, 0)
        r4 = Rectangle(5, 5)
        self.assertEqual(r4.id, 2)

    def test_getterAndSetter(self):
        """checks getter and setter"""
        Base._Base__nb_objects = 0
        r5 = Rectangle(10, 2, 0, 0)
        self.assertEqual(r5.width, 10)
        self.assertEqual(r5.height, 2)
        self.assertEqual(r5.x, 0)
        self.assertEqual(r5.y, 0)

    def test_errors(self):
        """checks invalid attributes"""
        Base._Base__nb_objects = 0
        r = Rectangle(10, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.width = "2"
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.width = -10
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.height = "2"
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.height = -10
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.x = {}
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -3, 1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.y = {}
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 3, -1)

    def test_area(self):
        """checks area"""
        Base._Base__nb_objects = 0
        r6 = Rectangle(3, 2)
        self.assertEqual(r6.area(), r6.width * r6.height)

    def test_display(self):
        """checks display"""
        Base._Base__nb_objects = 0
        r7 = Rectangle(4, 6)
        old_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        r7.display()
        sys.stdout = old_stdout
        result_string = result.getvalue()
        self.assertEqual(result_string,
                         "####\n####\n####\n####\n####\n####\n")

    def test_str(self):
        """checks str"""
        Base._Base__nb_objects = 0
        r8 = Rectangle(4, 6, 2, 1, 12)
        r9 = Rectangle(5, 5, 1)
        string1 = r8.__str__()
        string2 = r9.__str__()
        self.assertEqual(string1,
                         "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(string2,
                         "[Rectangle] (1) 1/0 - 5/5")

    def test_display_xy(self):
        """checks display xy"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(2, 3, 2, 2)
        old_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        r1.display()
        sys.stdout = old_stdout
        result_string = result.getvalue()
        self.assertEqual(result_string, "\n\n  ##\n  ##\n  ##\n")
        r2 = Rectangle(3, 2, 1, 0)
        old_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        r2.display()
        sys.stdout = old_stdout
        result_string = result.getvalue()
        self.assertEqual(result_string, " ###\n ###\n")

    def test_update(self):
        """checks update args"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        string = r1.__str__()
        self.assertEqual(string, "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        string = r1.__str__()
        self.assertEqual(string, "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        string = r1.__str__()
        self.assertEqual(string, "[Rectangle] (89) 10/10 - 2/3")
        r1.update(89, 2, 3, 4)
        string = r1.__str__()
        self.assertEqual(string, "[Rectangle] (89) 4/10 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        string = r1.__str__()
        self.assertEqual(string, "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        """checks update kwargs"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        string = r1.__str__()
        self.assertEqual(string, "[Rectangle] (1) 10/10 - 10/1")
        r1.update(width=1, x=2)
        string = r1.__str__()
        self.assertEqual(string, "[Rectangle] (1) 2/10 - 1/1")
        r1.update(y=1, width=2, x=3, id=89)
        string = r1.__str__()
        self.assertEqual(string, "[Rectangle] (89) 3/1 - 2/1")
        r1.update(x=1, height=2, y=3, width=4)
        string = r1.__str__()
        self.assertEqual(string, "[Rectangle] (89) 1/3 - 4/2")

    def test_dictionary(self):
        """checks dictionary conversion"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        a_dict = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertTrue(r1_dictionary == a_dict)

    def test_empty(self):
        """check empty arguments"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.width = None
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.width = ""

    def test_pep8_model(self):
        """tests for pep8"""
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['models/base.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_pep8_test(self):
        """tests for pep8"""
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")
