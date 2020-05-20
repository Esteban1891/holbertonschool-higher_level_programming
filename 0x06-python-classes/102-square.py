#!/usr/bin/python3
"""This module contains a class that defines a square.
In the Square class we initialize each object by the
__init__ method with a private instance variable called
__size that takes the size variable's value passed as
argument. Also checks if the size arg has a valid value.
"""


class Square():
    """A square class."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialization of the class square."""
        self.size = size
        self.position = position

    def area(self):
        """The area of the Square"""
        return self.__size ** 2

    @property
    def size(self):
        """The size of the Square"""
        return self.__size

    @size.setter
    def size(self, SizeValue):
        """set size of the Square"""
        if type(SizeValue) != int:
            raise TypeError("size must be an integer")
        if SizeValue < 0:
            raise ValueError("size must be >= 0")
        self.__size = SizeValue

    def __gt__(self, other):
        """greater"""
        return self.area() > other.area()

    def __lt__(self, other):
        """less"""
        return self.area() < other.area()

    def __eq__(self, other):
        """equal"""
        return self.area() == other.area()

    def __ge__(self, other):
        """greater than or equal"""
        return self.area() >= other.area()

    def __le__(self, other):
        """less than or equal"""
        return self.area() <= other.area()

    def __ne__(self, other):
        """not equal operator"""
        return self.area() != other.area()
