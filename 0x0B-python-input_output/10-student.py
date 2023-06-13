#!/usr/bin/python3
"""defining Student class"""


class Student:
    """represents a class student"""
    def __init__(self, first_name, last_name, age):
        """Initializes a Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of Student"""
        if attrs is not None:
            res = {k: self.__dict__[k] for k in self.__dict__.keys() & attrs}
            return res
        else:
            return self.__dict__
