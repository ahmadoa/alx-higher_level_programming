#!/usr/bin/python3
"""defining Base module"""
import json
import os
import csv
import turtle


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """write the csv serialization of a list of objects to csv file
        Args:
            list_objs: a list of instances
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as file:
            if list_objs is None or list_objs == []:
                file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                w = csv.DictWriter(file, fieldnames=fields)
                for obj in list_objs:
                    w.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize csv from a file"""
        filename = cls.__name__ + ".csv"
        list_i = []
        if os.path.exists(filename):
            with open(filename, "r") as file:
                read = csv.reader(file, delimiter=",")
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fields = ["id", "size", "x", "y"]
                for i, row in enumerate(read):
                    if i > 0:
                        el = cls(1, 1)
                        for j, k in enumerate(row):
                            if k:
                                setattr(el, fields[j], int(e))
                        list_i.append(el)
        return list_i

    @classmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws the rectangles and squares
        Args:
            list_rectangles: a list of rectangle instances
            list_squares: a list of square instances
        """
        window = turtle.Screen()
        pen = turtle.Pen()
        figs = list_rectangles + list_squares

        for f in figs:
            pen.up()
            pen.goto(f.x, f.y)
            pen.down()
            pen.forward(f.width)
            pen.right(90)
            pen.forward(f.height)
            pen.right(90)
            pen.forward(f.width)
            pen.right(90)
            pen.forward(f.height)
            pen.right(90)
        window.exitonclick()
