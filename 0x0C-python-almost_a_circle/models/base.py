#!/usr/bin/python3
class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize instance
        Args:
            id (int): id of object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
