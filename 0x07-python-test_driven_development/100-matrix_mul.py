#!/usr/bin/python3

"""A module that implements the multiplication of two matrix
"""


def matrix_mul(m_a, m_b):
    """ A function that multiplies two matrix
    first matrix: m_a
    second matrix: m_b
    """

    # Check if both inputs are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Check if both inputs are list of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Check if the input lists are empty
    if not m_a or any((not row) for row in m_a):
        raise ValueError("m_a can't be empty")
    if not m_b or any((not row) for row in m_b):
        raise ValueError("m_b can't be empty")

    # Check if elements in the lists are either integer or floats
    if not all(isinstance(x, (int, float)) for row in m_a for x in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(x, (int, float)) for row in m_b for x in row):
        raise TypeError("m_b should contain only integers or floats")

    # Check if the size of the rows are equal and consistent
    if not all((len(rows) == len(m_a[0])) for rows in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all((len(rows) == len(m_b[0])) for rows in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # Check if the matrix can be multiplied
    if (len(m_a[0]) != len(m_b)):
        raise ValueError("m_a and m_b can't be multiplied")

    # IMPLEMENTATION OF THE SOLUTION BEGINS
    matrix_result = []

    for i in range(len(m_a)):
        matrix_row = []
        for j in range(len(m_b[0])):
            element = 0
            for k in range(len(m_b)):
                element += (m_a[i][k] * m_b[k][j])

            matrix_row.append(round(element))

        matrix_result.append(matrix_row)

    return (matrix_result)
