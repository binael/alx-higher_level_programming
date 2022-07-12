#!/usr/bin/python3
"""Divides A Matrix by int or float"""


def matrix_divided(matrix, div):
    """Divides every element of a matrix by int/float div
    args:
        matrix: A matrix where all elements are either float or int
        div (int or float): divides all the matrix elements
        """

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not all(type(num) in [int, float] for row in matrix for num in row):
        text = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(text)

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
