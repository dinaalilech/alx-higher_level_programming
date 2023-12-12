#!/usr/bin/python3
""" rectangle.py """
from models.base import Base


class Rectangle(Base):
    """"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Returns: area value of Rectangle instance"""
        return (self.width * self.height)

    def display(self):
        """prints to stdout the Rectangle instance with character '#'
        No need to handle x & y attributes"""
        r = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(r, end='')

    def __str__(self):
        """makes Rectangle instance printable with 'print'
        Returns: custom Rectangle instance representation string"""
        return f'[Rectangle] ({self.id}) {self.x}/{self.y} \
- {self.width}/{self.height}'

    def update(self, *args, **kwargs):
        """assigns a key/value argument to each attribute"""
        attrs = ('id', 'width', 'height', 'x', 'y')
        if args:
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """Returns: dictionary representation of Rectangle instance"""
        rdict = {'id': 1, 'width': 0, 'height': 0, 'x': 0, 'y': 0}
        for key in rdict.keys():
            rdict[key] = getattr(self, key)
        return (rdict)
