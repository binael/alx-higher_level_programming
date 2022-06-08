#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """computes the square of a number"""

    new_matrix = []

    for i in matrix:
        if type(i) == list:
            new_matrix.append(list(map((lambda x: x ** 2), i)))
        else:
            new_matrix.append(i ** 2)

    return (new_matrix)
