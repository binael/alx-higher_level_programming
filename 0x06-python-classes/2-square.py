#!/usr/bin/python3
""" Creating a class Square"""


class Square:
    """A class that takes a square object"""

    def __init__(self, size=0):
        """initialize the instances of the class"""
        if not type(size) == int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
