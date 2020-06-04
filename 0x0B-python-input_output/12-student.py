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

    def to_json(self, attrs=None):
        """to_json
        """
        dic = {}
        if attrs is None:
            return self.__dict__
        for i in attrs:
            if hasattr(self, i):
                dic[i] = getattr(self, i)
        return dic
