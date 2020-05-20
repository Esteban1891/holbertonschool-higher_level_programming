#!/usr/bin/python3
class Square():
    """A square class."""
    def __init__(self, size=0):
        """Initialization of the class square."""
        self.__size = size

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

    def my_print(self):
        """print the Square"""
        size = self.__size
        if size == 0:
            print("")
            return
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print("")
