#!/usr/bin/python3
""" Creating a class Square"""


class Square:
    """A class that takes a square object"""

    def __init__(self, size=0):
        """Initilizes the instances of a classs"""
        self.size = size

    @property
    def size(self):
        """Sets the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the __size to value"""
        if not type(size) == int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return (self.__size ** 2)
