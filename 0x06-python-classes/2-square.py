#!/usr/bin/python3
class Square():
    """A square class."""
    def __init__(self, size=0):
        """Initialization of the class square."""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
