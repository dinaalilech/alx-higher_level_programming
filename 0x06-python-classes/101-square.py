#!/usr/bin/python3
"""Square class"""


class Square:
    """defines a square based on size
    TypeError & ValueError exceptions are handled
    Attributes:
        __size (int): size of square class
        __position (tuple of 2 integers): position of top left element
    """
    def __init__(self, size=0, position=(0, 0)):
        """instantiation of the square object
        Args:
            size (int, optional): size of square object
            position (tuple, optional): position of top left element
        """
        self.size = size
        self.position = position

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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get/set the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """returns the square area based on size"""
        return (self.__size ** 2)

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        """Define the print() representation of a Square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
