#!/usr/bin/python3

"""
add_integer - adds 2 integers
a - first integer for addition
b - second integer for addition
Return: sum of addition
"""


def add_integer(a, b=98):
	"""This def adds two integers and returns the sum.
	Float arguments are typecasted to ints before additon is performed.
	Raises a TypeError if either a or b is a non-integer or non-float."""
	if ((not isinstance(a, int) and not isinstance(a, float))):
		raise TypeError("a must be an integer")
	if ((not isinstance(b, int) and not isinstance(b, float))):
		raise TypeError("b must be an integer")
	return (int(a) + int(b))
