#!/usr/bin/python3
""" Creating a class Square"""


class Square:
    """A class that takes a square object"""

    def __init__(self, size=0):
        """initialize the instances of the class"""
        try:
            assert type(size) == int and size >= 0
            self.__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
