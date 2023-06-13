#!/usr/bin/python3
"""defining pascal_triangle function"""


def pascal_triangle(n):
    """returns a list of lists of integers"""
    rows = []
    for i in range(n):
        row = []
        for j in range(i+1):
            row.append(1)
        rows.append(row)
    for n in range(n):
        for i in range(n - 1):
            rows[n][i + 1] = sum(rows[n - 1][i:i + 2])
    return rows
