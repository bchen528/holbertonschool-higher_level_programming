#!/usr/bin/python3
class Square:
    """square"""
    def __init__(self, size=0):
        """
        initialize square size

        Args:
            size (int): size of square

        Returns: None
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """
        set size

        Args:
            value (int): value to assign size

        Returns: None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        calculate area of square

        Args: None

        Returns: area of square
        """

        return self.__size * self.__size
