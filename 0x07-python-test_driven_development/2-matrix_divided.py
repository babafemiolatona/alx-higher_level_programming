#!/usr/bin/python3
"""Divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix"""

    new_matrix = []
    try:
        length = len(matrix[0])
    except Exception:
        pass
    int_err = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        new_row = []
        if not isinstance(row, list):
            raise TypeError(int_err)
        if length != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError(int_err)
            result = round(i / div, 2)
            new_row.append(result)
        new_matrix.append(new_row)
    return new_matrix
