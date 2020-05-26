#!/usr/bin/python3
"""create the class"""


class Rectangle:
    """initialize"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """the getter of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """the setter in width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """the setter of self in height"""
        return self.__height

    @height.setter
    def height(self, value):
        """the getter of self in height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
