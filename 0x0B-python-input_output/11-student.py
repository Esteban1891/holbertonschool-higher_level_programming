#!/usr/bin/python3
"""initializate"""


class Student:
    """create class student"""

    def __init__(self, first_name, last_name, age):
        """initializate atrributes
        :param first_name:
        :param last_name:
        :param age:
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a dictionary """
        return self.__dict__
