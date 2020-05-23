#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """[summary]

    Arguments:
        first_name {[str]} -- [first name]

    Keyword Arguments:
        last_name {str} -- [last name] (default: {""})

    Raises:
        TypeError: [if first name is not str]
        TypeError: [if last name is not str]
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')

    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print('My name is {} {}'.format(first_name, last_name))
