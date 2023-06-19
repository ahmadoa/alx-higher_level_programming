#!/usr/bin/python3
"""defining test_square module"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class SquareTests(unittest.TestCase):
    """SquareTests class"""
    def starter(self):
        Base._Base__nb__objects = 0

    def test_uno(self):
        """first test"""
        squ = Square(1)
        self.assertEqual(squ.id, 1)
        self.assertEqual(squ.width, 1)
        self.assertEqual(squ.height, 1)
        self.assertEqual(squ.x, 0)
        self.assertEqual(squ.y, 0)
        self.assertEqual(squ.__str__(), "[Square] (1) 0/0 - 1")
        self.assertEqual(squ.area(), 1)
        res = {"id": 1, "x": 0, "size": 1, "y": 0}
        self.assertEqual(squ.to_dictionary(), res)
        squ.update()
        self.assertEqual(squ.__str__(), "[Square] (1) 0/0 - 1")
        squ.update(10)
        self.assertEqual(squ.__str__(), "[Square] (10) 0/0 - 1")
        squ.update(10, 1)
        self.assertEqual(squ.__str__(), "[Square] (10) 0/0 - 1")
        squ.update(10, 1, 2)
        self.assertEqual(squ.__str__(), "[Square] (10) 2/0 - 1")
        squ.update(10, 1, 2, 3)
        self.assertEqual(squ.__str__(), "[Square] (10) 2/3 - 1")
        squ.update(**{"id": 89})
        self.assertEqual(squ.__str__(), "[Square] (89) 2/3 - 1")
        squ.update(**{"id": 89, "size": 1})
        self.assertEqual(squ.__str__(), "[Square] (89) 2/3 - 1")
        squ.update(**{"id": 89, "size": 1, "x": 2})
        self.assertEqual(squ.__str__(), "[Square] (89) 2/3 - 1")
        squ.update(**{"id": 89, "size": 1, "x": 2, "y": 3})
        self.assertEqual(squ.__str__(), "[Square] (89) 2/3 - 1")
        squ_dictionary = squ.to_dictionary()
        squowen = Rectangle.create(**squ_dictionary)
        self.assertIsNot(squ, squowen)

    def test_dos(self):
        """second test"""
        squ = Square(1, 2)
        self.assertEqual(squ.id, 1)
        self.assertEqual(squ.width, 1)
        self.assertEqual(squ.height, 1)
        self.assertEqual(squ.x, 2)
        self.assertEqual(squ.y, 0)
        self.assertEqual(squ.__str__(), "[Square] (1) 2/0 - 1")
        self.assertEqual(squ.area(), 1)
        res = {"id": 1, "x": 2, "size": 1, "y": 0}
        self.assertEqual(squ.to_dictionary(), res)
        squ.update()
        self.assertEqual(squ.__str__(), "[Square] (1) 2/0 - 1")
        squ.update(10)
        self.assertEqual(squ.__str__(), "[Square] (10) 2/0 - 1")
        squ.update(10, 1)
        self.assertEqual(squ.__str__(), "[Square] (10) 2/0 - 1")
        squ.update(10, 1, 2)
        self.assertEqual(squ.__str__(), "[Square] (10) 2/0 - 1")
        squ.update(10, 1, 2, 3)
        self.assertEqual(squ.__str__(), "[Square] (10) 2/3 - 1")
        squ.update(**{"id": 89})
        self.assertEqual(squ.__str__(), "[Square] (89) 2/3 - 1")
        squ.update(**{"id": 89, "size": 1})
        self.assertEqual(squ.__str__(), "[Square] (89) 2/3 - 1")
        squ.update(**{"id": 89, "size": 1, "x": 2})
        self.assertEqual(squ.__str__(), "[Square] (89) 2/3 - 1")
        squ.update(**{"id": 89, "size": 1, "x": 2, "y": 3})
        self.assertEqual(squ.__str__(), "[Square] (89) 2/3 - 1")

    def test_tres(self):
        """third test"""
        squ = Square(1, 2, 3)
        self.assertEqual(squ.id, 1)
        self.assertEqual(squ.width, 1)
        self.assertEqual(squ.height, 1)
        self.assertEqual(squ.x, 2)
        self.assertEqual(squ.y, 3)
        self.assertEqual(squ.__str__(), "[Square] (1) 2/3 - 1")
        self.assertEqual(squ.area(), 1)
        res = {"id": 1, "x": 2, "size": 1, "y": 3}
        self.assertEqual(squ.to_dictionary(), res)
        squ.update()
        self.assertEqual(squ.__str__(), "[Square] (1) 2/3 - 1")
        squ.update(10)
        self.assertEqual(squ.__str__(), "[Square] (10) 2/3 - 1")
        squ.update(10, 1)
        self.assertEqual(squ.__str__(), "[Square] (10) 2/3 - 1")
        squ.update(10, 1, 2)
        self.assertEqual(squ.__str__(), "[Square] (10) 2/3 - 1")
        squ.update(10, 1, 2, 3)
        self.assertEqual(squ.__str__(), "[Square] (10) 2/3 - 1")
        squ.update(**{"id": 89})
        self.assertEqual(squ.__str__(), "[Square] (89) 2/3 - 1")
        squ.update(**{"id": 89, "size": 1})
        self.assertEqual(squ.__str__(), "[Square] (89) 2/3 - 1")
        squ.update(**{"id": 89, "size": 1, "x": 2})
        self.assertEqual(squ.__str__(), "[Square] (89) 2/3 - 1")
        squ.update(**{"id": 89, "size": 1, "x": 2, "y": 3})
        self.assertEqual(squ.__str__(), "[Square] (89) 2/3 - 1")

    def test_cuatro(self):
        """fourth test"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("1")

    def test_cinco(self):
        """fifth test"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")

    def test_seis(self):
        """sixth test"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3")

    def test_siete(self):
        """seventh test"""
        squ = Square(1, 2, 3, 4)
        self.assertEqual(squ.id, 4)
        self.assertEqual(squ.width, 1)
        self.assertEqual(squ.height, 1)
        self.assertEqual(squ.x, 2)
        self.assertEqual(squ.y, 3)
        self.assertEqual(squ.__str__(), "[Square] (4) 2/3 - 1")
        self.assertEqual(squ.area(), 1)
        res = {"id": 4, "x": 2, "size": 1, "y": 3}
        self.assertEqual(squ.to_dictionary(), res)
        squ.update()
        self.assertEqual(squ.__str__(), "[Square] (4) 2/3 - 1")
        squ.update(10)
        self.assertEqual(squ.__str__(), "[Square] (10) 2/3 - 1")
        squ.update(10, 1)
        self.assertEqual(squ.__str__(), "[Square] (10) 2/3 - 1")
        squ.update(10, 1, 2)
        self.assertEqual(squ.__str__(), "[Square] (10) 2/3 - 1")
        squ.update(10, 1, 2, 3)
        self.assertEqual(squ.__str__(), "[Square] (10) 2/3 - 1")
        squ.update(**{"id": 89})
        self.assertEqual(squ.__str__(), "[Square] (89) 2/3 - 1")
        squ.update(**{"id": 89, "size": 1})
        self.assertEqual(squ.__str__(), "[Square] (89) 2/3 - 1")
        squ.update(**{"id": 89, "size": 1, "x": 2})
        self.assertEqual(squ.__str__(), "[Square] (89) 2/3 - 1")
        squ.update(**{"id": 89, "size": 1, "x": 2, "y": 3})
        self.assertEqual(squ.__str__(), "[Square] (89) 2/3 - 1")

    def test_ocho(self):
        """eighth test"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)

    def test_nueve(self):
        """ninth test"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2)

    def test_diez(self):
        """tenth test"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -3)

    def test_once(self):
        """eleventh test"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)


if __name__ == "__main__":
    unittest.main()
