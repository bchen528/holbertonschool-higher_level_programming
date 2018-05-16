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

    def to_json(self):
        """retrieves a dictionary representation of a Student instance
        Returns:
            a dictionary representation of a Student instance
        """
        return self.__dict__
