#!/usr/bin/python3

"""
This module creates a class 'Rectangle' that inherits attributes
from the class 'BaseGeometry'
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """-Inherits from BaseGeometry class
    -Instantiated with width and height
    -width and heigth must be private
    -width and height must be positive integers, validated by
    integer_validator in BaseGeometry
    -Prints the area of our object with correct format
    -Returns the area of our object with correct format"""
    def __init__(self, width, height):
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area of our rectangle object"""
        area = self.__width * self.__height
        return area

    def __str__(self):
        """Returns the desired output"""
        return '[Rectangle] %d/%d' % (self.__width, self.__height)
