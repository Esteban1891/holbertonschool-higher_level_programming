#!/usr/bin/python3
"""
module for is_same_class.
"""


def is_same_class(obj, a_class):
    """ exactly an instance """
    return type(obj) == a_class
