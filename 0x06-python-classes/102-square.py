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
        self.size = size

    @property
    def size(self):
        """size getter"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """size setter
        Args:
            value (int): new size of square object
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the square area based on size"""
        return (self.__size ** 2)

    def __eq__(self, other):
        """returns True if equal objects"""
        return (self.__size == other.__size)

    def __ne__(self, other):
        """returns True if non equal objects"""
        return (self.__size != other.__size)

    def __gt__(self, other):
        """returns True if object is greater than other object"""
        return (self.__size > other.__size)

    def __ge__(self, other):
        """returns True if object is greater than or equal to other object"""
        return (self.__size >= other.__size)

    def __lt__(self, other):
        """returns True if object is lower than other object"""
        return (self.__size < other.__size)

    def __le__(self, other):
        """returns True if object is lower than or equal to other object"""
        return (self.__size <= other.__size)
