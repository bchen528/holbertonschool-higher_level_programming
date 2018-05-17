#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""superclass BaseGeometry"""


class Rectangle(BaseGeometry):
    """creates a subclass Rectangle of class BaseGeometry"""
    def __init__(self, width, height):
        """initialize attributes
        Args:
            width(int): width of Rectangle
            height(int): height of Rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
