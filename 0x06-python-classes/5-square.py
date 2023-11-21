#!/usr/bin/python3
class Square:
    def _init_(self, size=0):
        self.size = size
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self._size = value
    def area(self):
        return self._size ** 2

    def my_print(self):
        for i in range(self.size):
            for j in range(self.size):
                print('#', end="\n" if j is self.size - 1 and i ! = j else "")
        print()
