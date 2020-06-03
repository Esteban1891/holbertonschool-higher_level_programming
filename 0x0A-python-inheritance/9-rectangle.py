#!/usr/bin/python3
"""initialize module"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""import file 7-base_geometry"""

class Rectangle(BaseGeometry):
    """create class and inheritance BaseGeometry"""

    def __init__(self, width, height):
        """instancy"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """create Area"""
        return self.__width * self.__height

    def __str__(self):
        """str"""
        return "[rectangle] {}/{}".format(self.__width, self.__height)