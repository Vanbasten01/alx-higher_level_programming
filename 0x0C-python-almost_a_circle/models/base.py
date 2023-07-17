#!/usr/bin/python3
""" Base Module"""

import json
from pathlib import Path
import csv
import turtle


class Base:
    """ the Base class which will be inherited by all other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            it serializes a list of dictionaries to a Json string.
            args:
                list_dictionaries: a list of dictionaries to be serialized.
            returns:
                a Json string if list_dictionaries is not empty otherwise [].
        """
        return json.dumps(list_dictionaries) if list_dictionaries else "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        my_list = []
        if list_objs:
            for obj in list_objs:
                my_list.append(cls.to_dictionary(obj))
        with open(cls.__name__ + ".json", "w") as file:
            file.write(cls.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        return json.loads(json_string) if json_string else "[]"

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):

        file = cls.__name__ + ".json"
        try:
            with open(file, "r") as f:
                data = f.read()
        except FileNotFoundError:
            return []

        instances_data = cls.from_json_string(data)
        instances = [
                cls.create(**instance_data)
                for instance_data in instances_data
                ]
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"

        with open(filename, "w") as csv_file:
            if not Path(filename).is_file():
                return []
            else:
                if cls.__name__ == "Rectangle":
                    attributes = ["id", "width", "height", "x", "y"]
                else:
                    attributes = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csv_file, fieldnames=attributes)
                writer.writeheader()
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """deserialize a csv file"""
        filename = cls.__name__ + ".csv"
        my_list = []
        with open(filename, "r") as csv_file:
            if not Path(filename).is_file():
                return []
            else:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    for key, value in row.items():
                        row[key] = int(value)
                    my_list.append(cls.create(**row))
                return my_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draws our shapes"""
        turtle.getscreen()
        turtle.shape("turtle")
        for rect in list_rectangles:
            turtle.pencolor()
            turtle.setpos(rect.x, rect.y)
            turtle.pendown()
            for i in range(2):
                turtle.forward(rect.height)
                turtle.left(90)
                turtle.forward(rect.width)
                turtle.left(90)
            turtle.penup()
        for sq in list_squares:
            turtle.pencolor()
            turtle.setpos(sq.x, sq.y)
            turtle.pendown()
            for i in range(4):
                turtle.foward(sq.height)
                turtle.left(90)
            turtle.penup()
        turtle.exitonclick()
