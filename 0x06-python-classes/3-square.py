#!/usr/bin/python3
""" Square tasks"""

class Square:
    def _init_(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self._size = size
     def area(self):
	return self._size ** 2
