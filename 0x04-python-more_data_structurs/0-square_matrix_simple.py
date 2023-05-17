#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    temp_list = []
    for i in range(0, len(matrix) - 1):
        for j in range (0, len(matrix) - 1):
            temp_list.append(matrix[i][j]**2)
        new_matrix.append(temp_list)
        temp_list = []
    return new_matrix
