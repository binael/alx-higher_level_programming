#!/usr/bin/python3
"""An Rectangle class"""


class Rectangle:
    """A class that models a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes both height and width to zero"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width"""
        return self.__width

    @property
    def height(self):
        """Get the height"""
        return self.__height

    @width.setter
    def width(self, value):
        """Sets the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be >= 0")
