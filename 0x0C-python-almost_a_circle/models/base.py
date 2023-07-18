#!/usr/bin/python3
"""
    Base Module
"""

import json

import csv
from pathlib import Path


class Base:
    """ the Base class which will be inherited by all other classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base object.

        Args:
            id (int, optional)
        """
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

            Returns:
                a Json string if list_dictionaries is not empty otherwise [].
        """
        return json.dumps(list_dictionaries) if list_dictionaries else "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the Json string representation of `list_objs` to a file.

        Args:
            list_objs: List of objects to be written.
        """
        my_list = []
        if list_objs:
            for obj in list_objs:
                my_list.append(cls.to_dictionary(obj))
        with open(cls.__name__ + ".json", "w") as file:
            file.write(cls.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """Deserializes a Json string to Python object.

        Args:
            json_string: The Json string to deserialize.

        Returns: a Python object otherwise "[]".
        """
        if json_string == "" or json_string is None:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """a class method that creates an instance with all attributes set.
        Args:
            dictionary: Dictionary of arguments to be used to create instance.
        Returns:
            object: An instance of a class that inherits from this class.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Reads data from a JSON file and creates instances with the data.

        Returns:
            list: A list of instances created using the read data.
        """

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
        """ a class method that saves the serialized list of objects
        ta a Csv file.
        args:
            list_objs: the list of objects to be serialized.
        """
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
        """a method that deserializes a CSV file and uses
        the data to create new objects.

        Returns:
                a List of objects created with the data read from the CSV.
        """
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
