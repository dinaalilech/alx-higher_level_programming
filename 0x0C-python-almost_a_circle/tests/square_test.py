#!/usr/bin/python3
""" square_test.py """
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """defines unittests for Square(...)"""

    def no_args_test(self):
        """"""
        b = Base()
        self.assertEqual(b.id, 1)

    def one_arg_test(self):
        """"""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def id_inc_test(self):
        """"""
        b1, b2, b3 = Base(), Base(98), Base()
        self.assertEqual(b3.id, 2)
