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
        if not type(value) == int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square using #"""
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            print(f"{'#' * self.__size}")
