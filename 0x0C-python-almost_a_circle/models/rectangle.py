#!/usr/bin/python3
from models.base import Base
"""superclass Base"""


class Rectangle(Base):
    """subclass Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize instance attributes
        Args:
            width (int): width
            height (int): height
            x (int) = x
            y (int) = y
            id (int) = id
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
        super().__init__()

    @property
    def width(self):
        """get width
        Returns:
            width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """set width
        Args:
            value (int): value
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get height
        Returns:
            height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """set height
        Args:
            value (int): value
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get x
        Returns:
            x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """set x
        Args:
            value (int): value
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get y
        Returns:
            y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """set y
        Args:
            value (int): value
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
