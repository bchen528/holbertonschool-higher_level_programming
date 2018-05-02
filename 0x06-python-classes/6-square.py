#!/usr/bin/python3
class Square:
    """square"""
    def __init__(self, size=0, position=(0, 0)):
        """initialize square size

        Args:
            size (int): size of square
            position (int, int): coordinates of square
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.size = size

        self.position = position

    @property
    def size(self):
        """get size value

        Args: None

        Returns: size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """set size

        Args:
            value (int): value to assign size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calculate area of square

        Args: None

        Returns: area of square
        """

        return self.__size * self.__size

    @property
    def position(self):
        """get position of square

        Args: None

        Returns: position of square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """set position

        Args:
            value (int, int): value to assign position
        """

        if type(value) is tuple and len(value) == 2 and type(value[0]) is int\
           and type(value[1]) is int and value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """prints square to stdout using #

        Args: None
        """

        if self.__size == 0:
            print()
        else:
            for k in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
