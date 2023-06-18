#!/usr/bin/python3
"""defining test_base module"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """class TestBase"""
    def testing(self):
        """tests"""
        b_uno = Base()
        self.assertEqual(b_uno.id, 1)

        b_dos = Base()
        self.assertEqual(b_dos.id, 2)

        b_tres = Base()
        self.assertEqual(b_tres.id, 3)

        b_cuatro = Base()
        self.assertEqual(b_cuatro.id, 4)

        b_cinco = Base(15)
        self.assertEqual(b_cinco.id, 15)

        b_seis = Base()
        self.assertEqual(b_seis.id, 5)

    if __name__ == "__main__":
        unittest.main()
