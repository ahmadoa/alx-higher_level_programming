#!/usr/bin/python3
"""defining Student class"""


class Student:
    """represents a student"""
    def __init__(self, first_name, last_name, age):
        """initializes a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns dictionary representation of Student"""
        return self.__dict__
