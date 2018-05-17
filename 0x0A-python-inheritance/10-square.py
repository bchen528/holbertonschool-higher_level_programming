#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""superclass Rectangle"""


class Square(Rectangle):
    """creates subclass Square"""
    def __init__(self, size):
        """initialize instance attributes
        Args:
            size (int): size of square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
