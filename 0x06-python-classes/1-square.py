#!/usr/bin/python3
"""This module writes a class 'Square'.
In this class a size for the Square will be initalized."""


class Square:
    """Class that initalizes size as a prinvate instance attribute"""
    def __init__(self, size):
        self.__size = size
        """init func initalizes Square object and gives it a size"""
