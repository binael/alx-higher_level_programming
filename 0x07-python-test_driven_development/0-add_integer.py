#!/usr/bin/python3
"""Addition of two integer numbers"""


def add_integer(a, b=98):
    """Adds two numbers
    args:
    a - integer or float
    b - optional integer whose base value is 98
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
