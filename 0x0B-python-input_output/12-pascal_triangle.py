#!/usr/bin/python3
"""Module for Pascal Triangle"""


def pascal_triangle(n):
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    tri = [[1]]
    for rows in range(n-1):
        tri.append([a+b for a, b
                         in zip([0] + tri[-1], tri[-1] + [0])])
    return tri

