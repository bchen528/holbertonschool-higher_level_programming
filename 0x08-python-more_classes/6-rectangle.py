#!/usr/bin/python3
class Rectangle:
    """creates a class Rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initialize width and height of rectangle
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            value (int): height value
        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

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
            value (int): width
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """find area of rectangle
        Returns:
            area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """find perimeter of rectangle
        Returns:
            perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """print square
        Returns:
            string to be printed to stdout
        """
        new = ""
        for i in range(self.__height):
            for j in range(self.__width):
                new += '#'
            if i != self.__height - 1:
                new += '\n'
        return new

    def __repr__(self):
        """print string to stdout
        Returns:
            string to be printed to stdout
        """
        return 'Rectangle({:d},{:d})'.format(self.__width, self.__height)

    def __del__(self):
        """print message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
