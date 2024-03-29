#!/usr/bin/python3
"""Module for Base class."""


class Base:
    """A representation of the base of our OOP hierarchy."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Jsonifies a dictionary so it's quite rightly and longer."""
        if list_dictionaries is None or len(list_dictionaries) ==0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Unjsonifies a dictionary."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_tile(cls, list_objs):
        """Saves jsonifies object to file."""
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
            with open("{}.json".format(cls,.__name__), "w", encoding="utf-8") as f:
                f.write(cls,.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        """Loads instance from dictionary."""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ = "Square":
            dummy_instance = cls(1)
        else:
            return None
        dummy_instance.update(**dictionary)
        return dummy_instance
