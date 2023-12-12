#!/usr/bin/python3
""" square.py """
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Square class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns: custom tsring representation of Square instance"""
        return (f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}')

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns attributes"""
        if args:
            attrs = ('id', 'size', 'x', 'y')
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """Returns: dictionary representation of Square instance"""
        sdict = {'id': 1, 'size': 0, 'x': 0, 'y': 0}
        for key in sdict.keys():
            sdict[key] = getattr(self, key)
        return (sdict)
