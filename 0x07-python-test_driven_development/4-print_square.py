#!/usr/bin/python3
"""
This is the print_square module.
"""


def print_square(size):
    """Print square with #.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
