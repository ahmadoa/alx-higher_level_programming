#!/usr/bin/python3
"""defining Base module"""
import json
import os


class Base:
    """Class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes Base instance
        Args:
            id: object identifier
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON string representation of a list of dictionaries"""
        if list_dictionaries == [] or list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """write list_objs as JSON into a file
        Args:
            list_objs: list of instances
        """
        flname = cls.__name__ + ".json"
        if list_objs is None or list_objs == []:
            ls = "[]"
        else:
            dict_list = []
            for obj in list_objs:
                dict_list.append(obj.to_dictionary())
            ls = cls.to_json_string(dict_list)
        with open(flname, "w") as file:
            file.write(ls)
        return ls

    @staticmethod
    def from_json_string(json_string):
        """read list of JSON representation
        Args:
            json_string: string represents list of dicts
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        Args:
            dictionary: double pointer to a dictionary
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """return list of instances from json file"""
        filename = cls.__name__ + ".json"
        list_instances = []
        if os.path.exists(filename):
            with open(filename, "r") as file:
                res = file.read()
                list_dicts = cls.from_json_string(res)
                for dictu in list_dicts:
                    list_instances.append(cls.create(**dictu))
        return list_instances
