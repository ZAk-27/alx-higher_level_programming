#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # [[row[i] to be returned for row in matrix] for i in range(3)]
    return [[row[i]**2 for i in range(len(row))] for row in matrix]
