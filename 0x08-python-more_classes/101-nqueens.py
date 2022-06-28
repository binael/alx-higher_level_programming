#!/usr/bin/python3
"""placing N non-attacking queens on an N×N chessboard"""


def nqueen(N):
    """Function that solves the nqueen problem"""
    pass


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)

    if number != float(sys.argv[1]):
        print("N must be a number")
        sys.exit(1)

    if number < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueen(number)
