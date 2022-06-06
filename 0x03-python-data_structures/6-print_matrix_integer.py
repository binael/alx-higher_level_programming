#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Prints a matrix element"""

    if not matrix:
        return

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:d}".format(matrix[i][j], end=""))

            if j < len(matrix[1]) - 1:
                print(" ", end="")
        print("")
