#!/usr/bin/python3
"""A program that finds the maximum number in a list
Using divide and conquer algorithm with log(n)
"""

def find_peak(list_of_integers):
    if not (isinstance(list_of_integers, list)):
        return None

    size = len(list_of_integers)

    if size == 0:
        return None

    max_int = list_of_integers[0]

    if size == 1:
        return max_int

    for element in list_of_integers:
        if (element > max_int):
            max_int = element

    return max_int
