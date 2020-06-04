#!/usr/bin/python3
"""initializate"""


class Student:
    """create class student"""

    def __init__(self, first_name, last_name, age):
        """initializate atrributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dict"""
        return self.___dict___
