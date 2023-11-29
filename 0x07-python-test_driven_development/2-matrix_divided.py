#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.

It supplies one function, matrix_divided().
"""


def matrix_divided(matrix, div):
    """
        divides all elements of a matrix
    """
    if not isinstance(matrix, list) or any([not isinstance(l, list) for l in matrix]) \
            or any([not isinstance(i, (int, float)) for l in matrix for i in l]):
        raise TypeError("must be a matrix (list of lists) of integers/floats")
    elif not all([len(l) is len(matrix[0]) for l in matrix]):
        raise TypeError("Each row of the matrix must have the same size")
    elif not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(i / div, 2) for i in l] for l in matrix]
    return (new_matrix)
