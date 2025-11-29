#!/usr/bin/python3
"""Return a list of lists representing Pascal's triangle of n rows."""


def pascal_triangle(n):
    """Generate Pascal's triangle of n rows as a list of lists."""
    if n <= 0:
        return []

    triangle = [[1]]  # first row

    for i in range(1, n):
        prev_row = triangle[i - 1]
        row = [1]  # first element
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])  # sum of two above
        row.append(1)  # last element
        triangle.append(row)

    return triangle
