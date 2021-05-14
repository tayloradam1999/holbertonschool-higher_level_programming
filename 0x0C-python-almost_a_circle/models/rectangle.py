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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """Returns area of rectangle"""
        area = self.__width * self.__height
        return area

    def update(self, *args):
        """Assigns an argument to each attribute"""
        largs = list(args)
        if len(largs) == 5:
            self.y = largs[4]
            largs.pop()
        if len(largs) == 4:
            self.x = largs[3]
            largs.pop()
        if len(largs) == 3:
            self.height = largs[2]
            largs.pop()
        if len(largs) == 2:
            self.width = largs[1]
            largs.pop()
        if len(largs) == 1:
            self.id = largs[0]

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
