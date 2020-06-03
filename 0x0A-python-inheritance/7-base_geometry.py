#!/usr/bin/python3
"""initialize module"""


class BaseGeometry:
    """create class"""

    def area(self):
        """create instance public"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validator"""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
