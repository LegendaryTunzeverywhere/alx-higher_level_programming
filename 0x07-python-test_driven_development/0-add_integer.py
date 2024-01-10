#!/usr/bin/python3
"""
Module for one function to get the sum of two 
variables
"""

def add_integer(a, b=98):
    """a function that adds 2 integers"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
