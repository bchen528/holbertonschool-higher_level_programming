#!/usr/bin/python3
class BaseGeometry:
    """creates a class BaseGeometry"""
    def area(self):
        """calculate the area
        Raise:
            Exception: area is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the value
        Args:
            name(str): name
            value(int): value
        Raises:
            TypeError: if value is not type int
            ValueError: if value is less than or equal to 0
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
        """calculates area"""
        return self.__width * self.__height

    def __str__(self):
        """prints string"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)


class Square(Rectangle):
    """creates subclass Square"""
    def __init__(self, size):
        """initialize instance attributes"""
        self.__size = size
        super().integer_validator("size", self.__size)
        super().__init__(size, size)
        super().area()

    def __str__(self):
        """print string"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
