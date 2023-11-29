#!/usr/bin/python3
"""
This is the "0-add_integer" module

It supplies one function, add_integer().
"""


def add_integer(a, b=98):
    """
        Returns the result of addition of 2 integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
