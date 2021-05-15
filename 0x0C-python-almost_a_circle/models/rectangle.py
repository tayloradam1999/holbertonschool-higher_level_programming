#!/usr/bin/python3

"""
This module creates a class 'Rectangle'
"""


from models.base import Base
import inspect


class Rectangle(Base):

    """This is a class that inherits from 'Base'
    This class has 4 private instance attributes
    This class also has a constructor"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor method"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """Returns area of rectangle"""
        area = self.__width * self.__height
        return area

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        my_dict = {}
        for i in inspect.getmembers(self):
            if not i[0].startswith('_'):
                if not inspect.ismethod(i[1]) and not\
                       inspect.isfunction(i[1]):
                    my_dict[i[0]] = i[1]
        return my_dict

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args is None or len(args) == 0:
            for i in kwargs:
                if hasattr(self, i):
                    setattr(self, i, kwargs[i])
        largs = list(args)
        latts = ["id", "width", "height", "x", "y"]
        for i in range(len(largs)):
            setattr(self, latts[i], largs[i])

    def display(self):
        """Prints our rectangle to stdout with the character '#'"""
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """Overrides the return of our class to the desired format"""
        return '[Rectangle] (%d) %d/%d - %d/%d' % (self.id, self.x, self.y,
                                                   self.width, self.height)

    @property
    def width(self):
        """Property getter for width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Property setter for width with validator"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """Property getter for height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Property setter for width with validator"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """Property getter for x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Property setter for x with validator"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """Property getter for y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Property setter for y with validator"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y
