#!/usr/bin/python3
"""defining testing module for rectangle"""
import unittest
import contextlib
from models.base import Base
from models.rectangle import Rectangle
import io


class TestingRectangle(unittest.TestCase):
    """class TestingRectangle"""
    def starter(self):
        Base._Base__nb_objects = 0

    def test_uno(self):
        """first test"""
        inout = io.StringIO()
        rec = Rectangle(1, 2)
        self.assertEqual(rec.id, 1)
        self.assertEqual(rec.width, 1)
        self.assertEqual(rec.height, 2)
        self.assertEqual(rec.x, 0)
        self.assertEqual(rec.y, 0)
        self.assertEqual(rec.__str__(), "[Rectangle] (1) 0/0 - 1/2")
        self.assertEqual(rec.area(), 2)
        with contextlib.redirect_stdout(inout):
            rec.display()
        res = inout.getvalue()

        output = "#\n#\n"
        self.assertEqual(res, output)
        output = {"x": 0, "y": 0, "id": 1, "height": 2, "width": 1}
        self.assertEqual(rec.to_dictionary(), output)
        rec.update()
        self.assertEqual(rec.__str__(), "[Rectangle] (1) 0/0 - 1/2")
        rec.update(10)
        self.assertEqual(rec.__str__(), "[Rectangle] (10) 0/0 - 1/2")
        rec.update(10, 1)
        self.assertEqual(rec.__str__(), "[Rectangle] (10) 0/0 - 1/2")
        rec.update(10, 1, 2)
        self.assertEqual(rec.__str__(), "[Rectangle] (10) 0/0 - 1/2")
        rec.update(10, 1, 2, 3)
        self.assertEqual(rec.__str__(), "[Rectangle] (10) 3/0 - 1/2")
        rec.update(10, 1, 2, 3, 4)
        self.assertEqual(rec.__str__(), "[Rectangle] (10) 3/4 - 1/2")
        rec.update(**{"id": 89})
        self.assertEqual(rec.__str__(), "[Rectangle] (89) 3/4 - 1/2")
        rec.update(**{"id": 89, "width": 1})
        self.assertEqual(rec.__str__(), "[Rectangle] (89) 3/4 - 1/2")
        rec.update(**{"id": 89, "width": 1, "height": 2})
        self.assertEqual(rec.__str__(), "[Rectangle] (89) 3/4 - 1/2")
        rec.update(**{"id": 89, "width": 1, "height": 2, "x": 3})
        self.assertEqual(rec.__str__(), "[Rectangle] (89) 3/4 - 1/2")
        rec.update(**{"id": 89, "width": 1, "height": 2, "x": 3, "y": 4})
        self.assertEqual(rec.__str__(), "[Rectangle] (89) 3/4 - 1/2")
        rec_dictionary = rec.to_dictionary()
        recowen = Rectangle.create(**rec_dictionary)
        self.assertEqual(rec, recowen)

    def testing_dos(self):
        """second testing"""
        rec = Rectangle(1, 2, 3)
        self.assertEqual(rec.id, 1)
        self.assertEqual(rec.width, 1)
        self.assertEqual(rec.height, 2)
        self.assertEqual(rec.x, 3)
        self.assertEqual(rec.y, 0)
        self.assertEqual(rec.__str__(), "[Rectangle] (1) 3/0 - 1/2")
        self.assertEqual(rec.area(), 2)
        res = {"x": 3, "y": 0, "id": 1, "height": 2, "width": 1}
        self.assertEqual(rec.to_dictionary(), res)

    def testing_tres(self):
        """third testing"""
        rec = Rectangle(1, 2, 3, 4)
        self.assertEqual(rec.id, 1)
        self.assertEqual(rec.width, 1)
        self.assertEqual(rec.height, 2)
        self.assertEqual(rec.x, 3)
        self.assertEqual(rec.y, 4)
        self.assertEqual(rec.__str__(), "[Rectangle] (1) 3/4 - 1/2")
        self.assertEqual(rec.area(), 2)
        res = {"x": 3, "y": 4, "id": 1, "height": 2, "width": 1}
        self.assertEqual(rec.to_dictionary(), res)

    def testing_cuatro(self):
        """fourth testing"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("1", 2)

    def testing_cinco(self):
        """fifth testing"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "2")

    def testing_seis(self):
        """sixth testing"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "3")

    def testing_siete(self):
        """seventh testing"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "4")

    def testing_ocho(self):
        """eighth testing"""
        rec = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rec.id, 5)
        self.assertEqual(rec.width, 1)
        self.assertEqual(rec.height, 2)
        self.assertEqual(rec.x, 3)
        self.assertEqual(rec.y, 4)
        self.assertEqual(rec.__str__(), "[Rectangle] (5) 3/4 - 1/2")
        self.assertEqual(rec.area(), 2)
        res = {"x": 3, "y": 4, "id": 5, "height": 2, "width": 1}
        self.assertEqual(rec.to_dictionary(), res)

    def testing_nueve(self):
        """ninth testing"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def testing_deis(self):
        """tenth testing"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2)

    def testing_once(self):
        """eleventh testing"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def testing_doce(self):
        """twelve testing"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)


if __name__ == "__main__":
    unittest.main()
