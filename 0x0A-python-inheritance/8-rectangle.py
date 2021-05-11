#!/usr/bin/python3

"""
This module creates an empty class 'BaseGeometry'
Public instance method 'area(self)' that raises an exception with the message
'area() is not implemented'
"""


class BaseGeometry:
    """Empty class"""
    pass

    def area(self):
        """Raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value
        name is always a string
        if value is not an integer, raises a TypeError
        if value is less than or equal to 0, raises a ValueError"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Inherits from BaseGeometry class
    Instantiated with width and height
    width and heigth must be private
    width and height must be positive integers, validated by
    integer_validator in BaseGeometry"""
    def __init__(self, width, height):
        super().__init__()
        if BaseGeometry.integer_validator(self, "width", width):
            self.__width = width
        if BaseGeometry.integer_validator(self, "height", height):
            self.__height = height
