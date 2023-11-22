#!/usr/bin/python3
"""Define a MagicClass matching exactly a python bytecode"""
import math


class MagicClass:
    """magic class (Python bytecode)
    Attributes:
        __radius (int or float): radius of MagicClass class"""
    def __init__(self, radius=0):
        """instantiates the MagicClass object
        Args:
            radius (int or float): radius of MagicClass object"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """returns the area of MagicClass object"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """returns the circumference of MagicClass object"""
        return (2 * math.pi * self.__radius)
