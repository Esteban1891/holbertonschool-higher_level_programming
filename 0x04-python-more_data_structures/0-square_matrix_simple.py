#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return (list(map(lambda new_matrix: [a ** 2 for a in new_matrix], matrix)))
