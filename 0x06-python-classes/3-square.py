#!/usr/bin/python3
"""Square class"""


class Square:
    """defines a square based on size
    TypeError & ValueError exceptions are handled
    Attributes:
        __size (int): size of square class
    """
    def __init__(self, size=0):
        """instantiation of the square object
        Args:
            size (int, optional): size of square object
        """
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """returns the square area based on size"""
        return (self.__size ** 2)
