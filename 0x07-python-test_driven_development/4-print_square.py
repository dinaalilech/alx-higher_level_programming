#!/usr/bin/python3
"""
This is the "4-print_square" module.

It supplies one function, print_square().
"""


def print_square(size):
    """
        prints a square with character #
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    # float & less than 0 exception has no sense (already handled)
    print(('#' * size + '\n') * size, end='')
