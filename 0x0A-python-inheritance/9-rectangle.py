#!/usr/bin/python3
class BaseGeometry:
    """creates a class BaseGeometry"""
    def area(self):
        """calculate the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the value
        Args:
            name(str): name
            value(int): value
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """creates a subclass Rectangle of class BaseGeometry"""
    def __init__(self, width, height):
        """initialize attributes
        Args:
            width(int): width of Rectangle
            height(int): height of Rectangle
        """
        BaseGeometry.__init__(self)
        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)