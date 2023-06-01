#!/usr/bin/python3
"""Defining a list elements division function"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix

    Args:
        matrix (list): a list of lists of ints/floats
        div: the divider number

    Raises:
        TypeError: if matrix doesn't contain floats/ints
        TypeError: if matrix lists have different sizes
        TypeError: if div is not int/float
        ZeroDivisionError: if div is 0

    Returns:
        new matrix containing results of division
    """

    new_matrix = list()

    if (not isinstance(matrix, list) or
        not all(not isinstance(row, list) for row in matrix) or
        not all((isinstance(el, int) or isinstance(el, float)) for el in [i for
                row in matrix for i in row])) or len(matrix) == 0
    raise TypeError("matrix must be a matrix (list of lists) of "
                    "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) != float and type(div) != int:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    temp = list()
    for row in matrix:
        for el in row:
            temp.append(round(el / div, 2))
        new_matrix.append(temp)
        temp.clear()

    return new_matrix
