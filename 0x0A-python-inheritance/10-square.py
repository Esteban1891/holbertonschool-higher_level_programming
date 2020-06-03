#!/usr/bin/python3
"""initializate"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square1"""

    def __init__(self, size):
        """initial attributes"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
        self.area()
