#!/usr/bin/python3
"Writes an object to a text file, using JSON representation"
import json


def save_to_json_file(my_obj, filename):
    "Write the JSON representation of an object to a file"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
