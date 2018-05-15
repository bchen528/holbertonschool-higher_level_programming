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
