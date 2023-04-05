#!/usr/bin/python3
"""
    a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """ Dividing a matrix by an argument div """
    type_error = "matrix must be a matrix (list of lists) of integers/floats"
    new_matrix = []
    new_list = []
    if not matrix:
        raise TypeError(type_error)
    if isinstance(div, int) is False and isinstance(div, float) is False:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    len_matrix = len(matrix[0])
    for lists in matrix:
        if type(lists) is not list:
            raise TypeError(type_error)
        if len(lists) != len_matrix:
            raise TypeError("Each row of the matrix must have the same size")
        for item in lists:
            if not isinstance(item, int) and not isinstance(div, float):
                raise TypeError(type_error)
            num = item / div
            new_list.append(round(num, 2))
        new_matrix.append(new_list)
        new_list = []
    return new_matrix
