#!/usr/bin/python3
"""Module to divide a matrix list"""


def matrix_divided(matrix, div):
    """Method to divide the matric list.
    Returns a new matrix
    """
    if not all(isinstance(elements, list) for elements in matrix:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    else:
        if not all(isinstance(elements, (int, float)) for elements in matrix:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
