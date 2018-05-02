#!/usr/bin/python3
class _MagicClass:
    """creates a protected class, MagicClass"""
    def __init__(self, radius=0):
        """initialized attributes for instance of MagicClass

        Args:
            radius (int): radius
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """calculates area of circle"""
        return (self.__radius**2) * math.pi

    def circumference(self):
        """calculates circumference of circle"""
        return 2 * math.pi * self.__radius

import math
