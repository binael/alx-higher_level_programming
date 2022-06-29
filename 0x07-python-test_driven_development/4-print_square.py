#!/usr/bin/python3
"""Printing square"""


def print_square(size):
    """Prints a square using the given symbol #"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        print(f"{'#' * size}")
