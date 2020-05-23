#!/usr/bin/python3
def print_square(size):
    """[summary]

    Arguments:
        size {[int]} -- [size of square]

    Raises:
        TypeError: [if size is not int]
        ValueError: [if size <]
    """
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    if size == 0:
        print()
    else:
        for row in range(size):
            print('#' * size)
