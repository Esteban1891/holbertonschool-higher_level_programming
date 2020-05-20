#!/usr/bin/python3
"""Magic class"""
import math
"""This module contains a class that defines a square.
In the Square class we initialize each object by the
__init__ method with a private instance variable called
__size that takes the size variable's value passed as
argument. Also checks if the size arg has a valid value.
"""


class MagicClass():
    """Magic class."""

    def __init__(self, radius=0):
        """Init class."""
        self.__radius = 0
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Return area of class."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Return circumference of class."""
        return 2 * math.pi * self.__radius
