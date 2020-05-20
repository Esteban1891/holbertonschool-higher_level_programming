#!/usr/bin/python3
"""This module contains a class that defines a square.
In the Square class we initialize each object by the
__init__ method with a private instance variable called
__size that takes the size variable's value passed as
argument. Also checks if the size arg has a valid value.
"""


class Square:
    """Class that defines a square
    Attributes:
        __size (int): size of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """__init__ method that initialize the size and position attributes
        Args:
            size (int): Size to initialize the square.
            position (tuple): position in the square.
        """
        self.size = size
        self.position = position[0], position[1]

    @property
    def size(self):
        """ size method that returns the value of size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """size method that set size attribute to value
        Args:
            value (int): Size to set size attribute to.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ position method that returns the value of si attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """position method that set position attribute to value
        Args:
            value (tuple): value to set position attribute to.
        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value[0], value[1]

    def area(self):
        """area method return the value of the square's area"""
        return self.__size ** 2

    def my_print(self):
        """my_print method that prints the square with #"""
        if self.__size == 0:
            print("")
        else:
            for m in range(0, self.__position[1]):
                print("")
            for i in range(0, self.__size):
                k = 0
                for k in range(0, self.__position[0]):
                    print(" ", end="")
                for j in range(0, self.__size):
                    print('#', end="")
                print("")
