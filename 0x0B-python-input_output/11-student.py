#!/usr/bin/python3
"""defining class Student"""


class Student:
    """represents class Student"""
    def __init__(self, first_name, last_name, age):
        """initializes Student"""
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

    def reload_from_json(self, json):
        """replaces attributes of Student"""
        for key, value in json.items():
            self.__dict__[key] = value
