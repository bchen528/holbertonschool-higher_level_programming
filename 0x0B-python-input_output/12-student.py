#!/usr/bin/python3
class Student:
    """creates a class Student"""
    def __init__(self, first_name, last_name, age):
        """initialize instance attributes
        Args:
            first_name(str): first name
            last_name(str): last name
            age(int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance
        Args:
            attrs(list): a list of attributes
        Returns:
            a dictionary representation of a Student instance
        """
        new = {}
        i = 0
        count = 0
        if type(attrs) is list:
            for key in attrs:
                if key in self.__dict__:
                    new[key] = self.__dict__[key]
            return new
        return self.__dict__
