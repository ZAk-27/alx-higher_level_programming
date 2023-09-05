#!/usr/bin/python3
"""

Function used to add 2 integers

"""
def add_integer(a, b=98):
    """
    return after a and b
    """
    if not (type(a) is float or type(a) is int):
        raise TypeError("a must be an integer")
    elif not (type(b) is float or type(b) is int):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
