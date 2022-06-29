#!/usr/bin/python3
"""Addition of two integer numbers"""


def add_integer(a, b=98):
    """Adds two numbers"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (a + b)
