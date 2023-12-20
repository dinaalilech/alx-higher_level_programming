#!/usr/bin/python3
""" rectangle_test.py """
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """defines unittests for Rectangle(...)"""

    def two_args_test(self):
        """"""
        r = Rectangle()
        self.assertEqual(r.id, 1)

    def four_arg_test(self):
        """"""
        r = Rectangle(89)
        self.assertEqual(r.id, 89)

    def five_args_test(self):
        """"""
        r = Rectangle()

    def id_inc_test(self):
        """"""
        r1, r2, r3 = Rectangle(), Rectangle(98), Rectangle()
        self.assertEqual(r3.id, 2)
