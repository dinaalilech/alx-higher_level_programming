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
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """size setter
        Args:
            value (int): new size of square object
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the square area based on size"""
        return (self.__size ** 2)

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            [print('#' * self.__size) for i in range(self.__size)]
