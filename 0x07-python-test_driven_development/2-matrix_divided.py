#!/usr/bin/python3

"""This module defines a matrix division function.
Matrix: A list of lists of ints or floats
div: What to divide by
Return: New divided matrix"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.
    Raises TypeErrors if:
        Matrix contains non-numbers
        Matrix contains rows of different sizes
        Div is not an int or float
    Raises ZeroDivisionError if:
        Div is 0"""
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(element, int) or isinstance(element, float))
                    for element in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers'floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
