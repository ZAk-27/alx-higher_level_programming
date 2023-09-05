#!/usr/bin/python3
"""

function that dividing all matrix elements 

"""


def matrix_divided(matrix, div):
    """
    function that dividing all matrix elements

    """
    sizeErr = "Each row of the matrix to have same size"
    for x in matrix:
        if len(x) != len(matrix[0]):
            raise TypeError(sizeErr)
        for y in x:
            if not isinstance(y, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not (isinstance(div, (int, float))):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(y / div, 2) for y in x] for x in matrix]
