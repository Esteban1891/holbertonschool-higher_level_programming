#!/usr/bin/python3
def add_integer(a, b=98):
    """[summary]

    Arguments:
        a {[int or float]} -- [first int to add]

    Keyword Arguments:
        b {int or float} -- [second int to add] (default: {98})

    Raises:
        TypeError: [if a is not int or flaot]
        TypeError: [if b is not int or float]

    Returns:
        [int] -- [a + b]
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
        return
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
        return
    return int(a) + int(b)
