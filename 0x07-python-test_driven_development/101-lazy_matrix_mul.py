#!/usr/bin/python3

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """[lazy_matrix_mul using numpy]

    Arguments:
        m_a {[list of lists]} -- [matrice 1]
        m_b {[list of lists]} -- [matrice 2]

    Raises:
        TypeError: [if m_a not list]
        TypeError: [if m_b not list]
        TypeError: [if m_a not list of lists]
        TypeError: [if m_b not list of lists]
        ValueError: [if m_a empty]
        ValueError: [if m_b empty]
        TypeError: [if not all elements of m_a integers]
        TypeError: [if not all elements of m_b integers]
        TypeError: [if rows of m_a are not with the same size]
        TypeError: [if rows of m_b are not with the same size]
        ValueError: [if m_a and m_b cant be multiplied]

    Returns:
        [type] -- [description]
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(i, list) for i in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(i, list) for i in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a cant be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b cant be empty")

    if not all(all(isinstance(i, (float, int)) for i in row) for row in m_a):
        raise TypeError("m_a should contain only integers or floats")
    if not all(all(isinstance(i, (float, int)) for i in row) for row in m_b):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(x) == len(m_a[0]) for x in m_a):
        raise TypeError('each row of m_a must be of the same size')
    if not all(len(x) == len(m_b[0]) for x in m_b):
        raise TypeError('each row of m_b must be of the same size')

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    res = np.dot(m_a, m_b)
    return res
