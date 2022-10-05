#!/usr/bin/python3
"Initializes the Base class"
import json


class Base:
    "Base class"
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        "Returns the JSON string representation of a list of dictionaries"
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
