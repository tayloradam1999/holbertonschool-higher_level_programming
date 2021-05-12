#!/usr/bin/python3

"""
This module writes a class 'Student'
"""


class Student:
    """Student class that is defined by
    -first_name
    -last_name
    -age"""
    def __init__(self, first_name, last_name, age):
        """Constructor for 'Student' class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns dictionary representation of a 'Student' instance"""
        return self.__dict__
