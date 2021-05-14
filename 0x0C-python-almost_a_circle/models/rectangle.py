#!/usr/bin/python3

"""
This module creates a class 'Rectangle'
"""


from models.base import Base


class Rectangle(Base):
    """This is a class that inherits from 'Base'
    This class has 4 private instance attributes
    This class also has a constructor"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor method"""
        super().__init__(id)
        __width = width
        __height = height
        __x = x
        __y = y

    @property
    def width(self):
        """Property getter for width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Property setter for width"""
        self.__width = width

    @property
    def height(self):
        """Property getter for height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Property setter for width"""
        self.__height = height

    @property
    def x(self):
        """Property getter for x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Property setter for x"""
        self.__x = x

    @property
    def y(self):
        """Property getter for y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Property setter for y"""
        self.__y = y
