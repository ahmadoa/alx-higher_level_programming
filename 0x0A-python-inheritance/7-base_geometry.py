#!/usr/bin/python3
"""defining class BaseGeomtry"""


class BaseGeometry:
    """representes BaseGeometry"""
    def area(self):
        """ not implemented but raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value attribute

        Args:
            name (str): attribute name
            value : new value of name

        Raises:
            TypeError : if value is not an int
            ValueError : if value is less than or equals 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
