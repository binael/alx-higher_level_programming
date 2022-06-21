#!/usr/bin/python3
""" Creating a class Square"""


class Square:
    """A class that takes a square object"""

    def __init__(self, size=0, position=(0, 0)):
        """Initilizes the instances of a classs"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Sets the size"""
        return self.__size

    @property
    def position(self):
        """Set the position"""
        return self.__position

    @size.setter
    def size(self, value):
        """sets the __size to value"""
        if not type(value) == int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """sets the __position to value"""
        if not (type(value) == tuple and len(value) == 2 and
                all(type(num) == int for num in value) and
                all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square using #"""
        if self.__size == 0:
            print("", end="")
            return

        [print("") for i in range(self.__position[1])]
        for i in range(self.__size - 1):
            print(f"{' ' * self.__position[0]}{'#' * self.__size}")
        print(f"{' ' * self.__position[0]}{'#' * self.__size}", end="")

    def __str__(self):
        """Returns string version of the object call"""
        self.my_print()
        return ("")
